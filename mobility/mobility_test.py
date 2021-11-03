from mobility import Mobility

def main():
    left_forward = 3
    left_reverse = 5
    right_forward = 8
    right_reverse = 10

    mobile_bot = Mobility(left_forward, right_forward, left_reverse, right_reverse)

    mobile_bot.forward(2)
    mobile_bot.backward(2)

    mobile_bot.clean_up()

if __name__ == '__main__':
    main()
