# Logger.py
# GCEL Ground Control Event Logger
# Contributors: Levi Purdy
# 5/27/2021
# Constructed for ACUASI at UAF

# TODO: find time library for python and get to to ISO format
# TODO: setup logfile to log text in textbox when button is pressed
# TODO: setup python to executable compiler
# TODO: expand UI to 3 custom button rows


def log_from_buttton(text_to_log):
    print("Logging: ", text_to_log)


def on_custom_box_enter(instance):
    print("You Pressed enter in: ", instance, " With text in Box: ", instance.text)
