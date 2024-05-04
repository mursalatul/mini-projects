import turtle


# Function to create the face shape using a circle with given size
def createFace(size):
    t.pendown()
    t.pen(fillcolor="blue")
    t.begin_fill()
    t.circle(size)
    t.end_fill()
    t.penup()


# Function to position the turtle for drawing eyes or ears
def placePen(object: str, direction: str):
    t.penup()
    t.home()  # Return turtle to center
    t.left(90)  # Turn turtle to face upwards
    t.forward(size)  # Move turtle to top of face
    if direction == "left":
        t.left(45)  # Turn turtle left for left elements
    else:
        t.right(45)  # Turn turtle right for right elements
    if object == "eye":
        t.forward(round(size * 0.40))  # Move turtle to eye position
    else:
        t.forward(size)  # Move turtle to ear position
    t.right(90)  # Turn turtle to face right


# Function to draw red circles for eyes or ears
def redCircle(object: str):
    t.pendown()
    t.pen(fillcolor="red")
    t.begin_fill()
    if object == "ear":
        t.circle(size // 2)  # Draw larger circle for ears
    else:
        t.circle(round(size * 0.20))  # Draw smaller circle for eyes
    t.end_fill()
    t.penup()


# Initialize turtle
t = turtle.Turtle()
t.speed(2)  # Set drawing speed
size = 100  # Size of the face

# Draw the face
createFace(size)

# Draw the ears and eyes
for element in ["ear", "eye"]:
    for direction in ["left", "right"]:
        placePen(element, direction)  # Position turtle for drawing
        redCircle(element)  # Draw red circle for eye or ear

# Hide turtle and keep window open
t.hideturtle()
turtle.mainloop()
