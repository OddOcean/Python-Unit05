############################################################
#     Aidan Weygandt                        04.23.21       #
#     Unit 5 Problems                                      #    
#     Random Turtle                                        #
############################################################
import turtle
import random
t = turtle
ran = random
t.speed(0)
print ("Problem #6 - Random Turtle")
rgb = ""
def new_color(): #returns random color when called
  r = hex(ran.randint(0, 255))[2:]
  while r[1:] == "": #incase i receice one digit hex
    r = hex(ran.randint(0, 255))[2:]
  g = hex(ran.randint(0, 255))[2:]
  while g[1:] == "":  
    g = hex(ran.randint(0, 255))[2:]
  b = hex(ran.randint(0, 255))[2:]
  while b[1:] == "":
    b = hex(ran.randint(0, 255))[2:]
  rgb = "#" + str(r) + str(g) + str(b)
  return rgb
def shape(sides, size): #makes any equal sided shape
  t.color(new_color())
  for each in range(0, int(sides)): #repeats for each side of shape
    t.pendown()
    t.forward(int(size))
    t.right(360/int(sides))
    t.penup()
def r_tri(): #makes right triangle
  t.color(new_color())
  t.fillcolor(rgb)
  t.begin_fill()
  t.pendown()
  t.forward(60)
  t.right(180-45)
  t.forward((60**2/2)**0.5)
  t.right(90)
  t.forward((60**2/2)**0.5)
  t.right(180-45)
  t.end_fill()
  t.penup()
#cartesian grid
t.goto(-300, 0)
t.pendown()
t.goto(300, 0)
t.penup()
t.goto(0, 300)
t.pendown()
t.goto(0, -300)
t.penup()
for each in range(0, 100): #repeats a hundred times for 100 of each shape
  #circle
  t.color(new_color())
  t.goto(random.randint(-289, -11), random.randint(1, 289))
  t.pendown()
  t.circle(10)
  t.penup()
  #equilateral triangle
  t.goto(random.randint(1, 239), random.randint(53, 299))
  shape(3, 60)
  #right triangle
  t.goto(random.randint(-299, -61), random.randint(-239, -1))
  r_tri()
  #lines
  t.color(new_color())
  t.goto(random.randint(1, 299), random.randint(-299, -1))
  t.pendown()
  t.goto(random.randint(1, 299), random.randint(-299, -1))
  t.penup()