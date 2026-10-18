from pathlib import Path
import argparse
import hashlib
import html
import re

ROOT = Path(__file__).resolve().parent.parent

def inline(text):
    text = html.escape(text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'`(.+?)`', r'<code>\1</code>', text)
    return re.sub(r'\[([^\]]+)\]\((https?://[^\s)]+)\)', r'<a href="\2" target="_blank" rel="noopener noreferrer">\1</a>', text)

def build(source_path=None, output_path=None):
    source_path = Path(source_path or ROOT / 'cv_architecture_roadmap.md')
    output_path = Path(output_path or ROOT / 'index.html')
    source = source_path.read_text()
    css = (ROOT / 'work/roadmap.css').read_text()
    version = hashlib.sha256(source.encode() + css.encode() + Path(__file__).read_bytes()).hexdigest()
    operations_match = re.search(r'^## 1\. 운영계획\s*\n(.*?)^<!-- /운영계획 -->\n(?:\n---\n)?', source, re.M | re.S)
    operations_body = operations_match[1] if operations_match else ''
    if operations_match:
        source = source[:operations_match.start()] + source[operations_match.end():]
    title_match = re.search(r'^# (.+)$', source, re.M)
    title = title_match[1] if title_match else source_path.stem
    topics = []

    def render(body, model=False):
        lines = body.strip().splitlines()
        out = []
        i = 0
        serial = 0
        while i < len(lines):
            line = lines[i].strip()
            if not line or line == '---' or line.startswith(('# Part ', '### 공통 학습.', '### 선택 학습.')):
                i += 1
                continue
            if line == '<!-- presenter-guidance -->':
                i += 1
                guidance_lines = []
                while i < len(lines) and lines[i].strip() != '<!-- /presenter-guidance -->':
                    guidance_lines.append(lines[i])
                    i += 1
                if i == len(lines):
                    raise ValueError('담당자 안내의 끝 표시가 필요합니다.')
                i += 1
                guidance_content = render('\n'.join(guidance_lines))
                cards = []
                for card in re.finditer(r'<h4 class="subheading">(.*?)</h4>(.*?)(?=<h4 class="subheading">|\Z)', guidance_content, re.S):
                    title, content = card[1], card[2]
                    numbered = re.match(r'^(\d+)\. (.+)$', title)
                    if numbered:
                        heading = f'<span class="guidance-number">{int(numbered[1]):02d}</span><h4>{numbered[2]}</h4>'
                        card_class = 'guidance-card'
                    else:
                        heading = f'<h4>{title}</h4>'
                        card_class = 'guidance-card guidance-principle'
                    cards.append(f'<section class="{card_class}"><header class="guidance-card-heading">{heading}</header><div class="guidance-card-body">{content}</div></section>')
                out.append('<div class="presenter-guidance">' + ''.join(cards) + '</div>')
                continue
            if line == '…':
                out.append('<p class="example-more" aria-label="추가 학습 포인트가 이어집니다">…</p>')
                i += 1
                continue
            if line.startswith('|'):
                table = []
                while i < len(lines) and lines[i].strip().startswith('|'):
                    table.append([c.strip() for c in lines[i].strip().strip('|').split('|')])
                    i += 1
                if len(table) < 2:
                    continue
                data = table[2:]
                is_schedule = table[0] == ['소요 시간', '진행 구간', '단계', '진행 내용']
                is_framework = table[0] == ['소요 시간', '진행 구간', '단계', '중심 질문', '세부 안내']
                is_topics = model and ((len(table[0]) == 4 and table[0][1:3] == ['유형', '등급']) or (len(table[0]) == 3 and table[0][1] == '등급'))
                if is_framework:
                    out.append('<ol class="session-timeline session-framework">')
                    for row in data:
                        if len(row) != 5:
                            raise ValueError('세션 프레임워크 표는 소요 시간·진행 구간·단계·중심 질문·세부 안내의 다섯 열로 구성해야 합니다.')
                        duration, interval, stage, question, guidance = row
                        named_stage = re.fullmatch(r'([1-6])\. (.+?) · (.+)', stage)
                        if named_stage:
                            number, key, name = named_stage.groups()
                            stage_html = f'<span class="session-stage-number">{int(number):02d}</span><span class="session-stage-key">{inline(key)}</span><span class="session-stage-name">{inline(name)}</span>'
                        else:
                            stage_html = inline(stage)
                        points = re.split(r'<br\s*/?>', guidance)
                        guidance_html = '<ul>' + ''.join(f'<li>{inline(point.strip())}</li>' for point in points) + '</ul>'
                        out.append(f'<li class="session-step"><details class="session-disclosure"><summary class="session-summary"><div class="session-timing">{inline(duration)}<span>{inline(interval)}</span></div><div class="session-content"><h5>{stage_html}</h5><p>{inline(question)}</p></div><span class="session-chevron" aria-hidden="true"></span></summary><div class="session-guidance">{guidance_html}</div></details></li>')
                    out.append('</ol>')
                elif is_schedule:
                    out.append('<ol class="session-timeline">')
                    for row in data:
                        if len(row) != 4:
                            raise ValueError('세션 진행 표는 소요 시간·진행 구간·단계·진행 내용의 네 열로 구성해야 합니다.')
                        duration, interval, stage, description = row
                        out.append(f'<li class="session-step"><div class="session-timing">{inline(duration)}<span>{inline(interval)}</span></div><div class="session-content"><h5>{inline(stage)}</h5><p>{inline(description)}</p></div></li>')
                    out.append('</ol>')
                elif is_topics:
                    out.append('<div class="topic-list">')
                    for row in data:
                        if len(row) == 4:
                            name, topic_type, priority, description = row
                            if not topic_type:
                                raise ValueError(f'{name}: 학습 항목의 유형이 필요합니다.')
                        elif len(row) == 3:
                            name, priority, description = row
                            topic_type = ''
                        else:
                            raise ValueError('학습 항목 표는 이름·유형·등급·학습 내용으로 구성해야 합니다.')
                        serial += 1
                        topics.append((name, priority, description))
                        badge = 'essential' if '필수' in priority else 'extended'
                        type_label = f'<span class="topic-type" aria-label="유형: {inline(topic_type)}">{inline(topic_type)}</span>' if topic_type else ''
                        description_points = re.split(r'<br\s*/?>', description)
                        concepts_html = ''
                        concepts_match = re.fullmatch(r'\*\*포함 개념:\*\*\s*(.+)', description_points[0].strip())
                        if concepts_match:
                            concepts = re.split(r'\s+·\s+', concepts_match[1])
                            concepts_html = '<div class="topic-concepts"><h5>포함 개념</h5><ul>' + ''.join(f'<li>{inline(concept.strip())}</li>' for concept in concepts) + '</ul></div>'
                            description_points = description_points[1:]
                        if len(description_points) > 1:
                            description_html = '<ul class="topic-points">' + ''.join(f'<li>{inline(point.strip())}</li>' for point in description_points) + '</ul>'
                        else:
                            description_html = f'<p>{inline(description_points[0])}</p>' if description_points else ''
                        order_html = f'<span class="topic-order" aria-label="학습 순서 {serial}">{serial:02d}</span>'
                        out.append(f'<article class="topic"><details class="topic-disclosure"><summary class="topic-summary"><h4 class="topic-title">{order_html}<span class="topic-heading"><span class="topic-name">{inline(name)}</span>{type_label}</span><span class="badge {badge}">{inline(priority)}</span><span class="topic-chevron" aria-hidden="true"></span></h4></summary><div class="topic-description">{concepts_html}{description_html}</div></details></article>')
                    out.append('</div>')
                else:
                    out.append('<div class="table-wrap"><table><thead><tr>' + ''.join(f'<th scope="col">{inline(c)}</th>' for c in table[0]) + '</tr></thead><tbody>')
                    for row in data:
                        out.append('<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in row) + '</tr>')
                    out.append('</tbody></table></div>')
                continue
            heading = re.match(r'^(#{2,6}) (.+)$', line)
            if heading:
                subsection = re.fullmatch(r'(\d+)-([A-Z])\. (.+)', heading[2]) if model else None
                if subsection:
                    chapter_number, letter, name = subsection.groups()
                    serial = 0
                    out.append(f'<h4 class="study-subsection" id="chapter-{chapter_number}-{letter.lower()}"><span>{chapter_number}-{letter}</span>{inline(name)}</h4>')
                    i += 1
                    continue
                level = min(6, max(4, len(heading[1]))) if model else min(4, max(3, len(heading[1])))
                heading_class = 'session-phase' if re.match(r'^(시작 점검|핵심 학습|세션 프레임워크|학습 정리) · ', heading[2]) else 'subheading'
                out.append(f'<h{level} class="{heading_class}">{inline(heading[2])}</h{level}>')
                i += 1
                continue
            if line.startswith('- ') or re.match(r'^\d+\. ', line):
                ordered = bool(re.match(r'^\d+\. ', line))
                tag = 'ol' if ordered else 'ul'
                checklist = line.startswith(('- [ ] ', '- [x] ', '- [X] '))
                out.append(f'<{tag}' + (' class="checklist"' if checklist else '') + '>')
                while i < len(lines):
                    entry = lines[i].strip()
                    match = re.match(r'^\d+\. (.*)', entry) if ordered else re.match(r'^- (.*)', entry)
                    if not match:
                        break
                    value = match[1]
                    if value.startswith(('[ ] ', '[x] ', '[X] ')):
                        checked = '' if value.startswith('[ ]') else ' checked'
                        out.append(f'<li><label><input type="checkbox"{checked}><span>{inline(value[4:])}</span></label></li>')
                    else:
                        out.append(f'<li>{inline(value)}</li>')
                    i += 1
                out.append(f'</{tag}>')
                continue
            if line.startswith('<!--'):
                i += 1
                continue
            if line.startswith('>'):
                out.append(f'<p>{inline(line.lstrip("> "))}</p>')
                i += 1
                continue
            paragraph = [line]
            i += 1
            while i < len(lines) and lines[i].strip() and not lines[i].startswith(('|', '#', '- ', '>')):
                paragraph.append(lines[i].strip())
                i += 1
            out.append(f'<p>{inline(" ".join(paragraph))}</p>')
        return '\n'.join(out)

    operations_html = ''
    operations_nav = ''
    if operations_body:
        examples = list(re.finditer(r'<!-- point-example:([a-z][a-z0-9-]*) label:([^>\n]+) -->\s*(.*?)<!-- /point-example -->', operations_body, re.S))
        if examples:
            buttons, panels, chunks = [], [], []
            cursor = 0
            example_ids = set()
            for index, example in enumerate(examples):
                key, label, body = example[1], example[2].strip(), example[3]
                if key in example_ids:
                    raise ValueError('학습 포인트 예시의 ID는 중복될 수 없습니다.')
                example_ids.add(key)
                if not label:
                    raise ValueError('학습 포인트 예시에 탭 이름이 필요합니다.')
                selected = index == 0
                buttons.append(f'<button type="button" role="tab" id="example-tab-{key}" aria-controls="example-panel-{key}" aria-selected="{str(selected).lower()}" tabindex="{0 if selected else -1}">{inline(label)}</button>')
                panels.append(f'<section class="point-example-panel" id="example-panel-{key}" role="tabpanel" aria-labelledby="example-tab-{key}" tabindex="0"' + ('' if selected else ' hidden') + '>' + render(body) + '</section>')
                chunks.append(render(operations_body[cursor:example.start()]))
                if selected:
                    chunks.append('<!-- point-example-switcher -->')
                cursor = example.end()
            chunks.append(render(operations_body[cursor:]))
            switcher = '<div class="point-examples"><div class="point-example-tabs" role="tablist" aria-label="학습 포인트 예시 선택">' + ''.join(buttons) + '</div>' + ''.join(panels) + '</div>'
            operations_content = '\n'.join(chunks).replace('<!-- point-example-switcher -->', switcher)
        else:
            operations_content = render(operations_body)
        operations_toc = []
        operations_sidebar = []
        def operation_heading(match):
            section_id = f'operations-{len(operations_toc) + 1}'
            operations_toc.append(f'<a href="#{section_id}">{match[1]}</a>')
            numbered = re.match(r'^(\d+)\. (.+)$', match[1])
            if not numbered:
                raise ValueError('운영계획 세부 제목에는 번호가 필요합니다.')
            operations_sidebar.append(f'<a class="nav-link" href="#{section_id}"><span>{int(numbered[1]):02d}</span>{numbered[2]}</a>')
            return f'<h3 class="subheading" id="{section_id}">{match[1]}</h3>'
        operations_content = re.sub(r'<h3 class="subheading">(.*?)</h3>', operation_heading, operations_content)
        def operation_block(match):
            section_id, title, content = match[1], match[2], match[3]
            numbered = re.match(r'^(\d+)\. (.+)$', title)
            number, name = int(numbered[1]), numbered[2]
            return f'<section class="chapter operation-section" id="{section_id}" aria-labelledby="{section_id}-heading"><header class="chapter-heading"><span class="chapter-number">{number:02d}</span><div><h3 id="{section_id}-heading">{name}</h3></div></header><div class="chapter-body operation-section-body">{content}</div></section>'
        operations_content = re.sub(r'<h3 class="subheading" id="(operations-\d+)">(.*?)</h3>(.*?)(?=<h3 class="subheading" id="operations-\d+">|\Z)', operation_block, operations_content, flags=re.S)
        operations_html = '<section class="operations" id="operations" aria-labelledby="operations-heading"><header class="operations-heading"><span class="page-part-number">01</span><div><h2 id="operations-heading">운영계획</h2><p>준비부터 진행·학습 확인·기록까지</p></div></header><div class="operations-body">' + operations_content + '</div></section>'
        operations_nav = '<div class="operations-nav"><a class="nav-link page-part-link" href="#operations"><span>01</span>운영계획</a><div class="nav-group"><div class="nav-label">세션 운영</div>' + ''.join(operations_sidebar) + '</div></div>'

    h2s = list(re.finditer(r'^### (.+)$', source, re.M))
    sections = []
    chapters = []
    for j, match in enumerate(h2s):
        end = h2s[j + 1].start() if j + 1 < len(h2s) else len(source)
        body = source[match.end():end]
        chapter_match = re.match(r'^(\d+)\. (.+)$', match[1])
        if not chapter_match:
            sections.append((match[1], body))
            continue
        number, name = int(chapter_match[1]), chapter_match[2]
        goal_match = re.search(r'^#### 학습 목표\s*\n(.*?)(?=^#### |\Z)', body, re.M | re.S)
        outcome_match = re.search(r'^#### 도달 기준\s*\n(.*?)(?=^#### |\Z)', body, re.M | re.S)
        goal_html = ''
        if goal_match or outcome_match:
            goal_html = '<div class="learning-goal">'
            if goal_match:
                goal_html += '<div class="goal-line"><span class="goal-label">학습 목표</span><div>' + render(goal_match[1]) + '</div></div>'
            if outcome_match:
                goal_html += '<div class="goal-line"><span class="goal-label">도달 기준</span><div>' + render(outcome_match[1]) + '</div></div>'
            goal_html += '</div>'
        body = re.sub(r'^#### (학습 목표|도달 기준)\s*\n.*?(?=^#### |\Z)', '', body, flags=re.M | re.S)
        body = re.sub(r'^#### 학습 내용\s*\n', '', body, flags=re.M)
        content = render(body, model=True)
        section = f'<section class="chapter" id="chapter-{number}" aria-labelledby="heading-{number}"><header class="chapter-heading"><span class="chapter-number">{number:02d}</span><div><h3 id="heading-{number}">{inline(name)}</h3></div></header><div class="chapter-body">{goal_html}<div class="content-label">학습 내용 <span>위에서 아래로 권장 학습 순서</span></div>{content}</div></section>'
        subsections = [{'id': f'chapter-{n}-{letter.lower()}', 'label': f'{n}-{letter}', 'name': label} for n, letter, label in re.findall(r'^#### (\d+)-([A-Z])\. (.+)$', body, re.M)]
        entry = {'number': number, 'name': name, 'html': section, 'subsections': subsections}
        chapters.append(entry)

    chapter_range = f'{chapters[0]["number"]}–{chapters[-1]["number"]}장' if chapters else ''
    nav = '<div class="nav-group"><div class="nav-label">학습 과정 · ' + chapter_range + '</div>'
    for ch in chapters:
        nav += f'<a class="nav-link" href="#chapter-{ch["number"]}"><span>{ch["number"]:02d}</span>{inline(ch["name"])}</a>'
        if ch['subsections']:
            nav += '<div class="nav-subsections">' + ''.join(f'<a class="nav-link nav-sub-link" href="#{sub["id"]}"><span>{sub["label"]}</span>{inline(sub["name"])}</a>' for sub in ch['subsections']) + '</div>'
    nav += '</div>'
    part_html = ''.join(ch['html'] for ch in chapters)
    references, ref_nav, study_intro_references = '', '', ''
    special_ids = {'개념 유형 구분': 'taxonomy'}
    ordered_sections = enumerate(sections)
    for index, (name, body) in ordered_sections:
        section_id = special_ids.get(name, f'reference-{index}')
        reference_html = f'<details class="reference" id="{section_id}"><summary>{inline(name)}</summary><div class="reference-body">{render(body)}</div></details>'
        if section_id == 'taxonomy':
            study_intro_references += reference_html
        else:
            references += reference_html
        ref_nav += f'<a href="#{section_id}">{inline(name)}</a>'

    script = r'''
document.querySelectorAll('.point-examples').forEach(group=>{
 const tabs=[...group.querySelectorAll('[role="tab"]')];
 const panels=[...group.querySelectorAll('[role="tabpanel"]')];
 const select=tab=>{
  tabs.forEach(t=>{const active=t===tab;t.setAttribute('aria-selected',String(active));t.tabIndex=active?0:-1});
  panels.forEach(panel=>panel.hidden=panel.id!==tab.getAttribute('aria-controls'));
 };
 tabs.forEach((tab,index)=>{
  tab.addEventListener('click',()=>select(tab));
  tab.addEventListener('keydown',event=>{
   let next;
   if(event.key==='ArrowRight')next=(index+1)%tabs.length;
   else if(event.key==='ArrowLeft')next=(index-1+tabs.length)%tabs.length;
   else if(event.key==='Home')next=0;
   else if(event.key==='End')next=tabs.length-1;
   else return;
   event.preventDefault();select(tabs[next]);tabs[next].focus();
  });
 });
});
const chapters=[...document.querySelectorAll('.chapter, .operations, .study-items')];
const links=[...document.querySelectorAll('.nav-link')];
const observer=new IntersectionObserver(entries=>{const visible=entries.filter(e=>e.isIntersecting).sort((a,b)=>b.boundingClientRect.top-a.boundingClientRect.top);if(!visible.length)return;const id=visible[0].target.id;links.forEach(a=>{const active=a.hash==='#'+id;a.classList.toggle('active',active);if(active)a.setAttribute('aria-current','location');else a.removeAttribute('aria-current')})},{rootMargin:'-12% 0px -65% 0px',threshold:0});
chapters.forEach(c=>observer.observe(c));
document.querySelectorAll('.nav-small a').forEach(a=>a.addEventListener('click',()=>{const el=document.querySelector(a.hash);if(el?.tagName==='DETAILS')el.open=true}));
let closedBeforePrint=[];
window.addEventListener('beforeprint',()=>{closedBeforePrint=[...document.querySelectorAll('details:not([open])')];closedBeforePrint.forEach(d=>d.open=true)});
window.addEventListener('afterprint',()=>closedBeforePrint.forEach(d=>d.open=false));
document.querySelector('#print').addEventListener('click',()=>window.print());
if(location.protocol.startsWith('http')&&['127.0.0.1','localhost'].includes(location.hostname)){
 const version=document.querySelector('meta[name="roadmap-version"]').content;
 const previous=sessionStorage.getItem('roadmap-scroll');
 if(previous!==null){sessionStorage.removeItem('roadmap-scroll');requestAnimationFrame(()=>window.scrollTo(0,Number(previous)))}
 setInterval(async()=>{try{const r=await fetch('/__roadmap_version',{cache:'no-store'});if(!r.ok)return;const data=await r.json();if(data.version&&data.version!==version){sessionStorage.setItem('roadmap-scroll',String(scrollY));location.reload()}}catch{}},2000);
}
'''
    page = f'''<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light"><meta name="roadmap-version" content="{version}"><link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='7' fill='%233e5acd'/%3E%3C/svg%3E"><title>{inline(title)}</title><style>{css}</style></head><body>
<aside class="sidebar" aria-label="로드맵 목차"><a class="brand" href="#top"><span class="brand-icon">KCVL</span><span class="brand-title">{inline(title)}</span></a><p class="sidebar-subtitle">운영계획 · 학습 항목</p><nav aria-label="장별 이동">{operations_nav}<div class="study-nav"><a class="nav-link page-part-link" href="#study-items"><span>02</span>학습 항목</a>{nav}</div></nav><div class="nav-small">{ref_nav}</div><div class="sidebar-note">장 안의 항목은 위에서 아래로.<br>필수부터 시작하고 중요로 확장하세요.</div></aside>
<main class="main" id="top"><header class="hero"><div class="hero-top"><div class="eyebrow">KCVL · NEW STUDENT STUDY PLAN</div><button class="print" id="print" type="button">인쇄 / PDF</button></div><h1>{inline(title)}</h1><p class="hero-description">운영계획과 실제 학습할 항목을 두 파트로 정리했습니다.</p></header>
{operations_html}<section class="study-items" id="study-items" aria-labelledby="study-items-heading"><header class="study-items-heading"><span class="page-part-number">02</span><div><h2 id="study-items-heading">학습 항목</h2><p>신경망 기초부터 생성 모델까지 · 0–4장</p></div></header><div class="study-items-body"><p class="study-items-intro">각 모델의 구조·수식·학습·구현을 함께 살펴보며, 원리가 밀접하게 연결된 후속 모델은 주요 변화를 비교합니다.</p>{study_intro_references}{part_html}{references}</div></section>
<footer class="footer"><span>권장 학습 순서이며, 모든 항목이 다음 모델의 필수 선수조건은 아닙니다.</span><a href="{html.escape(source_path.name)}">Markdown 원문 ↗</a></footer>
<script>{script}</script></main></body></html>'''
    if not chapters:
        raise ValueError('숫자로 시작하는 장 제목이 없습니다.')
    assert all(html.escape(name) in page for name, _, _ in topics)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    temporary = output_path.with_suffix('.html.tmp')
    temporary.write_text(page)
    temporary.replace(output_path)
    return {'version': version, 'chapters': len(chapters), 'topics': len(topics)}

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    print(build(args.source, args.output))
