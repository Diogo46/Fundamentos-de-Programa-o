
# Exercise 5 on "How to think like a computer scientist", ch. 11.

import turtle

t = turtle.Turtle()

# Use t.up(), t.down() and t.goto(x, y)

# Put your code here
file = open('drawing.txt', 'r')
for line in file:
	item = line.split()
	if item[0] == 'UP':
		t.up()
	elif item[0] == 'DOWN':
		t.down()
	else:
		t.goto(float(item[0]),float(item[1]))
turtle.Screen().exitonclick()
