from gen import *
import sys
MODE=sys.argv[1]  # back | front
S=0.24;OX=120
def cells(o,X,Y0,H,segs,fill='#efe3cf',c='#8a6a1a'):
    x=0
    for w,lab in segs:
        R(o,X(x),Y0,w*S,H*S,fill,INK,1.3)
        for i,l in enumerate(lab.split('|')): T(o,X(x+w/2),Y0+H*S/2+4+(i-(len(lab.split('|'))-1)/2)*15,l,10,800,c)
        DIM(o,X(x),Y0+H*S+22,X(x+w),Y0+H*S+22,f'{w:,}',BL,16,11);x+=w
    return x
if MODE=='back':
    W,H=1900,1150
    o=mk(W,H,'⑦ 뒤 바 — 칸 구성 · 상판 기물 (3D 시안 「뒤 바 · 벽 쪽 정면」 기준)','단위 mm · 왼쪽 = 간이주방 쪽 · 오른쪽 = 창 쪽 · 3D 표기 치수 그대로 · 3D 상판 높이 860 (도면 ELE.02\' 하부장 924와 다름 — 확인)')
    X=lambda mm:OX+mm*S
    segs=[(600,'오픈 선반장|2단'),(950,'싱크|(수전)'),(400,'서랍장'),(350,'오픈'),(1250,'1200 냉장고|2도어'),(450,'2단 서랍장|소스 · 시럽'),(950,'900 냉동고'),(736,'오픈 하부'),(889,'제빙기|(스탠드)')]
    # 상판 위 기물 (정면에서 본 높이) — 3D 그림 위치대로
    y0=330;CH=860
    Yg=lambda mm:y0+(CH+900-mm)*S   # 바닥 기준 (상판 860)
    base=Yg(0)
    tot=cells(o,X,Yg(CH),CH,segs)
    # 상판
    R(o,X(-20),Yg(CH)-6,(tot+40)*S,6,WOOD,INK,1)
    def item(x,w,h,lab,fill='#fff'): R(o,X(x),Yg(CH+h),w*S,h*S,fill,INK,1.3,3);T(o,X(x+w/2),Yg(CH+h)-6,lab,10,800,INK)
    item(600+330,290,330,'수전 · 싱크','#dbe9f7');item(1550+120,212,557,'그라인더');item(1550+340,150,230,'템핑');item(2300+150,990,540,'커피머신 3그룹');item(3330,243,553,'온수기');item(3590,120,350,'컵');item(4650+350,330,330,'가루통 2','#cfe0f5')
    # 제빙기 standing (889 칸)
    R(o,X(5936),Yg(CH+900),889*S,(CH+900)*S,'#fff',INK,1.5,3);T(o,X(5936+444),Yg(CH+450),'제빙기 스탠드',11,800,INK);T(o,X(5936+444),Yg(CH+300),'850 · 920 (3D 표기)',9.5,700,MUT)
    # 상부 선반 2,300×300 · 상판에서 650
    sx=2300+150+300
    R(o,X(sx),Yg(CH+650+40),2300*S,40*S,WOOD,INK,1.2);T(o,X(sx+1150),Yg(CH+650+40)-8,'상부 선반 2,300 × 300 (깊이) · 상판에서 650',11,800,'#6e5a3a')
    DIM(o,X(5700),Yg(CH),X(5700),Yg(CH+650),'650',BL,-10,11)
    o.append(f'<line x1="{X(-100)}" y1="{base}" x2="{X(tot+100)}" y2="{base}" stroke="{INK}" stroke-width="3"/>')
    DIM(o,X(-100),Yg(0),X(-100),Yg(CH),'860',BL,10,12)
    DIM(o,X(0),base+70,X(tot),base+70,f'3D 표기 전체 6,945 (칸 합 {tot:,})',BL,18,13)
    NOTES(o,base+110,[(BL,'3D 시안 「뒤 바 · 벽 쪽 정면」: 600 · 950 · 400 · 350 · 1,250 · 450 · 950 · 736 · 889 · 상부 선반 2,300 × 300 · 상판에서 650 · 상판 860 · 제빙기 850/920'),
     (RED,f'확인: 칸 합계 {tot:,} ≠ 3D 전체 표기 6,945 · 상판 860(3D) vs 하부장 924(도면 ELE.02\') · 커피머신이 앞 바 · 뒤 바 3D 둘 다에 있음 — 어느 바인지 · 제빙기 스탠드(뒤 바) vs 언더카운터(앞 바)')],W)
    apply_overlays(o,'back3d',X,Yg);save(o,W,H,'bar3d_back.svg')
