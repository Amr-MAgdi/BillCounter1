import serial
import time


def initialize_bill_acceptor(port='/dev/ttyUSB0', baud_rate=9600):
    try:
        # Open the serial port
        ser = serial.Serial(port, baud_rate, timeout=1)
        print(f"Connected to {ser.name}")

        # Send initialization commands if needed
        # For example, you might need to send a command to enable the bill acceptor

        return ser
    except serial.SerialException as e:
        print(f"Error: {e}")
        return None


def read_bill(ser):
    try:
        # Send a command to the bill acceptor to request bill information
        # For example: ser.write(b'READ\r\n')

        # Read the response
        response = ser.readline().decode('utf-8').strip()

        if response:
            print(f"Received bill information: {response}")
        else:
            print("No response received")

    except serial.SerialException as e:
        print(f"Error: {e}")


def close_serial_port(ser):
    if ser:
        ser.close()
        print("Serial port closed.")


if __name__ == "__main__":
    # Modify the port and baud_rate based on your setup
    serial_port = '/dev/ttyUSB0'
    baud_rate = 9600

    bill_acceptor = initialize_bill_acceptor(serial_port, baud_rate)

    if bill_acceptor:
        try:
            while True:
                # Continuously read bills (you may want to add some delay)
                read_bill(bill_acceptor)
                time.sleep(1)

        except KeyboardInterrupt:
            # Close the serial port when the script is interrupted
            close_serial_port(bill_acceptor)
