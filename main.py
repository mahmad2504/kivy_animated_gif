from kivy.app import App
from kivy.lang.builder import Builder
from kivy.config import Config


Config.set('graphics', 'width', '440')
Config.set('graphics', 'height', '600')

container=Builder.load_string('''  

#:import utils kivy.utils
#:import Clock kivy.clock.Clock
BoxLayout:
    img_busy:img_busy
    btn_do_work:btn_do_work
    orientation: 'horizontal'
    BoxLayout:
        orientation :'vertical'
        size_hint_x:.5
        spacing: dp(24)
        padding: dp(24)

        canvas.before:
            Color:
                rgba: utils.get_color_from_hex('#ffffff')
            Rectangle:
                pos: self.pos
                size: self.size
                source: 'bg-login.png'
        AnchorLayout:
            orientation: 'bottom'
            Image:
                id:img_busy
                source: "busy.gif"
                opacity:0
                size_hint_y: None
                size_hint_x: None
                width: dp(74)
        Button:
            id:btn_do_work
            text:"Do some work"
            size_hint_y:.1
            background_normal: ''
            background_color: utils.get_color_from_hex('#097969')
            on_press:  root.img_busy.opacity=1
            on_press: Clock.schedule_interval(app.timer, 3)
            on_press: self.disabled=True
        
                
        ''')

class Main(App):
    def timer(self, dt):
        print("Timer Expired")
        self.root.img_busy.opacity=0
        self.root.btn_do_work.disabled=False
        return False
            
    def build(self):
        self.title = 'Animated gif demo'
        return container
       
if __name__ == '__main__':
    Main().run()