#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re

class ContactBook:
    def __init__(self):
        self.contacts = []

    def create_contact(self, name, phone, email):
        contact = {"name": name, "phone": phone, "email": email}
        self.contacts.append(contact)

    def read_contacts(self):
        return self.contacts

    def update_contact(self, index, name, phone, email):
        if index >= 0 and index < len(self.contacts):
            self.contacts[index]["name"] = name
            self.contacts[index]["phone"] = phone
            self.contacts[index]["email"] = email
            return True
        return False

    def delete_contact(self, index):
        if index >= 0 and index < len(self.contacts):
            del self.contacts[index]
            return True
        return False

def validate_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email)

def validate_phone(phone):
        if len(str(phone)) == 10:
            return True
        else:
            return False


def print_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for index, contact in enumerate(contacts):
            print(
                f"{index + 1}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}"
            )

def main():
    contact_book = ContactBook()


    while True:
        print("*** CONTACT BOOK MANAGEMENT ***")
        print("1. View Contacts")
        print("2. Add Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            contacts = contact_book.read_contacts()
            print_contacts(contacts)
        elif choice == "2":
            name = input("Enter the name: ")
            while True:
                phone = input("Enter the phone number: ")
                if not validate_phone(phone):
                    print("Invalid phone number ! please enter 10 digit only")
                else:
                    break
            while True:
                email = input("Enter the email address: ")
                if not validate_email(email):
                    print("Invalid email address! please enter proper Email")
                else:
                     break
            contact_book.create_contact(name, phone, email)
            print("Contact added successfully.")
        elif choice == "3":
            contacts = contact_book.read_contacts()
            print_contacts(contacts)
            index = int(input("Enter the index of the contact to update: ")) - 1
            if index >= 0 and index < len(contacts):
                name = input("Enter the updated name: ")
                while True:
                    phone = input("Enter the  updated phone number: ")
                    if not validate_phone(phone):
                        print("Invalid phone number ! please enter 10 digit only")
                    else:
                        break
                while True:
                    email = input("Enter the updated  email address: ")
                    if not validate_email(email):
                        print("Invalid email address! please enter proper Email")
                    else:
                        break
                if contact_book.update_contact(index, name, phone, email):
                    print("Contact updated successfully.")
                else:
                    print("Invalid contact index.")
            else:
                print("Invalid contact index.")
        elif choice == "4":
            contacts = contact_book.read_contacts()
            print_contacts(contacts)
            index = int(input("Enter the index of the contact to delete: ")) - 1
        elif choice == "5":
            print("existing")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()

