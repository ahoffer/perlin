import pyglet
from perlin_noise import PerlinNoise
from pyglet.gl import glClear, GL_COLOR_BUFFER_BIT, glLoadIdentity, glBegin, GL_TRIANGLES, glVertex2f, glEnd

# Not using these lines yet
display = pyglet.canvas.Display()
screen = display.get_default_screen()

# Resizeable
window = pyglet.window.Window(resizable=True)

# Full screen
# window = Window(fullscreen=True, config=config)

label = pyglet.text.Label('Hello, world',
                          color=(64, 128, 255, 255),
                          font_name='Times New Roman',
                          font_size=46,
                          x=window.width // 2, y=window.height // 2,
                          anchor_x='center', anchor_y='center')


@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glBegin(GL_TRIANGLES)
    glVertex2f(0, 0)
    glVertex2f(window.width, 0)
    glVertex2f(window.width, window.height)
    glEnd()
    label.update(window.width // 2, window.height // 2)
    label.draw()


@window.event
def on_close():
    print("I'm closing now")
    exit(0)


# MUSIC
music = pyglet.resource.media('cinematic-space-drone-10623.mp3')
# music.play()

# NOISE
noise = PerlinNoise(octaves=3, seed=1)
xpix, ypix = 100, 100
pic = [[noise([i / xpix, j / ypix]) for j in range(xpix)] for i in range(ypix)]

pyglet.app.run()
