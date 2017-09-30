# Created by: David Wang
# Created on: 25-Sep-2017
# Created for: ICS3U
# Daily Assignment - Unit1-04
# This program displays circumference

import ui

def calculate_touch_up_inside(sender):
    
    PI = 3.14
    
    radius = float(view['radius_textbox'].text)
    
    circumference = 2 * PI * radius
    
    view['answer_label'].text = 'The circumference is: ' + str(circumference) + ' cm'

view = ui.load_view()
view.present('full_screen')
