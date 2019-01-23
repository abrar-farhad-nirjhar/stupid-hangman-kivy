from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
import hangman_game
from kivy.core.window import Window
Window.clearcolor = (1, 1, 1, .1)


class MyImage(Image):
    def __init__(self, **kwargs):
        super(MyImage,self).__init__(**kwargs)



class MyLabel(Label):
    def __init__(self, **kwargs):
        super(MyLabel,self).__init__(**kwargs)
    


class mainApp(App):
    i1 = MyImage
    i1.source= '7.png'
    
    word = hangman_game.get_word()
    m1 = MyLabel
    m1.text = "_ "*len(word)
    # m1.font_size = 20

    def set_size(self):
        if len(self.word)>10 and len(self.word)<14: 
            self.m1.font_size  = 25
        elif len(self.word)<10:
            self.m1.font_size = 32
        elif len(self.word)>14 and len(self.word)<25:
            self.m1.font_size = 20
        else:
            self.m1.font_size = 17    
    
    def build(self):
        self.set_size()
        return GridLayout()


# self.MyLabel.setText("hello")
m = mainApp()
m.run()