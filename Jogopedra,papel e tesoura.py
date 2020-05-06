import random

print("Hello, and welcome to this game")
answer_player = input ("Please choose one rock(r), paper(p) or scissors(s): ")

while answer_player != 's' and answer_player != 'p' and answer_player != 'r':
    print('you need to choose one of the options')
    answer_player = input('choose between rock(r), paper(p) or scissors(s): ')
    print(answer_player)


def gen_random():
    number = random.randint(1,3)
    if number == 1:
        return 's'
    elif number == 2:
        return 'r'
    elif number == 3:
        return 'p'

computer = gen_random()

print("your answer was : " + answer_player)
print('Computer randomly generated answer was :' + str(computer))

if answer_player == 'r' and computer == 's':
    print('player wins')
elif answer_player == 's' and computer == 'p':
    print('player wins')
elif answer_player == 'p' and computer == 'r':
    print('player wins')
elif answer_player == computer:
    print('Draw!')
else:
    print ('Computer wins')