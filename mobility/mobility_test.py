from mobility import Mobility

def usage():
    print('''
        f -> Move bot forward
        b -> Move bot backward
        ''')

def run_command(bot, command, duration=None):
    if duration == None:
        duration = 2

    if command == 'f':
        bot.forward(duration)

    elif command == 'b':
        bot.backward(duration)

    else:
        print('Unrecognized command')
        usage()

    return


def main():
    left_forward = 3
    left_reverse = 5
    right_forward = 8
    right_reverse = 10

    mobile_bot = Mobility(left_forward, right_forward, left_reverse, right_reverse)

    usage()
    while True:

        command = input('Enter command: ')
        print(command)



    mobile_bot.clean_up()

if __name__ == '__main__':
    main()
