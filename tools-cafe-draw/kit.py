from gen import *
import sys
MODE=sys.argv[1] if len(sys.argv)>1 else 'all'
W,H=(1900 if MODE=='all' else 1500 if MODE=='kt' else 1100),1500
o=mk(W,H,{'all':'로뎀카페 간이주방 · 창고 (안)','kt':'⑫ 로뎀카페 간이주방 (안)','st':'⑬ 로뎀카페 창고 (안)'}[MODE]+' — 11/3 최종 도면 기준','단위 mm · 위에서 본 모습 · 치수는 11/3 실시설계 평면 · 냉동(장)고 = 10/20 계약 기종 1,260×800×1,900 · 빨간 글씨 = 확인할 것')
S=0.33;OX=200;OY=230
X=lambda mm:OX+mm*S;Y=lambda mm:OY+mm*S
# 좌표계: 왼쪽 창고(1,670 × 1,648) · 오른쪽 간이주방(2,870 × 2,300) · 위 = 바 쪽(북)
ST_W=1670;ST_H=323+398+1250;KW=2870;KH=2300;gap=150
T(o,X(0),Y(-130),'위에서 본 모습 (위가 뒤 바 · 바 안 통로 쪽 · 아래가 정면 유리 쪽)',20,900,INK,'start')
if MODE in ('all','st'):
    # 창고
    R(o,X(0),Y(KH-ST_H),ST_W*S,ST_H*S,'#f4efe6',INK,3)
    R(o,X(40),Y(KH-ST_H+323),(ST_W-80)*S,398*S,'#fff',INK,1.5,0,'8 5'); T(o,X(ST_W/2),Y(KH-ST_H+323+230),'앵글장 (원두 · 소모품) — 도면 점선 · 깊이 398',13,800,G); T(o,X(ST_W/2),Y(KH-ST_H+200),'323 (벽에서)',10,700,BL)
    # 우측 = 간이주방으로 뚫림 (문 없음) · 아무것도 안 둠
    o.append(f'<line x1="{X(ST_W)}" y1="{Y(KH-ST_H+40+398+80)}" x2="{X(ST_W)}" y2="{Y(KH-120)}" stroke="#fff" stroke-width="8"/>')
    o.append(f'<line x1="{X(ST_W)}" y1="{Y(KH-ST_H+40+398+80)}" x2="{X(ST_W)}" y2="{Y(KH-120)}" stroke="{G}" stroke-width="1.5" stroke-dasharray="6 4"/>')
    T(o,X(ST_W-40),Y((KH-ST_H+40+398+80+KH-120)/2),'→ 간이주방으로 뚫림 (문 없음) · 여기는 아무것도 안 둠',11,800,G,'middle',-90)
    # door (left wall, 875) swinging in
    o.append(f'<path d="M {X(0)} {Y(KH-200-875)} A {875*S} {875*S} 0 0 0 {X(-875)} {Y(KH-200)}" fill="none" stroke="{MUT}" stroke-width="1.2" stroke-dasharray="4 3"/>')
    o.append(f'<line x1="{X(0)}" y1="{Y(KH-200)}" x2="{X(0)}" y2="{Y(KH-200-875)}" stroke="#fff" stroke-width="5"/>')
    T(o,X(-30),Y(KH-200-437),'문 875 · 밖으로 열림 (11/4 확인)',11,700,G,'end',-90)
    T(o,X(ST_W/2-200),Y(KH-180),'바깥 문 — 자물쇠 · 도어락 (건축위 확인)',11,700,RED)
    DIM(o,X(0),Y(KH+70),X(ST_W),Y(KH+70),'1,670 (도면)',BL); DIM(o,X(-70),Y(KH-ST_H),X(-70),Y(KH-ST_H+323),'323',BL,10,11); DIM(o,X(-70),Y(KH-ST_H+323),X(-70),Y(KH-ST_H+721),'398',BL,10,11); DIM(o,X(-70),Y(KH-ST_H+721),X(-70),Y(KH),'1,250',BL,10,11); DIM(o,X(-160),Y(KH-ST_H),X(-160),Y(KH),'1,971',BL,10,12)
    T(o,X(ST_W/2),Y(KH-ST_H-30),'창고',18,900,INK)
