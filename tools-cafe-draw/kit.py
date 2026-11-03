from gen import *
import sys
MODE=sys.argv[1] if len(sys.argv)>1 else 'all'
W,H=(1900 if MODE=='all' else 1500 if MODE=='kt' else 1100),1500
o=mk(W,H,{'all':'로뎀카페 간이주방 · 창고 (안)','kt':'⑧ 로뎀카페 간이주방 (안)','st':'⑨ 로뎀카페 창고 (안)'}[MODE]+' — 11/3 최종 도면 기준','단위 mm · 위에서 본 모습 · 냉동(장)고는 10/20 기물 계약분(그랜드우성 CWSM-1242RF 1,260×800×1,900) · 빨간 글씨 = 확인할 것')
S=0.33;OX=200;OY=230
X=lambda mm:OX+mm*S;Y=lambda mm:OY+mm*S
# 좌표계: 왼쪽 창고(1,670 × 1,648) · 오른쪽 간이주방(2,870 × 2,300) · 위 = 바 쪽(북)
ST_W=1670;ST_H=398+1250;KW=2870;KH=2300;gap=150
T(o,X(0),Y(-130),'위에서 본 모습 (위가 뒤 바 · 바 안 통로 쪽 · 아래가 정면 유리 쪽)',20,900,INK,'start')
if MODE in ('all','st'):
    # 창고
    R(o,X(0),Y(KH-ST_H),ST_W*S,ST_H*S,'#f4efe6',INK,3)
    R(o,X(40),Y(KH-ST_H+40),(ST_W-80)*S,398*S,'#fff',INK,1.5,0,'8 5'); T(o,X(ST_W/2),Y(KH-ST_H+40+230),'앵글장 (원두 · 소모품) — 확정',13,800,G)
    # 우측 = 간이주방으로 뚫림 (문 없음) · 아무것도 안 둠
    o.append(f'<line x1="{X(ST_W)}" y1="{Y(KH-ST_H+40+398+80)}" x2="{X(ST_W)}" y2="{Y(KH-120)}" stroke="#fff" stroke-width="8"/>')
    o.append(f'<line x1="{X(ST_W)}" y1="{Y(KH-ST_H+40+398+80)}" x2="{X(ST_W)}" y2="{Y(KH-120)}" stroke="{G}" stroke-width="1.5" stroke-dasharray="6 4"/>')
    T(o,X(ST_W-40),Y((KH-ST_H+40+398+80+KH-120)/2),'→ 간이주방으로 뚫림 (문 없음) · 여기는 아무것도 안 둠',11,800,G,'middle',-90)
    # door (left wall, 875) swinging in
    o.append(f'<path d="M {X(0)} {Y(KH-200-875)} A {875*S} {875*S} 0 0 0 {X(-875)} {Y(KH-200)}" fill="none" stroke="{MUT}" stroke-width="1.2" stroke-dasharray="4 3"/>')
    o.append(f'<line x1="{X(0)}" y1="{Y(KH-200)}" x2="{X(0)}" y2="{Y(KH-200-875)}" stroke="#fff" stroke-width="5"/>')
    T(o,X(-30),Y(KH-200-437),'문 875 · 밖으로 열림 (11/4 확인)',11,700,G,'end',-90)
    T(o,X(ST_W/2-200),Y(KH-180),'바깥 문 — 자물쇠 · 도어락 (건축위 확인)',11,700,RED)
    DIM(o,X(0),Y(KH+70),X(ST_W),Y(KH+70),'약 1,670 (화장실 폭과 같음)',BL); DIM(o,X(-70),Y(KH-ST_H),X(-70),Y(KH),'약 1,650',BL,10)
    T(o,X(ST_W/2),Y(KH-ST_H-30),'창고',18,900,INK)
