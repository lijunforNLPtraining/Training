

with open('./data_index.csv','r',encoding='utf-8') as f_read:
    data = f_read.readlines()
f_read.close()

print(len(data))
n = 0
m = 0
for line in data:
    line = line.split(',')
    if len(line) == 1001:
        m +=1
    if int(line[-1]) == 1:
        n += 1
print(m)
print('total number of  xinhuashe is {}'.format(n))


















