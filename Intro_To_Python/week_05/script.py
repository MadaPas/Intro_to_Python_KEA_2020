
import sys
def msg():

    
    #print('Hello from function')
    if sys.argv[1] == 'MadaPas':
        print(sys.argv[1], 'You are in!')
    elif sys.argv[1] == 'Anna':
        print(sys.argv[1], 'you are not in')
    else:
        print('nope nope nope')
        #function_that_does_not_exists()


msg()