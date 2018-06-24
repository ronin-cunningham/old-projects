


def reverseinputs(x):

        string = []
        result = x.split(' ')
        string += reversed(result)
        print (' '.join(string))
        

while True:
        userinput = str(input("enter a sentence: \n"))
        reverseinputs(userinput)
