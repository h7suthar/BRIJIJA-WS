import back

print('\n')
print('##################################################################')
print('############# Welcome to the Online Shopping Mart ################')
print('##################################################################')
print('\n')

checkoutAmount_List = []

def display_list(arg):
    for x, element in enumerate(arg):
        print(x+1,element)
    print('\n')

def display_Dic(arg):
    for keys,values in arg.items():
        print(keys," : ",values)
    print('\n')

def check_Out(argList):
    total = 0
    print(argList)
    for i in range(len(argList)):
        total += argList[i]
    return total

def payment(total):
    userId = input('Please enter the username or email address: ')
    paswd = input('Please enter the password: ')
    type = input('Please enter payment type: ')
    address = input('Please enter your address: ')
    print('\n')
    print('Order Details: ')
    print('-Customer ID: ',userId)
    print('-Payment Method: ',type)
    print('-Total: ', total)
    print('-Address: ', address)
    
def customer_prompts(argList):
    print('\n')
    print("Shop by Categories, below are the list listed categories: ")
    categories = back.display_Category()
    display_list(categories)
    Cat_input = input('Please type in from the above catagories any name to look at the items list of corresponding categories: ')
    items = back.category_items(Cat_input)
    display_list(items)
    item_Input = input('Please type in from the above list of items to display its details: ')
    details = back.item_Info(item_Input)
    display_Dic(details)
    print('\n')
    #print('**********************************')
    print("\n  => To buy this item type 'Buy'. \n  => To quit shopping type 'Quit'. \n  => To go to home page again type 'Home'.\n  => To checkout  type 'Checkout'.")
    #print('**********************************')
    print('\n')
    option = input('Type from above given options: ')
    if option == 'Buy':
        print('\n')
        quantity = input('Please enter the quatity of item to buy: ')
        add_Cart(item_Input,int(quantity),argList)
        print('\n')
        #print('**********************************')
        print("\n  => To buy shop more type 'shope'. \n  => To checkout  type 'Checkout'.")
        #print('***********************************')
        print('\n')
        choice = input('Type from above given options: ')
        if choice == 'Checkout':
            due = check_Out(argList)
            payment(due)
        else:
            customer_prompts(argList)
    elif option == 'Quit':
        pass
    elif option == 'Home':
        customer_prompts(argList)
    elif option == 'Checkout':
        due = check_Out(argList)
        payment(due)
    else:
        pass

def add_Cart(argItem,argQuantity,argList):
    for i in range(argQuantity):
        Valid = back.update_Quantity(argItem,'add')
    if Valid: 
        cost = back.calculate_cost(argItem,argQuantity)
        argList.append(cost)
    elif not Valid:
        print('Item is out of stock, for order of given Quantity!!!')
        customer_prompts(argList)


if __name__ == '__main__':
    customer_Number = 1
    while(1):
        cart_List = []
        print('\n')
        print("****************************************************************")
        print("Welcome Customer No: ", customer_Number, " Enjoy your shopping! ")
        print("****************************************************************")
        customer_prompts(cart_List)
        customer_Number += 1
        
    