from roboflow import Roboflow
rf = Roboflow(api_key="lzm5pTN7P7mFFswAl5I2")
project = rf.workspace("guide-for-gardner").project("plant-dhk3u")
version = project.version(7)
dataset = version.download("yolov5")