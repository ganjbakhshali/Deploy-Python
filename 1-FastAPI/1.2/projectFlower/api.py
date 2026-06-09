import requests
import os
from openai import OpenAI

# دریافت API KEYها از محیط سیستم
Open_API_KEY = os.getenv("Open_API_KEY")
PlantNet_API_KEY = os.getenv("PlantNet_API_KEY")

client = OpenAI(
    base_url="https://api.gapgpt.app/v1",
    api_key=Open_API_KEY
)

def generate_image(prompt):
    try:
        # درخواست به GapGPT
        response = client.images.generate(
            model="gapgpt/z-image",
            prompt=prompt,
            size="720*420"
        )
        file_url = response.data[0].url

        # دانلود تصویر با timeout ایمن
        img_data = requests.get(file_url, timeout=60).content
        
        image_path = "generated-image.png"
        with open(image_path, "wb") as f:
            f.write(img_data)
        
        return image_path
    except Exception as e:
        print(f"Error in generate_image: {e}")
        return None  # اگر خطایی رخ داد، None برمی‌گردونیم تا main.py هندلش کنه




def identify_flower(image_path):

    absolute_path = os.path.join(os.getcwd(), image_path)
    
    print(f"DEBUG: Checking file at: {absolute_path}")

    if not os.path.exists(absolute_path):
        print(f"خطا: فایلی در مسیر {absolute_path} پیدا نشد!")
        return None

    url = "https://my-api.plantnet.org/v2/identify/all"
    

    api_key = os.getenv("PlantNet_API_KEY")
    payload = {"api-key": api_key}
    

    try:
        with open(absolute_path, 'rb') as f:
            files = {'images': f}
            

            response = requests.post(url, params=payload, files=files, timeout=30)
            
            if response.status_code == 200:
                print("Successful sending picture")
                return response.json()
            else:
                print(f"خطای سرور: {response.status_code} - {response.text}")
                return None
    
    except Exception as e:
        print(f"{e}")
        return None


