stack = []


def view():
  print(stack)

def push():
  item = input("Enter a number to add to stack: ")
  stack.append(item)

def pop():
  item = stack.pop(len(stack)-1)
  print("You just popped out: ", item)
    
while True:
    menu_choice = int(input("Please enter menu choice: "))
    if menu_choice == 1:
        view()
    elif menu_choice == 2:
        push()
    elif menu_choice == 3:
        pop()
    else:
        menu_choice = int(input("Please enter menu choice: "))

