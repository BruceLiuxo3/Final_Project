import random

print('This program generates a random number from 1 to X (you can choose the upper bound). After that, you have to try your best to guess the correct answer. Good Luck!')
while True:
    inputs = input('Please enter a random number bigger than 0:')
    try:
        if type(int(inputs)) == type(6):
            if int(inputs) >= 1:
                print(
                    "Nice Choice! Now we already chose a random integer between 1 and {}. Guess It!".format(inputs))
                break
            elif int(inputs) <= 0:
                print("The number have to be bigger than 0.")
    except:
        try:
            if type(float(inputs)) == type(3.3):
                print("Not Cool (●__●), it's a float. Plz enter an integer.")
        except:
            print("Wrong (●__●), it's a string or nothing. Plz enter an integer.")

result = random.randint(1, int(inputs))
# print('the result is '+str(result))   # Hint the correct result
time = 0

while True:
    answer0 = input(
        "Now, please guess the random number [NOTE: If you want to stop the program just enter 'stop']:")
    domain = int(inputs)
    try:
        if type(int(answer0)) == type(6):
            answer = int(answer0)
            if answer < result and answer <= domain and answer >= 1:
                print('The correct answer is bigger,guess again')
                time += 1
                print("you have guessed {} times.".format(time))
            elif answer > result and answer <= domain and answer >= 1:
                print('The correct answer is smaller,guess again')
                time += 1
                print("you have guessed {} times.".format(time))
            elif answer > domain:
                print('Input OUT of RANGE, too big ಠ▃ಠ the range is 1 to {}.'.format(inputs))
                time += 1
                print("you have guessed {} times.".format(time))
            elif answer <= 0:
                print('Input has to be positive (☉_☉), the range is 1 to {}.'.format(inputs))
                time += 1
                print("you have guessed {} times.".format(time))
            elif answer == result:
                time += 1
                print("TADA! It's correct!  ʕ◉ᴥ◉ʔ ")
                print('Totally, you have guessed {} times'.format(time))
                break
            else:
                continue
    except:
        try:
            if type(float(answer0)) == type(3.3):
                print("Not Cool (●__●) , it's a float. Plz enter an integer.")
                time += 1
                print("you have guessed {} times.".format(time))
        except:
            if answer0 == 'stop':
                print("BYE")
                break
            elif type(answer0) == type('str'):
                print("Wrong (●__●), it's a string or nothing. Plz enter an integer.")
                time += 1
                print("you have guessed {} times.".format(time))
