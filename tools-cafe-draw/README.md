# 로뎀카페 공간 그림 도구
- 치수 기준: gsmch-1f-cafe-spec.json (도면 ELE.01·02·02'·03·04 + 11/3 평면 + 기물 치수)
- 그림: bar3d.py front|back (6·7 3D 칸 구성) · hall.py(1 홀) el2.py(2 앞 바) frontwall.py(3 정면) plan.py(5 평면) el2b.py(6 뒤 바) el4.py(7 끝 벽) kit.py(8·9 간이주방·창고: all|kt|st) el3.py(10 창 쪽)
- 덧그리기: OVL='[{"view":"el2","type":"person","x":4200,"h":1600,"label":"160cm 여","apron":"#000"},{"view":"el2b","type":"cup","x":5200,"y":924,"n":6,"label":"다회용컵"}]' python3 el2.py
  view: el2 el2b el4 el3 front plan · type: person(x 발 위치, h 키) cup(x,y 상판 높이,n) box(x,y,w,h,label) label
- 렌더: NODE_PATH=/opt/npm-tools/node_modules node r.js el2.svg → el2.png
