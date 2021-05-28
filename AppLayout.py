# AppLayout.py
# GCEL Ground Control Event Logger
# Contributors: Levi Purdy
# 5/27/2021
# Constructed for ACUASI at UAF

from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

from kivy.clock import Clock

import Logger


def add_header_label(layout):
    lbl = Label(text='Current Logfile:\"'+Logger.logfile_string+'\"')
    layout.add_widget(lbl)

    return layout


def add_base_buttons(layout):
    uas_launch_button = Button(text='UAS_Launch')
    uas_launch_button.bind(on_press=Logger.log_from_button)
    layout.add_widget(uas_launch_button)

    uas_land_button = Button(text='UAS_Landed')
    uas_land_button.bind(on_press=Logger.log_from_button)
    layout.add_widget(uas_land_button)

    return layout


def add_custom_buttons(layout):
    custom1_button = Button(text='Log Custom 1')
    custom1_button.bind(on_press=Logger.log_from_text_box_button)
    custom1_button.text_input = TextInput(text='', multiline=False)
    custom1_button.text_input.bind(on_text_validate=Logger.on_custom_box_enter)
    layout.add_widget(custom1_button)
    layout.add_widget(custom1_button.text_input)

    custom2_button = Button(text='Log Custom 2')
    custom2_button.bind(on_press=Logger.log_from_text_box_button)
    custom2_button.text_input = TextInput(text='', multiline=False)
    custom2_button.text_input.bind(on_text_validate=Logger.on_custom_box_enter)
    layout.add_widget(custom2_button)
    layout.add_widget(custom2_button.text_input)

    custom3_button = Button(text='Log Custom 3')
    custom3_button.bind(on_press=Logger.log_from_text_box_button)
    custom3_button.text_input = TextInput(text='', multiline=False)
    custom3_button.text_input.bind(on_text_validate=Logger.on_custom_box_enter)
    layout.add_widget(custom3_button)
    layout.add_widget(custom3_button.text_input)

    return layout


def layout_main_grid():
    #super(MainScreenBox, self).__init__(**kwargs)
    #self.orientation = 'horizontal'
    layout = GridLayout(cols=1)

    layout = add_header_label(layout)
    layout = add_base_buttons(layout)

    custom_buttons_layout = GridLayout(cols=2, size_hint_y=None, height=3*50)
    custom_buttons_layout = add_custom_buttons(custom_buttons_layout)
    layout.add_widget(custom_buttons_layout)

    return layout
    # main_graph = FigureCanvasKivyAgg(plt.gcf())