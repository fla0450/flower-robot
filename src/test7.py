import signal
import sys
import inputs
import serial
import time
import threading

def signal_handler(signal, frame):
    print('byebye ^^')  
    sys.exit(0)

def left_joystick_show():
    print('run left_joystick_show')
    # 센터 값으로 초기화
    x = 128 
    y = 128
    x_state = "11"
    y_state = "11"
    ButtonA_flag = True
    previous_data = ""

    try:
        py_serial = serial.Serial(
            port='COM13',
            baudrate=115200,
            timeout=1  # Timeout 설정
        )
        py_serial2 = serial.Serial(
            port='COM14',
            baudrate=115200,
            timeout=1
        )
        time.sleep(2)  # 연결 안정화를 위해 잠시 대기
    except serial.SerialException as e:
        print('Failed to open serial port:', e)
        return

    def uart_receive():
        while True:
            try:
                if py_serial.in_waiting > 0:
                    received_data = py_serial.readline().decode('utf-8').strip()
                    print(f"Received: {received_data}")
            except Exception as e:
                print('UART Receive Error:', e)
                time.sleep(1)  # 에러 발생 시 잠시 대기 후 재시도

    # UART 수신 스레드 시작
    uart_thread = threading.Thread(target=uart_receive)
    uart_thread.daemon = True
    uart_thread.start()

    while True:
        try:
            # 게임패드 이벤트 전달 받기
            events = inputs.get_gamepad()
            for event in events:
                if event.ev_type == "Key":
                    if event.code == 'BTN_SOUTH':
                        if event.state == 1:
                            if ButtonA_flag:
                                py_serial2.write("3 180\n".encode())
                                ButtonA_flag = False
                            else:
                                py_serial2.write("3 0\n".encode())
                                ButtonA_flag = True
                    elif event.code == 'BTN_NORTH':
                        if event.state == 1:
                            if ButtonA_flag:
                                py_serial2.write("1 180\n".encode())
                                ButtonA_flag = False
                            else:
                                py_serial2.write("1 0\n".encode())
                                ButtonA_flag = True
                if event.ev_type == 'Absolute':
                    changed = False
                    # X축
                    if event.code == 'ABS_X':
                        x = int(event.state)
                        changed = True
                    # Y축
                    elif event.code == 'ABS_Y':
                        y = int(event.state)
                        changed = True
                    elif event.code == 'ABS_HAT0Y':
                        if event.state == -1:
                            z_state = "32"
                        elif event.state == 1:
                            z_state = "31"
                        elif event.state == 0:
                            z_state = "33"
                        print(z_state)
                        py_serial.write((z_state + "\n").encode('utf-8'))
                        py_serial.flush()
                    # 변경되었다면 즉, X나 Y가 변경되었을때 출력
                    if changed:
                        # X축 상태 설정
                        if x <= -20000:
                            x_state = "01"
                        elif x >= 20000:
                            x_state = "10"
                        else:
                            x_state = "11"
                        # Y축 상태 설정
                        if y <= -20000:
                            y_state = "01"
                            print("01")
                        elif y >= 20000:
                            y_state = "10"
                        else:
                            y_state = "11"
                        
                        data = x_state + y_state
                        
                        # 중복된 값이 아니면 전송
                        if data != previous_data:
                          
                            py_serial.write((data + "\n").encode('utf-8'))
                            previous_data = data
        except Exception as e:
            print('Error:', e)
            time.sleep(1)  # 에러 발생 시 잠시 대기 후 재시도

    py_serial.close()
    print('byebye!')

if __name__ == '__main__':
    # 키보드 ctrl + c 눌러 종료하기 위한 함수
    signal.signal(signal.SIGINT, signal_handler)
    
    # 실행
    left_joystick_show()
