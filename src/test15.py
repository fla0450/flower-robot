import cv2

def open_webcam():
    # 웹캠 캡처 객체 생성 (기본적으로 0번 카메라를 사용)
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2592)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1944)
    if not cap.isOpened():
        print("Cannot open webcam")
        return

    while True:
        # 프레임 읽기
        ret, frame = cap.read()

        if not ret:
            print("Cannot receive frame (stream end?). Exiting ...")
            break

        # 모니터 해상도에 맞게 프레임 크기 조정
        screen_width = 1280  # 예제 모니터 해상도, 필요시 모니터 해상도로 변경
        screen_height = 720  # 예제 모니터 해상도, 필요시 모니터 해상도로 변경
        frame = cv2.resize(frame, (screen_width, screen_height))

        # 프레임을 화면에 표시
        cv2.imshow('Webcam', frame)

        # 'q' 키를 누르면 루프 종료
        if cv2.waitKey(1) == ord('q'):
            break

    # 캡처 객체 및 윈도우 해제
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    open_webcam()
