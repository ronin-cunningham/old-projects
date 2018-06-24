import random


while True:
    inp = int(input("type in a number (between 0 and 100) \n> "))
    if inp > 0 and inp < 101:
        break
    else:
        print ('sorry try again')

def guessmachine(x, guess, guesstries=1, mn=0, mx=100):
    print("my guess was %s" %guess)
    print('{',mn,mx,'}')
    if guess != x:
        while True:
            response = input('was my guess too high or too low? Tell the truth \n>')
            if response in ['too high','too low']:
                guesstries += 1
                if response == 'too high':
                    if guess<mx:
                        mx=guess-1
                elif response == 'too low':
                    if guess>mn:
                        mn=guess+1
                guess = random.randint(mn, mx)
                guessmachine(x, guess, guesstries, mn ,mx)
                break
            else:
                print ('sorry didnt get that')
    else:
        print ("Found it! Your number was %s and it took me %s tries" %(guess, guesstries))

guessmachine(inp, random.randint(0, 100))