# 간이주방
kx=ST_W+gap if MODE=='all' else 0
if MODE in ('all','kt'):
    R(o,X(kx),Y(0),KW*S,KH*S,'#f4efe6',INK,3)
    o.append(f'<line x1="{X(kx)}" y1="{Y(1400)}" x2="{X(kx)}" y2="{Y(KH-120)}" stroke="#fff" stroke-width="8"/><line x1="{X(kx)}" y1="{Y(1400)}" x2="{X(kx)}" y2="{Y(KH-120)}" stroke="{G}" stroke-width="1.5" stroke-dasharray="6 4"/>')
    T(o,X(kx+40),Y(1900),'← 창고로 뚫림 (문 없음)',11,800,G,'start',-90)
    T(o,X(kx+KW/2),Y(-40),'간이주방 21.52㎡ · 지정 타일 마감',18,900,INK)
    # 냉동고 slot: 800 wide × 1,260 tall at top-left
    R(o,X(kx+50),Y(0),800*S,1260*S,'#e8eef5',INK,2,4)
    T(o,X(kx+450),Y(560),'4도어',12,800,INK); T(o,X(kx+450),Y(640),'냉동(장)고',12,800,INK); T(o,X(kx+450),Y(740),'1,260 × 800',10.5,600,MUT); T(o,X(kx+450),Y(820),'× 1,900',10.5,600,MUT)
    T(o,X(kx+450),Y(1000),'문은 → 이쪽',10,700,RED)
    o.append(f'<path d="M {X(kx+850)} {Y(100)} L {X(kx+850)} {Y(1160)}" stroke="{RED}" stroke-width="3"/>')
    # open area 1,120
    T(o,X(kx+850+560),Y(500),'빈 공간 1,120',12,700,MUT); T(o,X(kx+850+560),Y(580),'(작업대 · 선반?)',10.5,600,RED)
    # 바 출입 (top right opening)
    o.append(f'<line x1="{X(kx+KW-550-900)}" y1="{Y(0)}" x2="{X(kx+KW-550)}" y2="{Y(0)}" stroke="#fff" stroke-width="6"/>')
    o.append(f'<line x1="{X(kx+KW-550-900)}" y1="{Y(0)}" x2="{X(kx+KW-550)}" y2="{Y(0)}" stroke="{MUT}" stroke-width="1.2" stroke-dasharray="5 4"/>')
    T(o,X(kx+KW-550-450),Y(60),'↑ 바 안 통로로 (문 — 자물쇠 · 도어락 확인)',11,700,RED)
    # 550 column top-right
    R(o,X(kx+KW-550),Y(0),550*S,350*S,'#ddd',INK,1.2); T(o,X(kx+KW-275),Y(200),'기둥 550',9.5,600,MUT)
    # 분전함 bottom
    R(o,X(kx+1200),Y(KH-120),500*S,120*S,'#fff',INK,1.5); T(o,X(kx+1450),Y(KH-40),'분전함',10.5,700,INK)
    # right wall to 홀 (유리 쪽) 2,450 
    DIM(o,X(kx),Y(KH+70),X(kx+KW),Y(KH+70),'2,870 = 800 + 1,120 + 550 (+50)',BL); DIM(o,X(kx+KW+70),Y(0),X(kx+KW+70),Y(KH),'2,300',BL,-10)
    DIM(o,X(kx+50),Y(1260+60),X(kx+850),Y(1260+60),'800',MUT,14,12); DIM(o,X(kx+850),Y(1260+60),X(kx+850+1120),Y(1260+60),'1,120',MUT,14,12)
    T(o,X(kx+KW/2),Y(KH+185),'↓ 정면 유리 · 로비 쪽',13,700,BL)
# notes
NOTES(o,Y(KH)+260,[(BL,'도면: 간이주방 2,870 × 2,300 (21.52㎡ · 타일 마감) · 냉동(장)고 자리 800 × 1,260 (왼쪽 위 모서리, 세로로 세워 둠) · 빈 공간 1,120 · 기둥 550 · 분전함 아래 벽 · 창고는 앵글장(원두 · 소모품) 398 깊이 + 1,250'),
 (G,'기물 계약(10/20): 4도어 냉동(장)고 그랜드우성 CWSM-1242RF 1,260 × 800 × 1,900 → 도면 자리 800 × 1,260에 세로로 들어감 (문이 빈 공간 쪽을 보게)'),
 (G,'11/4 확인: 창고 바깥 문은 밖으로 열림 · 앵글장 자리 맞음 · 창고 오른쪽은 간이주방으로 문 없이 뚫려 있고 아무것도 안 둠'),
 (RED,'확인할 것: 창고 치수(도면에 직접 표기 없음 · 화장실 폭 1,670으로 추정) · 선반 제작은 어디에 (간이주방 빈 공간 1,120 쪽?) — 깊이 · 단수 · 사업단 구매 · 간이주방 바 쪽 문 자물쇠'),
 (MUT,'위 = 뒤 바 · 바 안 통로 쪽 · 아래 = 정면 유리 쪽 · 창고 왼쪽 문은 화장실 쪽 복도로 열림')],W)
save(o,W,H,{'all':'kit.svg','kt':'kitchen.svg','st':'storage.svg'}[MODE])
