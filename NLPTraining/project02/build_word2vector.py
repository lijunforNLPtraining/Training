

import re
import jieba

from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

def build_gensim(file_path):
    word2vec_model = Word2Vec(LineSentence(file_path), min_count=10, size=50)
    word2vec_model.save('./word2vec_model')
    return  word2vec_model

build_gensim('./txt_for_build_world2vec.txt')


# with open('./all_data.csv','r',encoding='utf-8') as f_read:
#     data = f_read.readlines()
# f_read.close()
#
# # words = []
# with open('txt_for_build_world2vec.txt','w',encoding='utf-8') as f_write:
#     for line in data:
#
#         line = line.replace('。', '')
#         # line = re.findall(r'[\w\d]+',line.strip())
#         line = line.replace(',','')
#         print(line)
#         words = jieba.cut(str(line))
#         f_write.write(' '.join(words))
# f_write.close()