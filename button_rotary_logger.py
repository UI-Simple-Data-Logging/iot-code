import requests
import time
import RPi.GPIO as GPIO

API_URL = 'http://192.168.63.213:5050/api/items'  # 👈 your local IP

button_pin = 17
clk_pin = 22
dt_pin = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(clk_pin, GPIO.IN)
GPIO.setup(dt_pin, GPIO.IN)

print("📲 Waiting for button press...")

def send_rotation(direction):
    try:
        payload = {
            "name": "rotary",
            "value": direction
        }
        response = requests.post(API_URL, json=payload)
        print(f"✅ Sent to DB: {direction}, status: {response.status_code}")
    except Exception as e:
        print(f"❌ Error: {e}")

try:
    while True:
        button_state = GPIO.input(button_pin)
        if button_state == GPIO.LOW:
            print("🔘 Button pressed! Start rotating...")
            last_clk = GPIO.input(clk_pin)
            start_time = time.time()

            while time.time() - start_time < 5:  # 5 seconds read window
                current_clk = GPIO.input(clk_pin)
                current_dt = GPIO.input(dt_pin)

                if current_clk != last_clk:
                    if current_dt != current_clk:
                        send_rotation("clockwise")
                    else:
                        send_rotation("counter-clockwise")
                    last_clk = current_clk

                time.sleep(0.01)

            print("⏹️ Done reading. Waiting for next press...")
        time.sleep(0.1)

except KeyboardInterrupt:
    print("🛑 Exiting")
finally:
    GPIO.cleanup()
