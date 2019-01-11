
import pandas as pd
import math

content = pd.read_csv('./sqlResult_1558435.csv',encoding='gb18030')
content = content.fillna('')
all_news = content['content']
import jieba
def cut(string):
    return list(jieba.cut(string))

def TF(term, cutted_passage):
    all_count = len(cutted_passage)
    return cutted_passage.count(term)/all_count
all_occurences = []
for c in all_news:
    all_occurences.append(cut(c))
D = len(all_occurences)

def idf(term):
    term_count = 0
    for passage_terms in all_occurences:
        if term in passage_terms:
            term_count +=1
    eps = 1e-6
    term_count += eps
    return math.log10(D/term_count)

def tf_idf(term,cutted_passage):
    return TF(term,cutted_passage)*idf(term)

import re
corpus_list = []
for index, row in content:
    corpus_list.append(cut(''.join(re.findall(r'[\w\d]+',row['content']))))
print(len(corpus_list))
print(corpus_list[:10])
with open('./all_news_words.txt','w',encoding='utf-8') as f_write:
    f_write.write(' '.join(corpus_list))











#这里是根据不同Word2vector模型采取认为控制权重的方式寻找相关词，方法比较值得学习
from collections import defaultdict
def graph_search_tune(init_word, model, limit_rate=0.7):
    max_size = 1000
    seen = defaultdict(int)
    need_seen = [init_word]
    n = 0

    while need_seen and len(seen) < max_size:
        if n % 1000 == 0:
            print('had run counts:{}'.format(n))
        if n > 5000:
            break
        node = need_seen.pop(0)
        new_words = [
            w for w, p in model.wv.most_similar(node, topn=15)
            if p > limit_rate
        ]
        need_seen += new_words
        seen[node] += 1
        n += 1

    return seen
# 通过加权的方式合并
def merge_model(news_rate, wiki_rate, news_word2vec_model,wiki_word2vec_model,topn=50):
    combine_similar = defaultdict(int)

    news_update_similar = graph_search_tune('说', news_word2vec_model)
    # 由于wiki中词汇较多，因此对概率限制更严格
    wiki_update_similar = graph_search_tune('说', wiki_word2vec_model, 0.83)

    for key in news_update_similar:
        combine_similar[key] = news_update_similar[
                                   key] * news_rate + wiki_update_similar[key] * wiki_rate

    result = sorted(combine_similar.items(), key=lambda x: x[1], reverse=True)
    return result[:topn]












