from sklearn.model_selection import train_test_split
from test2 import img_list
train_img_list, val_img_list = train_test_split(img_list, test_size=0.2, random_state=2000)

if __name__ == "__main__":
    print(len(train_img_list), len(val_img_list))