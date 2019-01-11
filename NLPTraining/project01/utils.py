
from pyltp import Segmentor
from pyltp import Postagger
# from pylab import
import pyltp
from pyltp import NamedEntityRecognizer


import os
LTP_DATA_DIR = 'D:\\Eclipse_workplace\\NLPTraining\\project01\\model\\ltp-models'
cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  # 分词模型路径，模型名称为`cws.model`
pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')  # 词性标注模型路径，模型名称为`pos.model`
ner_model_path = os.path.join(LTP_DATA_DIR, 'ner.model')  # 命名实体识别模型路径，模型名称为`pos.model`
par_model_path = os.path.join(LTP_DATA_DIR, 'parser.model')  # 依存句法分析模型路径，模型名称为`parser.model`
# srl_model_path = os.path.join(LTP_DATA_DIR, 'srl')


key_words = ['表示','指出','认为','坦言','看来','透露','介绍','明说','说','强调','所说','提到','说道','称','声称','建议','呼吁',
              '提及','地说','直言','普遍认为','批评','重申','提出','明确指出','觉得','宣称','猜测','特别强调','写道','引用','相信',
              '解释','谈到','深知','称赞','感慨','主张','还称','中称','指责','披露','明确提出','描述','提醒','深有体会','爆料',
              '裁定','宣布']

#分词
def cut(string):
    segmentor = Segmentor()
    segmentor.load(cws_model_path)
    words = segmentor.segment(string)
    # print('\t'.join(words))
    segmentor.release()
    return words

#词性标注模型
def tag(wordlist):
    postagger = Postagger()
    postagger.load(pos_model_path)
    postag_list = list(postagger.postag(wordlist))
    return postag_list


def ner(wordlist,postag_list):
    recognizer = NamedEntityRecognizer()
    recognizer.load(ner_model_path)
    netag_list = list(recognizer.recognize(wordlist,postag_list))
    return netag_list

def parser(words,postags):
    parser = pyltp.Parser()
    parser.load(par_model_path)
    arcs = parser.parse(words,postags)
    print('\t'.join('%d:%s'%(arc.head,arc.relation) for arc in arcs))
    parser.release()
    return arcs

wordlist= cut('王亮说喜欢吃苹果')
print(wordlist[0][0])
for i in range(len(wordlist)):
    print(wordlist[i])
taglist = tag(wordlist)
print(taglist)
a = parser(wordlist,taglist)
# print(a[2:])

#获取主语索引
def get_sbv_id(netags,arcs,key_word_index):
    n = 0
    for i in arcs:
        #这三个名词词性可以代表人名，机构名，我们
        is_person_or_org = 'nh' in netags[n] or 'pronoun' in netags[n] or 'ni' in netags[n]
        if i.head == key_word_index + 1 or i.relation == 'SBV' or is_person_or_org:
            return n
        n +=1
    return None

#获取关键字的索引
def get_keyword_index(wordlist):
    for i in range(len(wordlist)-1):
        if wordlist[i] in key_words:
            return i
    return None




def find_content(word_list,index):
    content = []
    for i in range(index+1,len(word_list)):
        content.append(word_list[i])
    return ''.join(content)

def model(string):
    word_list = cut(string)
    postag_list = tag(word_list)
    netag_list = ner(word_list,postag_list)
    arcs = parser(word_list,postag_list)
    for i in range(len(word_list)):
        if word_list[i] in key_words:
            content = find_content(word_list,i)
            main_index = get_sbv_id(netag_list, arcs, i)
            # print(word_list[main_index])
            # print(word_list[i])
            # print(content)
            print(word_list[main_index],'+',word_list[i],'+',content)




# model('王良说，明天会下冰爆。')






