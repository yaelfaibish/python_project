with open('game.txt', 'w') as file:
    for i in range(1, 10):
        w = (f'{i} ' * 20 + '\n')
        u= w.replace(' ', '')
        file.writelines(u)
    file.writelines('TRESURE')

with open('game.txt', 'a') as file:
    for i in range(9, 0, -1):
        n = (f'{i} ' * 20 +'\n')
        s=n.replace(' ', '')
        file.writelines(s)

with open('game.txt','r+') as file:
    content = file.read()
    found_treasure = False
    position = 0
    moves = 0
    last_index = len(content) - 1

    while position <= last_index:
        move = int(input('Where do you want to move? [1 - forward, 2 - backwards]: '))
        steps = int(input('How many characters?  '))

        if move == 1:
            position += steps
        elif move == 2:
            position -= steps

        file.seek(position)
        current_char = file.read(1)

        if current_char in 'TRESURE':
            print("You hit the treasure!")
            print("It took you", moves, "moves.")
            break
        else:
            print("You hit", current_char)
            moves += 1



    print("Final position:", position)