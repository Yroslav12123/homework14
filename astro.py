import requests


def get_astronauts_on_iss():
    url = "http://api.open-notify.org/astros.json"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        astronauts = data['people']

        iss_astronauts = [astro['name'] for astro in astronauts if astro['craft'] == "ISS"]

        return iss_astronauts
    else:
        return None


if __name__ == "__main__":
    astronauts_on_iss = get_astronauts_on_iss()

    if astronauts_on_iss is not None:
        print("Астронавти на станції (ISS):")
        for astro in astronauts_on_iss:
            print(f"- {astro}")
    else:
        print("Не вдалося отримати дані про астронавтів.")
