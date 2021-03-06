import turtle as t
import math as m
import time as ti
import random as r



t.reset()
t.bgcolor('black')
t.colormode(255)
t.hideturtle()
t.setup(width = 230, height = 430, startx=50.0, starty =200)
t.title("Tetris xD")
tl = 20
up = 0
mudanca = 0
p1 = 0
p2 = 0
p3 = 0
p4 = 0
verif = 0

def quadrado(tam, r, g, b, esp=1, cla="black"):
    t.pensize(esp)
    t.pencolor(cla)
    t.fillcolor(r, g, b)
    t.begin_fill()
    for i in range(4):
        t.forward(tam)
        t.left(90)
    t.end_fill()


def linha_de_quadrados(nq, tl, r, g, b, esp=1, cla='black'):
    t.pensize(esp)
    t.pencolor(cla)
    for i in range(nq):
        quadrado(tl, esp, r, g, b)
        t.forward(tl)
    t.backward(nq * tl)


def quadrado_de_quadrados(nq, tl, r, g, b, esp=1):
    for i in range(nq):
        linha_de_quadrados(nq, tl, esp, r, g, b)
        t.left(90)
        t.forward(tl)
        t.right(90)
    t.right(90)
    t.forward(nq * tl)
    t.left(90)


##PEÃ‡AS

def zero():
    quadrado(tl, r=0, g=0, b=0)
    return 0


def first():
    # nq = 4
    # for i in range(nq):
    #    quadrado(tl,r = 0, g = 240, b = 240)
    #    t.fd(tl)
    # t.backward(nq * tl)
    quadrado(tl, r=0, g=240, b=240)
    return 1


def second():
    ##    nq = 3
    ##    for i in range(nq):
    ##        quadrado(tl,r = 0, g = 0, b = 240)
    ##        t.fd(tl)
    ##    t.backward(nq * tl)
    ##    t.lt(90)
    ##    t.fd(tl)
    ##    t.rt(90)
    ##    quadrado(tl, r = 0, g = 0, b = 240)
    ##    t.rt(90)
    ##    t.fd(tl)
    ##    t.lt(90)
    quadrado(tl, r=0, g=0, b=240)
    return 2


def third():
    ##    nq = 3
    ##    for i in range(nq):
    ##        quadrado(tl,r = 240, g = 160, b = 0)
    ##        t.fd(tl)
    ##        if i == 1:
    ##            t.lt(90)
    ##            t.fd(tl)
    ##            t.rt(90)
    ##            quadrado(tl, r = 240, g = 160, b = 0)
    ##            t.rt(90)
    ##            t.fd(tl)
    ##            t.lt(90)
    ##    t.backward(nq * tl)
    quadrado(tl, r=240, g=160, b=0)
    return 3


def fourth():
    ##    nq = 2
    ##    nq1 = 2
    ##    for i in range(nq):
    ##        quadrado(tl, 240, 240, 0)
    ##        t.fd(tl)
    ##    t.backward(nq * tl)
    ##    t.lt(90)
    ##    t.fd(tl)
    ##    t.rt(90)
    ##    for i in range(nq1):
    ##        quadrado(tl, 240, 240, 0)
    ##        t.fd(tl)
    ##    t.backward(nq * tl)
    ##    t.lt(90)
    ##    t.bk(tl)
    ##    t.rt(90)
    quadrado(tl, r=240, g=240, b=0)
    return 4


def fifth():
    ##    nq = 2
    ##    nq1 = 2
    ##    for i in range(nq):
    ##        quadrado(tl,r = 0, g = 240, b = 0)
    ##        t.fd(tl)
    ##        if i == 0:
    ##            t.lt(90)
    ##            t.fd(tl)
    ##            t.rt(90)
    ##            for i in range(nq1):
    ##                quadrado(tl, r = 0, g = 240, b = 0)
    ##                t.fd(tl)
    ##            t.backward(nq * tl)
    ##            t.lt(90)
    ##            t.bk(tl)
    ##            t.rt(90)
    ##    t.backward(nq * tl)
    quadrado(tl, r=0, g=240, b=0)
    return 5


def sixth():
    ##    nq = 3
    ##    for i in range(nq):
    ##        quadrado(tl,r = 160, g = 0, b = 240)
    ##        t.fd(tl)
    ##        if i == 0:
    ##            t.lt(90)
    ##            t.fd(tl)
    ##            t.rt(90)
    ##            quadrado(tl, r = 160, g = 0, b = 240)
    ##
    ##            t.lt(90)
    ##            t.bk(tl)
    ##            t.rt(90)
    ##    t.backward(nq * tl)
    quadrado(tl, r=160, g=0, b=240)
    return 6


def seventh():
    quadrado(tl, r=240, g=0, b=0)
    return 7


# t.bk(200)

matriz = []
t.tracer(0, 0)
t.rt(90)
t.fd(200)
t.lt(90)
t.bk(105)
for i in range(20):
    matriz.append([])
    for j in range(10):
        matriz[i].append(zero())
        t.fd(tl)
    t.bk(tl * 10)
    t.lt(90)
    t.fd(tl)
    t.rt(90)
    t.update()
t.lt(90)
t.bk(tl * 20)
t.rt(90)


