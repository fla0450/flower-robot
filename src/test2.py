from glob import glob

img_list = glob('../dataset/plant-7/train/images//*.jpg')
print(img_list[0])
if __name__ == "__main__":
    print(len(img_list))