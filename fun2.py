def getsalary():
    val=int(input('enter amt: '))
    fine=0.9
    sal=val*fine
    return sal
print(getsalary())
ans=getsalary()
print('salary', ans)

def amount():
    p=int(input('enter amt :'))
    r=float(input('rate :'))
    t=int(input('time :'))
    si=p*r*t /100
    amt=si+p
    return amt,si
amt,si = amount()
print(f'the amount will be{ans}')