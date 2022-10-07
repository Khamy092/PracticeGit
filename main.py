# AppName:        PassGen
# Created by:     Taqi Khaliqdad
# Date created:   3 October 2022
# Purpose 0:      To enhance the security of my online accounts.
# Purpose 1:      To have in my portfolio


import random
import string

randomNum = [1, 4, 6, 3, 33, 65, 75, 46, 232, 66, 32, 46, 0, 19, 99, 271, 295, 29, 211, 765, 1213, 553, 7, 91, 927]
randomWord = ['hE11UOWA', 'oDewnaBakhtai', 'ShaReBakul0', 'sAyedBashii@zJAGHORI', 'geniPaP', 'AteNasserAghill', 'ajjabKHAR@sti2', 'goSSypol', 'MawliChaGHAI', 'bruMMagem', 'myGoschh', 'OhDeArguT', '4fu*ckcake!']
randomChar = ['!', '@&', '%', '$', '<#', '&', '*/', '!(', ')!', '<!', '>>', '!&?', '+=', '/', '<!>', '!?', '<!><$>']

def welcomeUser():
    
    print()
    userName = input('What is your name? ')
    print()
    print('Welcome to PassGen, ', userName)
    print()

def genPass():

    index0 = random.randint(0, 25) # to choose a random number from the num list.
    index1 = random.randint(0, 13) # for word
    index2 = random.randint(0, 17) # for character
    index3 = random.randint(0, 17) # for the second character

    genPassword = ''


    genPassword += (randomChar[index3])
    genPassword += (str(randomNum[index0]))
    genPassword += (randomWord[index1])
    genPassword += (randomChar[index2])

    # for item in genPassword:
    #     print(item, end='')
    # print()

    print('-----> ', genPassword)


welcomeUser()

print()
print('Your new password is:')
genPass()

print()

userInput = input('Would you like to generate a new one? [Y/N] ')

while userInput == 'Y' or userInput == 'y':
    print()
    print('Your new password is:')
    genPass()
    print()
    userInput = input('Would you like to generate a new one? [Y/N] ')

print()
input('Press enter to exit. ')
