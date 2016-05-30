# HANYANG UNIV. PYTHON GAME PROJECT

### Title : 프로한양러 by 3조
------------------------------------
신입한양러가 한양대에 적응한다는 컨셉을 베이스로한 게임.

기본적으로는 4가지 미니게임을 모두 클리어 하면 끝이 난다 ㅋㅋㅋㅋㅋㅋ

Dodge(탄막게임), Avoid(피하기게임), Mine(지뢰찾기), Rhythm(원라인 리듬게임)
등의 미니게임이 들어있다.

베이스로는 횡스크롤의 게임이 있고 진행 중 미니게임을 만나게 된다.
## TODO Checklist
### 베이스
---------------------------------
- [x] Box Collider 구현
- [x] Circle Collder 구현
- [x] Player Controller 구현
- [x] Top View Controller 구현
- [x] Image Component 구현
- [x] Button Component, Object 구현
- [x] Speech 구현
- [ ] MoveMap Component 구현
- [ ] Map 수치화.
- [ ] Data Compression
- [ ] Map 설계

###그래픽
----------------------------------
- [ ] Player Image
- [ ] Start Map Images
- [ ] End Map Images
- [ ] Base Player Image

- [ ] Rhythm Note Image
- [ ] Rhythm Effect Image
- [ ] Rhythm Background Image

- [ ] Dodge Player Image
- [ ] Dodge Bullet Image
- [ ] Dodge Background Image

- [ ] Mine Image
- [ ] Mine Digit Image
- [ ] Mine Block Image

- [ ] Avoid Background Image
- [ ] Avoid Ball Image
- [ ] Avoid Player Image

### Dodge
----------------------------------
- [x] Bullet Controller
- [x] Collision(Player, Bullet)
- [ ] Optimization
  - [x] Apply numpy  
  - [ ] Optimizing calling components
    - [x] Image, Bullet, Collider Container 
    - [x] Random Key Dictionary to Simple List
    - [ ] ...
- [x] Bullet Scenario Making script
- [x] Bullet Scenario Struct
- [ ] Bullet variation
- [ ] Improve graphic

### Mine
-----------------------------------
- [x] 지뢰찾기 게임에 대한 이해
- [x] 타일 작성
- [x] 클릭 시 퍼져 나가는 기능
- [x] 지뢰를 깃발로
- [ ] 그래픽 적용

### Avoid
-----------------------------------
- [x] 좌우 움직임
- [x] 장애물 생성 및 판정
- [ ] 장애물 시나리오 작성

### Rhythm
-----------------------------------
- [x] 인터페이스 작업
- [ ] 모션트윈
- [ ] 노트 이미지 이동
- [x] 노트 이미지 삽입
- [ ] 정확도 판정
- [ ] 콤보 구현
