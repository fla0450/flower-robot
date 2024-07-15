import serial
import time
py_serial = serial.Serial(
    port ='COM14',
    baudrate =115200,
    timeout=1,
    )


py_serial.write("1 180\n".encode())
py_serial.write("2 180\n".encode())
py_serial.write("3 180\n".encode())
time.sleep(5)
py_serial.write("1 0\n".encode())
py_serial.write("2 0\n".encode())
py_serial.write("3 0\n".encode())