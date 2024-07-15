import subprocess

# 'dir' 명령어 실행 (Windows)
result = subprocess.run(['python ../yolov5/detect.py --weights ../yolov5/runs/train/test/weights/best.pt --source 1'], shell=True, capture_output=True, text=True)

# 에러 처리
if result.returncode == 0:
    print("명령어가 성공적으로 실행되었습니다.")
    print(result.stdout)
else:
    print("명령어 실행 중 에러가 발생했습니다.")
    print(result.stderr)
