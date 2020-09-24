from turtle import *
from random import * 

#uma função para mover a tartaruga para uma posição aleatória
def moveToRandomLocation():
    penup()
    setpos( randint(-700,700) , randint(-700,700))
    pendown()
    
#uma função para desenhar uma estrela de um tamanho específico
def drawStar(starSize, starColour):
    color(starColour)
    pendown()
    begin_fill()
    for side in range(5):
        left(144)
        forward(starSize)
    end_fill()
    penup()

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

def drawGalaxy(number0fStars):
    starColours = ["White","SkyBlue"]
    moveToRandomLocation()
    #desenha várias pequenas estrelas coloridas
    for star in range(number0fStars):
        penup()
        left( randint(-180,180))
        forward( randint(5,20))
        pendown()
        #desenha uma pequena estrela de cor aleatória
        drawStar( 2, choice(starColours))

speed(30)

#isso desenha um fundo azul escuro
bgcolor("black")

#desenha 30 estrelas brancas (tamanho,posições aleatórias)
for star in range(200):
    moveToRandomLocation()
    drawStar( randint(1,5) , "White")

for star in range(200):
    moveToRandomLocation()
    drawStar( randint(1,5) , "SkyBlue")

for Planeta in range(1):
    penup()
    setpos(-700,-100)
    pendown()
    drawPlanet(3, "Gold")
    penup()
    setpos(-400,0)
    pendown()
    drawPlanet(0.9, "DarkRed")
    penup()
    setpos(-100,0)
    pendown()
    drawPlanet(1, "DeepSkyBlue")
    penup()
    setpos(0,0)
    pendown()
    drawPlanet(1.5, "Khaki")



hideturtle()
done  