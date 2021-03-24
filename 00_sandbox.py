# Help text row 1
self.game_help = Label(self.game_frame, text="Press 'enter' or 'open boxes to play!",
                       font="Arial 10 italic", fg="red")
self.game_help.grid(row=1, pady=10)

# Quit button
self.quit_button = Button(self.game_frame, text="Quit", fg="white",
                          bg="#660000", font="Arial 15 bold", width=20,
                          command=self.to_quit, padx=10, pady=10)
self.quit_button.grid(row=6, pady=10)

# Display prizes...
box_width = 5
self.box_frame = Frame(self.game_frame)
self.box_frame.grid(row=2, pady=10)

self.prize1_label = Label(self.box_frame, text="?\n", font=box_text,
                          bg=box_back, width=box_width, padx=10, pady=10)
self.prize1_label.grid(row=0, column=0)

# Add round results to stats list
round_summary = "{} | {} \ {} - Cost: ${} | " \
                "Payback: ${} | Current Balance: " \
                "${}".format(stats_prizes[0], stats_prizes[1],
                             stats_prizes[2],
                             5 * stakes_multiplier, round_winnings, current_balance)
self.round_stats_list.append(round_summary)
print(self.round_stats_list)

if current_balance < 5 * stakes_multiplier:
    self.game_play.config(state=DISABLED)
    self.game_box.focus()
    self.game_play.config(text="Game Over")

    balance_statement = "Current Balance ${}\n" \
                        "Your balance is too low. You can only quit " \
                        "or view your states.".format(current_balance)
    self.game_balance.config(fg="#660000", font="Arial 10 bold",
                             text=balance_statement)


def to_quit(self):
    root.destroy()
