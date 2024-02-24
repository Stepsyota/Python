from budget import *

Food = Category('Food')
Food.deposit(1000, 'Different things')
Food.withdraw(800, 'Fruits')

Auto = Category('Auto')
Auto.deposit(800, 'Different things')
Auto.withdraw(500, 'Repair')
Food.transfer(200, Auto)

Clothes = Category('Clothes')
Clothes.deposit(300, 'Different things')
Clothes.withdraw(100, 'Shirts')

print_category(Food)
print_category(Auto)
print_category(Clothes)
create_spend_chart(all_categories)