def add(a, b):
    return a + b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b
def sub(a, b):
    return a - b
print("avalible operations are :")
print("1.addition")
print("2.substraction")
print("3.multiplication")
print("4.division")
while True:
    choice=input("enter your choice('1','2','3','4'): ")
    if choice in ('1','2','3','4'):
        try:
            n1=int(input("enter first value: "))
            n2=int(input("enter second value: "))
        except :
            print("invalid value")
            continue
        if choice=='1':
            print(n1,"+",n2,"=", add(n1, n2))
        elif choice=='2':
            print(n1,"-",n2,"=", sub(n1, n2))
        elif choice=='3':
            print(n1,"*",n2,"=", mul(n1, n2))
        elif choice=='4':
            print(n1,"/",n2,"=", div(n1, n2))
        next_operation=input("do next operation(yes/no):")
        if next_operation=='no':
            break
    else:
        print("invalid choice")