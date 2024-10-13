def reverse_lookup(Phonebook, name):
    for phone, person_name in Phonebook.items():
        if person_name == name:
            return phone
    return "Not found"
phonebook = {
    '123-456-7890': 'Nurik',
    '987-654-3210': 'Zhasik',
    '555-666-7777': 'Islam'
}
phone_number = reverse_lookup(phonebook, 'Islam')
print("Номер телефона для Islam:", phone_number)
