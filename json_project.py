import requests

response = requests.get('https://dummyjson.com/users')
data = response.json()

count_under_30 = 0
count_women_green_eyes = 0
count_in_san_francisco = 0

for user in data['users']:
    if user['age'] < 30:
        count_under_30 += 1
    if user['gender'] == 'female' and user['eyeColor'] == 'green':
        count_women_green_eyes += 1
    if user['address']['city'] == 'San Francisco':
        count_in_san_francisco += 1
print(f"Кількість користувачів молодше 30 років: {count_under_30}")
print(f"Кількість жінок з зеленими очима: {count_women_green_eyes}")
print(f"Кількість людей, які живуть у San Francisco: {count_in_san_francisco}")
