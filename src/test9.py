import cv2
import numpy as np

def detect_aluminum(image_path):
    # 이미지 로드
    image = cv2.imread(image_path)

    # 색상 기반 세그멘테이션
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_gray = np.array([0, 0, 100])
    upper_gray = np.array([179, 50, 255])
    mask = cv2.inRange(hsv_image, lower_gray, upper_gray)

    # 엣지 검출 및 윤곽선 찾기
    edges = cv2.Canny(image, 100, 200)
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # 알루미늄 영역 추출
    aluminum_contours = []
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 1000:  # 최소 면적 설정
            aluminum_contours.append(cnt)

    # 마스크 이미지 생성
    aluminum_mask = np.zeros_like(image)
    cv2.drawContours(aluminum_mask, aluminum_contours, -1, (0, 255, 0), 2)

    return aluminum_mask

# 사용 예시
aluminum_mask = detect_aluminum('img/job.jpg')
cv2.imshow('Aluminum Mask', aluminum_mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
