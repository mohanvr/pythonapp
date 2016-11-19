'''
Created on 19-Nov-2016

@author: Mohan vishwa
'''

import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class calcgridlay(GridLayout):
    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "error"    

class calc(App):
    def build(self):
        return calcgridlay()
    
cal = calc()    
cal.run()