def teclaCima():
    global up, p1, p2, p3, p4
    global mudanca
    mudanca = 1
    if up == 3:
        up = -1
    up += 1
    if peca == 1:
        if up == 1 or up == 3:
            p1 = p1 + 1
            p2 = p2
            p3 = p3 - 1
            p4 = p4 - 2
            if i < 19:
                if i < 18:
                    if i < 17:
                        matriz[i + 3][p1] = first()
                    matriz[i + 2][p2] = first()
                matriz[i + 1][p3] = first()
            matriz[i][p4] = first()
            if mudanca == 1:
                matriz[i][p1 - 1] = zero()
                matriz[i][p3 + 1] = zero()
                matriz[i][p4 + 2] = zero()
                mudanca = 0

        elif up == 0 or up == 2:
            if p4 >= 9:
                p1 = 7
                p2 = 7
                p3 = 7
                p4 = 7
                if i < 19:
                    if i < 18:
                        if i < 17:
                            matriz[i+3][p3+2] = zero()
                        matriz[i+2][p2+2] = zero()
                    matriz[i+1][p1+2] = zero()
            if p1 > 0:
                p1 = p1 - 1
                p2 = p2
                p3 = p3 + 1
                p4 = p4 + 2
            else:
                p1 = p1
                p2 = p2 + 1
                p3 = p3 + 2
                p4 = p4 + 3
                if i < 19:
                    if i < 18:
                        if i < 17:
                            matriz[i + 3][p1] = zero()

                        matriz[i + 2][p1] = zero()

                    matriz[i + 1][p1] = zero()

            if mudanca == 1 and p1 >= 0:
                if i < 19:
                    if i < 18:
                        if i < 17:
                            matriz[i + 3][p1 + 1] = zero()
                        matriz[i + 2][p3 - 1] = zero()
                    matriz[i + 1][p1 + 1] = zero()
                mudanca = 0
            ##InÃ­cio da peÃ§a
            matriz[i][p1] = first()
            matriz[i][p2] = first()
            matriz[i][p3] = first()
            matriz[i][p4] = first()
    elif peca == 2:
        if up == 0:
            if p2 >= 9:
                p1 = 7
                p2 = 8
                p3 = 8
                p4 = 8
                if i < 19:
                    if i < 18:
                        matriz[i+2][p4+1] = zero()
                    matriz[i+1][p4+1] = zero()
            p1 = p1
            p2 = p2 - 1
            p3 = p3
            p4 = p4 + 1
            if i < 19:
                matriz[i + 1][p1] = second()
            matriz[i][p2] = second()
            matriz[i][p3] = second()
            matriz[i][p4] = second()
            if mudanca == 1:
                if i < 19:
                    if i < 18:
                        matriz[i + 2][p4 - 1] = zero()
                    matriz[i + 1][p3] = zero()
                mudanca = 0

        elif up == 1:
            p1 = p1+1
            p2 = p2
            p3 = p3-1
            p4 = p4-2
            if i < 19:
                matriz[i + 1][p3] = second()
                if i < 18:
                    matriz[i + 2][p1] = second()
                    matriz[i + 2][p2] = second()
            matriz[i][p4] = second()
            if mudanca == 1:
                if i < 20:
                    matriz[i][p3 + 1] = zero()
                    matriz[i][p4 + 2] = zero()
                mudanca = 0
        elif up == 2:
            if p1 >= 9:
                p1 = 8
                p2 = 7
                p3 = 7
                p4 = 7
                if i < 18:
                    matriz[i+2][p1+1] = zero()
                matriz[i][p3+1] = zero()
            p1 = p1 + 1
            p2 = p2
            p3 = p3 + 1
            p4 = p4 + 2
            matriz[i][p1] = second()
            matriz[i + 1][p2] = second()
            matriz[i + 1][p3] = second()
            matriz[i + 1][p4] = second()
            if mudanca == 1:
                if i < 18:
                    matriz[i + 2][p1 - 2] = zero()
                    matriz[i + 2][p3] = zero()
                matriz[i][p2] = zero()

                mudanca = 0
        elif up == 3:
            p1 = p1 - 2
            p2 = p2 + 1
            p3 = p3
            p4 = p4 - 1
            if i < 19:
                matriz[i + 1][p3] = second()
                if i < 18:
                    matriz[i + 2][p4] = second()
            matriz[i][p1] = second()
            matriz[i][p2] = second()
            if mudanca == 1:
                if i < 19:
                    matriz[i + 1][p2 - 1] = zero()
                    matriz[i + 1][p4 + 1] = zero()
                matriz[i][p1 + 2] = zero()
                mudanca = 0
    elif peca == 3:
        if up == 0:
            if p2 >=9:
                p1 = 7
                p2 = 8
                p3 = 8
                p4 = 8
                if i < 18:
                    matriz[i+2][p4+1] = zero()
            p1 = p1
            p2 = p2
            p3 = p3 + 1
            p4 = p4 + 1
            if i < 19:
                matriz[i + 1][p4] = third()
            matriz[i][p1] = third()
            matriz[i][p2] = third()
            matriz[i][p3] = third()
            if mudanca == 1:
                if i < 19:
                    if i < 18:
                        matriz[i + 2][p1] = zero()
                        matriz[i + 2][p2] = zero()
                    matriz[i + 1][p2] = zero()
                mudanca = 0
        elif up == 1:
            p1 = p1
            p2 = p2
            p3 = p3 - 2
            p4 = p4 - 2
            if i < 19:
                if i < 18:
                    matriz[i + 2][p4] = third()
                matriz[i + 1][p3] = third()
            matriz[i][p1] = third()
            matriz[i][p2] = third()
            if mudanca == 1:
                if i < 19:
                    matriz[i + 1][p4 + 2] = zero()
                matriz[i][p1 + 2] = zero()
                mudanca = 0
        elif up == 2:
            if p2 >=9:
                p1 = 7
                p2 = 8
                p3 = 7
                p4 = 7
                if i < 18:
                    matriz[i+2][p3+1] = zero()
                matriz[i][p4+2] = zero()
            p1 = p1
            p2 = p2 - 1
            p3 = p3 + 1
            p4 = p4 + 2
            if i < 19:
                matriz[i + 1][p2] = third()
                matriz[i + 1][p3] = third()
                matriz[i + 1][p4] = third()
            matriz[i][p1] = third()
            if mudanca == 1:
                if i < 19:
                    if i < 18:
                        matriz[i + 2][p1] = zero()
                matriz[i][p3] = zero()
                mudanca = 0
        elif up == 3:
            p1 = p1
            p2 = p2 + 1
            p3 = p3
            p4 = p4 - 1
            if i < 19:
                if i < 18:
                    matriz[i + 2][p1] = third()
                    matriz[i + 2][p2] = third()
                matriz[i + 1][p3] = third()
            matriz[i][p4] = third()
            if mudanca == 1:
                if i < 19:
                    matriz[i + 1][p4 + 1] = zero()
                    matriz[i + 1][p1] = zero()
                matriz[i][p1] = zero()
                mudanca = 0
    elif peca == 4:
        if up == 0 or up == 1 or up == 2 or up == 3:
            p1 = p1
            p2 = p2
            p3 = p3
            p4 = p4
            if mudanca == 1:
                mudanca = 0
    elif peca == 5:
        if up == 0 or up == 2:
            if p1 >= 9:
                p1 = 8
                p2 = 8
                p3 = 7
                p4 = 7
                if i < 18:
                    matriz[i+2][p2] = zero()
                matriz[i][p4+2] = zero()
            p1 = p1 -1
            p2 = p2
            p3 = p3 + 1
            p4 = p4 + 2
            if i < 19:
                matriz[i + 1][p2] = fifth()
                matriz[i + 1][p4] = fifth()
            matriz[i][p1] = fifth()
            matriz[i][p3] = fifth()
            if mudanca == 1:
                if i < 19:
                    if i < 18:
                        matriz[i + 2][p1] = zero()
                    matriz[i + 1][p1] = zero()
                mudanca = 0
        elif up == 1 or up == 3:
            p1 = p1 + 1
            p2 = p2
            p3 = p3 - 1
            p4 = p4 - 2
            if i < 19:
                if i < 18:
                    matriz[i + 2][p4] = fifth()
                matriz[i + 1][p3] = fifth()
                matriz[i + 1][p2] = fifth()
            matriz[i][p1] = fifth()
            if mudanca == 1:
                if i < 19:
                    matriz[i + 1][p4 + 2] = zero()
                matriz[i][p1 - 1] = zero()
                mudanca = 0
    elif peca == 6:
        if up == 0:
            if p1 >= 9:
                p1 = 8
                p2 = 8
                p3 = 7
                p4 = 8
                if i < 19:
                    if i < 18:
                        matriz[i+2][p4+1] = zero()
                    matriz[i+1][p4+1] = zero()

            p1 = p1 - 1
            p2 = p2
            p3 = p3 + 1
            p4 = p4 + 1
            if i < 19:
                matriz[i + 1][p3] = sixth()
            matriz[i][p1] = sixth()
            matriz[i][p2] = sixth()
            matriz[i][p4] = sixth()
            if mudanca == 1:
                if i < 19:
                    if i < 18:
                        matriz[i + 2][p2] = zero()
                    matriz[i + 1][p1] = zero()
                mudanca = 0
        elif up == 1:
            p1 = p1
            p2 = p2 - 1
            p3 = p3
            p4 = p4 - 2
            if i < 19:
                if i < 18:
                    matriz[i + 2][p4] = sixth()
                matriz[i + 1][p2] = sixth()
                matriz[i + 1][p3] = sixth()
            matriz[i][p1] = sixth()
            if mudanca == 1:
                matriz[i][p3] = zero()
                matriz[i][p3+1] = zero()
                mudanca = 0
        elif up == 2:
            if p3 >=9:
                p1 = 7
                p2 = 7
                p3 = 8
                p4 = 7
                if i < 18:
                    matriz[i+2][p3] = zero()
            p1 = p1
            p2 = p2 + 1
            p3 = p3
            p4 = p4 + 2
            if i < 19:
                matriz[i + 1][p1] = sixth()
                matriz[i + 1][p2] = sixth()
                matriz[i + 1][p4] = sixth()
            matriz[i][p3] = sixth()
            if mudanca == 1:
                if i < 18:
                    matriz[i + 2][p1] = zero()
                matriz[i][p1] = zero()
                mudanca = 0
        elif up == 3:
            p1 = p1 + 1
            p2 = p2
            p3 = p3 - 1
            p4 = p4 - 1
            if i < 19:
                if i < 18:
                    matriz[i + 2][p4] = sixth()
                matriz[i + 1][p3] = sixth()
                matriz[i + 1][p2] = sixth()
            matriz[i][p1] = sixth()
            if mudanca == 1:
                if i < 19:
                    matriz[i + 1][p2+1] = zero()

                mudanca = 0
    elif peca == 7:
        if up == 0 or up == 2:
            if p1 > 0:
                p1 = p1 - 1
                p2 = p2
                p3 = p3 - 1
                p4 = p4
            else:
                p1 = p1
                p2 = p2 + 1
                p3 = p3
                p4 = p4 + 1
                if i < 19:
                    if i < 18:
                        matriz[i+2][p2] = zero()
                matriz[i][p1] = zero()
            if i < 19 and p1 > 0:
                matriz[i + 1][p1] = seventh()
                matriz[i + 1][p2] = seventh()
            matriz[i][p3] = seventh()
            matriz[i][p4] = seventh()
            if mudanca == 1:
                if i < 19:
                    if i < 18:
                        matriz[i + 2][p4] = zero()
                    matriz[i+1][p4] = zero()
                mudanca = 0
        elif up == 1 or up == 3:
            p1 = p1 + 1
            p2 = p2
            p3 = p3 + 1
            p4 = p4
            if i < 19:
                if i < 18:
                    matriz[i + 2][p4] = seventh()
                matriz[i + 1][p3] = seventh()
                matriz[i + 1][p2] = seventh()
            matriz[i][p1] = seventh()
            if mudanca == 1:
                if i < 19:
                    matriz[i+1][p2-1] = zero()
                matriz[i][p1+1] = zero()
                mudanca = 0
    for x in range(20):
        for j in range(10):
            quad = matriz[x][j]
            if quad == 0:
                zero()
                t.fd(tl)
            elif quad == 1:
                first()
                t.fd(tl)
            elif quad == 2:
                second()
                t.fd(tl)
            elif quad == 3:
                third()
                t.fd(tl)
            elif quad == 4:
                fourth()
                t.fd(tl)
            elif quad == 5:
                fifth()
                t.fd(tl)
            elif quad == 6:
                sixth()
                t.fd(tl)
            else:
                seventh()
                t.fd(tl)
        t.bk(tl * 10)
        t.lt(90)
        t.fd(tl)
        t.rt(90)
    t.lt(90)
    t.bk(tl * 20)
    t.rt(90)
    t.update()
    print(1)
    print(up)



