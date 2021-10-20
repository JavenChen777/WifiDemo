import turtle
import math
import random
import time
from param_all import *


class main_ui():
    def __init__(self):
        self.t = turtle.Turtle()
        self.screen = turtle.Screen()
        self.screen.setup(1400, 900)
        self.screen.title('WIFI 6E general introduce')
        # self.screen.screensize(bg='black')
        self.screen.bgpic('ax_bg.gif')
        self.screen.update()
        self.screen.cv._rootwindow.resizable(False, False) #禁用修改尺寸
        self.x, self.y = self.screen.window_width(), self.screen.window_height()
        # print(self.x, self.y)

        self.t.ht()
        self.w_title(-40, 300)
        self.button_lists()
        self.draw_wifi(500, -400)

        # self.screen.onclick(self.turtle_goto)
        self.screen.onclick(self.click_subtitle)
        turtle.done()

    def button(self, x, y, but_name):
        self.turtle_goto(x, y)
        self.t.color('black')
        self.t.write(but_name, align='left', font=('calibri', '50', 'bold'))
        print(self.t.position())

    def turtle_goto(self, x, y):
        self.t.ht()
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()
        print("Now position:", x, y)

    def w_title(self, x, y):
        self.t.ht()
        self.turtle_goto(x, y)
        self.t.color('blue')
        self.t.write('WIFI 6E', align='center', font=('Imprint MT Shadow','70'))

    def button_lists(self):
        turtle.tracer(0)
        self.button(-650, 220, "What's WIFI 6E?")
        self.button(-650, 100, 'The WIFI 6 Frequency')
        self.button(-650, -20, 'The WiFi 6E Benefits')
        self.button(-650, -140, 'WIFI Differences')
        self.button(-650, -260, 'WIFI 6E Weakness')
        turtle.tracer(1)

    def detail_write(self, p_detail, d_x=-600, d_y=-100, size='30', color='black'):
        self.t.ht()
        self.turtle_goto(d_x, d_y)
        self.t.color(color)
        self.t.write(p_detail, align='left', font=('calibri', size, 'normal'))

    def attach_pic(self, pic_path):
        self.screen.register_shape(pic_path)
        self.t.shape(pic_path)

    def draw_road(self, x, y, width, t_num: int):
        self.turtle_goto(x, y)
        self.t.setheading(0)
        self.t.color('black')
        self.t.pensize(3)
        self.t.forward(200)
        self.turtle_goto(x, y - width)
        self.t.forward(200)
        self.t.pensize(1)
        self.t.shape("turtle")
        for i in range(t_num):
            yy= random.randint(3, width - 3)
            xx = random.randint(1, 200)
            self.turtle_goto(x + xx, y - yy)
            self.t.stamp()
        turtle.tracer(0)
        self.t.pencolor('red')
        self.turtle_goto(x, y - width / 2)
        self.t.forward(100)
        self.t.shape('turtle')
        self.t.stamp()
        turtle.tracer(1)

    def draw_arc(self,r, color, p_loc_x, p_loc_y):
        self.turtle_goto(p_loc_x, p_loc_y)
        self.t.color(color)
        self.t.begin_fill()
        self.t.forward(r)
        self.t.left(90)
        self.t.circle(r, extent=90, steps=720)
        self.turtle_goto(p_loc_x, p_loc_y)
        self.t.end_fill()
        self.t.setheading(0)

    def draw_cycle(self, ac_r, xx, yy, color, new_r=40, offset_r=40):# ac_r 最大半径
        offset = math.sqrt(ac_r*ac_r/2)
        new_xx = xx + offset
        new_yy = yy + offset
        self.turtle_goto(new_xx, new_yy-offset_r)
        self.t.begin_fill()
        self.t.color(color)
        self.t.circle(new_r, 360, 720)
        self.t.end_fill()

    def write_six(self, ac_r, color, x, y):
        offset = math.sqrt(ac_r * ac_r / 2)
        new_x = x + offset
        new_y = y + offset
        self.t.pencolor(color)
        self.t.pensize(7)
        self.t.left(70)
        self.turtle_goto(new_x + 10, new_y + 4)
        for i in range(1, 100):
            if i < 10:
                self.t.left(6)
                self.t.penup()
                self.t.forward(1)
            elif 10 <= i <33:
                self.t.left(6)
                self.t.pendown()
                self.t.forward(1)
            elif 33 <= i < 50:
                self.t.left(1)
                self.t.forward(1)
            elif 50 <= i < 80:
                self.t.left(6)
                self.t.forward(1)
            elif i >= 80:
                self.t.left(7)
                self.t.forward(1)

    def write_e(self, x, y):
        self.turtle_goto(x+95, y+40)
        self.t.color('black')
        self.t.setheading(0)
        self.t.begin_fill()
        self.t.forward(25)
        for i in range(2):
            self.t.left(90)
            self.t.forward(7)
            self.t.left(90)
            self.t.forward(17)
            self.t.right(90)
            self.t.forward(12)
            self.t.right(90)
            self.t.forward(17)
        self.t.left(90)
        self.t.forward(7)
        self.t.left(90)
        self.t.forward(25)
        self.t.left(90)
        self.t.forward(46)
        self.t.end_fill()

    def draw_wifi(self, xx, yy):
        turtle.tracer(0)
        for i in range(80, 10, -10):
            color = 'black'
            if i % 20 != 0:
                color = 'white'
            self.draw_arc(i, color, xx, yy)

        new_co = 'white'
        self.draw_cycle(80, xx, yy, new_co)
        new_c = 'black'
        self.draw_cycle(80, xx, yy, new_c, new_r=30, offset_r=30)
        # self.draw_cycle(80, xx, yy, new_co, new_r=-10, offset_r=0)
        self.write_six(80, new_co, xx, yy)
        self.write_e(xx, yy)
        turtle.tracer(1)

    def click_subtitle(self, t_x, t_y):
        subt_locs = [WHAT_RANGE, FREQUNCE_RANGE, BENIFY_RANGE, DIFF_RANGE, WEAK_RANGE]
        for loc in subt_locs:
            # print(t_x, t_y)
            # print('got param:', loc[0][0], loc[0][1], loc[1][0], loc[1][1])
            if loc[0][0] <= t_x <= loc[0][1] and loc[1][0] <= t_y <= loc[1][1]:
                self.screen.reset()
                if loc == WHAT_RANGE:
                    self.detail_write(WIFI_6E, d_y=-200, size='28')
                if loc == FREQUNCE_RANGE:
                    self.attach_pic('freq.gif')
                if loc == BENIFY_RANGE:
                    self.attach_pic('benefits.gif')
                if loc == DIFF_RANGE:
                    self.attach_pic('diff.gif')
                if loc == WEAK_RANGE:
                    self.detail_write(WEAKNESS, d_y=-200, size='35')

        if MAIN_RANGE[0][0] <= t_x <= MAIN_RANGE[0][1] and MAIN_RANGE[1][0] <= t_y <= MAIN_RANGE[1][1]:
            self.screen.reset()
            self.w_title(-40, 300)
            self.button_lists()

        #显示频率的图片
        if FREQUNCE_W_RANGE[0][0] <= t_x <= FREQUNCE_W_RANGE[0][1] and FREQUNCE_W_RANGE[1][0] <= t_y <= FREQUNCE_W_RANGE[1][1]:
            self.detail_write(WIFI_FREQUNCE, d_x=250, d_y=0, size='22', color='blue')

        #显示距离与速度的图片
        if DISTANCE_RANGE[0][0] <= t_x <= DISTANCE_RANGE[0][1] and DISTANCE_RANGE[1][0] <= t_y <= DISTANCE_RANGE[1][1]:
            self.screen.reset()
            self.attach_pic('distance.gif')

        if ROAD_RANGE[0][0] <= t_x <= ROAD_RANGE[0][1] and ROAD_RANGE[1][0] <= t_y <= ROAD_RANGE[1][1]:
            self.detail_write('2.4G:', -370, 310, '50')
            self.draw_road(-400, 300, 100, 20)
            time.sleep(1)
            self.detail_write('5G:', -360, 10, '50')
            self.draw_road(-400, 0, 300, 19)
            time.sleep(1)
            self.detail_write('6G:', 40, 310, '50')
            self.draw_road(0, 300, 600, 5)
            time.sleep(1)
            self.detail_write(WIFI_FREQUNCE, d_x=250, d_y=0, size='22', color='blue')
