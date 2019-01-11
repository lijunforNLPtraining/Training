
import os
import  jieba
from sklearn.feature_extraction.text import TfidfVectorizer
import  numpy as np
from functools import  reduce
from  operator import and_
import  re
from scipy.spatial.distance import cosine



file_path = './corpus/all_data.csv'



def cut(string):
    return  ' '.join(jieba.cut(string))

def get_corpus():
    with open(file_path,'r',encoding='utf-8') as f:
        data = f.readlines()
    corpus = []
    for line in data:
        corpus.append(cut(line))
    return corpus,data

def build_tfidf_vector():
    corpus,_ = get_corpus()
    vectorizer = TfidfVectorizer()
    vectorizer.fit_transform(corpus)
    # print(max(vectorizer.vocabulary_.values()))

    tfidf = vectorizer.fit_transform(corpus)
    transposed_tfidf = tfidf.transpose()

    return transposed_tfidf.toarray(),vectorizer,tfidf

def get_word_id(word):
    id= []
    _ ,vectorizer,_ = build_tfidf_vector()
    word_list = word.split(' ')
    for word in word_list:
        id.append(vectorizer.vocabulary_.get(word,None))
    return id

def get_candidates_pat(input_string):
    return '({})'.format('|'.join(cut(input_string).split()))


def get_candidates_ids(input_string):
    return [get_word_id(c) for c in cut(input_string).split()]

def search_enginer(query):
    corpus,data = get_corpus()
    transposed_tfidf,vectorizer,tfidf = build_tfidf_vector()
    candidates_ids = get_word_id(query)#知道检索词语的所有id
    #关于排序，如果不加任何排序操作，那么检索的输出结果就是按照相同部分的索引的顺序，这个肯定不对，所以我们利用检索结果中的文档与输入关键字之间的相似程度
    #来做排序操作，下面的V1就是代表这些检索词语的tf-idf值得向量，向量的维度是（1，num_vocabulary），得到这个向量结果再通过cos计算与每个文档中这些词组成的向量结果，
    #s算余弦就可以得到文本与检索词语之间的相似度，然后排序输出即可
    v1 = vectorizer.transform([cut(query)]).toarray()[0]

    # print(len(v1))
    # k = 0
    # for i in range(len(v1)):
    #     if v1[i] >0:
    #         print(i)
    #     k +=v1[i]
    # print(k)

    candidates = [set(np.where(transposed_tfidf[_id])[0]) for _id in candidates_ids]
    #这里是获得输入检索词语的对应含有词语的文档的id，比如输入含有手术，阑尾2个词，含有手术的文档的索引为[1,2,3,4]，含有阑尾的文档索引为[3,4,5,6],则
    #candidates表示[[1,2,3,4],[3,4,5,6]]

    merged_candidates = reduce(and_,candidates)#通过比较找到两个set中共同元素，也就是找到均包含检索词语的文档索引
    pat = re.compile(get_candidates_pat(query))#这个操作可以在检索结果的关键字上面标注，为了好看，类似百度索引里可以对关键字加粗或者变色的操作

    vector_with_id = [(tfidf[i], i) for i in merged_candidates]#算出检索结果文档的所有itidf矩阵
    sorted_vector_with_ids = sorted(vector_with_id, key=lambda x: cosine(x[0].toarray(), v1))#将检索词组成的向量与检索结果所有的
    #向量矩阵计算夹角的余弦值，再根据余弦值进行排序返回

    sorted_ids = [i for v, i in sorted_vector_with_ids]
    with open('./unsorted.txt','w',encoding='utf-8') as f1:
        for c in sorted_ids:
            print('*' * 10)
            output = pat.sub(repl='**\g<1>**', string=data[c])
            f1.write(' '.join(output.split()))
            print(' '.join(output.split()))

search_enginer('手术 阑尾 腹痛')

    # vector_with_id = [(tfidf[i],i) for i in merged_candidates]
    #
    # sorted_vector_with_ids = sorted(vector_with_id,key = lambda x:cosine(x[0].toarray(),v1))
    #
    # sorted_ids = [i for v,i in sorted_vector_with_ids]



# print(get_word_id('手术 阑尾'))
# transposed_tfidf, vectorizer, tfidf = build_tfidf_vector()
# shoushu = set(np.where(transposed_tfidf[3324])[0])
# lanwei = set(np.where(transposed_tfidf[5916])[0])
#
# retrieval =shoushu & lanwei
# corpus ,data= get_corpus()
# pat = re.compile(get_candidates_pat('手术 阑尾'))
#
# for r in retrieval:
#     print('*'*10)
#     output = pat.sub(repl = '**\g<1>**',string =data[r] )
#     print(' '.join(output.split()))

# with open('./result.txt','w',encoding='utf-8') as f_in:
#     for i,document in enumerate(search_enginer('腹痛 阑尾')):
#         f_in.write(document + '\n')

# print(search_enginer('腹痛 阑尾'))




# transposed_tfidf,vectorizer,tfidf = build_tfidf_vector()
# print(transposed_tfidf.shape)
# print(np.where(vectorizer[6]))