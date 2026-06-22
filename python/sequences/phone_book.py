phone_book = {}
 
def add_contact(name, number):
    phone_book[name] = number
    print(f"Added {name}: {number}")
 
def search_contact(name):
    if name in phone_book:
        print(f"{name}'s number is {phone_book[name]}")
    else:
        print(f"{name} not found in phone book")
 
def delete_contact(name):
    if name in phone_book:
        del phone_book[name]
        print(f"Deleted {name} from phone book")
    else:
        print(f"{name} not found")
 
# Using the functions
add_contact("Riya", "9876543210")
add_contact("Aman", "9123456789")
search_contact("Riya")
delete_contact("Aman")
search_contact("Aman")
 
print("Final phone book:", phone_book)
 
