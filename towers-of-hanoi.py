'''
Created on Jul 16, 2018

@author: yiyedang
'''
import turtle
from Stack import Stack

class Disk:
    def __init__(self, color, shape, width, x, y):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = color
        self.t = turtle.Turtle()
        self.height = 20
        self.width = width
        self.t.speed(0)
        self.moveto(x, y)
    def moveto(self, x, y):
        self.t.up()
        self.t.goto(x, y)
        self.t.down()
        self.t.shape(self.shape)
        self.t.color(self.color)
        
    def getX(self):
        return self.t.xcor()
    def getY(self):
        return self.t.ycor()     
            
class Pole:
    def __init__(self, x):
        self.x = x
        self.stack = Stack()
        
def draw_rectangle(t, color, width, height):
    t.color(color, color)
    t.begin_fill()
    for i in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

def draw_bk(t, l):
    t.pensize(1)
    t.speed(0)
    t.up()
    t.goto(-300, -100)
    t.down()
    draw_rectangle(t, '#804000', l, 30)
    t.up()
    t.left(90)
    t.forward(l // 20)
    t.right(90)
    t.forward(80)
    t.down()
    for i in range(3):
        draw_rectangle(t, 'brown', 5, 200)
        t.up()
        t.forward((l-160 - 5.0) // 2.0)
        t.down()
        
def move_disk(source, target, disks):
    tower1 = source.stack
    tower2 = target.stack
    if tower1.size() > 0:
        tower2.push(tower1.pop())
        for i in range(len(disks)):
            disk = disks[i]
            if disk.getX() == source.x:
                size = tower2.size()
                disk.moveto(target.x, -60 + (size - 1)* 20)
                break
                                    
def hanoi(n, source, helper, target, disks):
    if n > 0:
        hanoi(n - 1, source, target, helper, disks)
        move_disk(source, target, disks)
        print(source.stack, helper.stack, target.stack)
        hanoi(n - 1, helper, source, target, disks)
      
bk_t = turtle.Turtle()
wn = turtle.Screen()
draw_bk(bk_t, 600)
colormap = ['#FE007F','#96D7A0','#F88379','#ABE3E5','#C5A3FF',
                '#6FC0AB','#FFB114', '#F3F298', '#F8C5D0']
disks = []
n = int(input("How many disks would you like to have? (0 < n < 10) "))

for i in range(n, 0, -1):
    width = 10 * (i + 1)
    wn.register_shape('rectangle' + str(i), ((-10,-width),(-10,width),(10,width),(10,-width)))
    t = Disk(colormap[i - 1], 'rectangle' + str(i), 20 *(i + 1), -220, -60 + 20*(n-i))
    disks.insert(0, t)

source = Pole(-220)
helper = Pole(0)
target = Pole(220)
for i in range(n, 0, -1):
    source.stack.push(i)

hanoi(n,source,helper,target, disks)
#print(target.x)
wn.exitonclick()




