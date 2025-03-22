import serial
import led_blink_pb2  # A generált Protobuf Python fájl
import time

def receive_message():
    if ser.in_waiting > 0:  # Ha érkezett adat
        message = ser.readline().decode('utf-8').strip()  # Üzenet fogadása és dekódolása
        return message
    return None


# Soros port beállítása
ser = serial.Serial('COM11', 115200, timeout=1)  

# Üzenet létrehozása
msg = led_blink_pb2.LedStatus()
msg.status = 1

# Szerializálás és küldés
ser.write(msg.SerializeToString())
try:
    while True:
            # Fogadunk üzenetet
            received_message = receive_message()
            if received_message:
                print(f"Received: {received_message}")
            time.sleep(1)  # Várakozás a következő ciklus előtt

except KeyboardInterrupt:
    print("Program interrupted. Closing...")
finally:
    ser.close()  # Port lezárása, ha a program véget ér