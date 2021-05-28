# main.py
# GCEL Ground Control Event Logger
# Contributors: Levi Purdy
# 5/27/2021
# Constructed for ACUASI at UAF


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

import AppLayout
from kivy.core.window import Window
#import Config

# TODO: Add mission label text box, and append mission identifier to each entry
# TODO: Add config file to change defaults for custom inputs
# TODO: Add message number counter, and make it incriment between instances of the program


class MyApp(App):
    def build(self):
        # Run init setup functions here
        Window.size = (500, 300)
        #Config.init_config()
        self.title = 'Ground Control Event Logger'

        return AppLayout.layout_main_grid()


MyApp().run()