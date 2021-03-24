# Todo-Project
## 1. 소개
프로젝트별 관리가 가능한 Todo-List API Server.  
할일은 프로젝트와 단계(Todo, Doing, Done)별로 나누어 관리할 수 있습니다.

## 2. 기술 스텍
* Python 3.8.5
* Django 3.1.4
* DRF(Django Rest Framework) 3.12.2

## 3. 구현 기능
* 회원가입, 로그인, 소셜로그인
* 프로젝트별 관리
* 할일 등록, 조회, 수정, 삭제
  * 카테고리별 필터 제공
  * 마감 날짜 표시
  * 조회수 표시
* 이미지 업로드 기능(효율적인 업로드에 의한 이미지 파이프라인)
* 댓글
* 검색

## 4. 사용 방법
* [permissions.IsAuthenticatedOrReadOnly]  
  적용으로 가입하지 않은 회원은 Todo-List 등록 및 댓글 작성이 불가하며, 조회만 가능합니다.
* http://127.0.0.1:8000/accounts/join  
  회원가입 : email / username / password 3가지 필수 요소.
* http://127.0.0.1:8000/todos/projects  
  프로젝트 : 조회 or 등록
* http://127.0.0.1:8000/todos/list  
  할일(Todo, Doing, Done) : 조회 or 등록
* http://127.0.0.1:8000/todos/users/{user_id}  
  특정 유저 : 프로젝트 조회
