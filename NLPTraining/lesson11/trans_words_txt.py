
stopwords = [word.strip() for word in open('./stopwords.txt','r',encoding='utf-8').readlines()]
with open('./news_cutted_words.txt','r',encoding='utf-8') as f_read:
    words = f_read.readlines()
f_read.close()

with open('oneword_oneline_words.txt','w',encoding='utf-8') as f_write:
    for line in words:
        words = line.split(' ')
        for word in words:
            if word.strip() != '' and word not in stopwords:
                f_write.write(word + '\n')

f_write.close()





