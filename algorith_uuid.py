import uuid

# Množina pro ukládání již použitých osobních čísel
used_personal_numbers = set()

# Funkce pro generování personal number
def generate_personal_number(uuid_val):
    # Převedení uuid na číslo
    uuid_num = int(uuid_val.replace('-', ''), 16)
    # Normalizace na rozsah 1-999999999
    personal_number = (uuid_num % 1000000000) + 1
    return personal_number

# Funkce pro generování unikátního personal number
def generate_unique_personal_number():
    while True:
        # Generování uuid
        uuid_val = str(uuid.uuid4())
        # Generování personal number
        personal_number = generate_personal_number(uuid_val)
        # Kontrola, zda personal number již nebyl použit
        if personal_number not in used_personal_numbers:
            used_personal_numbers.add(personal_number)
            return personal_number

# Funkce pro testování generování personal number
def test_personal_number(num_tests):
    # Množina pro ukládání již použitých osobních čísel
    used_personal_numbers = set()
    duplicates = 0
    # Pro každý test se vygeneruje personal number pomocí funkce generate_unique_personal_number a zkontroluje, zda již nebyl použit pokud ano, zvýší se počet duplicit
    for i in range(num_tests):
        personal_number = generate_unique_personal_number()
        if personal_number in used_personal_numbers:
            duplicates += 1
        else:
            used_personal_numbers.add(personal_number)
    return duplicates

num_tests = 1000000
duplicates = test_personal_number(num_tests)
print('Duplicates: %d/%d (%.2f%%)' % (duplicates, num_tests, duplicates / num_tests * 100))
