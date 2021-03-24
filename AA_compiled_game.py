from tkinter import *
from functools import partial
import os
import random

class Start:
    def __init__(self, partner):
        # Start GUI
        self.start_frame = Frame(padx=10, pady=10, bg="#D4E1F5")
        self.start_frame.grid()

        # Set Initial balance to zero
        self.starting_funds = IntVar()
        self.starting_funds.set(0)

        # background
        background = "#D4E1F5"

        # Mystery box Heading (row 0)
        self.mystery_box_label = Label(self.start_frame, text="Mystery Box Game",
                                       font="Arial 16 bold", bg=background)
        self.mystery_box_label.grid(row=0)

        # Initial instructions (row 1)
        self.mystery_instructions = Label(self.start_frame, text='Please enter a dollar amount ($5~$50) in the box '
                                                                 'below. \n '
                                                                 'Then click the \'Add Funds\' button and choose your '
                                                                 'stakes. \n '
                                                                 'The higher the stakes, the more you can win!',
                                          font="Arial 8 italic", bg=background)
        self.mystery_instructions.grid(row=1)

        # Entry box and Error Label (row 2)
        self.start_error_frame = Frame(self.start_frame, width=200, bg=background)
        self.start_error_frame.grid(row=2)

        self.start_amount_entry = Entry(self.start_error_frame,
                                        font="Arial 13 bold")
        self.start_amount_entry.grid(row=0, column=0)

        self.start_add_funds = Button(self.start_error_frame, text="Add funds!",
                                      font="Arial 13 bold", bg=background, command=self.check_funds)
        self.start_add_funds.grid(row=0, column=1)

        self.amount_error_label = Label(self.start_error_frame, bg=background, fg="maroon", text="",
                                        font=" Arial 10 bold", wrap=275, justify=LEFT)
        self.amount_error_label.grid(row=1, columnspan=2, pady=5)

        # Buttons frame ( row 3)

        self.stakes_frame = Frame(self.start_frame, bg=background)
        self.stakes_frame.grid(row=3)

        # Button Font
        button_font = "Oswald 12 bold"

        # Low Stakes Button
        self.low_stakes_button = Button(self.stakes_frame, text="Low ($5)",
                                        font=button_font, bg="#FFAF7A",
                                        command=lambda: self.to_game(1))
        self.low_stakes_button.grid(row=0, column=0, pady=10)

        # Medium Stakes Button
        self.med_stakes_button = Button(self.stakes_frame, text="Medium ($10)",
                                        font=button_font, bg="#FFE5B4",
                                        command=lambda: self.to_game(2))
        self.med_stakes_button.grid(row=0, column=1, pady=10, padx=5)

        # High Stakes Button
        self.high_stakes_button = Button(self.stakes_frame, text="High ($15)",
                                         font=button_font, bg="#FFB6C1",
                                         command=lambda: self.to_game(3))
        self.high_stakes_button.grid(row=0, column=2, pady=10, padx=5)

        # Disable all stakes buttons at start.
        self.low_stakes_button.config(state=DISABLED)
        self.med_stakes_button.config(state=DISABLED)
        self.high_stakes_button.config(state=DISABLED)

    def check_funds(self):
        starting_balance = self.start_amount_entry.get()

        error_back = "#ffafaf"
        has_errors = "no"

        self.start_amount_entry.config(bg="white")
        self.amount_error_label.config(text="")

        self.low_stakes_button.config(state=DISABLED)
        self.med_stakes_button.config(state=DISABLED)
        self.high_stakes_button.config(state=DISABLED)

        try:
            starting_balance = int(starting_balance)

            if starting_balance < 5:
                has_errors = "yes"
                error_feedback = "Sorry, the minimum amount is $5"

            elif starting_balance > 50:
                has_errors = "yes"
                error_feedback = "Too high! the maximum amount is $50"



            elif starting_balance >= 15:
                self.low_stakes_button.config(state=NORMAL)
                self.med_stakes_button.config(state=NORMAL)
                self.high_stakes_button.config(state=NORMAL)


            elif starting_balance >= 10:
                self.low_stakes_button.config(state=NORMAL)
                self.med_stakes_button.config(state=NORMAL)
            else:
                self.low_stakes_button.config(state=NORMAL)


        except ValueError:
            has_errors = "yes"
            error_feedback = "Please enter a dollar amount (no text / decimal)"

        if has_errors == "yes":
            self.start_amount_entry.config(bg=error_back)
            self.amount_error_label.config(text=error_feedback)
        else:
            self.starting_funds.set(starting_balance)

    def to_game(self, stakes):
        starting_balance = self.starting_funds.get()

        Game(self, stakes, starting_balance)

        self.start_frame.destroy()
