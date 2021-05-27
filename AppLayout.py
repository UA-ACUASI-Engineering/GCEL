# AppLayout.py
# GCEL Ground Control Event Logger
# Contributors: Levi Purdy
# 5/27/2021
# Constructed for ACUASI at UAF

from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from kivy.clock import Clock

import Logger




def add_buttons(layout):
    custom1_button = Button(text='Log Custom 1')
    custom1_button.bind(on_press=Logger.log_from_buttton)
    custom1_button.text_input = TextInput(text='Mission Start', multiline=False)
    custom1_button.text_input.bind(on_text_validate=Logger.on_custom_box_enter)
    layout.add_widget(custom1_button)
    layout.add_widget(custom1_button.text_input)


    return layout


def layout_main_grid():
    #super(MainScreenBox, self).__init__(**kwargs)
    #self.orientation = 'horizontal'
    layout = GridLayout(cols=1)

    custom_buttons_layout = GridLayout(cols=2)
    custom_buttons_layout = add_buttons(custom_buttons_layout)
    layout.add_widget(custom_buttons_layout)

    return layout
    # main_graph = FigureCanvasKivyAgg(plt.gcf())