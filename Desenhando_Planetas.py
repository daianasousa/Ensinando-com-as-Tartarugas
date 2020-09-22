from turtle import *

#uma função para desenhar um planeta de um tamanho específico
def drawPlanet(starSize, starColour):
    color(starColour)
    pendown()
    begin_fill()
    for side in range(360):
        left(1)
        forward(starSize)
    end_fill()
    penup()


#isso desenha um fundo azul escuro
bgcolor("MidnightBlue")

#use a função para desenhar planetas de tamanhos diferentes!
drawPlanet(3, "yellow")
forward(140)
drawPlanet(2, "White")
left(15)
forward(150)
drawPlanet(1, "red")


hideturtle()
done()