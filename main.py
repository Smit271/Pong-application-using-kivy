# Step 1 : Create App
# Step 2 : Create Game
# Step 3 : Build Game
# Step 4 : Run App


from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint

class PongPaddle(Widget):
    score = NumericProperty(0)
    def bounce_off(self, ball):
        if self.collide_widget(ball):
            ball.velocity_x *= -1.01


class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    # Latest position = Cur. velocity  + Cur. position
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


# Update --- moving ball by calling the move function and other stuff

# on_touch_down() -- When finger touches screen
# on_touch_up()   -- When we lift off finger while touching it
# on_touch_move() -- When dragging finger on screen

class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    cpu = ObjectProperty(None)


    def serve_ball(self):
        self.ball.velocity = Vector(7, 3).rotate(randint(0, 360))

    def update(self, dt):
        self.ball.move()
        self.cpu.center_y = self.ball.center_y

        # bounce off paddles
        self.player1.bounce_off(self.ball)
        self.cpu.bounce_off(self.ball)

        # bounce off top and bottom
        if((self.ball.y < 0) or (self.ball.y > self.height - 50)):
            self.ball.velocity_y *= -1

        # if bounce off left and increase score of player1
        if self.ball.x < 0:
            self.ball.velocity_x *= -1
            self.player1.score += 1

        # if bounce off right and increase score of cpu
        if self.ball.x > self.width - 50:
            self.ball.velocity_x *= -1
            self.cpu.score += 1

        

    def on_touch_move(self, touch):

        if touch.x < self.width * 1/4:
            self.player1.center_y = touch.y 
        #if touch.x > self.width * 3/4:
            #self.cpu.center_y = touch.y 
   

class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0/90.0)
        return game

PongApp().run()



