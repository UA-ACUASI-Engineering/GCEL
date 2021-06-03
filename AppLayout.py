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

custom_buttons = 4
#uas_text_input = TextInput(text='', multiline=False)

def add_header_label(layout):
    lbl = Label(text='Current Logfile:\"'+Logger.logfile_string+'\"')
    layout.add_widget(lbl)

    return layout


def add_uav_launch_land_buttons(layout):
    grid = GridLayout(cols=1)
    uas_label_layout = GridLayout(cols=2)
    lbl = Label(text='UAS Name: ')
    uas_label_layout.add_widget(lbl)

    #global uas_text_input
    uas_text_input = TextInput(text='', multiline=False)
    uas_text_input.bind(on_text_validate=Logger.on_custom_box_enter)
    uas_label_layout.add_widget(uas_text_input)

    grid.add_widget(uas_label_layout)

    uas_launch_button = Button(text='UAS_Launch')
    uas_launch_button.bind(on_press=Logger.log_from_button_uav)
    uas_launch_button.uas_text_input = uas_text_input
    grid.add_widget(uas_launch_button)

    uas_land_button = Button(text='UAS_Landed')
    uas_land_button.bind(on_press=Logger.log_from_button_uav)
    uas_land_button.uas_text_input = uas_text_input
    grid.add_widget(uas_land_button)

    layout.add_widget(grid)

    return layout


def add_custom_buttons(layout):
    for i in range(1,custom_buttons+1):
        custom_button = Button(text=('Log Custom ' + str(i)))
        custom_button.bind(on_press=Logger.log_from_text_box_button)
        custom_button.text_input = TextInput(text='', multiline=False)
        custom_button.text_input.bind(on_text_validate=Logger.on_custom_box_enter)
        layout.add_widget(custom_button)
        layout.add_widget(custom_button.text_input)

    return layout


def layout_main_grid():
    #super(MainScreenBox, self).__init__(**kwargs)
    #self.orientation = 'horizontal'
    layout = GridLayout(cols=1)

    layout = add_header_label(layout)
    uas_launch_landing_grid = GridLayout(cols=2, size_hint_y=None, height=3*50)
    uas_launch_landing_grid = add_uav_launch_land_buttons(uas_launch_landing_grid)
    uas_launch_landing_grid = add_uav_launch_land_buttons(uas_launch_landing_grid)
    layout.add_widget(uas_launch_landing_grid)

    custom_buttons_layout = GridLayout(cols=2, size_hint_y=None, height=custom_buttons*50)
    custom_buttons_layout = add_custom_buttons(custom_buttons_layout)
    layout.add_widget(custom_buttons_layout)

    return layout
    # main_graph = FigureCanvasKivyAgg(plt.gcf())