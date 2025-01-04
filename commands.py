from models import AddressBook, Record, Phone, Birthday
from utils import input_error

@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(Phone(phone))
    return message

@input_error
def change_contact(args, book: AddressBook):
    name, old_phone, new_phone, *_ = args
    record = book.find(name)
    if record:
        for phone in record.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                return f"Phone number for {name} updated to {new_phone}."
        return f"Phone number {old_phone} not found for {name}."
    else:
        return f"Record with name {name} not found."

@input_error
def show_phones(args, book: AddressBook):
    name, = args
    record = book.find(name)
    if record:
        return ", ".join([phone.value for phone in record.phones])
    else:
        return f"Record with name {name} not found."

@input_error
def show_all(book: AddressBook):
    return "\n".join([f"{record.name.value}: {', '.join([phone.value for phone in record.phones])}" for record in book.records.values()])

@input_error
def add_birthday(args, book: AddressBook):
    name, date = args
    record = book.find(name)
    if record:
        record.add_birthday(Birthday(date))
        return f"Birthday for {name} added."
    else:
        return f"Record with name {name} not found."

@input_error
def show_birthday(args, book: AddressBook):
    name, = args
    record = book.find(name)
    if record and record.birthday:
        return f"{name}'s birthday is {record.birthday.value.strftime('%d.%m.%Y')}."
    else:
        return f"Birthday for {name} not found."

@input_error
def birthdays(args, book: AddressBook):
    upcoming_birthdays = book.get_upcoming_birthdays()
    if upcoming_birthdays:
        return "\n".join([f"{record.name.value} - {record.birthday.value.strftime('%d.%m.%Y')}" for record in upcoming_birthdays])
    else:
        return "No upcoming birthdays."

def show_help():
    return (
        "Available commands:\n"
        "add [ім'я] [телефон]: Додати або новий контакт з іменем та телефонним номером, або телефонний номер до контакту, який вже існує.\n"
        "change [ім'я] [старий телефон] [новий телефон]: Змінити телефонний номер для вказаного контакту.\n"
        "phone [ім'я]: Показати телефонні номери для вказаного контакту.\n"
        "all: Показати всі контакти в адресній книзі.\n"
        "add-birthday [ім'я] [дата народження]: Додати дату народження для вказаного контакту.\n"
        "show-birthday [ім'я]: Показати дату народження для вказаного контакту.\n"
        "birthdays: Показати дні народження, які відбудуться протягом наступного тижня.\n"
        "hello: Отримати вітання від бота.\n"
        "close або exit: Закрити програму."
    )
