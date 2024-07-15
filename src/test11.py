import inputs

def main():
    print("게임 패드의 버튼 입력을 확인합니다. 종료하려면 Ctrl+C를 누르세요.")
    while True:
        events = inputs.get_gamepad()
        for event in events:
            if event.ev_type == 'Key':
                print(f'Button {event.code} state: {event.state}')
            elif event.ev_type == 'Absolute':
                print(f'Axis {event.code} state: {event.state}')

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n프로그램을 종료합니다.")
