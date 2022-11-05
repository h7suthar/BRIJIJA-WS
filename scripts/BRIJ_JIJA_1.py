print('\n')
print('######## Welcome to the ELECTRIC-BILL Calculator ############')
print('\n')


''''
def calculate_Bill(units):
    
    if units <= 100:
        amount = 0
    elif units > 100 and units <= 200:
        amount = (units - 100)*5
    elif units > 200:
        units_level2 = units - 200
        units_level1 = 100
        amount = (units_level2*10) + (units_level1*5)
    else:
        print("Please enter valid 'UNITS'!!!")
    return amount

if __name__ == '__main__' :
    customer = 1
    units = input('Please enter the number of Electricity Units for customer 1: ')
    while (True):
        units = int(units)
        total_amount = calculate_Bill(units)
        print('Total bill is customer no.' + str(customer) + ': Rs.', total_amount)
        customer += 1
        print('\n')
        units = input('Please enter the number of Electricity Units for next customer-' + str(customer) + ': ')
'''
unit = int(input())
if unit <= 100:
    amount = 0
    print("no change")
elif unit > 100 and unit <= 200:
    print(((unit-100)*5)," " + "Rs. 5 per unit")
else:
    print(((unit-200)*10 + (100*5)),""+ "Rs.10 per unit")