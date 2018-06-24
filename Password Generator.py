import random

strength = ['Weak', 'Medium', 'Strong']
charbank = ('1234567890qwertyuiopASDFGHJKLZXCVBNM')
chosenchars = ('')
choice = ('')

def inputfunction(choice):
    while True:
        userchoice = input("Would you like your password to be: \n Weak \n Medium? \n Strong?\n")
        if userchoice in strength:
            choice = ''.join(userchoice)
            break
        else:
            print ('oops, that\'s not one of the options. Enter again...')
    return choice

def strengththing(x):
    if choice == 'Weak':
        return RandomPass(5)
    if choice == 'Medium':
        return RandomPass(10)
    if choice == 'Strong':
        return RandomPass(15)

def RandomPass(passlen):
    x = ''.join(random.sample(charbank, passlen))
    return x

choice = inputfunction(choice)
chosenchars = strengththing(chosenchars)

print ('this is your password: %s' %chosenchars)
