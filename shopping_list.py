#create a list to hold our items
shopping_list = []

#Instructions for using the app
print("what should we pick up at the store?")
print("enter 'DONE' to stop adding items")

#ask for new items
while True : 
    newItem = input('> ')

    #be able to quit the app
    if newItem == 'DONE':
        break
    #add new items to our list
    shopping_list.append(newItem)

#print list items
print("Here's your list: ")
for item in shopping_list:
    print(item)