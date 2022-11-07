from excelpy import database
import excelpy

#lamdas...
lambda_multiply = lambda input1, input2 : input1 * input2
lambda_add = lambda input1, input2 : input1 + input2
lambda_sub = lambda input1, input2 : input1 - input2

# Update function...
def update_Quantity(arg,cmd):
    for cell in database[excelpy.getHeader_Index(database,'Item')]:
        if cell.value == arg:
            itemRow = cell.row
            currentQauntity = database[excelpy.getHeader_Index(database,'Quantity') + str(itemRow)].value
            if currentQauntity == 0:
                excelpy.dataBook.save('NewInventry.xlsx')
                return False
            elif 'add' == cmd:
                updatedQauntity = lambda_sub(currentQauntity,1)
                database[excelpy.getHeader_Index(database,'Quantity') + str(itemRow)] = updatedQauntity
                excelpy.dataBook.save('NewInventry.xlsx')
                return True
            elif 'sub' == cmd:
                updatedQauntity = lambda_add(currentQauntity,1)
                database[excelpy.getHeader_Index(database,'Quantity') + str(itemRow)] = updatedQauntity
                excelpy.dataBook.save('NewInventry.xlsx')
                return True

# Read function...
def calculate_cost(argItem,argQuantity):
    for cell in database[excelpy.getHeader_Index(database,'Item')]:
        if cell.value == argItem:
            itemRow = cell.row
            final_Price = database[excelpy.getHeader_Index(database,'Final Price') + str(itemRow)].value
            return lambda_multiply(final_Price,argQuantity)
            

# delete function -> for application admin only not for client...
def delete_database(arg):
    for cell in database[excelpy.getHeader_Index(database,'Item')]:
        if cell.value == arg:
            itemRow = cell.row
            database.delete_row(itemRow)
            database.insert_row(itemRow)  # Inserting blank row
            excelpy.dataBook.save('NewInventry.xlsx')

# Get item info...
def item_Info(arg):
    details = []
    for cell in database[excelpy.getHeader_Index(database,'Item')]:
        if cell.value == arg:
            itemRow = cell.row
            for column in database[str(itemRow)]:
                detail_feild = column.value
                details.append(detail_feild)
    feilds = ['Item','Categaory','Seller','Remaining Quantity','MSRP','Warranty Period','Discount Offer','Final Price']
    item_Details = dict(zip(feilds, details))
    return item_Details

# Filter the categories...
def category_items(arg):
    itemsList = []
    for i in range (2,database.max_row + 1):
        if database[excelpy.getHeader_Index(database,'Categaory') + str(i)].value == arg:
            itemsList.append(database[excelpy.getHeader_Index(database,'Item') + str(i)].value)
    return itemsList

def display_Category():
    categories = set()
    for cell in database[excelpy.getHeader_Index(database,'Categaory')]:
        types = cell.value
        if not types == 'Category':
            categories.add(types)
    return categories