def teclaEsq():
    global p1, p2, p3, p4, peca, up
    if peca == 1:
        if up == 0 or up == 2:
            if p1 > 0:
                if matriz[i][p1 - 1] == 0:
                    matriz[i][p4] = zero()
                    p1 -= 1
                    p2 -= 1
                    p3 -= 1
                    p4 -= 1
                    matriz[i][p1] = first()
                    matriz[i][p2] = first()
                    matriz[i][p3] = first()
                    matriz[i][p4] = first()
        elif up == 1 or up == 3:
            if p4 > 0:
                if matriz[i][p4-1] == 0:
                    if i < 19:
                        if matriz[i+1][p3-1] == 0:
                            if i < 18:
                                if matriz[i+2][p2-1] == 0:
                                    if i < 17:
                                        if matriz[i+3][p1 - 1] == 0:
                                            matriz[i+3][p1] = zero()
                                    matriz[i+2][p2] = zero()
                            matriz[i+1][p3] = zero()
                    matriz[i][p4] = zero()
                    p1 -= 1
                    p2 -= 1
                    p3 -= 1
                    p4 -= 1
                    if i < 19:
                        if i < 18:
                            if i < 17:
                                matriz[i+3][p1] =  first()
                            matriz[i+2][p2] = first()
                        matriz[i+1][p3] = first()
                    matriz[i][p4] = first()
    if peca == 2:
        if up == 0:
            if p1 > 0:
                if matriz[i][p1-1] == 0:
                    if i < 19:
                        if matriz[i+1][p2-1] == 0:
                            if i < 19:
                                matriz[i+1][p2] = zero()
                            matriz[i][p4] = zero()
                            p1 -= 1
                            p2 -= 1
                            p3 -= 1
                            p4 -= 1
                            matriz[i][p1] = second()
                            matriz[i+1][p2] = second()
                            matriz[i][p3] = second()
                            matriz[i][p4] = second()

        elif up == 1:
            if p2 > 0:
                if i < 18:
                    if matriz[i+2][p4-1] == 0 and matriz[i+1][p3-1] == 0 and matriz[i][p2-1] == 0:
                        if i < 19:
                            if i < 18:
                                matriz[i+2][p1] = zero()
                            matriz[i+1][p3] = zero()
                        matriz[i][p2] = zero()
                        p1 -= 1
                        p2 -= 1
                        p3 -= 1
                        p4 -= 1
                        matriz[i+2][p1] = second()
                        matriz[i+2][p4] = second()
                        matriz[i+1][p3] = second()
                        matriz[i][p2] = second()
        elif up == 2:
            if p2 > 0:
                if i < 19:
                    if matriz[i+1][p2-1] == 0 and matriz[i][p4-1] == 0:
                        if i < 19:
                            matriz[i+1][p4] = zero()
                        matriz[i][p1] = zero()
                        p1 -= 1
                        p2 -= 1
                        p3 -= 1
                        p4 -= 1
                        matriz[i][p1] = second()
                        matriz[i+1][p4] = second()
                        matriz[i+1][p3] = second()
                        matriz[i+1][p2] = second()
        elif up == 3:
            if p1 > 0:
                if i < 18:
                    if matriz[i][p1-1] == 0 and matriz[i+1][p3-1] == 0 and matriz[i+2][p4-1] == 0:
                        if i < 19:
                            if i < 18:
                                matriz[i+2][p4] = zero()
                            matriz[i+1][p3] = zero()
                        matriz[i][p2] = zero()
                        p1 -= 1
                        p2 -= 1
                        p3 -= 1
                        p4 -= 1
                        matriz[i][p1] = second()
                        matriz[i][p2] = second()
                        matriz[i+1][p3] = second()
                        matriz[i+2][p4] = second()
    if peca == 3:
        if up == 0:
            if p1 > 0:
                if i < 19:
                    if matriz[i][p1-1] == 0 and matriz[i+1][p4-1] == 0:
                        if i < 19:
                            matriz[i+1][p4] = zero()
                        matriz[i][p3] = zero()
                        p1 -= 1
                        p2 -= 1
                        p3 -= 1
                        p4 -= 1
                        matriz[i][p1] = third()
                        matriz[i][p2] = third()
                        matriz[i][p3] = third()
                        matriz[i+1][p4] = third()

        if up == 1:
            if p1 > 0:
                if i < 18:
                    if matriz[i][p1-1] == 0 and matriz[i+1][p3-1] == 0 and matriz[i][p4-1] == 0:
                        if i < 19:
                            if i < 18:
                                matriz[i+2][p4] = zero()
                            matriz[i+1][p3] = zero()
                        matriz[i][p2] = zero()
                        p1 -= 1
                        p2 -= 1
                        p3 -= 1
                        p4 -= 1
                        matriz[i][p1] = third()
                        matriz[i][p2] = third()
                        matriz[i+1][p3] = third()
                        matriz[i+2][p4] = third()
        if up == 2:
            if p1 > 0:
                if i < 19:
                    if matriz[i][p1-1] == 0 and matriz[i+1][p2-1] == 0:
                        if i < 19:
                            matriz[i+1][p4] = zero()
                        matriz[i][p1] = zero()
                        p1 -= 1
                        p2 -= 1
                        p3 -= 1
                        p4 -= 1
                        matriz[i][p1] = third()
                        matriz[i+1][p2] = third()
                        matriz[i+1][p3] = third()
                        matriz[i+1][p4] = third()
        if up == 3:
            if p1 > 0:
                if i < 18:
                    if matriz[i][p4-1] == 0 and matriz[i+1][p3-1] == 0 and matriz[i+2][p1-1] == 0:
                        if i < 19:
                            if i < 18:
                                matriz[i+2][p4] = zero()
                            matriz[i+1][p3] = zero()
                        matriz[i][p2] = zero()
                        p1 -= 1
                        p2 -= 1
                        p3 -= 1
                        p4 -= 1
                        matriz[i+2][p1] = third()
                        matriz[i][p2] = third()
                        matriz[i+1][p3] = third()
                        matriz[i+2][p4] = third()
    if peca == 4:
        if p1 > 0:
            if i < 19:
                if matriz[i][p1-1] == 0 and matriz[i+1][p2-1] == 0:
                    if i < 19:
                        matriz[i+1][p4] = zero()
                        matriz[i+1][p2] = zero()
                    matriz[i][p1] = zero()
                    matriz[i][p3] = zero()
                    p1 -= 1
                    p2 -= 1
                    p3 -= 1
                    p4 -= 1
                    matriz[i][p1] = fourth()
                    matriz[i+1][p2] = fourth()
                    matriz[i][p3] = fourth()
                    matriz[i+1][p4] = fourth()
    if peca == 5:
        if up == 0 or up == 2:
            if p1 > 0:
                if i < 19:
                    if matriz[i][p1-1] == 0 and matriz[i+1][p2-1] == 0:
                        if i < 19:
                            matriz[i+1][p4] = zero()
                        matriz[i][p2] = zero()
                        p1 -= 1
                        p2 -= 1
                        p3 -= 1
                        p4 -= 1
                        matriz[i][p1] = fifth()
                        matriz[i][p2] = fifth()
                        matriz[i+1][p3] = fifth()
                        matriz[i+1][p4] = fifth()
        if up == 1 or up == 3:
            if p3 > 0:
                if i < 18:
                    if matriz[i][p1-1] == 0 and matriz[i+1][p3-1] == 0 and matriz[i+2][p4-1] == 0:
                        if i < 19:
                            if i < 18:
                                matriz[i+2][p4] = zero()
                            matriz[i+1][p2] = zero()
                        matriz[i][p1] = zero()
                        p1 -= 1
                        p2 -= 1
                        p3 -= 1
                        p4 -= 1
                        matriz[i][p1] = fifth()
                        matriz[i+1][p2] = fifth()
                        matriz[i+1][p3] = fifth()
                        matriz[i+2][p4] = fifth()
    if peca == 6:
        if up == 0:
            if p1 > 0:
                if i < 19:
                    if matriz[i][p1-1] == 0 and matriz[i+1][p3-1] == 0:
                        if i < 19:
                            matriz[i+1][p3] =  zero()
                        matriz[i][p4] = zero()
                        p1 -= 1
                        p2 -= 1
                        p3 -= 1
                        p4 -= 1
                        matriz[i][p1] = sixth()
                        matriz[i][p2] = sixth()
                        matriz[i+1][p3] = sixth()
                        matriz[i][p4] = sixth()
        if up == 1:
            if p1 > 0:
                if i < 18:
                    if matriz[i][p1-1] == 0 and matriz[i+1][p2-1] == 0 and matriz[i+2][p4-1] == 0:
                        if i < 19:
                            if i < 18:
                                matriz[i+2][p4] = zero()
                            matriz[i+1][p3] = zero()
                        matriz[i][p1] = zero()
                        p1 -= 1
                        p2 -= 1
                        p3 -= 1
                        p4 -= 1
                        matriz[i][p1] = sixth()
                        matriz[i+1][p2] = sixth()
                        matriz[i+1][p3] = sixth()
                        matriz[i+2][p4] = sixth()
        if up == 2:
            if p1 > 0:
                if i < 19:
                    if matriz[i+1][p1-1] == 0 and matriz[i][p3-1] == 0:
                        if i < 19:
                            matriz[i+1][p4] = zero()
                        matriz[i][p3] = zero()
                        p1 -= 1
                        p2 -= 1
                        p3 -= 1
                        p4 -= 1
                        matriz[i+1][p1] = sixth()
                        matriz[i+1][p2] = sixth()
                        matriz[i][p3] = sixth()
                        matriz[i+1][p4] = sixth()
        if up == 3:
            if p3 > 0:
                if i < 18:
                    if matriz[i][p1-1] == 0 and matriz[i+1][p3-1] == 0 and matriz[i+2][p4-1] == 0:
                        if i < 19:
                            if i < 18:
                                matriz[i+2][p4] = zero()
                            matriz[i+1][p2] = zero()
                        matriz[i][p1] = zero()
                        p1 -= 1
                        p2 -= 1
                        p3 -= 1
                        p4 -= 1
                        matriz[i][p1] = sixth()
                        matriz[i+1][p2] = sixth()
                        matriz[i+1][p3] = sixth()
                        matriz[i+2][p4] = sixth()
    if peca == 7:
        if up == 0 or up == 2:
            if p1 > 0:
                if i < 19:
                    if matriz[i][p3-1] == 0 and matriz[i+1][p1-1] == 0:
                        if i < 19:
                            matriz[i+1][p3] = zero()
                        matriz[i][p4] = zero()
                        p1 -= 1
                        p2 -= 1
                        p3 -= 1
                        p4 -= 1
                        matriz[i+1][p1] = seventh()
                        matriz[i+1][p2] = seventh()
                        matriz[i][p3] = seventh()
                        matriz[i][p4] = seventh()
        if up == 1 or up == 3:
            if p1 > 0:
                if i < 18:
                    if matriz[i][p1-1] == 0 and matriz[i+1][p2-1] == 0 and matriz[i+2][p4-1] == 0:
                        if i < 19:
                            if i < 18:
                                matriz[i+2][p4] = zero()
                            matriz[i+1][p3] = zero()
                        matriz[i][p1] = zero()
                        p1 -= 1
                        p2 -= 1
                        p3 -= 1
                        p4 -= 1
                        matriz[i][p1] = seventh()
                        matriz[i+1][p2] = seventh()
                        matriz[i+1][p3] = seventh()
                        matriz[i+2][p4] = seventh()
    for x in range(20):
        for j in range(10):
            quad = matriz[x][j]
            if quad == 0:
                zero()
                t.fd(tl)
            elif quad == 1:
                first()
                t.fd(tl)
            elif quad == 2:
                second()
                t.fd(tl)
            elif quad == 3:
                third()
                t.fd(tl)
            elif quad == 4:
                fourth()
                t.fd(tl)
            elif quad == 5:
                fifth()
                t.fd(tl)
            elif quad == 6:
                sixth()
                t.fd(tl)
            else:
                seventh()
                t.fd(tl)
        t.bk(tl * 10)
        t.lt(90)
        t.fd(tl)
        t.rt(90)
    t.lt(90)
    t.bk(tl * 20)
    t.rt(90)
    t.update()

    print(p1)

