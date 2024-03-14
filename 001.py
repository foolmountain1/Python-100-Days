# 百钱百鸡
'''
for x in range(0, 21):
    for y in range(0, 34):
        z = 100- x- y
        if 5*x+3*y+z/3 == 100 :
            print(x,y,z)
'''
# 水仙花数（0-1000）
'''for i in range(100,1000):
    m = i % 100
    u = i //10 %10
    s = i //100
    num = (s**3 +u**3 +m**3)
    if i == num :
        print(f"{i} is Narcissistic number")'''
# 数字颠倒
'''num = int(input('please input some number:'))
num1 = 0
while num >0 :
    num1 = num1*10 + num%10
    num //= 10
print(num1)'''

# 双骰赌博游戏
'''
import random
money = int(input('please input your money'))
times = 0
bet = int(input('please input your bet'))
i = False
large_money = []
while money-bet >0:
    large_money.append(money)
    x = random.randint(1,6)
    y = random.randint(1,6)
    z = x+y
    times +=1
    print(z)
    if z == 7 or z == 14:
        money += bet
        print(f'你赢了 money = {money}')
    elif z == 2 or z == 3 or z == 12:
        money -= bet
        print(f'你输了money = {money}')
    else:
        i = True
        while i:
            i= False
            x1 = random.randint(1, 6)
            y1 = random.randint(1, 6)
            z1 = x1 + y1
            print(z1)
            if z1 == 7:
                money -=bet
                print(f'你输了money = {money}')

            elif z1 == z:
                money += bet
                print(f'你赢了money = {money}')

            else:
                i = True

print(f'times is {times}and large money is {max(large_money)}')
'''
# 斐波那契数列
'''a = 0
b = 1
for i in range(1,20):
    a,b = b,a+b
    print(a)
'''
# 完美数
import math
'''
num = 0
for i in range(1,10001):
    num = 0
    for j in range(1,i):
        if i % j == 0 :
            num += j
    if num == i:
        print(num)
'''
# 素数(100以内）
'''
import math
for i in range(2,101):
    is_prime = True
    for j in range(2, int(math.sqrt(i))+1):
        if i % j == 0 :
            is_prime =False
            break
        else:
            is_prime = True
    if is_prime:
        print(i)
'''










