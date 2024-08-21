print('Welcome to the tip calculator!')
bill = float(input('What was the bill total? $'))
tip = float(input('How much would you like to give? 10%, 12%, or 15%? ' ))
split = int(input('How many people to split the bill? '))

total = tip / 100 * bill + bill / split

final_total = round(total,2)
print('Each person should pay: $' + str(final_total))