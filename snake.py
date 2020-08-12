import turtle
import time
import random

ve = 0
vel = 0
numeros_para_velocidad_random = list(range(8,100000))
velocidad = input("Seleccione el modo de juego\n1 = muy fácil\n2 = fácil\n3 = normal\n4 = difícil\n5 = extremo\n6 = imposible\n7 = modo practica(pudes configurar la velocidad del juego y de la culebrita)\nEscriba su indice de la dificultad ")

if int(velocidad) in numeros_para_velocidad_random:
    velocidad = random.randint(1,8)
elif int(velocidad) == 1:
    vel += 1
    ve += 0.085
elif int(velocidad) == 2:
    vel += 3
    ve += 0.0835
elif int(velocidad) == 3:
    vel += 0
    ve += 0.07
elif int(velocidad) == 4:
    vel += 10
    ve += 0.0445
elif int(velocidad) == 5:
    vel += 0
    ve += 0.039
elif int (velocidad) == 6:
    vel += 0
    ve += 0.029
elif int(velocidad) == 7:
    velo = input("Seleccione la velocidad de la culebrita\n1 = lento\n2 = normal\n3 = rapido\n4 = muy rapida\nEscriba la velocidad ")
    veo = input("Seleccione la velocidad del juego\n1 = lento\n2 = normal\n3 = rapido\nEscriba la velocidad ")
    if int(veo) and int(velo) in numeros_para_velocidad_random:
        velo = random.randint(1,4)
        veo = random.randint(1,3)
    elif int(velo) == 1 and int(veo) == 1:
        vel += 1
        ve += 0.085
    elif int(velo) == 1 and int(veo) == 2:
        vel += 3
        ve += 0.0835
    elif int(velo) == 1 and int(veo) == 3:
        vel += 6
        ve += 0.07
    elif int(velo) == 2 and int(veo) == 2:
        vel += 6
        ve += 0.07
    elif int(velo) == 2 and int(veo) == 3:
        vel += 10
        ve += 0.0445
    elif int(velo) == 3 and int(veo) == 3:
       vel += 0
       ve += 0.039
    elif int(velo) == 4 and int(veo) == 1:
        vel += 0
        ve += 0.039
    elif int(velo) == 4 and int(veo) == 2:
        vel += 10
        ve += 0.0445
    elif int(velo) == 4 and int(veo) == 3:
        vel += 0
        ve += 0.039



posponer = float(ve)

# Marcadores
score = 0
high_score = 0

wn = turtle.Screen()
wn.title('Snake')
wn.bgcolor("#263238")
wn.setup(width = 750, height = 750)
wn.tracer(0)
# def muyfácil():
#     vel = 1
#     ve = 0.085
# def fácil():
#     vel = 3
#     ve = 0.0835
# def normal():
#     vel = 0
#     ve = 0.07
# def difícil():
#     vel = 10
#     ve = 0.0445
# def extremo():
#     vel = 0
#     ve = 0.039
# def imposible():
#     vel = 0
#     ve = 0.029

# # 
# wn.listen()
# wn.onkeypress(muyfácil, "Numpad1")
# wn.onkeypress(fácil, "Numpad2")
# wn.onkeypress(normal, "Numpad3")
# wn.onkeypress(difícil, "Numpad4")
# wn.onkeypress(extremo, "Numpad5")
# wn.onkeypress(imposible, "Numpad6")

# Cabeza serpiente
cabeza = turtle.Turtle()
cabeza.speed(int(vel))
cabeza.shape("square")
cabeza.color("white")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"

# Comida
comida = turtle.Turtle()
comida.speed(0.5)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)

# bordes derecha
bordr = turtle.Turtle()
bordr.speed(0)
bordr.color("black")
bordr.penup()
bordr.hideturtle()
bordr.goto(1383,-455)
bordr.write("|", align = "center", font = ("Fixedsys", 20000,"normal"))

# borde izquerda
bordl = turtle.Turtle()
bordl.speed(0)
bordl.color("black")
bordl.penup()
bordl.hideturtle()
bordl.goto(-1404,-485)
bordl.write("|", align = "center", font = ("Fixedsys", 20000,"normal"))

bordt = turtle.Turtle()
bordt.speed(0)
bordt.color("black")
bordt.penup()
bordt.hideturtle()
bordt.goto(-375,260)
bordt.write("--------------------------------------", align = "center", font = ("Fixedsys", 100,"normal"))

