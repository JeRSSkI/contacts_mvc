class ContactView:
    def show_menu(self):
        print("1. Додати контакт")
        print("2. Показати контакти")
        print("3. Вийти")

    def get_contact_info(self):
        name = input("Введіть ім'я: ")
        phone = input("Введіть номер телефону: ")
        return name, phone

    def show_contacts(self, contacts):
        if not contacts:
            print("Контактів немає")
        for contact in contacts:
            print(f"{contact.name} - {contact.phone}")

    def show_message(self, message):
        print(message)
