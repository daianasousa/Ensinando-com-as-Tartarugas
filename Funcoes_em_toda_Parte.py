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

speed(30)

#isso desenha um fundo preto
bgcolor("black")

#desenha 200 estrelas brancas e 200 estrelas Azuis (tamanho,posições aleatórias)
for star in range(200):
    moveToRandomLocation()
    drawStar( randint(1,5) , "White")

for star in range(200):
    moveToRandomLocation()
    drawStar( randint(1,5) , "SkyBlue")


#desenha Planetas e sol (tamanho,posições especificas)
for Planeta in range(1):
    #SOL
    penup()
    setpos(-700,-100)
    pendown()
    drawPlanet(3, "gold")
    #MERCURIO
    penup()
    setpos(-400,30)
    pendown()
    drawPlanet(0.4, "gray")
    #VENUS
    penup()
    setpos(-300,10)
    pendown()
    drawPlanet(0.7,"DarkGoldenrod")
    #TERRA
    penup()
    setpos(-170,-10)
    pendown()
    drawPlanet(1.1,"LightSkyBlue")
    #MARTE
    setpos(-25,0)
    pendown()
    drawPlanet(0.8,"DarkRed")
    #JUPITE
    penup()
    setpos(130,-30)
    pendown()
    drawPlanet(1.5, "Khaki")
    #SATURNO
    penup()
    setpos(300,0)
    pendown()
    drawPlanet(0.9,"PaleGoldenrod")
    #URANO
    penup()
    setpos(410,20)
    pendown()
    drawPlanet(0.6, "blue")
    #NETUNO
    penup()
    setpos(500,25)
    pendown()
    drawPlanet(0.4,"DeepSkyBlue")

hideturtle()
done()
