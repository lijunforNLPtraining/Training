

from project02.tool import get_sentences_vec,word_freq,get_model_from_file,get_sent_vec_sims
import jieba
import random
import matplotlib.pyplot as plt
import itertools
import numpy as np


def plot_confusion_matrix(cm, classes, title='Confusion matrix'):
    plt.imshow(cm, interpolation='nearest', cmap=None)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=0)
    plt.yticks(tick_marks, classes)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.show()

def plot_matrix(y_true, y_pred):
    from sklearn.metrics import confusion_matrix
    confusion_matrix = confusion_matrix(y_true, y_pred)
    class_names = ['positive', 'negative']
    plot_confusion_matrix(confusion_matrix
                          , classes=class_names
                          , title='Confusion matrix')



get_word_frequency = word_freq('./txt_for_build_world2vec.txt')

word2vector = get_model_from_file('./word2vec_model')

with open('./positive.txt','r',encoding='utf-8') as f_positive:
    positive = f_positive.readlines()
f_positive.close()
with open('./negative.txt','r',encoding='utf-8') as f_negative:
    negative = f_negative.readlines()
f_negative.close()

# a  = random.sample(positive, 10)
# print(len(a))
# print(a[:3])

with open('./liver_test_data.csv','r',encoding='utf-8') as f_data:
    testdataSet = f_data.readlines()
f_data.close()
print(len(testdataSet))
with open('./liver_test_label.csv','r',encoding='utf-8') as f_label:
    testlabel = f_label.readlines()
f_label.close()
print(len(testlabel))




true_label = []
predict_lable = []
num_samples = 20
for i in range(len(testdataSet)):
    one_test_input = testdataSet[i]
    one_test_label = int(testlabel[i].split('\t')[0])
    if one_test_label > 0:
        one_test_label = 1
    else:
        one_test_label = 0
    true_label.append(one_test_label)
    #计算和健康样本的余弦相似度
    positive_sentences_list = []
    ten_positive = random.sample(positive, num_samples)
    tmep_list = []
    positive_sentences_list.append(list(jieba.cut(str(one_test_input))))
    for sentence in ten_positive:
        positive_sentences_list.append(list(jieba.cut(str(sentence))))
    positive_sentences = get_sentences_vec(word2vector,positive_sentences_list,get_word_frequency)
    sims_positive = get_sent_vec_sims(positive_sentences)

    #计算患病样本的余弦相似度
    negative_sentences_list = []
    ten_negative = random.sample(negative, num_samples)
    tmep_list = []
    negative_sentences_list.append(list(jieba.cut(str(one_test_input))))
    for sentence in ten_negative:
        negative_sentences_list.append(list(jieba.cut(str(sentence))))
    negative_sentences = get_sentences_vec(word2vector, negative_sentences_list, get_word_frequency)
    sims_negative = get_sent_vec_sims(negative_sentences)
    if sims_negative < sims_positive:
        result = 0
        print('第{}个样本实际label是 {},预测结果是:{}'.format(i,one_test_label,result))
    else:
        result = 1
        print('第{}个样本实际label是 {},预测结果是:{}'.format(i,one_test_label,result))
    predict_lable.append(result)
plot_matrix(true_label,predict_lable)