class Game:
    def __init__(self, partner, stakes, starting_balance):

        self.balance = IntVar()

        self.balance.set(starting_balance)

        # Get value of stakes (multiplier for winnings)
        self.multiplier = IntVar()
        self.multiplier.set(stakes)

        # List for holding stats
        self.round_stats_list = []
        self.game_stats_list = [starting_balance, starting_balance]

        # Set up GUI
        self.game_box = Toplevel()

        self.game_box.protocol('WM_DELETE_WINDOW', self.to_quit)

        self.game_frame = Frame(self.game_box, padx=10)
        self.game_frame.grid()

        # Play Heading row 0
        self.game_heading = Label(self.game_frame, text="Play!", font="Arial 20 bold")
        self.game_heading.grid(row=0)

        # Help text row 1
        self.game_help = Label(self.game_frame, text="Press 'enter' or 'open boxes to play!",
                               font="Arial 10 italic", fg="red")
        self.game_help.grid(row=1, pady=10)

        # The photo winnings frame row 2

        self.game_box_frame = Frame(self.game_frame)
        self.game_box_frame.grid(row=2, pady=10)

        photo = PhotoImage(file="./Mystery_box_winnings_images/question.gif")

        self.prize1_label = Label(self.game_box_frame, image=photo,
                                  padx=10, pady=10)
        self.prize1_label.photo = photo
        self.prize1_label.grid(row=0, column=0)

        self.prize2_label = Label(self.game_box_frame, image=photo,
                                  padx=10, pady=10)
        self.prize2_label.photo = photo
        self.prize2_label.grid(row=0, column=1, padx=10)

        self.prize3_label = Label(self.game_box_frame, image=photo,
                                  padx=10, pady=10)
        self.prize3_label.photo = photo
        self.prize3_label.grid(row=0, column=2)

        # Play button row 3

        self.game_play = Button(self.game_frame, text="Spin!", font="Arial 20 bold",
                                bg="yellow", width=13, command=self.reveal_boxes)
        self.game_play.grid(row=3)

        self.game_play.focus()
        self.game_play.bind('<Return>', lambda e: self.reveal_boxes())
        self.game_play.grid(row=3)

        # Text that shows ur starting balance. Row 4

        start_text = "Game Cost: ${} \n " "\nHow much " \
                     "will you win?".format(stakes * 5)

        self.game_balance = Label(self.game_frame, text=start_text,
                                  font="arial 15 bold", fg="green", pady=10)
        self.game_balance.grid(row=4)

        # Help and Game stats button row 5

        self.start_help_frame = Frame(self.game_frame, pady=10)
        self.start_help_frame.grid(row=5)

        # Help and statistics buttons
        self.start_help_button = Button(self.start_help_frame, text="Help",
                                        font="Arial 15 bold",
                                        command=self.to_help)
        self.start_help_button.grid(row=0, column=0)

        self.start_statistics_button = Button(self.start_help_frame, text="Statistics / Export",
                                              font="Arial 15 bold",
                                              command=lambda: self.to_stats(self.round_stats_list,self.game_stats_list))
        self.start_statistics_button.grid(row=0, column=1, padx=5)

        # Quit button
        self.quit_button = Button(self.game_frame, text="Quit", fg="white",
                                  bg="#660000", font="Arial 15 bold", width=20,
                                  command=self.to_quit, padx=10, pady=10)
        self.quit_button.grid(row=6, pady=10)

    def reveal_boxes(self):

        current_balance = self.balance.get()
        stakes_multiplier = self.multiplier.get()

        round_winnings = 0
        prizes = []
        stats_prizes = []

        copper = []
        for cu in os.listdir("Mystery_box_winnings_images/cu"):
            if cu.endswith(".gif"):
                copper.append("Mystery_box_winnings_images/cu/{}".format(cu))
        copper.sort()

        silver = []
        for ag in os.listdir("Mystery_box_winnings_images/ag"):
            if ag.endswith(".gif"):
                silver.append("Mystery_box_winnings_images/ag/{}".format(ag))
        silver.sort()

        gold = []
        for au in os.listdir("Mystery_box_winnings_images/au"):
            if au.endswith(".gif"):
                gold.append("Mystery_box_winnings_images/au/{}".format(au))
        gold.sort()

        for thing in range(0, 3):

            prize_num = random.randint(1, 100)

            if 0 < prize_num <= 5:
                prize = PhotoImage(file=gold[stakes_multiplier-1])
                prize_list = "Gold\n(${})".format(5 * stakes_multiplier)
                round_winnings += 5 * stakes_multiplier
            elif 5 < prize_num <= 25:
                prize = PhotoImage(file=silver[stakes_multiplier-1])
                prize_list = "Silver\n(${})".format(2 * stakes_multiplier)
                round_winnings += 2 * stakes_multiplier
            elif 25 < prize_num <= 65:
                prize = PhotoImage(file=copper[stakes_multiplier-1])
                prize_list = "Copper\n(${})".format(1 * stakes_multiplier)
                round_winnings += 1 * stakes_multiplier
            else:
                prize = PhotoImage(file="./Mystery_box_winnings_images/lead.gif")
                prize_list = "Lead $0"

            prizes.append(prize)
            stats_prizes.append(prize_list)

        photo1 = prizes[0]
        photo2 = prizes[1]
        photo3 = prizes[2]

        # Display prizes...
        self.prize1_label.config(image=photo1)
        self.prize1_label.photo = photo1
        self.prize2_label.config(image=photo2)
        self.prize2_label.photo = photo2
        self.prize3_label.config(image=photo3)
        self.prize3_label.photo = photo3

        # Deduct cost of game
        current_balance -= 5 * stakes_multiplier

        # Add winnings
        current_balance += round_winnings

        # Set balance to new balance
        self.balance.set(current_balance)

        self.game_stats_list[1]=current_balance

        balance_statement = "Game Cost: ${} \nPayback: ${} \n" \
                            "Current Balance: ${}".format(5 * stakes_multiplier,
                                                          round_winnings,
                                                          current_balance)

        # Add round results to stats list
        round_summary =  \
                        "Round Winnings ${} | Balance: " \
                    "${}".format(round_winnings,
                                 current_balance)
        self.round_stats_list.append(round_summary)

        # Edit label so users can see their new balance
        self.game_balance.configure(text=balance_statement)

        if current_balance < 5 * stakes_multiplier:
            self.game_play.config(state=DISABLED)
            self.game_box.focus()
            self.game_play.config(text="Game Over")

            balance_statement = "Current Balance ${}\n" \
                                "Your balance is too low. You can only quit " \
                                "or view your stats.".format(current_balance)
            self.game_balance.config(fg="#660000", font="Arial 10 bold",
                                     text=balance_statement)

    def to_quit(self):
        root.destroy()

    def to_help(self):
        get_help = Help(self)
        get_help.help_text.configure(text="Choose an amount to play with and then choose your stakes. \n\nHigher "
                                          "the stakes means that it costs more per round but you can win "
                                          "more as well\n\n"
                                            "Safe (x1), Medium(x2) and Extreme (x3)\n\n"
                                          "Once pressing your stakes there will be three mystery boxes. \n"
                                          "To reveal the contents press 'Spin!', if you do not have sufficient funds "
                                          "button will no longer operate. \n\n"
                                          "The winnings will be automatically added back to your balance \n\n"
                                          "The following winnings are... \n\n"
                                          "Lead ($0)|Copper ($1)|Silver($2)|Gold($5)")

    def to_stats(self, game_history, game_stats):
        History(self, game_history, game_stats)
