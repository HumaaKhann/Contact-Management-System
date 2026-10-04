# Contact Management System
# Practice using functions, lists, dictionaries, and JSON file handling.
# Includes adding, displaying, searching, deleting, and validating contacts.

import json


def add_person(person):
    name = input("Name:")
    age = input("Age:")
    email= input("Email:")

    for person in people:
        if person["email"].lower() == email.lower():
            print("This contact already exists.")
            return
        
    person={"name": name, "age": age, "email": email}
    return person


def display_contacts(people):
       if len(people) == 0:
        print("No contacts to display.")
        return
       
       for i, person in enumerate(people): 
        #i.e for every item in people, give me it's position and actual item
        print(i+1,"-",person["name"],person["age"],person["email"])

        
def delete_contact(people):
    display_contacts(people)

    while True:
        name = input("Enter the name of the contact to delete: ")
        email = input("Enter email: ")
        for person in people:
              if person["name"].lower() == name.lower() and person["email"].lower() == email.lower():
                people.remove(person)
                return
            
        print("Contact not found.")

def search_contact(people):
    name = input("Enter the name of the contact to search: ").lower()

    results = []

    for person in people:
        if name in person["name"].lower():
            results.append(person)

    if len(results) == 0:
        print("Contact not found.")
    else:
        print("\nContacts found:")
        display_contacts(results)


print("Hi , welcome to the contact management list")
print()

with open("contacts.json","r") as f:
    people = json.load(f)["contacts"]

while True:
    print("Contact list size:",len(people))
    command = input(
        "You can 'Add', 'Display', 'Delete' or 'Search' and 'Quit': "
    ).lower()
    
    if command == "add":
        person = add_person(people)

        if person:
            people.append(person)
            print("Person added successfully!")

    elif command == "display":
        display_contacts(people)

    elif command== "delete":
         delete_contact(people)
         print("Person deleted successfully!")

    elif command== "search":
         search_contact(people)

    elif command== "quit":
         break

    else:
         print("Invalid command. Please enter 'add', 'delete', or 'search'.")

with open("project3contacts.json", "w") as f:
    json.dump({"contacts": people}, f)