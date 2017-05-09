import pyglet

class Bola():
def __init__(self,nome):
self.x = 150
self.y = 150
self.dx = 5
self.dy = 5
self.image = pyglet.resource.image(nome)
def move(self):
self.x += self.dx
self.y += self.dy
def quicar(self,width,height):
if self.x < 0 or self.x > width-self.image.width//2:
self.dx = - self.dx
if self.y < 0 or self.y > height-self.image.height//2:
self.dy = - self.dy
def rebate(self,x,y,dx,dy):
nx = self.x + self.dx
ny = self.y + self.dy
if nx < x+dx and nx+self.image.width > x \
 and ny < y+dy and ny+self.image.height > y :
if (nx < x+dx and self.x >= x+dx) or (nx > x and self.x <= x):
self.dx = - self.dx
if (ny < y+dy and self.y >= y+dy) or (ny > y and self.y <= y):
self.dy = - self.dy
def draw(self):
self.image.blit(self.x,self.y)
class Raquete():
def __init__(self,nome,x,y):
self.x = x
self.y = y
self.addy = 0
self.image = pyglet.resource.image(nome)
def draw(self):
self.y += self.addy
self.image.blit(self.x,self.y)
Engenharia -		Design	de	Software
class Window(pyglet.window.Window):
def __init__(self):
super(Window, self).__init__(800, 600, caption="Jogo Pong Pyglet")
self.raquete1 = Raquete('tijolo.jpeg',20,231)
self.raquete2 = Raquete('tijolo.jpeg',680,231)
self.bola = Bola('bola.png')
pyglet.clock.schedule_interval(self.update, 0.001)
def update(self, dt):
self.clear()
self.bola.bounce_ball(self.width,self.height)
self.bola.rebate(self.raquete1.x,self.raquete1.y,self.raquete1.image.width,
self.raquete1.image.height)
self.bola.rebate(self.raquete2.x,self.raquete2.y,self.raquete2.image.width,
self.raquete2.image.height)
self.bola.move()
self.raquete1.draw()
self.raquete2.draw()
self.bola.draw()
def on_key_press(self, symbol, modifiers):
if symbol == pyglet.window.key.UP: self.raquete1.addy = 10
elif symbol == pyglet.window.key.DOWN: self.raquete1.addy = -10
def on_key_release(self, symbol, modifiers):
if symbol == pyglet.window.key.UP: self.raquete1.addy = 0
elif symbol == pyglet.window.key.DOWN: self.raquete1.addy = 0
def on_mouse_motion(self, x, y, dx, dy):
self.raquete2.y = y+dy
def main():
window = Window()
pyglet.app.run()
if __name__ == "__main__":
main()