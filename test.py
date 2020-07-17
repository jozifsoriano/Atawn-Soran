import random

input1 = '1d20'
input = '3d15'
input1 = '1x1'
input1 = '444'
x = int(input[0])
y = int(input[2:])
if(input[1] != 'd'):
    print("ERROR")
else:
    for i in range (x):
        print(f'**Dice {x} Max {y}:** || **{random.randint(1,y)}**')