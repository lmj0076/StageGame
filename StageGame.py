from bangtal import *
import random


#장면 생성 1280 * 720
scene = Scene('StartGame', 'images/background5.png')
scene1 = Scene('stage 1', 'images/background2.png')
scene_width = 1280
scene_height = 720
scene2 = Scene('stage 2', 'images/background7.png')


#배경음악
sound1 = Sound('sounds/sound1.mp3')
sound1.play(1)
sound2 = Sound('sounds/song2.mp3')
sound3 = Sound('sounds/sound3.mp3')
get = Sound('sounds/get.mp3')


#타이머(stage2)
timer = Timer(0.5)


##############################################
#scene

#강아지 캐릭터
dog3 = Object('images/dog.png')
dog3.locate(scene, 330, 450)
dog3.setScale(0.8)
dog3.show()

    
#title
title = Object('images/title.png')
title.locate(scene, 500, 450)
title.show()


#게임 설명
exp = Object('images/설명2.png')
exp.locate(scene, 330, 30)
exp.setScale(0.5)
exp.show()


#start 버튼
s_btn = Object('images/start.png')
s_btn.locate(scene, int((scene_width - 100) / 2), int(scene_height / 2))
s_btn.setScale(2.0)
s_btn.show()
def s_btn_oMA(x, y, action):
    scene1.enter()
    sound1.stop()
    sound2.play(1)
s_btn.onMouseAction = s_btn_oMA


##############################################
#scene1

#문
door = Object('images/door.png')
door.locate(scene1, 250, 30)
door.setScale(0.2)
door.show()


#end 버튼
e_btn = Object('images/end.png')
e_btn.locate(scene1, 1100, 100)
e_btn.show()
def e_btn_oMA(x, y, action):
    endGame()
e_btn.onMouseAction = e_btn_oMA


#key
key = Object('images/key.png')
key.locate(scene1, 1000, 30)
key.setScale(0.3)
key.hide()


#x
x = Object('images/x2.png')
x.locate(scene1, 650, 400)
x.setScale(0.2)
x.show()


#o
o = Object('images/o2.png')
o.locate(scene1, 1000, 500)
o.setScale(0.2)
o.show()


#세모
t = Object('images/t2.png')
t.locate(scene1, 850, 30)
t.setScale(0.4)
t.show()


#삽
sap = Object('images/삽2.png')
sap.locate(scene1, 300, 400)
sap.show()


#restart 버튼 
rs_btn = Object('images/restart.png')
rs_btn.locate(scene1, 1100, 500)
rs_btn.hide()


