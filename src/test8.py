import serial
import time


def send_data(x1,y1,x0,y0):
    py_serial = serial.Serial(
    port ='COM13',
    baudrate =115200,
    )
    x_data = "01"
    y_data = "11"
    data = x_data + y_data+"\n"
    data = data.encode()
    py_serial.write(data)
    time.sleep(1)
    
if __name__ == "__main__":
    send_data(480,200,320,320)
