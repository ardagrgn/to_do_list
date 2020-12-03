from itertools import count

from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.textinput import TextInput
from kivy.core.text import LabelBase
from kivy.properties import StringProperty
from kivy.uix.button import Button,ButtonBehavior

class MainApp(App):
    def __init__(self):
        App.__init__(self)
        self.i = 0 # parameter for ids list
        self.liste = ["gorev", "gorev1", "gorev2", "gorev3"] #list of ids of labels
        self.command= []
        self.buttons=["button","button1","button2","button3"] #list of ids of buttons
        self.n = 0 # parameter for edit method


    def write(self): # writing in to "to do" list
        self.i = self.i

        input = self.root.ids["yazi"].text

        self.command.append(input)
        self.root.ids[self.liste[self.i]].text= f"{input}"
        self.root.ids["yazi"].text = ""

        if self.i < 3:
            self.i = self.i+1
        else:
            self.i = 0

    def delete(self,a):

        if len(self.command)-a > 0: # figure outs whether the list has given index
            self.command.pop(a)
            self.re_list()
            self.i = len(self.command)
            return self.i #returns last element number of command list

    def re_list(self): # re-ordering commands when delete command is used

        for n in range(len(self.command)):
            self.root.ids[self.liste[n]].text = f"{self.command[n]}"
        remains = 4- len(self.command)
        if remains > 0:
            for n in range(len(self.command),4):
              self.root.ids[self.liste[n]].text = "Görevini Yaz"

    def edit(self,e_no): # refers for editing specific label
        edit_text = self.root.ids["yazi"].text
        self.n = self.n
        if self.n == 0:
            self.root.ids[self.buttons[e_no]].background_color = [1,1,0,1]
            self.root.ids["yazi"].text = self.root.ids[self.liste[e_no]].text
            self.n = 1
            return self.n
        else:
            self.root.ids[self.buttons[e_no]].background_color = [1, 1, 1, 1]
            self.root.ids[self.liste[e_no]].text= edit_text
            self.n = 0
            self.root.ids["yazi"].text= ""
            return self.n


my_app= MainApp()
my_app.run()

