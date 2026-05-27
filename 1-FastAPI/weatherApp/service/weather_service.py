import requests


def load_api_key():
    with open("config.txt", "r") as f:
        return f.readline().strip()


def get_weather(city_name):

    try:

        api_key = load_api_key()

        url = (
            "https://api.weatherapi.com/v1/current.json"
            f"?q={city_name}&aqi=no&key={api_key}"
        )

        response = requests.get(url, timeout=5)

        print("STATUS:", response.status_code)
        print("TEXT:", response.text)

        if response.status_code != 200:
            return {
                "condition": "API Error",
                "wind_kph": "--",
                "humidity": "--"
            }

        data = response.json()

        current = data["current"]

        return {
            "condition": current["condition"]["text"],
            "wind_kph": current["wind_kph"],
            "humidity": current["humidity"]
        }

    except Exception as e:

        print("ERROR:", e)

        return {
            "condition": "Error",
            "wind_kph": "--",
            "humidity": "--"
        }