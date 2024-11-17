import sys, time

def issempty(lst):
    if lst==[]:
        return True
    else:
        return False

def push(lst,ele):
    global top
    lst.append(ele)
    top = len(lst)-1
    print("Pushed element to stack. ")
    time.sleep(2)
def Pop(lst):
    global top
    if issempty(lst):
        print("Underflow")
        time.sleep(2)
    else:
        popped=lst.pop()
        print("Popped the element: ",popped)
        time.sleep(2)
        if len(lst)==0:
            top=None
        else:
            top=len(lst)-1
def display(lst):
    top=len(lst)-1
    if issempty(lst):
        print("The stack is empty.")
        time.sleep(2)
    else:
        print("Top of the stack.\n")
        for i in range(top,-1,-1):
            print(lst[i])

top = None
lst=[]
while True:
    ele={}
    choice = int(input("Weclome to the stack menu.\n\n1. Push to stacks.\n2. Pop from stack.\n3. Display the elements.\n4. Exit\n\nChoose a option to continue..."))
    if choice==1:
        print("Enter the customer number: ")
        num = input()
        print("Enter the customer name: ")
        name = input()
        print("Enter the balance amount: ")
        balance= input()
        if balance>2500:
            final_amt = balance
            ele.update({"Customer Number":num})
            ele.update({"Customer Name":name})
            ele.update({"Balance":final_amt})
            push(lst,ele)
        else:
            print("Cannot push cuz of balance limit.")
        
    elif choice==2:
        Pop(lst)
    elif choice==3:
        display(lst)
    elif choice==4:
        sys.exit()  
    else:
        print("Choose a valid option...")