def teclaDir():
    global p1, p2, p3, p4, peca, up
    if peca == 1:
        if up == 0 or up == 2:
            if p4 < 9:
                if matriz[i][p4 + 1] == 0:
                    matriz[i][p1] = zero()
                    if p4 >= 9:
                        p1 = 6
                        p2 = 7
                        p3 = 8
                        p4 = 9
                    else:
                        p1 +=1
                        p2 +=1
                        p3 +=1
                        p4 +=1
                    matriz[i][p1] = first()
                    matriz[i][p2] = first()
                    matriz[i][p3] = first()
                    matriz[i][p4] = first()
        if up == 1 or up == 3:
            if p1 < 9:
                if i < 17:
                    if matriz[i][p4 + 1] == 0 and matriz[i+1][p3 + 1] == 0 and matriz[i+2][p2 + 1] == 0 and matriz[i+3][p1 + 1] == 0:
                        matriz[i][p1] = zero()
                        matriz[i+1][p2] = zero()
                        matriz[i+2][p3] = zero()
                        matriz[i+3][p4] = zero()
                        p1 +=1
                        p2 +=1
                        p3 +=1
                        p4 +=1
                        matriz[i][p1] = first()
                        matriz[i+1][p2] = first()
                        matriz[i+2][p3] = first()
                        matriz[i+3][p4] = first()
    if peca == 2:
        if up == 0:
            if p4 < 9:
                if i < 19:
                    if matriz[i+1][p2+1] == 0 and matriz[i][p4+1] == 0:
                        matriz[i+1][p2] = zero()
                        matriz[i][p1] = zero()
                        p1 += 1
                        p2 += 1
                        p3 += 1
                        p4 += 1
                        matriz[i][p1] = second()
                        matriz[i+1][p2] = second()
                        matriz[i][p3] = second()
                        matriz[i][p4] = second()
        if up == 1:
            if p1 < 9:
                if i < 18:
                    if matriz[i][p3+1] == 0 and matriz[i+1][p2+1] == 0 and matriz[i+2][p1+1] == 0:
                        matriz[i+2][p4] = zero()
                        matriz[i+1][p3] = zero()
                        matriz[i][p2] = zero()
                        p1 += 1
                        p2 += 1
                        p3 += 1
                        p4 += 1
                        matriz[i][p2] = second()
                        matriz[i+1][p3] = second()
                        matriz[i+2][p4] = second()
                        matriz[i+2][p1] = second()
        if up == 2:
            if p1 < 9:
                if i < 19:
                    if matriz[i][p1+1] == 0 and matriz[i+1][p4+1] == 0:
                        matriz[i][p1] = zero()
                        matriz[i+1][p2] = zero()
                        p1 += 1
                        p2 += 1
                        p3 += 1
                        p4 += 1
                        matriz[i][p1] = second()
                        matriz[i+1][p4] = second()
                        matriz[i+1][p3] = second()
                        matriz[i+1][p2] = second()
        if up == 3:
            if p2 < 9:
                if i < 18:
                    if matriz[i][p2+1] == 0 and matriz[i+1][p3+1] == 0 and matriz[i+2][p4+1] == 0:
                        matriz[i][p1] = zero()
                        matriz[i+1][p3] = zero()
                        matriz[i+2][p4] = zero()
                        p1 += 1
                        p2 += 1
                        p3 += 1
                        p4 += 1
                        matriz[i][p1] = second()
                        matriz[i][p2] = second()
                        matriz[i+1][p3] = second()
                        matriz[i+2][p4] = second()
    if peca == 3:
        if up == 0:
            if p3 < 9:
                if i < 19:
                    if matriz[i+1][p3+1] == 0 and matriz[i][p4+1] == 0:
                        matriz[i+1][p4] = zero()
                        matriz[i][p1] = zero()
                        p1 += 1
                        p2 += 1
                        p3 += 1
                        p4 += 1
                        matriz[i][p1] = third()
                        matriz[i][p2] = third()
                        matriz[i][p3] = third()
                        matriz[i+1][p4] = third()
        if up == 1:
            if p2 < 9:
                if i < 18:
                    if matriz[i][p2+1] == 0 and matriz[i+1][p3+1] == 0 and matriz[i+2][p4+1] == 0:
                        matriz[i][p1] = zero()
                        matriz[i+1][p3] = zero()
                        matriz[i+2][p4] = zero()
                        p1 += 1
                        p2 += 1
                        p3 += 1
                        p4 += 1
                        matriz[i][p1] = third()
                        matriz[i][p2] = third()
                        matriz[i+1][p3] = third()
                        matriz[i+2][p4] = third()
        if up == 2:
            if p4 < 9:
                if i < 19:
                    if matriz[i][p1+1] == 0 and matriz[i+1][p4+1] == 0:
                        matriz[i][p1] = zero()
                        matriz[i+1][p2] = zero()
                        p1 += 1
                        p2 += 1
                        p3 += 1
                        p4 += 1
                        matriz[i][p1] = third()
                        matriz[i+1][p2] = third()
                        matriz[i+1][p3] = third()
                        matriz[i+1][p4] = third()
        if up == 3:
            if p2 < 9:
                if i < 18:
                    if matriz[i][p2+1] == 0 and matriz[i+1][p3+1] == 0 and matriz[i+2][p4+1] == 0:
                        matriz[i+2][p1] = zero()
                        matriz[i+1][p3] = zero()
                        matriz[i][p2] = zero()
                        p1 += 1
                        p2 += 1
                        p3 += 1
                        p4 += 1
                        matriz[i+2][p1] = third()
                        matriz[i+2][p4] = third()
                        matriz[i+1][p3] = third()
                        matriz[i][p2] = third()
    if peca == 4:
        if p3 < 9:
            if i < 19:
                if matriz[i][p3+1] == 0 and matriz[i+1][p4+1] == 0:
                    matriz[i][p1] = zero()
                    matriz[i+1][p2] = zero()
                    p1 += 1
                    p2 += 1
                    p3 += 1
                    p4 += 1
                    matriz[i][p1] = fourth()
                    matriz[i+1][p2] = fourth()
                    matriz[i][p3] = fourth()
                    matriz[i+1][p4] = fourth()
    if peca == 5:
        if up == 0 or up == 2:
            if p4 < 9:
                if i < 19:
                    if matriz[i][p2+1] == 0 and matriz[i+1][p4+1] == 0:
                        matriz[i][p1] = zero()
                        matriz[i+1][p3] = zero()
                        p1 += 1
                        p2 += 1
                        p3 += 1
                        p4 += 1
                        matriz[i][p1] = fifth()
                        matriz[i][p2] = fifth()
                        matriz[i+1][p3] = fifth()
                        matriz[i+1][p4] = fifth()
        if up == 1 or up == 3:
            if p1 < 9:
                if i < 18:
                    if matriz[i][p1+1] == 0 and matriz[i+1][p2+1] == 0 and matriz[i+2][p4+1] == 0:
                        matriz[i][p1] = zero()
                        matriz[i+1][p3] = zero()
                        matriz[i+2][p4] = zero()
                        p1 += 1
                        p2 += 1
                        p3 += 1
                        p4 += 1
                        matriz[i+2][p4] = fifth()
                        matriz[i+1][p3] = fifth()
                        matriz[i+1][p2] = fifth()
                        matriz[i][p1] = fifth()
    if peca == 6:
        if up == 0:
            if p4 < 9:
                if i < 19:
                    if matriz[i][p4+1] == 0 and matriz[i+1][p3+1] == 0:
                        matriz[i][p1] = zero()
                        matriz[i+1][p3] = zero()
                        p1 += 1
                        p2 += 1
                        p3 += 1
                        p4 += 1
                        matriz[i][p1] = sixth()
                        matriz[i][p2] = sixth()
                        matriz[i+1][p3] = sixth()
                        matriz[i][p4] = sixth()
        if up == 1:
            if p3 < 9:
                if i < 18:
                    if matriz[i][p1+1] == 0 and matriz[i+1][p3+1] == 0 and matriz[i+2][p4+1] == 0:
                        matriz[i][p1] = zero()
                        matriz[i+1][p2] = zero()
                        matriz[i+2][p4] = zero()
                        p1 += 1
                        p2 += 1
                        p3 += 1
                        p4 += 1
                        matriz[i][p1] = sixth()
                        matriz[i+1][p2] = sixth()
                        matriz[i+1][p3] = sixth()
                        matriz[i+2][p4] = sixth()
        if up == 2:
            if p4 < 9:
                if i < 19:
                    if matriz[i][p3+1] == 0 and matriz[i+1][p4+1] == 0:
                        matriz[i][p3] = zero()
                        matriz[i+1][p1] = zero()
                        p1 += 1
                        p2 += 1
                        p3 += 1
                        p4 += 1
                        matriz[i+1][p1] = sixth()
                        matriz[i+1][p2] = sixth()
                        matriz[i][p3] = sixth()
                        matriz[i+1][p4] = sixth()
        if up == 3:
            if p1 < 9:
                if i < 18:
                    if matriz[i][p1+1] == 0 and matriz[i+1][p2+1] == 0 and matriz[i+2][p4+1] == 0:
                        matriz[i][p1] = zero()
                        matriz[i+1][p3] = zero()
                        matriz[i+2][p4] = zero()
                        p1 += 1
                        p2 += 1
                        p3 += 1
                        p4 += 1
                        matriz[i][p1] = sixth()
                        matriz[i+1][p2] = sixth()
                        matriz[i+1][p3] = sixth()
                        matriz[i+2][p4] = sixth()
    if peca == 7:
        if up == 0 or up == 2:
            if p4 < 9:
                if i < 19:
                    if matriz[i][p4+1] == 0 and matriz[i+1][p2+1] == 0:
                        matriz[i+1][p1] = zero()
                        matriz[i][p3] = zero()
                        p1 += 1
                        p2 += 1
                        p3 += 1
                        p4 += 1
                        matriz[i+1][p1] = seventh()
                        matriz[i+1][p2] = seventh()
                        matriz[i][p3] = seventh()
                        matriz[i][p4] = seventh()
        if up == 1 or up == 3:
            if p4 < 9:
                if i < 18:
                    if matriz[i][p1+1] == 0 and matriz[i+1][p3+1] == 0 and matriz[i+2][p4+1] == 0:
                        matriz[i+2][p4] = zero()
                        matriz[i+1][p2] = zero()
                        matriz[i][p1] = zero()
                        p1 += 1
                        p2 += 1
                        p3 += 1
                        p4 += 1
                        matriz[i+2][p4] = seventh()
                        matriz[i+1][p3] = seventh()
                        matriz[i+1][p2] = seventh()
                        matriz[i][p1] = seventh()
    for x in range(20):
        for j in range(10):
            quad = matriz[x][j]
            if quad == 0:
                zero()
                t.fd(tl)
            elif quad == 1:
                first()
                t.fd(tl)
            elif quad == 2:
                second()
                t.fd(tl)
            elif quad == 3:
                third()
                t.fd(tl)
            elif quad == 4:
                fourth()
                t.fd(tl)
            elif quad == 5:
                fifth()
                t.fd(tl)
            elif quad == 6:
                sixth()
                t.fd(tl)
            else:
                seventh()
                t.fd(tl)
        t.bk(tl * 10)
        t.lt(90)
        t.fd(tl)
        t.rt(90)
    t.lt(90)
    t.bk(tl * 20)
    t.rt(90)
    t.update()

