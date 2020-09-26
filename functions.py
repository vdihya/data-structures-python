def fib(n):
    a,b = 0,1
    while a < n:
        print(a,end =' ')#appends with space instead of newline
        a,b = b,a+b

def area(b,h):
    a = b * h * 0.5
    return a
moves = 0
def hanoi(d,l,r,m):
        while d>1:
                hanoi(d-1,l,m,r)
                print("move disk from ",l," to ",r)
                hanoi(d-1,m,r,l)

                
def fact(n):
        if n==0 or n==1:
                return 1
        else:
                return n*fact(n-1)

def var(*x):
        print(x)


var("1",123,2.11,True)
print("3! =",fact(3))
#hanoi(3,"left","right","middle")
fib(3)
print("area =",area(2,3))
print("area =",area(b=2,h=3))
print("area =",area(h=3,b=2))# any order