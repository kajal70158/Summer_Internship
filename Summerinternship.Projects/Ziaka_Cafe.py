print("Welcome in Zaika Cafe")
menu = {
    "pasta" :   60,
    "burger"    :  50,
    "rajma-rice"    :  50,
    "juice" :   40,
    "chowmin"   : 70,
    "cold-drink"    :  50,
    "biryani"   : 70,
    "cold-coffee"   : 60,
    "sandwich"  :    20
}
print("Our Menu:")
print("---------------------")
total_order = 0
for item, price in menu.items():
    print(f"{item} :    Rs.{price}")
next_order = True
while next_order:
    order = input("Enter the name of item you want to add in your order: ").lower()
    if order in menu:
        total_order += menu[order]
        print(f"{order} added in your order")
    else:
        print(f"{order} is not available")
        another_order = input("Do you want to place another order: yes/no").lower()
        if another_order == 'yes':
            next_order = True
        else:
            next_order = False

print(f"Your total bill is : Rs. {total_order}")
