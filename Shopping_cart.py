from IPython.display import clear_output
#create global list
cart = [ ]

#add items
def addItem(item):
    cart.append(item)
    print(f"{item} has been added.")

#remove items
def removeItem(item):
    try:
        cart.remove(item)
        print(f"Your {item} has beem removed.")
    except:
        print("Sorry we could not remove that item. This item is not available")

#show cart
def showCart():
    if cart:
        print("Here is Your cart:")
        for item in cart:
            print(f"- {item} ")
    else:
        print("Your cart is empty.")

#clearing cart
def clearCart():
    clear_output()
    cart.clear()
    print("Your cart is Empty")

#cretae a main loop
def main():
    done = False
    while not done:
        ans = input("quit/add/remove/show/clear: ").lower()
        if ans == "quit":
            print("Thanks for Using our Program")
            showCart()
            done = True
        
        elif ans == "add":
            item = input("What would you like to add? ").title()
            addItem(item)
        
        elif ans == "remove":
            showCart()
            item = input("What item would you like to remove? ").title()
            removeItem(item)

        elif ans == "show":
            showCart( )
        
        elif ans == "clear":
            clearCart()

        else:
            print("Sorry that was not an Option")
main()

        

