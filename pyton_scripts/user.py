import serial
import led_blink_pb2 

# Serial port configuration
ser = serial.Serial('COM11', 115200, timeout=1)

try:
    while True:
        user_input = input("Enter a command ('on' / 'off'): ").strip().lower()

        if user_input in ["on", "off"]:
            msg = led_blink_pb2.LedStatus()
            msg.status = 1 if user_input == "on" else 0

            message = b'\xFF' + msg.SerializeToString()
            ser.write(message)
            print(f"Command sent: {user_input.upper()}")
        else:
            print("Unknown command! Available options: 'on' / 'off'")

except KeyboardInterrupt:
    print("\nExit...")
finally:
    ser.close()   #Close the port when the program ends