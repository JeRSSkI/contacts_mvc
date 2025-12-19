from model import ContactModel
from view import ContactView

class ContactController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        while True:
            self.view.show_menu()
            choice = input("Виберіть опцію: ")
            if choice == '1':
                name, phone = self.view.get_contact_info()
                self.model.add_contact(name, phone)
                self.view.show_message("Контакт додано!")
            elif choice == '2':
                contacts = self.model.get_contacts()
                self.view.show_contacts(contacts)
            elif choice == '3':
                self.view.show_message("До побачення!")
                break
            else:
                self.view.show_message("Невірний вибір")
