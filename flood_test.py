import serial
import led_blink_pb2  # A generált Protobuf Python fájl
import time
import random

# Soros port beállítása (Windows: COMxx, Linux/macOS: /dev/ttyUSBx)
ser = serial.Serial('COM11', 115200, timeout=0.1)  

# Helyes üzenetek létrehozása
msg_on = led_blink_pb2.LedStatus()
msg_on.status = 1

msg_off = led_blink_pb2.LedStatus()
msg_off.status = 0

# Flood teszt
try:
    while True:
        if random.random() < 0.8:  
            # 80%-ban helyes üzenet küldése
            message = msg_on.SerializeToString() if random.random() < 0.5 else msg_off.SerializeToString()
            message = b'\xFF' + message
        else:
            # 20%-ban érvénytelen adatok küldése
             message = b"INVALID_DATA_" + bytes([random.randint(0, 255)]) * random.randint(1, 5)

        ser.write(message)  # Küldés UART-on
        print(f"Sent: {message}")

        # Várakozás egy kis időt, hogy elkerüljük a buffer túlcsordulását
        time.sleep(0.01)  

        # Visszajelzés olvasása, ha van
        if ser.in_waiting > 0:
            received_message = ser.readline().decode('utf-8', errors='ignore').strip()
            print(f"Received: {received_message}")

except KeyboardInterrupt:
    print("Flood test stopped...")
finally:
    ser.close()  # Port lezárása a kilépéskor
