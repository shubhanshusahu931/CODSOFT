def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def rem(a,b):
    return a%b

def calculator():
    try:
        a = float(input("enter any number :"))
        b = float(input("enter any number :"))
    except ValueError:
        print("enter a valid number!")
        return
    print("select among ")
    print("1 for addition")
    print("2 for substraction")
    print("3 for multiplication")
    print("4 for division")
    print("5 for reminder")

    choice = int(input("enter choice from above list : "))
    if(choice == 1):
        print(f"Result is :{add(a,b)}")
    elif(choice == 2):
        print(f"Result is :{sub(a,b)}")
    elif(choice == 3):
        print(f"Result is :{mul(a,b)}")
    elif(choice == 4):
        print(f"Result is :{div(a,b)}")
    elif(choice == 5):
        print(f"Result is :{rem(a,b)}")
    else:
        print("Plz enter a valid input !")


calculator()