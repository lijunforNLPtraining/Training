


with open('./liver_train_data.csv','r',encoding='utf-8') as f_word:
    data = f_word.readlines()
with open('./liver_train_label.csv','r',encoding='utf-8') as f_label:
    label = f_label.readlines()

print(len(data))
print(len(label))

positive = open('./positive.txt','w',encoding='utf-8')
nagetive = open('./negative.txt','w',encoding='utf-8')

positive_index = []
negative_index = []
for i in range(len(label)):
    line = label[i]
    line = line.split('\t')
    tmp1 = int(line[0])
    if tmp1 > 0:
        negative_index.append(i)
    else:
        positive_index.append(i)
print(len(negative_index))
print(len(positive_index))

for index in positive_index:
    positive.write(data[index])
for index in negative_index:
    nagetive.write(data[index])