#똥
for i in range(9):
    dong = Object('images/똥2.png')
    dong.locate(scene1, 100 + (350 * (i % 3)), 500 - (200 * (i // 3)))
    dong.show()


#강아지 238 * 230
dog = Object('images/dog.png')
dog_width = 230
dog_height = 230

dog_x_ps = int((scene_width - dog_width) / 2)
dog_y_ps = 0

dog.locate(scene1, dog_x_ps, dog_y_ps)
dog.setScale(0.8)
dog.show()


#방향키 버튼
bg = Object('images/background6.png')
bg.locate(scene1, 970, 190)
bg.show()
l_btn = Object('images/left_btn.png')
r_btn = Object('images/right_btn.png')
u_btn = Object('images/up_btn.png')
d_btn = Object('images/down_btn.png')

l_btn.setScale(0.3)
r_btn.setScale(0.3)
u_btn.setScale(0.3)
d_btn.setScale(0.3)

l_btn.locate(scene1, 980, 200)
r_btn.locate(scene1, 1100, 200)
u_btn.locate(scene1, 980, 320)
d_btn.locate(scene1, 1100, 320)

l_btn.show()
r_btn.show()
u_btn.show()
d_btn.show()


#강아지 목숨 count
life_cnt = 5


#restart  버튼 클릭 이밴트
def rs_btn_oMA(x, y, action):
    global life_cnt
    global dog_x_ps
    global dog_y_ps
    life_cnt = 5
    dog_x_ps = int((scene_width - dog_width) / 2)
    dog_y_ps = 0
    dog.locate(scene1, dog_x_ps, dog_y_ps)
    dog.show()
    rs_btn.hide()
rs_btn.onMouseAction = rs_btn_oMA


#똥에 닿으면 이밴트
def a():
    global life_cnt
    if life_cnt > 0:
        for i in range(9):
            if 100 + (350*(i%3)) <= dog_x_ps <= 200 + (300*(i%3)) + (100*0.5) and 500 - (200*(i//3)) <= dog_y_ps <= 500 - (200*(i//3)) + (120*0.7):
                life_cnt -= 1
                showMessage('남은 목숨 >> {}'.format(life_cnt))
            if 100 + (350*(i%3)) <= dog_x_ps + 75 <= 200 + (300*(i%3)) + (100*0.5) and 500 - (200*(i//3)) <= dog_y_ps <= 500 - (200*(i//3)) + (120*0.7):
                life_cnt -= 1
                showMessage('남은 목숨 >> {}'.format(life_cnt))
            if 100 + (350*(i%3)) <= dog_x_ps + 150 <= 200 + (300*(i%3)) + (100*0.5) and 500 - (200*(i//3)) <= dog_y_ps <= 500 - (200*(i//3)) + (120*0.7):
                life_cnt -= 1
                showMessage('남은 목숨 >> {}'.format(life_cnt))
    elif life_cnt == 0:
        showMessage('실패ㅠㅠ 재도전 할래요?')
        dog.hide()
        rs_btn.show()

        
#문에 닿으면 이밴트
def b():
    if key.inHand():
        if 250 <= dog_x_ps + 150 <= 350 and 30 <= dog_y_ps <= 100:
            scene2.enter()
            sound2.stop()
            sound3.play(1)
            timer.start()
        if 250 <= dog_x_ps + 75 <= 350 and 30 <= dog_y_ps <= 100:
            scene2.enter()
            sound2.stop()
            sound3.play(1)
            timer.start()
        if 250 <= dog_x_ps <= 350 and 30 <= dog_y_ps <= 100:
            scene2.enter()
            sound2.stop()
            sound3.play(1)
            timer.start()
    else:
        if 250 <= dog_x_ps + 150 <= 350 and 30 <= dog_y_ps <= 100:
            showMessage('열쇄가 필요해요~')
        if 250 <= dog_x_ps + 75 <= 350 and 30 <= dog_y_ps <= 100:
            showMessage('열쇄가 필요해요~')
        if 250 <= dog_x_ps <= 350 and 30 <= dog_y_ps <= 100:
            showMessage('열쇄가 필요해요~')


#x, o, 세모에 닿으면 이밴트
def c():
    if sap.inHand():
        if 650 <= dog_x_ps <= 650 + 100 and 400 <= dog_y_ps <= 400 + 70:
            x.hide()
        if 650 <= dog_x_ps + 75 <= 650 + 100 and 400 <= dog_y_ps <= 400 + 70:
            x.hide()
        if 650 <= dog_x_ps + 150 <= 650 + 100 and 400 <= dog_y_ps <= 400 + 70:
            x.hide()
        if 850 <= dog_x_ps <= 850 + 100 and 30 <= dog_y_ps <= 30 + 100 + 70:
            t.hide()
            key.show()
        if 850 <= dog_x_ps + 75 <= 850 + 100 and 30 <= dog_y_ps <= 30 + 100 + 70:
            t.hide()
            key.show()
        if 850 <= dog_x_ps + 150 <= 850 + 100 and 30 <= dog_y_ps <= 30 + 100 + 70:
            t.hide()
            key.show()
        if 1000 <= dog_x_ps <= 1000 + 100 and 500 <= dog_y_ps <= 30 + 100 + 70:
            o.hide()
        if 1000 <= dog_x_ps + 75 <= 1000 + 100 and 500 <= dog_y_ps <= 30 + 100 + 70:
            o.hide()
        if 1000 <= dog_x_ps + 150 <= 1000 + 100 and 500 <= dog_y_ps <= 30 + 100 + 70:
            o.hide()



#key 줍기
def key_pick():
    if 1000 <= dog_x_ps + 75 <= 1000 + 100 and 30 <= dog_y_ps <= 30 + 50:
        key.pick()


#삽 줍기
def sap_pick():
    if 300 <= dog_x_ps + 75 <= 300 + 90 and 400 <= dog_y_ps <= 400 + 90:
        sap.pick()


#왼쪽 방향키 - 강아지 좌이동
def l_btn_oMA(x, y, action):
    global dog_x_ps 
    to_x = 0
    global dog_width
    if dog_x_ps < 0:
        to_x = 0
    else:
        to_x = to_x - 20
    dog_x_ps = dog_x_ps + to_x
    a()
    b()
    sap_pick()
    c()
    key_pick()
    dog.locate(scene1, dog_x_ps, dog_y_ps)
l_btn.onMouseAction = l_btn_oMA


#오른쪽 방향키 - 강아지 우이동
def r_btn_oMA(x, y, action):
    global dog_x_ps 
    to_x = 0
    global dog_width
    if dog_x_ps > scene_width - dog_width:
        to_x = 0
    else:
        to_x = to_x + 20
    dog_x_ps = dog_x_ps + to_x
    a()
    b()
    sap_pick()
    c()
    key_pick()
    dog.locate(scene1, dog_x_ps, dog_y_ps)
r_btn.onMouseAction = r_btn_oMA


#위쪽 방향키 - 강아지 위이동
def u_btn_oMA(x, y, action):
    global dog_y_ps 
    to_y = 0
    global dog_hei
    if dog_y_ps > scene_height - dog_height:
        to_y = 0
    else:
        to_y = to_y + 20
    dog_y_ps = dog_y_ps + to_y
    a()
    b()
    sap_pick()
    c()
    key_pick()
    dog.locate(scene1, dog_x_ps, dog_y_ps)
u_btn.onMouseAction = u_btn_oMA


#아래쪽 방향키 - 강아지 아래이동
def d_btn_oMA(x, y, action):
    global dog_y_ps 
    to_y = 0
    global dog_hei
    if dog_y_ps < 0:
        to_y = 0
    else:
        to_y = to_y - 20
    dog_y_ps = dog_y_ps + to_y
    a()
    b()
    sap_pick()
    c()
    key_pick()
    dog.locate(scene1, dog_x_ps, dog_y_ps)
d_btn.onMouseAction = d_btn_oMA


##############################################
#scene2

#간식 선물 상자
box = Object('images/box1.png')
box.locate(scene2, 400, 150)
box.show()
def box_oMA(x, y, action):
    showKeypad("MELON", box)
box.onMouseAction = box_oMA


#end 버튼
end = Object('images/end.png')
end.locate(scene2, int((scene_width - 100) / 2), int(scene_height / 2))
end.setScale(2.0)
end.hide()
def end_oMA(x, y, action):
    endGame()
end.onMouseAction = end_oMA


#암호(간식상자)
def box_onKeypad():
    showMessage("오늘의 간식은 메론~~")
    box.setImage('images/melon.png')
    end.show()
    sound3.stop()
    get.play(0)
box.onKeypad = box_onKeypad


#판
pz = []
for i in range(16):
    piece = Object("images/{}.png".format(str(i+1)))
    piece.locate(scene2, (320 * (i % 4)), 540 - (180 * (i // 4)))
    piece.show()
    pz.append(piece)


#렌덤 number
number = random.randint(1, 14)
numbers = []
def ran_num():
    global number
    for x in numbers:
        if x == number:
            number = random.randint(0, 14)

    numbers.append(number)


#강아지2
dog2 = Object('images/dog.png')
dog2.locate(scene2, 1000, 30)
dog2.show()


#강아지 누르면 판 렙덤 보이기 
def dog2_oMA(x, y, action):
    ran_num()
    pz[number].show()
dog2.onMouseAction = dog2_oMA


#타이머 시작과 판 렌덤 숨기기
def onTimeout():
    timer.set(0.5)
    ran_num()
    pz[number].hide()
    timer.start()
timer.onTimeout = onTimeout


##############################################
startGame(scene)

