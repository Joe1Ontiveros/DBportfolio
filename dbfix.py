import random
import csv
from faker import Faker

fake = Faker()

def generate_users(num_users: int, start_id: int = 1):
    users = []
    used_emails = set()
    used_phones = set()
    i = 0
    while i < num_users:
        name = fake.name()
        email = fake.email()
        phone = fake.phone_number()
        if email not in used_emails and phone not in used_phones:
            users.append((start_id + i, name, email, phone))
            used_emails.add(email)
            used_phones.add(phone)
            i += 1
    return users

def generate_requests(num_requests, user_ids, start_id: int = 1):
    requests = []
    for i in range(num_requests):
        user_id = random.choice(user_ids)
        date = fake.date_this_century()
        method = fake.word()
        requests.append((start_id + i, user_id, date, method))
    return requests

def generate_programming_requests(num_requests, request_ids, start_id: int = 1):
    requests = []
    for i in range(num_requests):
        request_id = request_ids[i]
        area_of_focus = fake.word()
        company = fake.company()
        due_date = fake.date_this_century()
        description = fake.text()[:50]
        requests.append((start_id + i, area_of_focus, due_date, description))
    return requests

def generate_consulting_requests(num_requests, request_ids, start_id: int = 1):
    requests = []
    for i in range(num_requests):
        request_id = request_ids[i]
        area_of_focus = fake.word()
        company = fake.company()
        due_date = fake.date_this_century()
        description = fake.text()[:50]
        requests.append((start_id + i, due_date, description, area_of_focus, company))
    return requests

def generate_game_dev_requests(num_requests, request_ids, start_id: int = 1):
    requests = []
    for i in range(num_requests):
        request_id = request_ids[i]
        game_category = fake.word()
        description = fake.text()[:50]
        due_date = fake.date_this_century()
        requests.append((start_id + i, due_date, game_category, description))
    return requests

def generate_tutoring_requests(num_requests, request_ids, start_id: int = 1):
    requests = []
    for i in range(num_requests):
        request_id = request_ids[i]
        school_year = random.randint(1, 12)
        language = fake.word()
        description = fake.text()[:50]
        due_date = fake.date_this_century()
        requests.append((start_id + i, school_year, due_date, language, description))
    return requests

def write_to_csv(filename: str, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
        
if __name__ == "__main__":

    print('started')
    num_users = 1_000_000
    num_requests = 1_000_000

    users = generate_users(num_users)
    requests = generate_requests(num_requests, [user[0] for user in users])

    existing_user_ids = [user[0] for user in users]
    existing_request_ids = [request[0] for request in requests]

    programming_requests = generate_programming_requests(num_requests, existing_request_ids)
    consulting_requests = generate_consulting_requests(num_requests, existing_request_ids)
    game_dev_requests = generate_game_dev_requests(num_requests, existing_request_ids)
    tutoring_requests = generate_tutoring_requests(num_requests, existing_request_ids)

    write_to_csv('users.csv', users)
    write_to_csv('requests.csv', requests)
    write_to_csv('programming_requests.csv', programming_requests)
    write_to_csv('consulting_requests.csv', consulting_requests)
    write_to_csv('game_dev_requests.csv', game_dev_requests)
    write_to_csv('tutoring_requests.csv', tutoring_requests)
    print('done')