class History:
    def __init__(self, partner, game_history, game_stats):

        # disable history button
        partner.start_statistics_button.config(state=DISABLED)

        heading = "Arial 12 bold"
        content = "Arial 12"

        # Sets up child window (ie: history box)
        self.history_box = Toplevel()

        # If users press 'x' cross at the top, closes history and 'releases' history button.
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))

        # Set up GUI Frame
        self.history_frame = Frame(self.history_box)
        self.history_frame.grid()

        # Set up history heading (row 0)
        self.how_heading = Label(self.history_frame, text="Game Statistics",
                                 font=("Arial", "19", "bold",)
                                 )
        self.how_heading.grid(row=0)

        # history text (label, row 1)
        self.history_text = Label(self.history_frame, text="Here are your Game Statistics. "
                                                           "Please use the export button to access the result",
                                  justify=LEFT, width=40, wrap=250, padx=10, pady=10)
        self.history_text.grid(row=1)

        # Stating Balance (row 2)
        self.detail_frame = Frame(self.history_frame)
        self.detail_frame.grid(row=2)


        #Starting Balance row 2.0

        self.start_balance_label = Label(self.detail_frame,
                                         text="Starting Balance:",
                                         font=heading,
                                         anchor="e")
        self.start_balance_label.grid(row=0, column=0, padx=0)

        self.start_balance_value_label = Label(self.detail_frame,
                                               font=content, text="${}".format(game_stats[0]),
                                               anchor="w")
        self.start_balance_value_label.grid(row=0,column=1,padx=0)

        # Current Balance (row2.2)
        self.current_balance_label = Label (self.detail_frame,
                                            text="Current Balance:", font=heading,
                                            anchor="e")
        self.current_balance_label.grid(row=1, column=0, padx=0)

        self.current_balance_value_label= Label(self.detail_frame, font=content,text="${}".format(game_stats[1]),
                                                anchor="w")
        self.current_balance_value_label.grid(row=1,column=1,padx=0)

        if game_stats[1] >= game_stats[0]:
            win_loss = "Amount won:"
            amount = game_stats[1] - game_stats[0]
            win_loss_fg = "green"
        else:
            win_loss = "Amount Lost:"
            amount = game_stats[0] - game_stats[1]
            win_loss_fg = "red"

        # Amount won/ lost (row 2.3)
        self.wind_loss_label = Label(self.detail_frame,
                                     text=win_loss, font=heading,
                                     anchor="e")
        self.wind_loss_label.grid(row=2, column=0, padx=0)

        self.wind_loss_value_label = Label(self.detail_frame, font=content,
                                           text="${}".format(amount),
                                           fg=win_loss_fg, anchor="w")
        self.wind_loss_value_label.grid(row=2 ,column=1 ,padx=0)

        # Rounds Played (row2.4)
        self.games_played_label = Label(self.detail_frame,
                                        text="Rounds Played:", font=heading,
                                        anchor="e")
        self.games_played_label.grid(row=4,column=0,padx=0)

        self.games_played_value_label = Label(self.detail_frame, font=content,
                                              text=len(game_history), anchor="w")
        self.games_played_value_label.grid(row=4, column=1, padx=0)

        # Export / Dismiss Buttons Frame (Row 3)
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        # Export Button
        self.export_button = Button(self.export_dismiss_frame, text="Export",
                                    font="Arial 15 bold", bg="darkblue",fg="white",
                                    command=partial(lambda: self.export(game_history,game_stats)))
        self.export_button.grid(row=0, column=0,padx=5)

        if len(game_history) == 0:
            self.export_button.config(state=DISABLED)

        # Dismiss Button
        self.dismiss_button = Button(self.export_dismiss_frame, text="Dismiss",
                                     font="Arial 15 bold",bg="maroon",fg="white",
                                    command=partial(self.close_history, partner))
        self.dismiss_button.grid(row=0, column=1)

    def close_history(self, partner):
        # Put history button back to normal...
        partner.start_statistics_button.config(state=NORMAL)
        self.history_box.destroy()

    def export(self, game_history, all_game_stats):
        Export(self, game_history, all_game_stats)
