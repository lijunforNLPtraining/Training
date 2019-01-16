import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy as np
import jieba

import jieba
# plt.xlabel('news content length range')
# plt.ylabel('Number of news')
# plt.title('The statistics of news dataset')
# plt.xlim(0,3000)
# plt.ylim(0,1500)
# x = 0
# y = {}
#
#
# content = pd.read_csv('sqlResult_1558435.csv', encoding='gb18030')
# content = content.fillna('')
# news_from = content['source']
# # print(all_news)
# print('一共包含了{}条新闻数据'.format(len(news_from)))
# num = 0
# for title in news_from:
#     if title.strip() == '新华社':
#         num +=1
# print('一共包含了{}条新华社出版的数据'.format(num))
# news_content = content['content']
# print(len(news_content))
# for new in news_content:
#     if x%1000 ==0:
#         print('have finished {} lines'.format(x))
#     x +=1
#     line = str(new.strip())
#     words = list(jieba.cut(line))
#     length = len(words)
#     if length in y.keys():
#         y[length] +=1
#     else:
#         y[length] = 1
# plt.bar(y.keys(),y.values(),facecolor='green')
# plt.show()

#这里可以确定将max_length设置为1000比较合理
import re

data_path = 'D:\\Eclipse_workplace\\Training\\NLPTraining\\News_Extraction\\sqlResult_1558435.csv'
content = pd.read_csv(data_path, encoding='gb18030')
news_content = content['content']
stopwords = [word.strip() for word in open('./stopwords.txt','r',encoding='utf-8').readlines()]
# print(stopwords)

with open('./news_cutted_words.txt','w',encoding='utf-8') as f_in:
    temp = []
    for line in news_content:
        # line = re.sub('[\s+\.\!\/_,$%^*(+\"\')]+|[+——\-()?【】《》“”！，。？、~@#￥%……&*（）]+', '', line)
        line = list(jieba.cut(str(line).strip()))
        for word in line:
            if word not in stopwords:
                temp.append(word)
    f_in.write(' '.join(temp))










