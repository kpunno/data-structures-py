control = 0
while 'no' != control:
    print('- - - - - - - - - - - - - - -')
    print('enter a value to see if it\'s in the list')
    def check_num():
        my_num = int(input())
        nums = [10, 4, 5, 9, 21, 94]
        for key in nums:
            if my_num == key:
                return True
        return False

    x = check_num()
    if x:
        print('it is in the list!')
    else: print('not in the list :(')
    print('- - - - - - - - - - - - - - -')
    print('would you like to continue?')
    control = input()