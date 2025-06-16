
import csv
import re


def default_view(phone):
    """Приводит номер телефона к формату +7(ххх)ххх-хх-хх [доб. хххх]"""
    add_match = re.search(r'[\s,;()]+доб\.?[\s\.]*(\d{4})', phone, re.IGNORECASE) # поиск нечувствительный к регистру
    add_part = ''
    if add_match:
        add_number = add_match.group(1)
        add_part = f' доб.{add_number}' # приводим добавочный к формату доб.#### 
        phone = phone[:add_match.start()]  

    
    cleaned_phone = re.sub(r'\D', '', phone) # чистим основной номер от всего

    
    last_digits = cleaned_phone[-10:]
    default_phone_view = re.sub(
        r'^(\d{3})(\d{3})(\d{2})(\d{2})$',
        r'+7(\1)\2-\3-\4',
        last_digits)  # приводим к стандартному виду +7 (ххх)-ххх-хх-хх

    return default_phone_view + add_part


with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = []
    for row in rows:
        # Дополняем недостающие поля пустыми строками
        while len(row) < 7:
            row.append('')
        contacts_list.append(row)



unique_contacts = {}

for row in contacts_list:
    full_name_str = ' '.join([part.strip() for part in row[:3] if part.strip()])
    full_name = full_name_str.split()

    lastname = full_name[0] if len(full_name) > 0 else ''
    firstname = full_name[1] if len(full_name) > 1 else ''
    surname = full_name[2] if len(full_name) > 2 else ''

    organization = row[3].strip() if len(row) > 3 and row[3] else ''
    position = row[4].strip() if len(row) > 4 and row[4] else ''
    phone = row[5].strip() if len(row) > 5 and row[5] else ''
    email = row[6].strip() if len(row) > 6 and row[6] else ''


    phone = default_view(phone)

    key = (lastname.strip(), firstname.strip(), surname.strip()) # группировка по ФИО

    if key in unique_contacts:
        
        existing = unique_contacts[key]

        existing[0] = existing[0] or lastname
        existing[1] = existing[1] or firstname
        existing[2] = existing[2] or surname
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

for idx, contact in enumerate(contacts_list):
    while len(contact) < 7:
        contact.append('')
    if len(contact) > 7:
        contact = contact[:7]
    contacts_list[idx] = contact


with open("phonebook.csv", "w", encoding="utf-8", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(contacts_list)