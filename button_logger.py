from gpiozero import Button
import requests
import time

button = Button(17)  # GPIO17

def send_to_db():
    data = {
        "name": "Button",
        "value": "1"
    }
    try:
        response = requests.post("http://192.168.63.213:5050/api/items", json=data)
        print("✅ Data sent:", response.status_code)
    except Exception as e:
        print("❌ Failed:", e)

button.when_pressed = send_to_db

print("📡 Waiting for button press...")
while True:
    time.sleep(1)
