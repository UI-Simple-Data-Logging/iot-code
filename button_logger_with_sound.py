from gpiozero import Button
import requests
import time

button = Button(17)  # GPIO17

def send_to_mac_and_db():
    # Mongo backend
    db_data = { "name": "Button", "value": "1" }
    try:
        r1 = requests.post("http://192.168.63.213:5050/api/items", json=db_data)
        print("✅ DB status:", r1.status_code)
    except Exception as e:
        print("❌ DB failed:", e)

    # MacBook IP
    try:
        r2 = requests.post("http://192.168.63.213:8888")  # Replace IP
        print("🎵 Mac notified:", r2.status_code)
    except Exception as e:
        print("❌ Mac notify failed:", e)

button.when_pressed = send_to_mac_and_db

print("📡 Waiting for button press...")
while True:
    time.sleep(1)
