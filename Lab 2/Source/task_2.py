n = int(input("No. of contacts to be added to list: "))
contacts_list = []
contact_dictionary = {}
for i in range(n) :
    contact_dictionary["name"] = input("Enter name ")
    contact_dictionary["number"] = input("Enter number ")
    contact_dictionary["email"] = input("Enter email ")
    contacts_list.append(contact_dictionary.copy())
print(contacts_list)
def opt() :
    x = str(input("a)Display contact by name \nb)Display contact by number \nc)Edit contact by name \nd)Exit:"))
    return x

if opt()=='a':
    name = str(input("Enter the name: "))
    for a in contacts_list:
        if a['name'] == name:
            print(a)
if opt()=='b':
    num = str(input("Enter the number: "))
    for a in contacts_list:
        if a['number'] == num:
            print(a)
if opt()=='c':
    name = str(input("Enter the name: "))
    number = int(input("Enter the number: "))
    for index,a in enumerate(contacts_list):
        if a['name'] == name:
            contacts_list[index]['number']=number
    print(contacts_list)
if opt()=='d' :
    exit()