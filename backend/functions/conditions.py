def check_if_even(number):
    if number % 2 == 0:
        print(f"{number} is even")
def check_odd_even(number):
    if number % 2 ==0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

def check_divisibility(n):
    for x in range(1,n+1):
        if x %2 ==0:
            print(f"{x} divisible by 2")
        elif x % 3==0:
            print(f"{x} divisible by 3")
        elif x % 5 ==0:
            print(f"{x} divisible by 5")
        else:
            print(f"{x} not divisible by 2,3, or 5")

def countdown(start):
    while start>=0:
        print(start)
        start-=1

def countdown_with_break(start,stop):
    while start>0:
        print(start)
        
        if start==stop:
            break
        start-=1
def countdown_with_odd_numbers(start):
    while start>=0:
        if start%2==0:
            start-=1
            continue
        print(start)    
        start-=1

        
