#create a list to hold our items
shopping_list = []

#Instructions for using the app
def show_help():
    #Instructions for using the app
    print("what should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items
Enter 'HELP' for this help
Enter 'SHOW' to see your current list
""")

def show_list():
    #print list items
    print("Here's your list: ")

    for item in shopping_list:
         print(item)

def add_newItem(newItem):
    #add new items to our list
    shopping_list.append(newItem)
    print("Added {}. Shopping list now has {} items".format(newItem, len(shopping_list)))

show_help()

#ask for new items
while True : 
    newItem = input('> ')

    #be able to quit the app
    if newItem == 'DONE':
        break
    elif newItem == 'HELP':
        show_help()
        continue
    elif newItem == 'SHOW':
        show_list()
        continue
    add_newItem(newItem)
    

show_list()