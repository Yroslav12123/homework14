import requests

url = "https://dummyjson.com/users"
response = requests.get(url)

if response.status_code == 200:
    users = response.json().get('users', [])
else:
    print("Не вдалося отримати дані:", response.status_code)
    users = []

under_30_count = sum(1 for user in users if user['age'] < 30)

women_with_green_eyes_count = sum(1 for user in users if user['gender'] == 'female' and user['eyeColor'] == 'Green')

living_in_san_francisco_count = sum(1 for user in users if user['address']['city'] == 'San Francisco')

print(f"Кількість користувачів молодше 30 років: {under_30_count}")
print(f"Кількість жінок з зеленими очима: {women_with_green_eyes_count}")
print(f"Кількість людей, які живуть у Сан-Франциско: {living_in_san_francisco_count}")
