import turtle

def set_screen(bkgcolor):
    window = turtle.Screen()
    window.bgcolor(bkgcolor)
    return window
##################


###################
def draw_triangle(agent,arm):
    for i in range(0,3):
        agent.forward(arm)
        agent.left(120)
###################

def draw_triangle_right(agent,arm):
    corners = []
    for i in range(0,3):
        corners.append(agent.pos())
        agent.forward(arm)
        agent.right(120)
    return corners
###################

def split_block(agent,arm_len,div_able):
    if type(div_able) == type(1):
        if div_able == 0:
            return
        else:
            div_able -= 1
    else:
        return
    basepoint = agent.pos()
    basehed = agent.heading()
    draw_triangle(agent,arm_len)
    arm_len /= 2
    agent.forward(arm_len)
    agent.left(120)
    sec_pos = agent.pos()
    corners = draw_triangle_right(agent,arm_len)

    for i in [basepoint,corners[1],corners[0]]:
        agent.penup()
        agent.goto(i)
        agent.seth(basehed)
        agent.pendown()
        split_block(agent,arm_len,div_able)
###################

def triangle_mess():
    #define window
    window = set_screen("green")

    #define actor
    messy = turtle.Turtle()
    messy.shape("arrow")
    messy.color("blue")
    messy.speed(4)

    #draw your shape
    arm_len = 100
    split_block(messy, arm_len, 3)

    #exit with a mouse click
    window.exitonclick()
####################
triangle_mess()
