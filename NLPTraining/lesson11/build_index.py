import gensim
import numpy as np
import pandas as pd
import jieba

D = 50
max_length = 1000

class Wordlist(object):
    def __init__(self, filename):
        lines = [x.split() for x in open(filename, 'r', encoding='utf-8').readlines()]
        self.size = len(lines)
        self.voc = [(item[0][0], item[1]) for item in zip(lines, range(self.size))]
        self.voc = dict(self.voc)
    def getID(self, word):
        try:
            return self.voc[word]
        except:
            return 0
def load_vec(vocab, model):
    word_vecs = {}
    for i in vocab:
        try:
            word_vecs[i] = model[i]
        except:
            word_vecs[i] = np.random.uniform(-0.5, 0.5, D)
    return word_vecs

def get_W(word_vecs, D):
    vocab_size = len(word_vecs)
    word_idx_map = dict()
    W = np.zeros(shape=(vocab_size + 1, D), dtype='float32')
    W[0] = np.random.uniform(-0.5, 0.5, D)
    i = 1
    for word in word_vecs:
        try:
            W[i] = word_vecs[word]
            word_idx_map[word] = i
            i += 1
        except:
            word_idx_map[word] = 0
    return W, word_idx_map

data_path = 'D:\\Eclipse_workplace\\Training\\NLPTraining\\News_Extraction\\sqlResult_1558435.csv'
content = pd.read_csv(data_path, encoding='gb18030')
content = content.fillna('')
num_sample = int(len(content))
stopwords = [word.strip() for word in open('./stopwords.txt','r',encoding='utf-8').readlines()]


model = gensim.models.Word2Vec.load('./news_word2vec_model')
vocab = Wordlist('./oneword_oneline_words.txt')
w2v = load_vec(vocab.voc, model)
newword2vector, word_idx_map = get_W(w2v, D)
ids = np.zeros((num_sample,max_length+1))
# print(model['中国'])
# print(word_idx_map['中国'])
# print(newword2vector[word_idx_map['中国']])
# print(word_idx_map.keys())


for index,row in content.iterrows():
    # print(index)
    index = int(index)
    if index%1000 ==0:
        print('have finished {} news'.format(index))
    one_news_content = str(row['content']).strip()
    one_news_source = str(row['source']).strip()
    if one_news_content != '' and one_news_source != '':
        one_news_content = one_news_content.strip()
        one_news_content_words = list(jieba.cut(one_news_content))
        for i in range(len(one_news_content_words)):
            if i < max_length-1:
                if one_news_content_words[i] in word_idx_map.keys():
                    # print(one_news_content_words[i])
                    ids[index][i] = word_idx_map[one_news_content_words[i]]
            else:
                continue
        if one_news_source == '新华社':
            ids[index][-1] = 1


ids = ids.astype(int)
np.savetxt('./data_index.csv',ids,delimiter=',',fmt="%.d")























