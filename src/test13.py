from glob import glob
labels = glob("../dataset/Gerbera/train/labels/*.txt")
new_data = ""
for label in labels:
    with open(label,'r') as f:
        lines = f.readlines()
        print(lines)
        data = lines[0].split(' ')
        if data[0] == '15':
            data[0] = '21'
        new_data = data[0]+" "+data[1]+" "+data[2]+" "+data[3]+" "+data[4]+"\n"
    with open(label,'w') as f:
        f.write(new_data)
    print(label)

#print(labels)