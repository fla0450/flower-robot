import yaml

with open('../dataset/plant-7/data.yaml', 'r') as f:
  data = yaml.load(f,Loader=yaml.FullLoader)



data['train'] = '../dataset/plant-7/train.txt'
data['val'] = '../dataset/plant-7/val.txt'

with open('../dataset/plant-7/data.yaml', 'w') as f:
  yaml.dump(data, f)

