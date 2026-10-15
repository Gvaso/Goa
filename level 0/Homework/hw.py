from turtle import *
#we want to paint a house


#step 1: draw a square 
speed(1)
shape("turtle")
width(5)
color("Pink")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door
forward(75)
color("Brown")
begin_fill()
left(90)
forward(100)
right(90)         #height of door
forward(50)
right(90)
forward(100)
end_fill()


#end of door

penup()
goto(200,200)
pendown()

color("Red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#end of roof 



#drawing a window   
penup()
goto(50,100)
pendown()

right(150)
color("Blue")
forward(70)
left(90)
forward(30)
left(90)
forward(70)
left(90)
forward(30)

penup()
goto(150,100)
pendown()

left(90)
forward(70)
right(90)
forward(30)
right(90)
forward(70)
right(90)
forward(30)
#Window is done


exitonclick()