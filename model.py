class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class ContactModel:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone):
        contact = Contact(name, phone)
        self.contacts.append(contact)

    def get_contacts(self):
        return self.contacts
