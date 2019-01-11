
import re
import sys
import codecs
import jieba
import hanziconv
import time
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

#繁体转中文
def tradition_to_simplify(input_file, out_file_name):
    i = 1
    outfile = codecs.open(out_file_name, 'w', 'utf-8')
    with codecs.open(input_file, 'r', 'utf-8') as myfile:
        for line in myfile:
            if i % 100 == 0:
                print('finished {} line'.format(i))
            i += 1
            outfile.write(hanziconv.HanziConv.toSimplified(line))
    outfile.close()


#去掉一些没有关系的东西
def filter_symbols(input_file, out_file_name):
    i = 0
    p1 = re.compile('（）')
    p2 = re.compile('《》')
    p3 = re.compile('「')
    p4 = re.compile('」')
    p5 = re.compile('<doc (.*)>')
    p6 = re.compile('</doc>')
    outfile = codecs.open(out_file_name, 'w', 'utf-8')
    with codecs.open(input_file, 'r', 'utf-8') as myfile:
        for line in myfile:
            if i%1000 == 0:
                print('finished {} line'.format(i))
            i +=1
            line = p1.sub('', line)
            line = p2.sub('', line)
            line = p3.sub('', line)
            line = p4.sub('', line)
            line = p5.sub('', line)
            line = p6.sub('', line)
            outfile.write(line)
    outfile.close()



# oldfile_names = ['./wiki_00','./wiki_01','./wiki_02']
# new_filename = './new_filename.txt'
# final_name = './final.txt'
# filter_symbols(new_filename,final_name)
# for name in oldfile_names:
#     tradition_to_simplify(name,new_filename)
#     print('finished one file')

def write_token_to_file(input_file, output_file):
    file = open(input_file,encoding='utf8')
    for line in file:
        w = list(jieba.cut(line.strip()))
#         使用writelines一次写入，由于一次性加载文件过大导致内存耗尽，改用write多次写入
        output_file.write(' '.join(w)+'\n')

def build_gensim(file_path):
    word2vec_model = Word2Vec(LineSentence(file_path), min_count=10, size=50)
    word2vec_model.save('./wiki_word2vec_model')
    return  word2vec_model


# start = time.time()
# with open('./wiki_words.txt','w',encoding='utf-8') as f_write:
#     write_token_to_file('./final.txt',f_write)
#     end = time.time()
#     print('have been happed {}'.format(end-start))
#     f_write.close()


word2vec_model = build_gensim('./wiki_words.txt')
# print(word2vec_model.wv['数学'])
# print(word2vec_model.most_similar('数学'))
































