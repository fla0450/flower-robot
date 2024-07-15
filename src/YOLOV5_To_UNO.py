import serial
import time
def send_data(x1,y1,x0,y0):
    py_serial = serial.Serial(
    port ='COM9',
    baudrate =115200,
    )
    x_data = 0b0000
    y_data = 0b0000
   
    if x1 > x0 and x1 < x0+30:
        y_data = 0b0000
        if y1 > y0 and y1 > y0 +30:
            x_data = 0b0000
        elif y1 > y0:
            x_data = 0b0100
        elif y1 < y0 and y1 > y0 -30:
            x_data = 0b0000
        elif y1 < y0:
            x_data = 0b1000
    elif x1 > x0:
        y_data = 0b0010
    elif x1 < x0 and x1 > x0-30:
        y_data = 0b0000
        if y1 > y0:
            x_data = 0b0100
        if y1 > y0 and y1 > y0 +30:
            x_data = 0b0000
        if y1 < y0:
            x_data = 0b1000
        if y1 < y0 and y1 > y0 -30:
            x_data = 0b0000 
        elif x1 < x0:
            y_data = 0b0001
    data = x_data + y_data
    print(data)
    py_serial.write(data)
    time.sleep(1)
    
if __name__ == "__main__":
    for i in range(0,25):
        send_data(480,200,320,320)


