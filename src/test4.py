from test3 import train_img_list,val_img_list
with open('../dataset/plant-7/train.txt', 'w') as f:
  f.write('\n'.join(train_img_list) + '\n')

with open('../dataset/plant-7/val.txt', 'w') as f:
  f.write('\n'.join(val_img_list) + '\n')