def funcaoVerificadora():
    global verif
    for i in range(20):
        auxi = 0
        for j in range(10):
            if matriz[i][j] != 0:
                auxi += 1

        if auxi == 10:
            verif = 1
            for x in range(20 - (20 - i), 20):
                for j in range(10):
                    if x == 19:
                        matriz[x][j] = zero()
                    else:
                        matriz[x][j] = matriz[x + 1][j]
        if i == 19:
            if verif == 1:
                verif = 0
                funcaoVerificadora()

t.onkey(teclaCima, "Up")
t.onkey(teclaEsq, "Left")
t.onkey(teclaDir, "Right")
t.listen()
while True:
    peca = r.randint(1, 7)
    if peca == 1:
        ##PosiÃ§Ãµes da peÃ§a
        p1 = 3
        p2 = 4
        p3 = 5
        p4 = 6
    elif peca == 2:
        ##PosiÃ§Ãµes da peÃ§a
        p1 = 4
        p2 = 4
        p3 = 5
        p4 = 6
    elif peca == 3:
        ##PosiÃ§Ãµes da peÃ§a
        p1 = 4
        p2 = 5
        p3 = 6
        p4 = 6
    elif peca == 4:
        ##PosiÃ§Ãµes da peÃ§a
        p1 = 4
        p2 = 4
        p3 = 5
        p4 = 5
    elif peca == 5:
        ##Posições da peça
        p1 = 4
        p2 = 5
        p3 = 5
        p4 = 6
    elif peca == 6:
        p1 = 4
        p2 = 5
        p3 = 5
        p4 = 6
    elif peca == 7:
        p1 = 4
        p2 = 5
        p3 = 5
        p4 = 6
    ##MOVENDO AS PEÃ‡AS PARA BAIXO
    ##Sorteando uma das 7 peÃ§as
    for i in range(19, -1, -1):

        if peca == 1:
            if up == 1 or up == 3:
                if matriz[i][p4] != 0:
                    break
                if i < 19:
                    if i < 18:
                        if i < 17:
                            matriz[i + 3][p1] = first()
                        matriz[i + 2][p2] = first()
                    matriz[i + 1][p3] = first()
                matriz[i][p4] = first()
                if i < 16:
                    matriz[i + 4][p1] = zero()

            elif up == 0 or up == 2:
                if matriz[i][p1] != 0 or matriz[i][p2] != 0 or matriz[i][p3] != 0 or matriz[i][p4] != 0:
                    break
                ##InÃ­cio da peÃ§a
                matriz[i][p1] = first()
                matriz[i][p2] = first()
                matriz[i][p3] = first()
                matriz[i][p4] = first()
                ##                if mudanca == 1:
                ##                    if i < 19:
                ##                        matriz[i+1][p1+1] = first()
                ##                    matriz[i][p2] = first()
                ##                    matriz[i-1][p3-1] = first()
                ##                    matriz[i-2][p4-2] = first()
                ##                    mudanca = 0
                ##Colocando a peÃ§a para baixo e limpando a de cima
                if i < 19:
                    matriz[i + 1][p1] = zero()
                    matriz[i + 1][p2] = zero()
                    matriz[i + 1][p3] = zero()
                    matriz[i + 1][p4] = zero()

        elif peca == 2:

            ##InÃ­cio da peÃ§a
            ##Tratando a exceÃ§Ã£o da peÃ§a comeÃ§ar acima da matriz
            if up == 0:
                if matriz[i][p1] != 0 or matriz[i][p3] != 0 or matriz[i][p4] != 0:
                    break
                if i < 19:
                    matriz[i + 1][p1] = second()
                matriz[i][p2] = second()
                matriz[i][p3] = second()
                matriz[i][p4] = second()
                ##Colocando a peÃ§a para baixo e limpando a de cima
                if i < 19:
                    ##Tratando a exceÃ§Ã£o da peÃ§a ser acima da matriz
                    if i < 18:
                        matriz[i + 2][p1] = zero()

                    matriz[i + 1][p3] = zero()
                    matriz[i + 1][p4] = zero()
            elif up == 1:
                if matriz[i][p2] != 0:
                    break
                if i < 19:
                    matriz[i + 1][p3] = second()
                    if i < 18:
                        if matriz[i+2][p1] != 0:
                            break
                        matriz[i + 2][p1] = second()
                        matriz[i + 2][p2] = second()
                matriz[i][p4] = second()
                if i < 17:
                    matriz[i + 3][p1] = zero()
                    matriz[i + 3][p1 - 1] = zero()
            elif up == 2:
                if matriz[i][p1] != 0:
                    break
                if i < 19:
                    if matriz[i+1][p2] != 0 or matriz[i+1][p3] != 0:
                        break
                    matriz[i][p1] = second()
                    matriz[i + 1][p2] = second()
                    matriz[i + 1][p3] = second()
                    matriz[i + 1][p4] = second()
                if i < 18:
                    matriz[i + 2][p2] = zero()
                    matriz[i + 2][p3] = zero()
                    matriz[i + 2][p4] = zero()
            elif up == 3:
                if matriz[i][p1] != 0 or matriz[i][p2] != 0:
                    break
                if i < 19:
                    matriz[i + 1][p3] = second()
                    if i < 18:
                        matriz[i + 2][p4] = second()
                matriz[i][p1] = second()
                matriz[i][p2] = second()
                if i < 19:
                    if i < 17:
                        matriz[i + 3][p3] = zero()
                    matriz[i + 1][p1] = zero()
        elif peca == 3:

            ##InÃ­cio da peÃ§a
            ##Tratando a exceÃ§Ã£o da peÃ§a comeÃ§ar acima da matriz
            if up == 0:
                if matriz[i][p1] != 0 or matriz[i][p2] != 0 or matriz[i][p3] != 0:
                    break
                if i < 19:
                    matriz[i + 1][p4] = third()
                matriz[i][p1] = third()
                matriz[i][p2] = third()
                matriz[i][p3] = third()

                if i < 19:
                    ##Tratando a exceÃ§Ã£o da peÃ§a ser acima da matriz
                    if i < 18:
                        matriz[i + 2][p4] = zero()
                    matriz[i + 1][p1] = zero()
                    matriz[i + 1][p2] = zero()
            elif up == 1:
                if matriz[i][p1] != 0 or matriz[i][p2] != 0:
                    break
                if i < 19:
                    if i < 18:
                        matriz[i + 2][p4] = third()
                    matriz[i + 1][p3] = third()
                matriz[i][p1] = third()
                matriz[i][p2] = third()
                if i < 19:
                    if i < 17:
                        matriz[i + 3][p4] = zero()
                    matriz[i + 1][p2] = zero()
            elif up == 2:
                if matriz[i][p1] != 0:
                    break

                if i < 19:
                    if matriz[i+1][p3] != 0 or matriz[i+1][p4] != 0:
                        break
                    matriz[i + 1][p2] = third()
                    matriz[i + 1][p3] = third()
                    matriz[i + 1][p4] = third()
                matriz[i][p1] = third()
                if i < 18:
                    matriz[i + 2][p2] = zero()
                    matriz[i + 2][p3] = zero()
                    matriz[i + 2][p4] = zero()
            elif up == 3:
                if matriz[i][p2] != 0:
                    break
                if i < 19:
                    if i < 18:
                        if matriz[i+2][p1] != 0:
                            break
                        matriz[i + 2][p1] = third()
                        matriz[i + 2][p2] = third()
                    matriz[i + 1][p3] = third()
                matriz[i][p4] = third()
                if i < 17:
                    matriz[i + 3][p1] = zero()
                    matriz[i + 3][p2] = zero()

        elif peca == 4:

            ##InÃ­cio da peÃ§a
            if matriz[i][p1] != 0 or matriz[i][p3] != 0:
                break
            if i < 19:
                matriz[i + 1][p2] = fourth()
                matriz[i + 1][p4] = fourth()
            matriz[i][p1] = fourth()
            matriz[i][p3] = fourth()
            if i < 18:
                matriz[i + 2][p2] = zero()
                matriz[i + 2][p4] = zero()

        elif peca == 5:
            ##Iniciando a peça
            if up == 0 or up == 2:
                if matriz[i][p1] != 0 or matriz[i][p2] != 0:
                    break
                if i < 19:
                    if matriz[i + 1][p4] != 0:
                        break
                    matriz[i + 1][p2] = fifth()
                    matriz[i + 1][p4] = fifth()
                matriz[i][p1] = fifth()
                matriz[i][p3] = fifth()
                if i < 19:
                    if i < 18:
                        matriz[i + 2][p3] = zero()
                        matriz[i + 2][p4] = zero()
                    matriz[i + 1][p1] = zero()
            elif up == 1 or up == 3:
                if matriz[i][p1] != 0:
                    break
                if i < 19:
                    if matriz[i + 1][p3] != 0:
                        break
                    if i < 18:
                        matriz[i + 2][p4] = fifth()
                    matriz[i + 1][p3] = fifth()
                    matriz[i + 1][p2] = fifth()
                matriz[i][p1] = fifth()
                if i < 18:
                    if i < 17:
                        matriz[i + 3][p4] = zero()
                    matriz[i + 2][p1] = zero()

        elif peca == 6:

            ##Iniciando a peça
            if up == 0:
                if matriz[i][p1] != 0 or matriz[i][p2] != 0 or matriz[i][p4] != 0:
                    break
                if i < 19:
                    matriz[i + 1][p3] = sixth()
                matriz[i][p1] = sixth()
                matriz[i][p2] = sixth()
                matriz[i][p4] = sixth()

                if i < 19:
                    if i < 18:
                        matriz[i + 2][p3] = zero()
                    matriz[i + 1][p1] = zero()
                    matriz[i + 1][p4] = zero()
            elif up == 1:
                if matriz[i][p1] != 0:
                    break
                if i < 19:
                    if matriz[i + 1][p3] != 0:
                        break
                    if i < 18:
                        matriz[i + 2][p4] = sixth()
                    matriz[i + 1][p2] = sixth()
                    matriz[i + 1][p3] = sixth()
                matriz[i][p1] = sixth()
                if i < 18:
                    if i < 17:
                        matriz[i + 3][p1] = zero()
                    matriz[i + 2][p2+1] = zero()
            elif up == 2:
                if matriz[i][p3] != 0:
                    break
                if i < 19:
                    if matriz[i + 1][p1] != 0 or matriz[i + 1][p4] != 0:
                        break
                    matriz[i + 1][p1] = sixth()
                    matriz[i + 1][p3] = sixth()
                    matriz[i + 1][p4] = sixth()
                matriz[i][p2] = sixth()
                if i < 18:
                    matriz[i + 2][p1] = zero()
                    matriz[i + 2][p3] = zero()
                    matriz[i + 2][p4] = zero()
            elif up == 3:
                if matriz[i][p4] != 0:
                    break
                if i < 19:
                    if matriz[i + 1][p3] != 0:
                        break
                    if i < 18:
                        matriz[i + 2][p4] = sixth()
                    matriz[i + 1][p3] = sixth()
                    matriz[i + 1][p2] = sixth()
                matriz[i][p1] = sixth()
                if i < 18:
                    if i < 17:
                        matriz[i + 3][p4] = zero()
                    matriz[i + 2][p3] = zero()
        elif peca == 7:
            ##Iniciando a peça
            if up == 0 or up == 2:
                if matriz[i][p3] != 0 or matriz[i][p4] != 0:
                    break
                if i < 19:
                    if matriz[i + 1][p1] != 0:
                        break
                    matriz[i + 1][p1] = seventh()
                    matriz[i + 1][p2] = seventh()
                matriz[i][p3] = seventh()
                matriz[i][p4] = seventh()

                ##Apagando a peça
                if i < 19:
                    if i < 18:
                        matriz[i + 2][p1] = zero()
                        matriz[i + 2][p2] = zero()
                    matriz[i + 1][p4] = zero()
            elif up == 1 or up == 3:
                if matriz[i][p1] != 0:
                    break
                if i < 19:
                    if matriz[i + 1][p3] != 0:
                        break
                    if i < 18:
                        matriz[i + 2][p4] = seventh()
                    matriz[i + 1][p3] = seventh()
                    matriz[i + 1][p2] = seventh()
                matriz[i][p1] = seventh()
                if i < 18:
                    if i < 17:
                        matriz[i + 3][p3] = zero()
                    matriz[i + 2][p2] = zero()
        for x in range(20):
            for j in range(10):
                quad = matriz[x][j]
                if quad == 0:
                    zero()
                    t.fd(tl)
                elif quad == 1:
                    first()
                    t.fd(tl)
                elif quad == 2:
                    second()
                    t.fd(tl)
                elif quad == 3:
                    third()
                    t.fd(tl)
                elif quad == 4:
                    fourth()
                    t.fd(tl)
                elif quad == 5:
                    fifth()
                    t.fd(tl)
                elif quad == 6:
                    sixth()
                    t.fd(tl)
                else:
                    seventh()
                    t.fd(tl)
            t.bk(tl * 10)
            t.lt(90)
            t.fd(tl)
            t.rt(90)
        ti.sleep(0.25)
        t.lt(90)
        t.bk(tl * 20)
        t.rt(90)
        t.update()
        t.clear()
    funcaoVerificadora()
    up = 0
    ##for i in range(20):
    ##    for j in range(10):
    ##        quad = matriz[i][j]
    ##        if quad = 0:
    ##            zero()
    ##            t.fd(tl)
    ##        elif quad = 1:
    ##            first()
    ##            t.fd(tl)
    ##        elif quad = 2:
    ##            second()
    ##            t.fd(tl)
    ##        elif quad = 3:
    ##            third()
    ##            t.fd(tl)
    ##        elif quad = 4:
    ##            fourth()
    ##            t.fd(tl)
    ##        elif quad = 5:
    ##            fifth()
    ##            t.fd(tl)
    ##        elif quad = 6:
    ##            sixth()
    ##            t.fd(tl)
    ##        else:
    ##            seventh()
    ##            t.fd(tl)
    ##    t.bk(tl*10)
    ##    t.lt(90)
    ##    t.fd(tl)
    ##    t.rt(90)
    ##    t.update()

