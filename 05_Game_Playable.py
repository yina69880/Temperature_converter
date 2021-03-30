from tkinter import *
import random


class Start:
    def __init__(self, parent):

        # GUI to get started balance and stakes
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        self.push_me_button = Button(text="Push Me", command=self.to_game)
        self.push_me_button.grid(row=0, pady=10)

    def to_game(self):

        # retrieve starting balance
        starting_balance = 50
        stakes = 2

        Game(self, stakes, starting_balance)

        # hide start up window
        root.withdraw()


class Game:
    def __init__(self, partner, stakes, starting_balance):
        print(stakes)
        print(starting_balance)

        # initialise variables
        self.balance = IntVar()
        # set starting balance to amount entered by user at start of game
        self.balance.set(starting_balance)

        # Get value of stakes (multiplier for winnings)
        self.multiplier = IntVar()
        self.multiplier.set(stakes)

        # Set up GUI
        self.game_box = Toplevel()
        self.game_frame = Frame(self.game_box)
        self.game_frame.grid()


        # Play Heading row 0
        self.heading_label = Label(self.game_frame, text="Play!",
                                  font="Arial 24 bold", pady=10,
                                  padx=10)
        self.heading_label.grid(row=0)


        # instructions label
        self.instructions_label = Label(self.game_frame, wrap=300, justify=LEFT,
                                        text="Press <enter> or click the 'Open Boxes' button"
                                             " to reveal the contents of the mystery boxes.",
                                        font="Arial 10", padx=10, pady=10)
        self.instructions_label.grid(row=1)

        # Boxes go here
        box_text = "Arial 16 bold"
        box_back = "#b9ea96"
        box_width = 5
        self.box_frame = Frame(self.game_frame)
        self.box_frame.grid(row=2, pady=10)

        self.prize1_label = Label(self.box_frame, text="?\n", font=box_text,
                                  bg=box_back, width=box_width, padx=10, pady=10)
        self.prize1_label.grid(row=0, column=0)

        self.prize2_label = Label(self.box_frame, text="?\n", font=box_text,
                                  bg=box_back, width=box_width, padx=10, pady=10)
        self.prize2_label.grid(row=0, column=1)

        self.prize3_label = Label(self.box_frame, text="?\n", font=box_text,
                                  bg=box_back, width=box_width, padx=10, pady=10)
        self.prize3_label.grid(row=0, column=2)

        # Play button row 3
        self.game_play = Button(self.game_frame, text="Spin!", font="Arial 20 bold",
                                bg="#FFFF33", width=13, command=self.reveal_boxes, pady=10, padx=10)
        self.game_play.grid(row=3)

        # Text that shows ur starting balance. Row 4

        start_text = "Game Cost: ${} \n " "\nHow much " \
                     "will you win?".format(stakes * 5)

        self.game_balance = Label(self.game_frame, text=start_text,
                                  font="Arial 12 bold", fg="green", wrap=300, justify=LEFT)
        self.game_balance.grid(row=4, pady=10)

        # Help and Game stats button row 5
        self.help_export_frame = Frame(self.game_frame)
        self.help_export_frame.grid(row=5, pady=10)

        self.help_button = Button(self.help_export_frame, text="Help",
                                        font="Arial 15 bold", bg="#808080", fg="white")
        self.help_button.grid(row=0, column=0, padx=2)

        self.start_statistics_button = Button(self.help_export_frame, text="Statistics / Export",
                                              font="Arial 15 bold", bg="#003366",
                                              fg="white")
        self.start_statistics_button.grid(row=0, column=1, padx=2)

        #Quit Button
        self.quit_button = Button(self.game_frame, text="Quit", fg="white",
                                 bg="#660000", font="Arial 15 bold", width=20, padx=10, pady=10, commabd=self.to_quit)
        self.quit_button.grid(row=6, pady=10)

    def reveal_boxes(self):
        # retrieve the balance from the initial function...
        current_balance = self.balance.get()
        stakes_multiplier = self.multiplier.get()

        round_winnings = 0
        prizes = []
        backgrounds = []
        for thing in range(0, 3):
            prize_num = random.randint(1, 100)

            if 0 < prize_num <= 5:
                prize = "Gold\n(${})".format(5 * stakes_multiplier)
                back_colour = '#CEA935'
                round_winnings += 5 * stakes_multiplier
            elif 5 < prize_num <= 25:
                prize = "Silver\n(${})".format(2 * stakes_multiplier)
                back_colour = '#B7B7B5'
                round_winnings += 2 * stakes_multiplier
            elif 25 < prize_num <= 65:
                prize = "Copper\n(${})".format(1 * stakes_multiplier)
                back_colour = '#BC7F61'
                round_winnings += stakes_multiplier
            else:
                prize = "Lead\n$0"
                back_colour = '#595E71'

            prizes.append(prize)
            backgrounds.append(back_colour)
            print(prizes)

        # Display prizes...
        self.prize1_label.config(text=prizes[0], bg=backgrounds[0])
        self.prize2_label.config(text=prizes[1], bg=backgrounds[1])
        self.prize3_label.config(text=prizes[2], bg=backgrounds[2])

        # Deduct cost of game
        current_balance -= 5 * stakes_multiplier

        # Add winnings
        current_balance += round_winnings

        # Set balnce to new balance
        self.balance.set(current_balance)

        balance_statement = "Game Cost: ${} \nPayback: ${} \n" \
                            "Current Balance: ${}".format(5 * stakes_multiplier,
                                                          round_winnings,
                                                          current_balance)

        # Edit label so users can see their new balance
        self.game_balance.configure(text=balance_statement)

        if current_balance < 5 * stakes_multiplier:
            self.play_button.config(state=DISABLED)
            self.game_box.focus()
            self.play_button.config(text="Game Over")

            balance_statement = "Current Balance: ${}\n" \
                                "Your balance is too low. you can only quit " \
                                "or view your stats. Sorry about that.".format(current_balance)
            self.balance_label.config(fg="#660000", font="Arial 10 bold",
                                      text=balance_statement)

    def to_quit(self):
        root.destroy()



# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box")
    something = Start(root)
    root.mainloop()