else:
    W,H=1900,1150;S=0.235
    o=mk(W,H,'⑥ 앞 바 — 칸 구성 · 상판 기물 (3D 시안 「앞 바 위에서 본 모습」 기준)','단위 mm · 왼쪽 = RETURN/PICK UP (창 쪽) · 오른쪽 = 쇼케이스 (출입구 쪽) · 3D 표기 치수 그대로 · 위 = 위에서 본 상판 · 아래 = 직원 쪽에서 본 하부장 칸')
    X=lambda mm:OX+mm*S
    y0=250;D=875
    Yp=lambda mm:y0+mm*S
    segs=[(500,'2단 오픈장'),(868,'오픈장'),(800,'하부 제빙기'),(1250,'1200 냉장고|2도어'),(400,'오픈|(넉박스)'),(500,'3단 서랍장'),(500,'오픈장'),(1230,'쇼케이스|(하부)'),(50,'')]
    tot=sum(w for w,_ in segs)
    R(o,X(0),Yp(0),tot*S,D*S,'#f6efe0',INK,1.5)
    zones=[(0,1500,'RETURN / PICK UP','#fff3b8'),(1500,200,'','#efe3cf'),(1700,1718,'음료 제조','#fff'),(3418,1400,'ORDER','#fff'),(4818,1230,'쇼케이스','#dbe9f7')]
    for x,w,lab,f in zones: R(o,X(x),Yp(0),w*S,D*S,f,INK,1);T(o,X(x+w/2),Yp(D-60),lab,11,900,'#8a4b12')
    def ti(x,y,w,d,lab,f='#fff'): R(o,X(x),Yp(y),w*S,d*S,f,INK,1.2,3);T(o,X(x+w/2),Yp(y+d/2)+4,lab,9,800,INK)
    ti(1720,120,300,500,'피처린서 · 컵');ti(2040,120,243,353,'온수기');ti(2300,80,990,540,'커피머신 3그룹');ti(3310,120,212,309,'그라인더');ti(3540,120,212,309,'그라인더');ti(3330,520,150,160,'넉박스');ti(4150,250,400,350,'POS')
    DIM(o,X(0),Yp(-30),X(1500),Yp(-30),'1,500',BL,-6,11);DIM(o,X(1500),Yp(-30),X(1700),Yp(-30),'200',BL,-6,10);DIM(o,X(tot+60),Yp(0),X(tot+60),Yp(D),'875',BL,-10,11)
    T(o,X(tot/2),Yp(D+150),'위에서 본 상판 (아래쪽이 손님 쪽)',11,700,MUT)
    y1=Yp(D+260);CH=860;x=0
    for w,lab in segs:
        R(o,X(x),y1,w*S,CH*S,'#efe3cf',INK,1.3)
        for i,l in enumerate(lab.split('|')): T(o,X(x+w/2),y1+CH*S/2+4+(i-(len(lab.split('|'))-1)/2)*15,l,10,800,'#8a4b12')
        if w>60: DIM(o,X(x),y1+CH*S+22,X(x+w),y1+CH*S+22,f'{w:,}',BL,16,11)
        x+=w
    R(o,X(-20),y1-6,(tot+40)*S,6,WOOD,INK,1)
    DIM(o,X(-100),y1,X(-100),y1+CH*S,'860',BL,10,12)
    o.append(f'<line x1="{X(-100)}" y1="{y1+CH*S}" x2="{X(tot+100)}" y2="{y1+CH*S}" stroke="{INK}" stroke-width="3"/>')
    DIM(o,X(0),y1+CH*S+75,X(tot),y1+CH*S+75,f'칸 합 {tot:,} (3D 전체 표기 6,945)',BL,18,13)
    NOTES(o,y1+CH*S+115,[(BL,'3D 시안 「앞 바」: 500 · 868 · 800(하부 제빙기) · 1,250(1200 냉장고) · 400 · 500(3단 서랍장) · 500 · 1,230(쇼케이스) · 50 — RETURN/PICK UP 1,500 + 200 — 상판 기물: 피처린서 · 온수기 · 커피머신 3그룹 · 그라인더 2 · 넉박스 · POS'),
     (RED,f'확인: 칸 합 {tot:,} vs 3D 전체 표기 6,945 · 도면 평면 앞 바 6,295 × 875 · 상판 높이 860(3D) vs 1,050(도면 ELE.02) · 커피머신 어느 바인지(3D는 앞 바 · 뒤 바 둘 다)')],W)
    apply_overlays(o,'front3d',X,Yp);save(o,W,H,'bar3d_front.svg')
