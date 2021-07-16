import random

#Guessing Game
while True:
    user = int(input('Guess a number  that range in (1 to 20): '))
    user1 = random.randint(1,20)
    if user == user1:
        print(f'User Guess: {user}\nRight Number: {user1}\n\nYou lose!')
    else:
       print(f'User Guess: {user}\nRight Number: {user1}\n\n You lose!')
#Again
    again = str(input('\nGuess again, yes/ no? '))
    if again == 'yes':
        continue
    else:
        break
