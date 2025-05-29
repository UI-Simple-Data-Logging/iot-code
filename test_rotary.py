import RPi.GPIO as GPIO
import time

# Set GPIO pins
CLK = 22
DT = 23

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(CLK, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(DT, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("🔁 Rotary encoder test running. Rotate the knob...")

# Initial state
clk_last = GPIO.input(CLK)

try:
    while True:
        clk_current = GPIO.input(CLK)
        if clk_current != clk_last:
            dt_current = GPIO.input(DT)
            if dt_current != clk_current:
                print("⏩ Clockwise")
            else:
                print("⏪ Counter-clockwise")
        clk_last = clk_current
        time.sleep(0.01)

except KeyboardInterrupt:
    print("\n🛑 Exiting")
    GPIO.cleanup()
