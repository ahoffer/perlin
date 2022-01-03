from pyglet.gl import *

# Direct OpenGL commands to this window.
window = pyglet.window.Window()

label = pyglet.text.Label('Hello, world',
                          color=(128, 128, 255, 255),
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
    label.draw()


music = pyglet.resource.media('cinematic-space-drone-10623.mp3')
music.play()

pyglet.app.run()

pyglet.app.run()
