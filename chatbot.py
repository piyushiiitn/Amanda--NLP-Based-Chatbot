#General Libraries
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn
import re
import aiml
import subprocess
import os
import argparse
from MyKernel import MyKernel
from time import sleep
#end of general libraries

#Graphics library
import kivy
import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.widget import Widget

from kivy.uix.popup import Popup
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from kivy.uix.modalview import ModalView
from kivy.properties import (StringProperty, ObjectProperty, OptionProperty,NumericProperty, ListProperty)


import time, threading
#end of Graphics libraries

DEBUG = True
SHOW_MATCHES = True

def course_code(sentence):
	try:
		words = re.compile('\w+').findall(sentence)
		new_sentence = ""
		for index, word in enumerate(words):
			if (word == "cs") and (index < len(words)-1) and (words[index+1].isdigit()):
				new_sentence = new_sentence + word
			else:
				new_sentence = new_sentence + word + " "
		return new_sentence
	except:
		return sentence

def remove_aiml_char(sentence):
    try:
        new_sentence = sentence.replace("_","")
        new_sentence = new_sentence.replace("*","")
        return new_sentence
    except:
        return sentence

dict = {'NN': 'NOUN', 'JJ': 'ADJ'}
dict['NNS'] = 'NOUN'
dict['NNP'] = 'NOUN'
dict['NNPS'] = 'NOUN'
dict['PRP'] = 'NOUN'
dict['PRP$'] = 'NOUN'
dict['RB'] = 'ADV'
dict['RBR'] = 'ADV'
dict['RBS'] = 'ADV'
dict['VB'] = 'VERB'
dict['VBD'] = 'VERB'
dict['VBG'] = 'VERB'
dict['VBN'] = 'VERB'
dict['VBP'] = 'VERB'
dict['VBZ'] = 'VERB'
dict['WRB'] = 'ADV'

grade_codes = ["ap","aa","ab","bb","bc","cc","cd","dd","dx","fr"]

BOT_INFO = {
    "name": "Amanda",
    "birthday": "July 5th 2017",
    "location": "Kanpur",
    "master": "I have no Master",
    "website":"follow me on twitter",
    "gender": "Female",
    "age": "20",
    "size": "",
    "religion": "Humanity",
    "party": "All night !"
}

k = MyKernel()
k.learn("aiml/standard/std-startup.xml")
k.respond("LOAD AIML B")

for key,val in BOT_INFO.items():
	k.setBotPredicate(key,val)

class PopupBox(ModalView):
    '''
    :Events:
        `on_open`:
            Fired when the Popup is opened.
        `on_dismiss`:
            Fired when the Popup is closed. If the callback returns True, the
            dismiss will be canceled.
    '''

    title = StringProperty('No title')
    '''String that represents the title of the popup.

    :attr:`title` is a :class:`~kivy.properties.StringProperty` and defaults to
    'No title'.
    '''

    title_size = NumericProperty('14sp')
    '''Represents the font size of the popup title.

    .. versionadded:: 1.6.0

    :attr:`title_size` is a :class:`~kivy.properties.NumericProperty` and
    defaults to '14sp'.
    '''

    title_align = OptionProperty('left',
                                 options=['left', 'center', 'right', 'justify'])
    '''Horizontal alignment of the title.

    .. versionadded:: 1.9.0

    :attr:`title_align` is a :class:`~kivy.properties.OptionProperty` and
    defaults to 'left'. Available options are left, center, right and justify.
    '''

    title_font = StringProperty('Roboto')
    '''Font used to render the title text.

    .. versionadded:: 1.9.0

    :attr:`title_font` is a :class:`~kivy.properties.StringProperty` and
    defaults to 'Roboto'.
    '''

    content = ObjectProperty(None)
    '''Content of the popup that is displayed just under the title.

    :attr:`content` is an :class:`~kivy.properties.ObjectProperty` and defaults
    to None.
    '''

    title_color = ListProperty([1, 1, 1, 1])
    '''Color used by the Title.

    .. versionadded:: 1.8.0

    :attr:`title_color` is a :class:`~kivy.properties.ListProperty` and
    defaults to [1, 1, 1, 1].
    '''

    separator_color = ListProperty([47 / 255., 167 / 255., 212 / 255., 1.])
    '''Color used by the separator between title and content.

    .. versionadded:: 1.1.0

    :attr:`separator_color` is a :class:`~kivy.properties.ListProperty` and
    defaults to [47 / 255., 167 / 255., 212 / 255., 1.]
    '''

    separator_height = NumericProperty('2dp')
    '''Height of the separator.

    .. versionadded:: 1.1.0

    :attr:`separator_height` is a :class:`~kivy.properties.NumericProperty` and
    defaults to 2dp.
    '''

    # Internal properties used for graphical representation.

    _container = ObjectProperty(None)

