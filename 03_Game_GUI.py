from tkinter import *
import random


class Start:
    def __init__(self,parent):

        self.start_frame = Frame(pady=10, padx=10)
        self.start_frame.grid()


        self.push_me_button = Button(text="push", command=self.to_game)
        self.push_me_button.grid(row=0, pady=10)


    def to_game(self):

        starting_balance = 50
        stakes = 1

        Game(self, stakes, starting_balance)

        root.withdraw()

class Game:
    def __init__(self,partner, stakes, starting_balance):

        print(stakes)
        print(starting_balance)

        self.balance =IntVar()

        self.balance.set(starting_balance)

        # Set up GUI
        self.game_box =Toplevel()
        self.game_frame = Frame(self.game_box, padx=10)
        self.game_frame.grid()

        #Play Heading row 0
        self.game_heading = Label(self.game_frame, text="Play!", font="Arial 20 bold")
        self.game_heading.grid(row=0)

        #Help text row 1
        self.game_help = Label(self.game_frame, text="Press 'enter' or 'open boxes to play!",
                               font= "Arial 10 italic", fg="red")
        self.game_help.grid(row=1, pady=10)

        box_text = "Arial 16 bold"
        box_back ="#b9ea96"
        box_width= 5



        # The photo winnings frame row 2
        self.game_box_frame = Frame(self.game_frame)
        self.game_box_frame.grid(row=2, pady=10)

        self.game_box1 = Label(self.game_box_frame, text= "?\n", font=box_text, bg=box_back,
                               width=box_width, padx=10,pady=10)
        self.game_box1.grid(row=0, column=0)

        self.game_box2 = Label(self.game_box_frame, text="?\n", font=box_text, bg=box_back,
                               width=box_width, padx=10, pady=10)
        self.game_box2.grid(row=0, column=1, padx=10)

        self.game_box3 = Label(self.game_box_frame, text="?\n", font=box_text, bg=box_back,
                               width=box_width, padx=10, pady=10)
        self.game_box3.grid(row=0, column=2)

        # Play button row 3

        self.game_play = Button(self.game_frame, text="Spin!", font="Arial 20 bold",
                                bg="yellow", width=13)
        self.game_play.grid(row=3)

        # Text that shows ur starting balance. Row 4

        self.game_balance = Label(self.game_frame, text="Welcome, your starting balance is {}!".format(starting_balance),
                                  font="arial 15 bold", fg="green", pady=10)
        self.game_balance.grid(row=4)

        # Help and Game stats button row 5

        self.start_help_frame = Frame(self.game_frame, pady=10)
        self.start_help_frame.grid(row=5)

        # Help and statistics buttons
        self.start_help_button = Button(self.start_help_frame, text="Help",
                                        font="Arial 15 bold",
                                        command=lambda: self.to_help)
        self.start_help_button.grid(row=0, column=0)

        self.start_statistics_button = Button(self.start_help_frame, text="Statistics / Export",
                                              font="Arial 15 bold",
                                              command=lambda: self.to_stats)
        self.start_statistics_button.grid(row=0, column=1, padx=5)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box")
    something = Start(root)
    root.mainloop()