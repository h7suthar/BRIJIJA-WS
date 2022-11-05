print('\n')
print('######## Welcome to the WASHING-TIME Calculator ############')
print('\n')

def calculate_Bill(weight):
    if weight == 0:
        amount = '0 Minutes'
    elif weight > 0 and weight <= 2000:
        amount = '25 Minutes'
    elif weight > 2000 and weight <= 4000:
        amount = '35 Minutes'
    elif weight > 4000 and weight <= 7000:
        amount = '45 Minutes'
    elif weight > 7000:
        amount = 'OVERLOADED!'
    else:
        amount = "INVALID->'WEIGHT-LOAD-VALUE'!!!"
    return amount 

if __name__ == '__main__' :
    while (True):
        weight = input("Please enter approximate load weight in 'grams' for the current Load-Cycle: ")
        if not weight.isdigit():
            print('INVALID')
            print('\n')
            continue
        weight = int(weight)
        Time_amount = calculate_Bill(weight)
        print('Approximate time(minutes) to finish this load will be : ', Time_amount)
        print('\n')
        