point = int(input("Enter the Score Point:"))
count1 = int(0)
count2 = int(0)
n = 0
while (n<point):
    usr1 = input("Player 1:")
    usr2 = input("Player 2:")
    if usr1 == 'rock' and usr2 == 'rock':
        print('Same input - No points')
        continue
    elif usr1 == 'paper' and usr2 == 'paper':
        print('Same input - No points')
        continue
    elif usr1 == 'scissor' and usr2 == 'scissor':
        print('Same input - No points')
        continue
    elif usr1 == 'stone' and usr2 == 'paper':
        print('Point to Player 2')
        count2 = count2+1
    elif usr1 == 'stone' and usr2 == 'scissor':
        print('Point to Player 1')
        count1 = count1+1
    elif usr1 =='paper' and usr2 == 'stone':
        print('Point to Player 1')
        count1 = count1+1
    elif usr1 =='paper' and usr2 == 'scissor':
        print('Point to Player 2')
        count2 = count2+1
    elif usr1 =='scissor' and usr2 == 'stone':
        print('Point to Player 2')
        count2 = count2+1
    elif usr1 =='scissor' and usr2 == 'paper':
        print('Point to Player 1')
        count1 = count1+1
    n = n+1
    print('count1:',count1)
    print('count2:\n',count2)
if count1>= count2:
    print(3*' Player 1 Wins |')
else:
    print(3*' Player 2 Wins |')