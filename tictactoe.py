# я писала инструкцию на английском, так как мне так проще (не нужно постоянно переключаться)
# к сожалению, я не смогла придумать функцию, выявляющую победителя,
# хотя потратила на это несколько часов и перепробовала несколько вариантов
# (склонялась к методу подсчета определенного символа в списке - l.count(a))

# вам, при вводе данных, ошибаться нельзя (ничего кроме 00/01/02 и т.д. приниматься не будет);
# этот момент можно было бы исправить, но сил моих нет, я хочу спать

start = input("If you want to read the instructions, type 'y', "
              "if you want to skip the instructions, type 'n': ")
if start == "y":
    print('''There are two players: x-player and o-player. To be able to play, you need to input coordinates, 
    for example, "00" means that you've chosen the very 1st square. Like this:
    x - -
    - - -
    - - -
    
    Here is the structure of the grid:
      |0 |1 |2 |
    0  -  -  -
    1  -  -  -
    2  -  -  -
   
    So, if you input "02", you'll get this:
     - - x 
     - - -
     - - -
   
    NB x-player starts.''')
else:
    print("OK, let's begin.")

tictactoe = [
       ['-', '-', '-'],
       ['-', '-', '-'],
       ['-', '-', '-']
   ]

def answer_adder(coo_1, coo_2, x_or_o):
    if x_or_o % 2 == 0:
        tictactoe[coo_1][coo_2] = 'o'
    else:
        tictactoe[coo_1][coo_2] = 'x'
    for look_OK in tictactoe:
        print(*look_OK)

x_or_o = 1

while x_or_o < 10:
    if x_or_o % 2 == 0:
        answers = input("That's your turn, o-player: ")
        coo_1 = int(answers[-2])
        coo_2 = int(answers[-1])
        answer_adder(coo_1, coo_2, x_or_o)
        x_or_o += 1
    else:
        answers = input("That's your turn, x-player: ")
        coo_1 = int(answers[-2])
        coo_2 = int(answers[-1])
        answer_adder(coo_1, coo_2, x_or_o)
        x_or_o += 1