# Segmentos serpiente
segmentos = []

# Texto
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,335)
texto.write("Score: 0       High Score: 0", align = "center", font = ("Fixedsys", 24,"normal"))

# game over
textoq = turtle.Turtle()
textoq.speed(0)
textoq.color("white")
textoq.penup()
textoq.hideturtle()
textoq.goto(0,0)
textoq.write("GAME OVER", align = "center", font = ("Fixedsys", 48,"normal"))
textoq.clear()

# Funciones
def arriba():
    cabeza.direction = "up"
def abajo():
    cabeza.direction = "down"
def izquierda():
    cabeza.direction = "left"
def derecha():
    cabeza.direction = "right"


def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)
    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)
    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)
    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

# Teclado
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")

false_or_true1 = False
false_or_true2 = True

if velocidad == 1 or velocidad == 2 or  velocidad == 3 or velocidad == 4 or velocidad == 5 or velocidad == 6:
    false_or_true1 = True
    false_or_true2 = False
elif velocidad == 7:
    false_or_true1 = False
    false_or_true2 = True

while false_or_true1:
    wn.update()
    # Colisiones bordes
    if cabeza.xcor() > 349 or cabeza.xcor() < -360 or cabeza.ycor() > 300 or cabeza.ycor() < -349:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction = "stop"

        for segmento in segmentos:
            segmento.goto(10000,10000)

        segmentos.clear()
        score = 0
        texto.clear()
        texto.write("Score: {}       High Score: {}".format(score, high_score), align = "center", font = ("Fixedsys", 24,"normal"))
        score = 0

        textoq.write("GAME OVER", align = "center", font = ("Fixedsys", 48,"normal"))
        textoq.clear()
        time.sleep(1)
        score = 0

    if cabeza.distance(comida) < 15:
        x = random.randint(-355,300)
        y = random.randint(-355,335)
        comida.goto(x,y)

        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(1)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("#151515")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)

        score += 1

        if score > high_score:
            high_score = score

        texto.clear()
        texto.write("Score: {}       High Score: {}".format(score, high_score), align = "center", font = ("Fixedsys", 24,"normal"))

    # mover el cuerpo de la serpiente
    totalSeg = len(segmentos)
    for index in range(totalSeg -1, 0, -1):
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor()
        segmentos[index].goto(x,y)

    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)

    mov()
    for segmento in segmentos:
        if segmento.distance(cabeza) < 15:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction = "stop"

            for segmento in segmentos:
                segmento.goto(10000,10000)
            segmentos.clear()

            texto.clear()
            score = 0
            texto.write("Score: {}       High Score: {}".format(score, high_score), align = "center", font = ("Fixedsys", 24,"normal"))
            textoq.write("GAME OVER", align = "center", font = ("Fixedsys", 48,"normal"))
            textoq.clear()
            time.sleep(2)
    time.sleep(posponer)

while false_or_true2:
    wn.update()
    # Colisiones bordes
    if cabeza.xcor() > 349 or cabeza.xcor() < -360 or cabeza.ycor() > 300 or cabeza.ycor() < -349:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction = "stop"

        texto.clear()
        texto.write("Score: {}       High Score: {}".format(score, high_score), align = "center", font = ("Fixedsys", 24,"normal"))

        textoq.write("GAME OVER", align = "center", font = ("Fixedsys", 48,"normal"))
        textoq.clear()
        time.sleep(1)

    if cabeza.distance(comida) < 15:
        x = random.randint(-355,300)
        y = random.randint(-355,355)
        comida.goto(x,y)

        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(1)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("#151515")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)

        score += 1

        if score > high_score:
            high_score = score

        texto.clear()
        texto.write("Score: {}       High Score: {}".format(score, high_score), align = "center", font = ("Fixedsys", 24,"normal"))

    # mover el cuerpo de la serpiente
    totalSeg = len(segmentos)
    for index in range(totalSeg -1, 0, -1):
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor()
        segmentos[index].goto(x,y)

    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)

    mov()
    for segmento in segmentos:
        if segmento.distance(cabeza) < 15:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction = "stop"

            texto.clear()
            texto.write("Score: {}       High Score: {}".format(score, high_score), align = "center", font = ("Fixedsys", 24,"normal"))
            textoq.write("GAME OVER", align = "center", font = ("Fixedsys", 48,"normal"))
            textoq.clear()
            time.sleep(2)
    time.sleep(posponer)