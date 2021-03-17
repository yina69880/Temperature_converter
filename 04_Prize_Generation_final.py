import random

NUM_TRIALS = 100
winnings = 0

cost = NUM_TRIALS * 5

for item in range(0, NUM_TRIALS):
    prize=""
    round_winnings=0

    for thing in range(0,3):

        # radint finds numbers between endpoints , including both end points
        prize_num = random.randint(1,100)
        prize += " "
        if 0 < prize_num <= 5:
            prize += "Gold"
            round_winnings += 5
        elif 5 <prize_num <= 25:
            #get silver if number is between 1 and 3
            prize += "Silver"
            round_winnings += 2
        elif 25 < prize_num <= 65:
            prize += "Copper"
            round_winnings += 1
        else:
            prize += "Lead"

    print("You won {} which is worth {}".format(prize,round_winnings))
    winnings += round_winnings

print("Paid in: {}".format(cost))
print("Paid out: {}".format(winnings))

if winnings > cost:
    print("You came out ${} ahead!".format(winnings - cost))
elif winnings == cost:
    print("You broke even today")
else:
    print("Sorry, you lost ${}".format(cost - winnings))
