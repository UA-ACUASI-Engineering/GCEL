# Logger.py
# GCEL Ground Control Event Logger
# Contributors: Levi Purdy
# 5/27/2021
# Constructed for ACUASI at UAF


import csv
from datetime import datetime

starting_time = datetime.now()
logfile_string = starting_time.strftime('%Y-%m-%dT%H%M%S') + '_GCEL_Event_Log.csv'

with open(logfile_string, 'w', newline='') as csvfile:
    logwriter = csv.writer(csvfile, delimiter=',', quotechar='\"', quoting=csv.QUOTE_MINIMAL)
    logwriter.writerow([datetime.now().isoformat(),'GCEL_Logger_Start'])
    csvfile.close()


def log_from_button(button):
    print("Logging: ", button.text)
    log(button.text)


def log_from_text_box_button(button):
    print("Logging: ", button.text_input.text)
    log(button.text_input.text)


def on_custom_box_enter(instance):
    print("You Pressed enter in: ", instance, " With text in Box: ", instance.text)


def log(text):
    with open(logfile_string, 'a', newline='') as csvfile:
        logwriter = csv.writer(csvfile, delimiter=',', quotechar='\"', quoting=csv.QUOTE_MINIMAL)
        logwriter.writerow([datetime.now().isoformat(), text])
        csvfile.close()