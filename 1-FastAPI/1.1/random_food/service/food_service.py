import requests


def get_random_food():

    try:

        response = requests.get(
            "https://foodish-api.com/api/",
            timeout=15
        )

        data = response.json()

        image_url = data["image"]

        food_name = image_url.split("/")[-2]

        image_response = requests.get(
            image_url,
            timeout=15
        )

        return {
            "food_name": food_name.title(),
            "image_bytes": image_response.content
        }

    except Exception as e:

        print("ERROR:", e)

        return {
            "food_name": "Unknown",
            "image_bytes": None
        }