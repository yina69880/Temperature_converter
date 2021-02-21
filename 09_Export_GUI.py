from tkinter import *
from functools import partial   # To prevent unwanted windows

import random


class Converter:
    def __init__(self):

        # formatting vaiables...
        background_color = "light blue"

       # in actual program this is blank and is populated with user calculations
        self.all_calc_list = ['0 degrees C is -17.8 degrees F',
                              '0 degrees C is 32 degrees F',
                              '40 degrees C 104 degrees F',
                              '40 degrees C 4.4 degrees F',
                              '12 degrees C 53.6 degrees F',
                              '24 degrees C 75.2 degrees F',
                              '100 degrees C 212 degrees F']

        # converter main screen GUI
        self.converter_frame = Frame(width=300, )