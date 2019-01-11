
import re
import sys
import codecs
import jieba
from project01.utils import model
key_words = ['表示','指出','认为','坦言','看来','透露','介绍','明说','说','强调','所说','提到','说道','称','声称','建议','呼吁',
              '提及','地说','直言','普遍认为','批评','重申','提出','明确指出','觉得','宣称','猜测','特别强调','写道','引用','相信',
              '解释','谈到','深知','称赞','感慨','主张','还称','中称','指责','披露','明确提出','描述','提醒','深有体会','爆料',
              '裁定','宣布']

def split_sentence(text):
    text = text.replace('\n', '')
    # print(text[:2])
    sentences = re.split('(。|!|\!|\.|？|\?)', text)  #这里按照代表一句话结束的标点符号将文章划分为
    #一个个的句子
    new_sents = []
    # print('text',len(sentences))
    for i in range(int(len(sentences)/2)):
        sent = sentences[2*i] + sentences[2*i + 1]
        #这里比较巧妙，按照上面的划分，有多少个句子，就有多少个对应的标点符号，所以这样就可以取到所有的完整句子
        #实在搞不懂的话自己写一小段来测试就明白了
        new_sents.append(sent)
    print(len(new_sents))
    return new_sents

def get_target_sentence(sentences,keywords):
    target_sentences = []
    for sentence in sentences:
        words = jieba.cut(sentence)
        if len([word for word in words if word in keywords]):
            target_sentences.append(sentence)
    return target_sentences


with open('./news_content.txt','r',encoding='utf-8') as f_read:
    news_content = f_read.read()
    print(len(news_content))

target_sentences = get_target_sentence(split_sentence(news_content),key_words)
for i in range(20):
    print(model(target_sentences[i]))
# print(target_sentences[:5])
































































