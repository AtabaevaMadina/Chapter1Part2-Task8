start_a = int(input('Input a first integer A '))
stop_b = int(input('Input a second integer B '))

if start_a > stop_b:
    print('input second integer B more then A')
else:
    print(list(range(start_a, stop_b + 1)))