class Export:
    def __init__(self, partner, game_history, all_game_stats):

        # disable export button
        partner.export_button.config(state=DISABLED)

        # Sets up child window (ie: export box)
        self.export_box = Toplevel()

        # If users press 'x' cross at the top, closes export and 'releases' export button.
        self.export_box.protocol('WM_DELETE_WINDOW', partial(self.close_export, partner))

        # Set up GUI Frame
        self.export_frame = Frame(self.export_box, width=300)
        self.export_frame.grid()

        # Set up Export heading (row 0)
        self.how_heading = Label(self.export_frame, text="Export / Instructions",
                                 font="Arial 15 bold")
        self.how_heading.grid(row=0)

        # Export text (label, row 1)
        self.export_text = Label(self.export_frame, text="Enter a filename in the box below",
                                 justify=LEFT, width=40, wrap=250)
        self.export_text.grid(row=1)

        # Warning text (label, row2)
        self.export_text = Label(self.export_frame, text="If the filename you entered already exists,"
                                                         "it will be overwritten.", justify=LEFT,
                                 fg='red', font="Arial 10 italic",
                                 wrap=225, padx=10, pady=10)
        self.export_text.grid(row=2, pady=10)

        # Filename Entry Box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="Arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        # Error Message Labels (initially blank, row 4)
        self.save_error_label = Label(self.export_frame, text="", fg="maroon"
                                      )
        self.save_error_label.grid(row=4)

        # Save / Cancel Frame (row 5)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        # Save and Cancel buttons (row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, text="Save",
                                  command=partial(lambda: self.save_history(partner, game_history,all_game_stats)))
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)

    def close_export(self, partner):
        # Put export button back to normal...
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()

    def save_history(self, partner, game_history, game_stats):

        valid_char = "[A-Za-z0-9_]"
        has_error = "no"

        filename = self.filename_entry.get()

        for letter in filename:
            if re.match(valid_char, letter):
                continue

            elif letter == " ":
                problem = " (no spaces allowed)"

            else:
                problem = ("(no {}'s allowed)".format(letter))
            has_error = "yes"
            break

        if filename == "":
            problem = "can't be blank"
            has_error = "yes"

        if has_error == "yes":
            self.save_error_label.config(text="Invalid filename - {}".format(problem))

            self.filename_entry.config(bg="#ffafaf")
            print()

        else:
            filename = filename + ".txt"

            f = open(filename, "w+")

            f.write("Game Statistics\n\n")


            f.write("Starting Balance ${}".format(game_stats[0]) + "\n"
                        "Ending Balance ${}".format(game_stats[1]) + "\n")

            #Heading for rounds
            f.write("\nRound Details - Most Recent at the bottom\n\n")

            for item in game_history:
                f.write(item + "\n")

            f.close()

            self.close_export(partner)
class Help:
    def __init__(self, partner):
        # disable help button
        partner.start_help_button.config(state=DISABLED)

        # Sets up child window (ie: help box)
        self.help_box = Toplevel()

        # If users press 'x' cross at the top, closes help and 'releases' help button.
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box)
        self.help_frame.grid()

        # Set up Help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help / Instructions",
                                 font="Arial 15 bold")
        self.how_heading.grid(row=0)

        # Help text (label, row 1)
        self.help_text = Label(self.help_frame, text="",
                               justify=LEFT, width=40, wrap=250)
        self.help_text.grid(row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss", width=10, bg="maroon", fg="white",
                                  font="arial" "10" "bold", command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # Put help button back to normal...
        partner.start_help_button.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box")
    something = Start(root)
    root.mainloop()