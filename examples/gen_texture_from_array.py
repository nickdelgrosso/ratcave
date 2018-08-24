import numpy as np
import pyglet
import ratcave as rc


window = pyglet.window.Window()

size = (128, 128, 4)
cube = rc.Mesh.from_primitive('Cube', position=(0, 0, -3), rotation=(45, 45, 0), dynamic=True)
cube.texcoords[:] *= 4
cube.dynamic = False
# cube.uniforms['diffuse'] = 1, 0, 0

arr = np.random.randint(0, 255, size=size)
arr = np.zeros_like(arr)# + 255
arr[:, :, 0] = 255

tex2 = rc.Texture(values=arr)
tex2.values = np.random.randint(0, 255, size=size)

cube.textures.append(tex2)

@window.event
def on_draw():
    window.clear()
    rc.clear_color(1, 1, 1)
    with rc.default_shader, rc.default_camera, rc.default_states:
        cube.draw()


def randomize_texture(dt):
    tex2.values = np.random.randint(0, 255, size=size)
pyglet.clock.schedule(randomize_texture)

pyglet.app.run()