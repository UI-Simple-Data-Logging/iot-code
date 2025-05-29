import RPi.GPIO as GPIO
import time

# Use Broadcom (BCM) pin numbering
GPIO.setmode(GPIO.BCM)

# List of all GPIO pins (excluding reserved ones like 0, 1 if needed)
gpio_pins = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
             12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
             22, 23, 24, 25, 26, 27]

print("Reading GPIO input status:")
for pin in gpio_pins:
    try:
        GPIO.setup(pin, GPIO.IN)
        value = GPIO.input(pin)
        print(f"GPIO {pin}: {'HIGH' if value else 'LOW'}")
    except Exception as e:
        print(f"GPIO {pin}: Error - {e}")

GPIO.cleanup()
