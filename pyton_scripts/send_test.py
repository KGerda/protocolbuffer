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

msg2 = led_blink_pb2.LedStatus()
msg2.status = 0

msg3= led_blink_pb2.LedStatus()
msg3.status = 12

msg4 = led_blink_pb2.LedStatus()
msg4.status = 1

msg5 = led_blink_pb2.LedStatus()
msg5.status = 1

message = b'\xFF' + msg.SerializeToString()
message2 = b'\xFF' + msg2.SerializeToString()
message3 = b'\xFF' + msg3.SerializeToString()
message4 = b'\xFF' + msg4.SerializeToString()
message5 = b'\xFF' + msg5.SerializeToString()
# Szerializálás és küldés

ser.write(message)
ser.write(message2)
ser.write(message3)
ser.write(message4)
ser.write(message5)
ser.write(message)
ser.write(message2)
ser.write(message3)
ser.write(message4)
ser.write(message5)

try:
    while True:

            # Fogadunk üzenetet
            received_message = receive_message()
            if received_message:
                print(f"Received: {received_message}")
            time.sleep(0.5)  # Várakozás a következő ciklus előtt

except KeyboardInterrupt:
    print("Program interrupted. Closing...")
finally:
    ser.close()  # Port lezárása, ha a program véget ér
    