class MyApp(App):
# layout
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.lbl1 = Label(text="Amanda:   Welcome\n",size_hint=(1,0.86),color=(255,255,255,1),multiline=True,font_size=25,text_size=(1150,450),halign='left',valign='bottom')
        layout.add_widget(self.lbl1)
        layout2 = BoxLayout(size_hint=(1,0.14))
        self.txt1 = TextInput(text='',size_hint=(0.8,1),font_size=20)
        layout2.add_widget(self.txt1)
        self.btn1 = Button(text="Submit",size_hint=(0.2,1))
        self.btn1.bind(on_press=self.buttonClicked)
        # self.btn1.bind(on_press=self.open_popup)
        layout2.add_widget(self.btn1)
        layout.add_widget(layout2)
            
        return layout

    def show_popup(self):
        print "hi"
        content=Label(text="thinking")
        self.pop_up = Popup(title='Test popup',
                  size_hint=(None, None), size=(256, 256),
                  content=content, disabled=True)
        self.pop_up.open()

    # def open_popup(self,instance):
    #     self.popup.open()
    #     Clock.schedule_once(self.do_stuff(), 0)

    # def do_stuff(self):
    #     self.buttonClicked()
    #     self.popup.dismiss()
    #     class myApp(App):
    # def build(self):
    #     self.btn = Button(text='Run')
    #     self.btn.bind(on_press = self.open_popup)
    #     self.box = BoxLayout()
    #     self.box.add_widget(self.btn)
    #     self.popup = Popup(title='',content=Label(text='Loading'))
    #     return self.box

    # def open_popup(self, instance):
    #     self.popup.open()
    #     t = threading.Thread(target=self.do_stuff).start()
        
    # def do_stuff(self):
    #     self.box.clear_widgets()
    #     self.box.add_widget(MyGraph())
    #     self.popup.dismiss()

################################################################################
        

    # def __init__(self, **kwargs):
    #     self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
    #     self._keyboard.bind(on_key_down=self._on_keyboard_down)

    # def _keyboard_closed(self):
    #     self._keyboard.unbind(on_key_down=self._on_keyboard_down)
    #     self._keyboard = None

    # def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
    #     if keycode[1] == 'enter':
    #         self.btn1.buttonClicked()
    #     return True

# button click function
    def dismiss_popup(self):
        print "closing"
        self.pop_up.dismiss()

    def buttonClicked(self,button):
        # mythread = threading.Thread(target=self.show_popup)
        # mythread.start()
        # mythread.join()  
        # print "clicked"
        myinput = self.txt1.text
        self.lbl1.text = self.lbl1.text + "\nUser:   "+myinput
        sentence = myinput.lower()
        sentence = course_code(sentence)
        stop_words = set(stopwords.words('english'))

        word_tokens = word_tokenize(sentence)

        filtered_sentence = [w for w in word_tokens if not w in stop_words]
        # print filtered_sentence
        temp = nltk.pos_tag(filtered_sentence)
        new_sentence = ""
        for i in temp:
            try:
                z = i[1]
                if (dict[z] != None):
                    part_speech = dict[z]
                else:
                    part_speech = 'NOUN'

                if(part_speech == 'NOUN'):
                    word = wn.morphy(i[0],wn.NOUN)
                elif(part_speech == 'VERB'):
                    word = wn.morphy(i[0],wn.VERB)
                elif(part_speech == 'ADV'):
                    word = wn.morphy(i[0],wn.ADV)
                elif(part_speech == 'ADJ'):
                    word = wn.morphy(i[0],wn.ADJ)
                word1 = wn.synsets(word)[0].lemmas()[0].name()
                if i[0] in grade_codes:
                    word1 = i[0]
            except:
                word1 = i[0]
            new_sentence = new_sentence+" "+word1.lower()
            new_sentence = remove_aiml_char(new_sentence)

        #----------uncomment to debug----------------------
        if DEBUG:
            #printing first output
            matchedPattern = k.matchedPattern(myinput)
            response = k.respond(myinput)
            try:
                if SHOW_MATCHES:
                    print "Matched Pattern: "
                    print k.formatMatchedPattern(matchedPattern[0])
                    pattern = k.getPredicate("topic",'_global')
                    print "TOPIC:",pattern
                else:
                    print "-------------------------"
            except:
                print "No match found"
            print "Normal Response: ",response

            # printing after processing
            print "--------------------------------"
            print "new_sentence :",new_sentence
            matchedPattern = k.matchedPattern(new_sentence)
            response = k.respond(new_sentence)
            try:
                if SHOW_MATCHES:
                    print "Matched Pattern: "
                    print k.formatMatchedPattern(matchedPattern[0])
                    pattern = k.getPredicate("topic",'_global')
                    print "TOPIC:",pattern
                else:
                    print "-------------------------"
            except:
                print "No match found"
            print "New Response: ",response

        #--------------------------------------------------
        response = k.respond(myinput)
        response1 = k.respond(new_sentence)
        if response1 != "" and response1[0] == '$':
            response = response1[1:]
        # print response  
        # mythread = threading.Thread(target=self.dismiss_popup)
        # mythread.start()   
        # mythread.join()       
        # self.show_popup()
        self.lbl1.text = self.lbl1.text + "\nAmanda:   "+response+"\n"
        self.txt1.text = ""

MyApp().run()
