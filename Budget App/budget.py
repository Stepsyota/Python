all_categories = []
all_expences = []
all_procents = []

def create_spend_chart(all_categories):
    all_categories = Category.all_categories
    
    #Creating a list of expenses and calculating their amount
    total_expences = 0 
    for category in all_categories:
        all_expences.append(category.expences)
        total_expences += category.expences
    
    #Creating a list of expenses as a percentage
    for expence in all_expences:
        all_procents.append(expence / total_expences * 100)
    
    print('Percentage spent by category')
    percents = list(range(100, -1, -10))
    for x in percents:
        #make indents
        for _ in range(len(str(100)) - len(str(x))): 
            print(' ', end = '')
            
        #printing the number of percentages  
        print(f'{x}|', end = '')
        
        #printing the number of percentages of a given category
        for one_category in all_categories:
            index = all_categories.index(one_category)
            print(' ', end = '')
            if all_procents[index] >= x:
                print('o', end = '')
            else:
                print(' ', end = '')
            print(' ', end = '')
        print('')
            
    #printing the line
    print(' ' * 4, end = '')
    for _ in range(len(all_categories)*3 + 1):
        print('-', end = '')
        
    print('')
        
    #printing names of category
    max_length_name = 0
    for one_category in all_categories:
        max_length_name = len(one_category.name_category) if max_length_name < len(one_category.name_category) else max_length_name
    counter = 0
    for y in range(max_length_name):
        print(' ' * 5, end = '')
        for one_category in all_categories:
            if counter < len(one_category.name_category):
                print(one_category.name_category[counter], end ='')
            else:
                print(' ', end = '')
            print('  ', end = '')
        counter += 1
        print('')
        
    print('')
        
def print_category(Category):
    
    #Calculating the number of characters *
    len_category = len(Category.name_category)
    str_characters ='*' * ((30-len_category) // 2)
    
    #Output of the category name
    print(f'{str_characters}{Category.name_category}', end = '')
    if len(str_characters) * 2 != 30 - len_category:
        print(f'{str_characters}*')
    else:
        print(f'{str_characters}')
            
    #Output of the description and amount
    total_sum = 0
    
    for x in range(len(Category.ledger)):
        description = Category.ledger[x]['description']
        amount = Category.ledger[x]['amount']
        total_sum += float(convert_numb_to_str(amount))
        #Output description
        for index in range(23):
            if index < len(description):
                print(description[index], end = '')
            else:
                print(' ', end = '')
            
        #Output amount     
        max_len = 7
        len_amount = len(convert_numb_to_str(amount))
        spaces = ' ' * (max_len - len_amount)
        if max_len >= len_amount:
            print(f'{spaces}{convert_numb_to_str(amount)}')
        else:
            print('Error')
            return
    print(f'Total: {convert_numb_to_str(total_sum)}', '\n')    
        
def convert_numb_to_str(numbers):
    str_numbers = str(numbers)
    index = str_numbers.index('.') if '.' in str_numbers else -1
    if index != -1:
        symbols_after = str_numbers[index + 1:]
        if len(symbols_after) > 2:
           str_numbers = str(round(numbers, 2))
        elif len(symbols_after) == 1:
            str_numbers += '0'
    else:
        symbols_after = '.00'
        str_numbers += symbols_after
    return str_numbers
            
class Category: 
    all_categories = []
    def __init__(self, name_category):
        self.name_category = name_category
        self.ledger = []
        self.expences = 0
        Category.all_categories.append(self)
    
    def deposit(self, amount, desciption = ''):
        record = {"amount": amount, "description": desciption}
        self.ledger.append(record)

    def withdraw(self, amount, desciption = ''):
        if self.check_funds(amount):
            record = {"amount": -amount, "description": desciption}
            self.ledger.append(record)
            self.expences += amount
            return True
        else:
            return False
        
    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)
   
    def transfer(self, amount, another_budget_category):
        if self.check_funds(amount):
            self.expences += amount
            self.ledger.append({'amount' : -amount, 'description' : f'Transfer to {another_budget_category.name_category}'})
            another_budget_category.ledger.append({'amount' : amount, 'description' : f'Transfer from {self.name_category}'})
            return True
        else:
            return False
        
    def check_funds(self, amount):
        return amount <= self.get_balance()