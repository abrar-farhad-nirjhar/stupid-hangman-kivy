from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
import hangman_game
from kivy.core.window import Window
from kivy.uix.button import Button
Window.clearcolor = (1, 1, 1, .1)


 


class MyImage(Image):
    def __init__(self, **kwargs):
        super(MyImage,self).__init__(**kwargs)



class MyLabel(Label):
    def __init__(self, **kwargs):
        super(MyLabel,self).__init__(**kwargs)



class MyButton(Button):
    def label_change(self, event):
        self.event = event

        if self.event=='A':
           mainApp.m1.text = "Hello"

class MyGridLayout(GridLayout):
    i1 = MyImage
    i1.source= '7.png'
    
    word = hangman_game.get_word()
    m1 = MyLabel
    m1.text = "_ "*len(word)
    word = word.upper()
    word_list = list(word)

    def set_size(self):
        if len(self.word)>10 and len(self.word)<14: 
            self.display.font_size  = 25
        elif len(self.word)<10:
            self.display.font_size = 32
        elif len(self.word)>14 and len(self.word)<25:
            self.display.font_size = 20
        else:
            self.display.font_size = 17

    # m1.font_size = 20



    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.display.text = "_ "*len(self.word)
        self.mistakes = 0
        self.turn = 1
        self.changes = 0
        self.im.source='1.png'
        self.set_size()
        

        
    def reset(self):
        word = hangman_game.get_word()
        self.set_size()
        self.display.text = "_ "*len(self.word)
        self.mistakes = 0
        self.turn = 1
        self.changes = 0
        self.im.source='1.png'

                 
    
    def punish(self):
        if self.mistakes==1:
            self.im.source='2.png'
        elif self.mistakes==2:
            self.im.source='3.png'
        elif self.mistakes==3:
            self.im.source='4.png'
        elif self.mistakes==4:
            self.im.source='5.png'
        elif self.mistakes==5:
            self.im.source='6.png'
        elif self.mistakes==6:
            self.im.source='7.png'
        
        


    def match(self, value):
        count = 0
        temp = self.display.text
        temp = temp.split(' ')
        for i in range(len(self.word_list)):
            if value == self.word_list[i]:
                temp[i] = value
                count = count+1
                self.changes = self.changes+1
        if count>0:
            self.display.text = ' '.join(temp)
        else:
            self.mistakes = self.mistakes+1
            self.punish()

    
    def PressbtnA(self):
        self.match('A')
    
    def PressbtnB(self):
        self.match('B')
    
    def PressbtnC(self):
        self.match('C')
    
    def PressbtnD(self):
        self.match('D')
    
    def PressbtnE(self):
        self.match('E')
    
    def PressbtnF(self):
        self.match('F')
    
    def PressbtnG(self):
        self.match('G')
    
    def PressbtnH(self):
        self.match('H')
    
    def PressbtnI(self):
        self.match('I')
    
    def PressbtnJ(self):
        self.match('J')
    
    def PressbtnK(self):
        self.match('K')
    
    def PressbtnL(self):
        self.match('L')
    
    def PressbtnM(self):
        self.match('M')
    
    def PressbtnN(self):
        self.match('N')
    
    def PressbtnO(self):
        self.match('O')
    
    def PressbtnP(self):
        self.match('P')
    
    def PressbtnQ(self):
        self.match('Q')
    
    def PressbtnR(self):
        self.match('R')
    
    def PressbtnS(self):
        self.match('S')
    
    def PressbtnT(self):
        self.match('T')
    
    def PressbtnU(self):
        self.match('U')
    
    def PressbtnV(self):
        self.match('V')
    
    def PressbtnW(self):
        self.match('W')
    
    def PressbtnX(self):
        self.match('X')
    
    def PressbtnY(self):
        self.match('Y')
    
    def PressbtnZ(self):
        self.match('Z')
    
    def PressbtnRESTART(self):
        self.reset()
    
  
    



class mainApp(App):
    def build(self):
        
        
        App.get_running_app()
    
        return MyGridLayout()


# self.MyLabel.setText("hello")
m = mainApp()
m.run()