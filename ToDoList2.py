#1/12
#ToDo List

GroceryList = ["Apples", "Milk", "Bread", "Eggs", "Yougurt", "Cereal"]

#Functions

def start():
    while True:
        print("Please chose an option to alter your list")
        print(" 1.) Add an item to the list \n 2.) View the current list \n 3.) Mark an item as completed \n 4.) Remove an item from the list \n 5.) Exit the program \n 6.) Remove all items from list \n 7.) Count number of items on list \n 8.) Sort list alphabetically")
        option = int(input("option: "))
        if option == 1:
            add()
        if option == 2:
            view()
        if option == 3:
            completed()
        if option == 4:
            remove()
        if option == 5:
            exit()
            break
        if option == 6:
            delete()
        if option == 7:
            count()
        if option == 8:
            organize()
       


def add():
    x = input("What would you like to add to the list?")
    GroceryList.append(x)
    print(GroceryList)

def view():
    print(GroceryList)

def completed():
    ans = input("Select an item from the list to mark as completed: ")
    print(ans)
    i = GroceryList.index(ans)
    print(i)
    GroceryList[i] = ans +  " x"
    print(GroceryList)

def remove():
    ans = input("Which item would you like to remove?")
    print(ans)
    i = GroceryList.index(ans)
    GroceryList.pop(i)
    print(GroceryList)

def exit():
    print("You have exited the program")

def delete():
    GroceryList.clear()
    print(GroceryList)

def count():
    x = len(GroceryList)
    print(x)

def organize():
    x = sorted(GroceryList)
    print(x)


#Main

start()



