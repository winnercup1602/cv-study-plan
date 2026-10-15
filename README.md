# CV 핵심 개념과 모델 스터디 계획

CV의 기초 개념부터 주요 모델까지, 필요성과 동작 원리를 함께 공부하기 위한 스터디 계획입니다.

- [스터디 계획 보기](https://winnercup1602.github.io/cv-study-plan/)
- [Markdown 원문](cv_architecture_roadmap.md)
- 진행: 주 1회, 회당 60분(방학 중에는 주 2회)

## 수정 및 게시

`cv_architecture_roadmap.md`를 수정한 뒤 다음 명령으로 페이지를 생성합니다. Python 3 외에 추가 패키지는 필요하지 않습니다.

```sh
python3 work/build_roadmap_from_md.py
```

생성된 `index.html`과 원문을 함께 `main` 브랜치에 반영하면 GitHub Pages에 자동으로 게시됩니다.

- `index.html`: 스타일과 동작을 포함한 웹 페이지
- `cv_architecture_roadmap.md`: 학습 계획 원문
- `work/build_roadmap_from_md.py`: Markdown을 HTML로 변환
- `work/roadmap.css`: 페이지 스타일
