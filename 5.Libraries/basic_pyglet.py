import pyglet
import math

class Vec2:
    """Pyglet doesn't have a vector so we need to make one"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Even though we don't use them in this example here are some of the basic methods
    # Note that you can also use __add__, __sub__ etc, in this example I'll simply use add
    # Also there is no error checking in case of division by 0, wrong inputs, etc

    def add(self, vector):
        self.x += vector.x
        self.y += vector.y

    def sub(self, vector):
        self.x -= vector.x
        self.y -= vector.y

    def mult(self, scalar):
        self.x *= scalar
        self.y *= scalar

    def div(self, scalar):
        self.x /= scalar
        self.y /= scalar

    def mag(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normalize(self):
        m = self.mag()
        self.div(m)

class Line:
    """A class which helps us to draw a line to the screen more easily"""
    def __init__(self, start_pos, end_pos, color):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.color = color

    # We can either show the line when we init it or we can put the code which renders it
    # in a separate function and call it when we want
    # Also note that there are better ways to draw things on the screen
    def show(self):
        # You start with how many vertices the shape will have, in our case 2, after that you specify the shape type
        pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
            # "v2f" stands for vertex2intenger, there is also a "v2f" which accepts floats instead of ints,
            # A vertex holds 2, 3 or 4 components (for 2D, 3D, or non-homogeneous coordinates) - ("v2i", "v3i", "v4i")
            # The values are basically coordinates
            # Note that the (0, 0) coord is at the bottom left of the window
            ("v2f", (self.start_pos.x, self.start_pos.x, self.end_pos.x, self.end_pos.y)),
            # "c4B" stands for color4Byte and accepts 4 values(RGBA, 0 - 255), there is aslo a "v3B" which accepts
            # only RGB color, you need a color for every vertex
            # Note that with list comprehension and multiplying the tuple with 2 we create the necessary values
            # This will become very handy when we will draw more complex structures
            ("c4B", tuple(self.color[i] for i in range(0, 4)) * 2))
            # The generated code looks like this: (self.color[0], self.color[1], self.color[2], self.color[3], self.color[0], self.color[1], self.color[2], self.color[3]))

class Rect:
    """Drawing a rectangle is a little bit more complicated, you'll need to draw two trangles to obtain one"""
    def __init__(self, pos, width, height, color, mode = None):
        self.pos = pos
        self.color = color
        self.w = width
        self.h = height
        self.mode = mode

    def show(self):
        # For better understand of the coords I recommend trying to draw them on a piece of paper to visualize them
        # We can draw the rectangle around the coords, making them the center of the rectangle
        if self.mode == "CENTER":
            # Because division has as a result always a float you should use "v2f"
            vertices = (-self.w / 2 + self.pos.x, -self.h / 2 + self.pos.y,
                       -self.w / 2 + self.pos.y,  self.h / 2 + self.pos.y,
                        self.w / 2 + self.pos.x, -self.h / 2 + self.pos.y,
                        self.w / 2 + self.pos.x,  self.h / 2 + self.pos.y)
        else:
            # The pos coords are at the bottom left of the rectangle
            vertices = (self.pos.x, self.pos.y, self.pos.x, self.pos.y + self.h, 
                        self.pos.x + self.w, self.pos.y, self.pos.x + self.w, self.pos.y + self.h)

        # Again the number of vertices, you can learn more about triangle strips at:
        # https://en.wikipedia.org/wiki/Triangle_strip
        pyglet.graphics.draw(4, pyglet.gl.GL_TRIANGLE_STRIP, ("v2f", vertices),
            # Note how easy is to scale the tuple using this shorthand
            ("c4B", tuple(self.color[i] for i in range(0, 4)) * 4))

class Circle:
    """A circle is even more complicated, we'll have to use trigonometry to obtain one"""
    def __init__(self, pos, radius, points, color):
        self.pos = pos
        self.radius = radius
        # You usually have the amount of points based on the radius
        self.points = points
        self.color = color

    def show(self):
        # We start at 0 rad which is 0 degrees, 360 degrees is PI * 2(~6.28...)
        angle = 0
        # How much we want to increment the angle with each iteration
        increment = (math.pi * 2) / self.points
        # An array to store the generated vertices
        vertices = []
        for i in range(0, self.points):
            # What we need to do is to find the x and y coords around a central point
            # For this we'll used trigonometry, you can learn more here:
            # https://www.mathsisfun.com/sine-cosine-tangent.html
            # It's also very important to add the pos to the generated coords
            x = self.radius * math.sin(angle) + self.pos.x
            y = self.radius * math.cos(angle) + self.pos.y
            # After we calculate them we need to store the coords in the array
            vertices.append(x)
            vertices.append(y)
            # Don't forget to increment the angle with each generation
            angle += increment

        # Again the number of vertices and then the shape type
        # You can learn more about the triangle fan here: 
        # https://en.wikipedia.org/wiki/Triangle_fan
        # We basically draw some triangles around a central point
        # It is important to use "v2f" because the coords are going to be floats, you can also use
        # "v2i" but you'll to transform the coords in intengers
        pyglet.graphics.draw(self.points, pyglet.gl.GL_TRIANGLE_FAN, ("v2f", vertices),
            # Here we can see the full power of this shorthand
            ("c4B", tuple(self.color[i] for i in range(0, 4)) * self.points))

class Text:
    """Making this class will help you to display a text much easier"""
    def __init__(self, pos, msg, size, color):
        self.pos = pos
        self.msg = msg
        self.size = size
        self.color = color

    def show(self):
        # The arguments are pretty self explanatory, also note that you need .draw() at the end
        pyglet.text.Label(self.msg, font_name = "Times New Roman", font_size = self.size,
                        x = self.pos.x, y = self.pos.y, anchor_x = "center", anchor_y = "center", 
                        color = tuple(self.color[i] for i in range(0, 4))).draw()

class MainWindow(pyglet.window.Window):
    def __init__(self):
        # Init the window with the width, height and title
        super().__init__(500, 500, "Basic Pyglet")

        # This is the main loop, the second argument is how often to update the screen in seconds
        pyglet.clock.schedule_interval(self.update, 1 / 60)

        # Init a line, note that we can use the vector class which we created to give the position
        self.line = Line(Vec2(50, 50), Vec2(100, 100), (0, 0, 0, 255))

        # Init a rectangle, we'll test the alpha too
        self.rect = Rect(Vec2(100, 100), 50, 50, (255, 0, 0, 127), "CENTER")

        # Init a circle, try to play with the points number to see what it does
        # Note that the every point adds up and if you draw too many the performance will drop
        self.circle = Circle(Vec2(200, 200), 50, 16, (0, 255, 0, 255))

        # Init a text
        self.text = Text(Vec2(300, 300), "Hello World!", 26, (0, 0, 255, 255))

    def on_draw(self):
        # Clear the screen every frame
        self.clear()

        # Sets the color of the screen, 0 - 1 -> 0 - 255, RGBA format
        pyglet.gl.glClearColor(1, 1, 1, 1)

        # To use colors with an alpha value for your shapes you need this code
        pyglet.gl.glEnable(pyglet.gl.GL_BLEND)
        pyglet.gl.glBlendFunc(pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)

        # Display the line on screen
        self.line.show()

        # Now we can play with the line coordinates, for example
        if self.line.end_pos.x < 450:
            self.line.end_pos.x += 1
            self.line.end_pos.y += 1
        # Now the line will grow every frame

        # Display the rectangle
        self.rect.show()

        # Display the circle
        self.circle.show()

        # Display the text
        self.text.show()

    def update(self, dt):
        pass

window = MainWindow()
pyglet.app.run()