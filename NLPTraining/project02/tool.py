

import re
import time
from collections import Counter
from collections import defaultdict

import jieba
import numpy as np
import pandas as pd
from gensim.models import Word2Vec



# 计算余弦相似度
def get_cos_similarity(v1, v2):
    if len(v1) != len(v2):
        return 0
    return np.sum(np.array(v1) * np.array(v2)) / (np.linalg.norm(v1) * np.linalg.norm(v2))

# 加载训练好的维基W2V模型
def get_model_from_file(filename):
    model = Word2Vec.load(filename)
    return model


def word_freq(corpus_file):
    word_list = []
    with open(corpus_file, 'r', encoding='utf-8') as fin:
        for line in fin.readlines():
            word_list += line.split()
    print(len(word_list))
    cc = Counter(word_list)
    # print(cc)
    num_all = sum(cc.values())

    def get_word_freq(word):
        return cc[word] / num_all

    return get_word_freq



# 获得句子向量矩阵
def get_sentences_vec(model, sent_list, get_wd_freq):
    # 词向量加权部分
    a = 0.001
    row = model.wv.vector_size#获取在Word2vector模型中每个词的维度是多少
    col = len(sent_list)#获得一共有多少个句子需要参加比较
    sent_mat = np.mat(np.zeros((row, col)))#将np.zeros((row, col))这样一个二维数组转为矩阵
    for i, sent in enumerate(sent_list):
        # new_sent = rm_spec(sent)
        new_sent = sent
        if not new_sent: continue
        sent_vec = np.zeros(row)
        for word in new_sent:
            pw = get_wd_freq(word)
            # print(pw)
            w = a / (a + pw)
            try:
                vec = np.array(model.wv[word])
                sent_vec += w * vec#这里相当于将每个词的向量经过与自己的权重相乘之后叠加在一起，叠加在一起之后还是一个1*row的向量
            except:
                pass
        sent_mat[:, i] += np.mat(sent_vec).T#sent_vec是一行的向量，根据sent_mat = np.mat(np.zeros((row, col)))的定义
        #需要将每次句子表示成竖着的列向量，所以做了一次转置
        sent_mat[:, i] /= len(new_sent)#根据论文，这里需要除以整个句子的长度

    # 减去PCA中的第一主成分
    u, s, vh = np.linalg.svd(sent_mat)#这里类似线性代数里面的矩阵相似一样，中间那个矩阵是特征值组成的
    #只不过这个函数可以自动将为0的特征值去掉缩小维度，参考博客：https://blog.csdn.net/u012162613/article/details/42214205
    sent_mat = sent_mat - u * u.T * sent_mat
    #论文上面是这样相减，但是具体原因还没有明白
    return sent_mat


# 返回句子向量矩阵中各列向量与第一列向量的相似度
def get_sent_vec_sims(sent_mat):
    first = np.array(sent_mat[:, 0])[:, 0]
    col = sent_mat.shape[1]
    sims = []
    for i in range(1, col):
        vec = np.array(sent_mat[:, i])[:, 0]
        sims.append(get_cos_similarity(first, vec))
    avg_similarity = np.mean(np.array(sims))
    num = 0
    for sim in sims:
        if sim > 0.5:
            num +=1
    return num

# 获得最终说的话
def get_final_sents(sents, sims):
    senlist = []
    threshold = 0.5  # 相似度超过0.5即认为两句话相关
    for i in range(len(sims)):
        if sims[i] > threshold:
            senlist.append(sents[i])
    ret = [''.join(s) for s in senlist]
    return ret


