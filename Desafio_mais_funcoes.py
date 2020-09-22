from turtle import *

#uma função para desenhar um quadrado
#'def' signica 'define'
def drawSquare():
    pendown()
    begin_fill()
    for side in range(4):
        left(90)
        forward(120)
    end_fill()
    penup()


#isso vai desenhar uma quadrado de cor Ciano em um fundo Carmesim
color("#00FFFF")
bgcolor("#DC143C")

#use a função para desenhar quadrado!
drawSquare()
forward(140)
drawSquare()
right(0)
forward(140)
drawSquare()


hideturtle()
done()
