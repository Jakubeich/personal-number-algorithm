import hashlib
import time
from faker import Faker
import uuid

fake = Faker()

# Funkce pro generování osobních čísel
def generate_personal_number(name, surname):
    # Vytvoření hashu z náhodného UUID (univerzální unikátní identifikátor), jména a příjmení a aktuálního času které se zašifrují pomocí SHA-256 algoritmu
    uuid_str = str(uuid.uuid4())
    message = uuid_str + name + surname + str(time.time())
    hash_object = hashlib.sha256(message.encode())
    print(hash_object.hexdigest())
    return hash_object.hexdigest()

# Funkce pro testování
def test_personal_number(num_tests):
    # Vytvoření množiny pro ukládání osobních čísel a proměnné pro počítání duplicit
    personal_numbers = set()
    duplicates = 0
    # Pro každý test vytvoříme náhodné jméno a příjmení a pomocí funkce generate_personal_number získáme osobní číslo
    for i in range(num_tests):
        name = fake.first_name()
        surname = fake.last_name()
        personal_number = generate_personal_number(name, surname)
        if personal_number in personal_numbers:
            duplicates += 1
        else:
            personal_numbers.add(personal_number)
    return duplicates

# Testování s 1 000 000 iteracemi
num_tests = 1000000
duplicates = test_personal_number(num_tests)
print("Počet osobních čísel: {}".format(num_tests))
print("Počet duplicit: {}".format(duplicates))