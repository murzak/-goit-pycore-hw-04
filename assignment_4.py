import re

def parse_input(user_input):
    """Parse user input into command and params"""
    args = user_input.strip().split()
    if not args:
        return '', []
    func = args[0].lower()
    args = args[1:]
    return func, args


def is_valid_phone(phone):
    """
    Check if a phone number has the right format. Whether it starts from 380, 
    followed by 3 digit carier code and 7 digit phone number of a user.
    As example, 380997654321 
    """
    pattern = r"^380\d{9}$"
    return bool(re.match(pattern, phone))


def add_contact(args, contacts):
    """Add new contact into contacts dictionary"""
    if len(args) != 2:
        return 'Invalid input. Follow the example: add [name] [phone]'
    name, phone = args
    if name in contacts.keys():
        return 'This contact does already exist. Please enter a different user or type change [name] [phone] to alter this entry'
    elif (not contacts or name not in contacts.keys()) and is_valid_phone(phone):
        contacts[name] = phone
        return "Contact's been added"
    return "Please provide the right phone format in the following pattern like 380997654321"


def change_contact(args, contacts):
    """Changes contact information of a user which exists in contacts dict. 
    In case, user isn't there, return a message to provide info of an existant user in contacts dict"""
    if len(args) != 2:
        return 'Invalid input. Follow the example: add [name] [new_phone]'
    name, new_phone = args
    if name not in contacts.keys():
        return 'You cannot change unexistant contact'
    elif name in contacts.keys() and is_valid_phone(new_phone):
        contacts[name] = new_phone
        return "Contact has been updated"
    return "Please provide the right phone format in the following pattern like 380997654321"


def show_phone(args, contacts):
    """Returns a phone number of a given user if present in contacts dictionary"""
    if len(args) != 1:
        return 'Invalid input. Follow example: phone [name]'
    name = args[0]
    if name in contacts.keys():
        return contacts[name]
    return f"Contact '{name}' not found"


def show_all(contacts):
    """Returns all contacts information"""
    if not contacts:
        return "No contacts saved."
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result)


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "":
            continue
        else:
            print("Invalid command.")

main()
