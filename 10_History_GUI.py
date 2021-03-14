from tkinter import *
from functools import partial

import random


class converter:
    def __init__(self):
        # Formatting variables... This color is light orange
        background_color = "#pale green"

        self.all_calc_list = ['0 degrees C is -17.8 degrees F',
                              '0 degrees C is 32 degrees F',
                              '40 degrees C 104 degrees F',
                              '40 degrees C 4.4 degrees F',
                              '12 degrees C 53.6 degrees F',
                              '24 degrees C 75.2 degrees F',
                              '100 degrees C 212 degrees F']

        # Converter Main Screen GUI...
        self.converter_frame = Frame(width=300, height=300, bg=background_color,
                                     pady=10)
        self.converter_frame.grid()

        # Temperature Conversion Heading (row 0)
        self.temp_converter_label = Label(self.converter_frame, text="Temperature Converter",
                                          font=("Arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

        # history Button (row 1)
        self.history_button = Button(self.converter_frame, text="Information",
                                  font=("Arial", "8", "bold"),
                                  bg=background_color,
                                  padx=10, pady=10,
                                  command=lambda: self.history(self.all_calc_list))
        self.history_button.grid(row=1)

    def history(self, calc_history):
        History(self, calc_history)



class History:
    def __init__(self, partner, calc_history):
        # This color is Lightish Yellow
        background = "#EBFF6B"

        # disable history button
        partner.history_button.config(state=DISABLED)

        # Sets up child window (ie: history box)
        self.history_box = Toplevel()

        # If users press 'x' cross at the top, closes history and 'releases' history button.
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))

        # Set up GUI Frame
        self.history_frame = Frame(self.history_box, bg=background)
        self.history_frame.grid()

        # Set up history heading (row 0)
        self.how_heading = Label(self.history_frame, text="Calculation history",
                                 font=("Arial", "15", "bold",),
                                 bg=background)
        self.how_heading.grid(row=0)

        # history text (label, row 1)
        self.history_text = Label(self.history_frame, text="Here are your most recent calculations ",

                               justify=LEFT, width=40, bg=background, wrap=250, padx=10,pady=10)
        self.history_text.grid(row=1)

        # history Output goes here... (Row 2)

        #Generate string from list of calcualtions...

        history_string =""
        if len(calc_history) >= 7:
            for item in range(0,7):
                history_string += calc_history[lens(calc_history)- item -1] + "\n"


        else:
            for item in calc_history:
                history_string += calc_history[len(calc_history) -
                        calc_history.index(item) - 1] + "\n"
                self.history_text.config(text="Here are your most recent calculations ")



        #Dismiss button

        self.dismiss_btn = Button(self.history_frame, text="Dismiss", width=10, bg="orange",
                                  font="arial" "10" "bold", command=partial(self.close_history, partner))
        self.dismiss_btn.grid(row=2, pady=10)



    def close_history(self, partner):
        # Put history button back to normal...
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    something = converter()
    root.mainloop()