import csv
import re
import os
from functools import wraps
from datetime import datetime


def logger(path):
    def __logger(old_function):
        @wraps(old_function)
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            
            log_message = (
                f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: "
                f"function '{old_function.__name__}' called with args: {args}, kwargs: {kwargs}, "
                f"returned: {result}\n")
            
            with open(path, 'a', encoding='utf-8') as log_file:
                log_file.write(log_message)

            return result
        return new_function
    return __logger

@logger('phonebook.log')
def default_view(phone):
    add_match = re.search(r'[\s,;()]+доб\.?[\s\.]*(\d{4})', phone, re.IGNORECASE)
    add_part = ''
    if add_match:
        add_number = add_match.group(1)
        add_part = f' доб.{add_number}'
        phone = phone[:add_match.start()]
    
    cleaned_phone = re.sub(r'\D', '', phone)
    last_digits = cleaned_phone[-10:]
    default_phone_view = re.sub(
        r'^(\d{3})(\d{3})(\d{2})(\d{2})$',
        r'+7(\1)\2-\3-\4',
        last_digits)
    
    return default_phone_view + add_part

@logger('phonebook.log')
def load_contacts(path='phonebook_raw.csv'):
    with open(path, encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts = []
        for row in rows:
            while len(row) < 7:
                row.append('')
            contacts.append(row)
    return contacts

@logger('phonebook.log')
def save_contacts(contacts, path='phonebook.csv'):
    with open(path, "w", encoding="utf-8", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(contacts)


contacts_list = load_contacts()

unique_contacts = {}

for row in contacts_list:
    full_name_str = ' '.join([row[0].strip(), row[1].strip(), row[2].strip()])
    full_name = [p for p in full_name_str.split() if p]

    lastname = full_name[0] if len(full_name) > 0 else ''
    firstname = full_name[1] if len(full_name) > 1 else ''
    surname = full_name[2] if len(full_name) > 2 else ''

    organization = row[3].strip()
    position = row[4].strip()
    phone = row[5].strip()
    email = row[6].strip()

    phone = default_view(phone)

    key = (lastname, firstname, surname)

    if key in unique_contacts:
        existing = unique_contacts[key]
        existing[3] = existing[3] or organization
        existing[4] = existing[4] or position
        existing[5] = existing[5] or phone
        existing[6] = existing[6] or email
    else:
        unique_contacts[key] = [
            lastname, firstname, surname,
            organization, position, phone, email
        ]

contacts_list = list(unique_contacts.values())
save_contacts(contacts_list)