# 간이주방
kx=ST_W+gap if MODE=='all' else 0
if MODE in ('all','kt'):
    R(o,X(kx),Y(0),KW*S,KH*S,'#f4efe6',INK,3)
    o.append(f'<line x1="{X(kx)}" y1="{Y(1400)}" x2="{X(kx)}" y2="{Y(KH-120)}" stroke="#fff" stroke-width="8"/><line x1="{X(kx)}" y1="{Y(1400)}" x2="{X(kx)}" y2="{Y(KH-120)}" stroke="{G}" stroke-width="1.5" stroke-dasharray="6 4"/>')
    T(o,X(kx+40),Y(1900),'← 창고로 뚫림 (문 없음)',11,800,G,'start',-90)
    T(o,X(kx+KW/2),Y(-130),'',18,900,INK)
    # 냉동고 slot: 800 wide × 1,260 tall at top-left
    R(o,X(kx+50),Y(0),800*S,1250*S,'#e8eef5',INK,2,4)
    T(o,X(kx+450),Y(560),'4도어',12,800,INK); T(o,X(kx+450),Y(640),'냉동(장)고',12,800,INK); T(o,X(kx+450),Y(740),'자리 800 × 1,250 (도면)',10,600,MUT); T(o,X(kx+450),Y(820),'기물 1,260 × 800 × 1,900',10,600,RED)
    T(o,X(kx+450),Y(1000),'문은 → 이쪽',10,700,RED)
    o.append(f'<path d="M {X(kx+850)} {Y(100)} L {X(kx+850)} {Y(1160)}" stroke="{RED}" stroke-width="3"/>')
    # open area 1,120
    T(o,X(kx+850+560),Y(500),'빈 공간 1,120',12,700,MUT); T(o,X(kx+850+560),Y(580),'(작업대 · 선반?)',10.5,600,RED)
    # 바 출입 (top right opening)
    o.append(f'<line x1="{X(kx+KW-900)}" y1="{Y(0)}" x2="{X(kx+KW)}" y2="{Y(0)}" stroke="#fff" stroke-width="6"/>')
    o.append(f'<line x1="{X(kx+KW-900)}" y1="{Y(0)}" x2="{X(kx+KW)}" y2="{Y(0)}" stroke="{INK}" stroke-width="2"/>')
    T(o,X(kx+KW-450),Y(60),'↑ 슬라이딩 도어 900 — 바 안 통로로 (자물쇠 · 도어락 확인)',11,700,RED)
    DIM(o,X(kx+KW-900),Y(-60),X(kx+KW),Y(-60),'900',BL,-6,11)
    # 기둥 550 — 간이주방 바깥 오른쪽 (도면)
    R(o,X(kx+KW+30),Y(0),550*S,550*S,'#ddd',INK,1.2); T(o,X(kx+KW+305),Y(300),'기둥 550',9.5,600,MUT)
    # 분전함 bottom
    R(o,X(kx+1200),Y(KH-120),500*S,120*S,'#fff',INK,1.5); T(o,X(kx+1450),Y(KH-40),'분전함',10.5,700,INK)
    # right wall to 홀 (유리 쪽) 2,450 
    DIM(o,X(kx),Y(KH+70),X(kx+KW),Y(KH+70),'2,870 = 50 + 800 + 1,120 + 900(슬라이딩 도어)',BL); DIM(o,X(kx+KW+70),Y(0),X(kx+KW+70),Y(KH),'2,300',BL,-10)
    DIM(o,X(kx+50),Y(1250+60),X(kx+850),Y(1250+60),'800',MUT,14,12); DIM(o,X(kx+850),Y(1250+60),X(kx+850+1120),Y(1250+60),'1,120',MUT,14,12); DIM(o,X(kx-60),Y(0),X(kx-60),Y(1250),'1,250',MUT,10,11); DIM(o,X(kx-60),Y(1250),X(kx-60),Y(KH),'840 + 벽',MUT,10,10)
    T(o,X(kx+KW/2),Y(KH+185),'↓ 정면 유리 · 로비 쪽',13,700,BL)
# notes
NOTES(o,Y(KH)+260,[(BL,'도면: 간이주방 2,870 × 2,300 = 50 · 냉동(장)고 자리 800 × 1,250 · 빈 공간 1,120 · 슬라이딩 도어 900 · 기둥 550은 바깥 · 냉동고 아래 840'),
 (BL,'창고 1,670 × 1,971 (323 + 앵글장 398 + 1,250) · 왼쪽 벽 문 875'),
 (G,'계약 기종 1,260 × 800 × 1,900 → 자리 800 × 1,250에 세로로 — 1,260이 1,250보다 10 큼 · 확인'),
 (G,'11/4 확인: 바깥 문 밖으로 열림(도면 호는 안쪽) · 앵글장 자리 맞음 · 오른쪽은 간이주방으로 뚫림 · 아무것도 안 둠'),
 (RED,'확인: 냉동고 1,260 vs 자리 1,250 · 선반 제작 위치(간이주방 빈 공간 1,120?) · 바 쪽 문 자물쇠'),
 (MUT,'위 = 뒤 바 · 바 안 통로 쪽 · 아래 = 정면 유리 쪽 · 창고 왼쪽 문은 화장실 쪽 복도로 열림')],W)
save(o,W,H,{'all':'kit.svg','kt':'kitchen.svg','st':'storage.svg'}[MODE])
