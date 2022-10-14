from curses.ascii import isupper


def deaf_grandma():

    goodbye_count = 0

    print('HEY KID!')

    while goodbye_count < 2:
        usr_input = input()

        if usr_input == '':
            print('WHAT?!')

        elif usr_input == 'GOODBYE!' and goodbye_count == 0:
            print('LEAVING SO SOON?')
            goodbye_count += 1

        elif usr_input == 'GOODBYE!' and goodbye_count == 1:
            print('LATER, SKATER!')
            break

        elif usr_input.isupper() and usr_input != 'GOODBYE!':
            print('NO, NOT SINCE 1946!')
        
        else:
            print('SPEAK UP, KID')


deaf_grandma()