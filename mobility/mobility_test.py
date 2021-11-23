from mobility import Mobility
import sys

def usage():
    print('''
        \' COMMAND DURATION=optional \'

        test -> Test each motor
        x -> exit
        f -> Move bot forward
        b -> Move bot backward
        l -> Spin left
        r -> Spin right
        test -> Run test motor commmand

        ''')

def run_command(bot, command, duration=None):
    if duration == None:
        duration = 2

    if command == 'test':
        bot.motor_test(duration)

    elif command == 'x':
        print('Exiting...')
        sys.exit(0)


    elif command == 'f':
        bot.forward(duration)

    elif command == 'b':
        bot.backward(duration)

    elif command == 'l':
        bot.turn_left(duration)

    elif command == 'r':
        bot.turn_right(duration)
        
    else:
        print('Unrecognized command')
        usage()

    return


def main():
    left_forward = 20
    left_reverse = 21
    left_velocity = 16
    right_forward = 19
    right_reverse = 26
    right_velocity = 13

    mobile_bot = Mobility(left_forward, right_forward, left_reverse, right_reverse, left_velocity, right_velocity)

    usage()
    while True:

        command = list(input('Enter command: '))

        if len(command) == 1:
            run_command(mobile_bot, command[0])

        elif len(command) == 2:
            run_command(mobile_bot, command[0], command[1])



    mobile_bot.clean_up()

if __name__ == '__main__':
    main()
