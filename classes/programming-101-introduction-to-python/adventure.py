'''Adventure game by INSERTYOURNAMEHERE.

INSERTDESCRIPTIONHERE

ANDHERE TOO
'''

import sys


def adventure():
    '''Play the adventure, reading from standard input and writing to standard output.'''

    rooms = {'lab': 'A bright and messy labratory.',
             'toilet': 'A dark and clean toilet.'}
    room = 'lab'
    
    name = input('Welcome traveler!  What be yer name? ')
    print('That is a strange name, {}, but I like it.'.format(name))
    
    living = True
    winning = False
    while living and not winning:
        print('You are in the {}'.format(room))
        print(rooms[room])
        action = input('What will {} do?\n> '.format(name)).strip().lower()

        if 'die' == action:
            print('Suddenly, you do not feel so good.  Maybe you should lie down.')            
            living = False
        elif 'north' == action:
            if 'lab' == room:
                room = 'toilet'
        elif 'south' == action:
            if 'toilet' == room:
                room = 'lab'
        elif 'sleep' == action:
            print('You feel fine, no need to sleep.')
        else:
            print('Not sure what you meant by that, boss.')
            

    if living:
        print('You made it out alive, {}!'.format(name))
    else:
        print('Sorry, {}, but you are DEAD!'.format(name))

    if winning:
        print('I am not sure how, but you also managed to win!  Great job!')


def main(argv):
    '''Return exit code as integer, receives commandline arguments as list of strings, runs Adventure in between.'''
    adventure()
    return 0

if '__main__' == __name__:
    sys.exit(main(sys.argv))
