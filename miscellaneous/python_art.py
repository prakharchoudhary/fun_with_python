#module to make the pointer move on the screen
import turtle

def make_square(some_turtle,p):
	for i in range(4):
		some_turtle.forward(p)			#makes the turtle move forward
		some_turtle.right(90)				#makes the turtle turn right by 90 degrees

	# angie = turtle.Turtle()
	# angie.shape('classic')
	# angie.color('white')

	# angie.circle(100)
	# angie.speed(2)

	# sam = turtle.Turtle()
	# sam.shape('arrow')
	# sam.color('blue')
	# sam.speed(2)

	# for i in range(3):
	# 	sam.forward(100)
	# 	sam.left(120)

def make_art():
	window = turtle.Screen()
	#opens a screen
	window.bgcolor("red")
	#sets background color of screen to "red"
	jimmy = turtle.Turtle()
	jimmy.shape('turtle')
	jimmy.color('yellow')
	jimmy.speed(20)

	for i in range(1,73):
		make_square(jimmy,100)
		jimmy.right(5)

	for i in range(1,25):
		jimmy.color("blue")
		make_square(jimmy,50)
		jimmy.right(15)	
	window.exitonclick()

make_art()