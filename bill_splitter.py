
number_in_the_group = input("How many people are in the group? ")
names_of_the_group_members = input("Name of the member in the group separated with commas (Solomon, Njobvu) ").strip()
total_bill = input("Enter the total bill: ").strip()

def bill_spitter(number, names, total_bill):
    
    names = names.split(",")
    number = int(number)
    split = int(total_bill) / number
    
    if len(names) == number:
        print(f'\nTotal bill: {total_bill}\nPeople: {names_of_the_group_members}\n\nEach person owes: {split}\n')
        for name in names:
            print(f"{name.strip()} owes: {round(split, 2)}")
    else:
        print(f'Name provided doesn\'t with the number of people in the group!' )
    
border = "*-*" * 30
print(border)
bill_spitter(number_in_the_group, names_of_the_group_members, total_bill)
print(f"\n{border}")