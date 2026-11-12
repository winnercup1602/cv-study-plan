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

## 세션 노트

각 회차의 **노트 링크 등록**에서 웹 주소와 참가자 등록 코드를 입력합니다. 등록한 URL은 공개 로드맵의 같은 회차에서 바로 열 수 있습니다. 원본 자료의 열람 권한은 원본 서비스에서 관리합니다.

링크 옆 **수정 / 삭제**에서 주소를 바꾸거나 링크를 목록에서 삭제할 수 있습니다. 참가자 등록 코드를 아는 사람은 등록된 링크를 관리할 수 있습니다.

노트는 회차 번호를 기준으로 Google Apps Script의 스크립트 속성에 저장됩니다. 날짜 변경이나 GitHub Pages 재배포와 별도로 유지됩니다.

- 서버 코드: `work/session-notes.gs`
- 페이지 코드와 웹 앱 주소: `work/session-notes.js`
- 등록 코드: Apps Script 프로젝트 설정의 스크립트 속성 `registrationCode`. 코드는 참가자에게만 공유합니다.

서버를 수정할 때는 Apps Script의 `Code.gs`에 적용한 뒤 기존 웹 앱 배포를 새 버전으로 갱신합니다. 웹 앱은 배포자 권한으로 실행하며 공개 목록 조회를 위해 모든 사용자가 접근할 수 있도록 설정합니다. 서버는 등록·수정·삭제 시 참가자 코드를 확인합니다.
