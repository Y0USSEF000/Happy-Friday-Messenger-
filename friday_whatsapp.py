import time
import pywhatkit
import os
import random
from datetime import datetime

numbers = [
   
]

IMAGE_FOLDER = "./image"
IMAGE_COUNT = 6

def get_random_image():
    images = []
    for x in range(1, IMAGE_COUNT + 1):


        path = os.path.join(IMAGE_FOLDER, f"image{x}.jpg")
        if os.path.exists(path):
            images.append(path.replace("\\", "/"))
    if not images:
        raise Exception("No images found!")
    return random.choice(images)

def send_to_all():
    random_image = get_random_image()
    print(f"\n🎲 Selected image: {random_image}\n")

    for num in numbers:
        print(f"➡️ Sending {random_image} to {num} ...")
        pywhatkit.sendwhats_image(
            receiver=num,
            img_path=random_image,
            caption="Happy Friday 😊",
            wait_time=20,
            tab_close=True
        )
        time.sleep(10)

    print("\n🎉 DONE — All numbers received the image.\n")

# ------------------- LOOP -------------------

print("⏳ Waiting for Friday... (any hour)")

last_sent_week = None  # prevents sending twice the same Friday

while True:
    now = datetime.now()

    # Friday ?
    if now.weekday() == 1:  # 4 = Friday
        week_number = now.isocalendar().week

        # send only ONCE per Friday
        if week_number != last_sent_week:
            print("\n📅 Today is Friday — Sending now!")
            send_to_all()
            last_sent_week = week_number
        else:
            print(f"✔ Already sent this Friday (week {week_number}).")

    time.sleep(60)  # check every 1 minute
