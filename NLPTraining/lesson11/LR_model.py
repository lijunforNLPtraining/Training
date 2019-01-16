
import pandas as pd
from sklearn.cross_validation import train_test_split
from gensim.models import Word2Vec
import numpy as np
import matplotlib.pyplot as plt
import itertools
import pickle as pickle


D = 50

def all_data(filename):
    data = pd.read_csv(filename)
    X = data.loc[:, data.columns != 'Class']
    y = data.loc[:, data.columns == 'Class']
    return X,y

def splitdata(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y , test_size=0.2,random_state=0)
    X_train = np.array(X_train)
    X_test = np.array(X_test)
    y_train = np.array(y_train)
    y_test = np.array(y_test)
    return X_train, X_test, y_train, y_test

def get_model_from_file(filename):
    model = Word2Vec.load(filename)
    return model

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

def get_tran_word2vec(modelpath,wordspath):
    D = 50
    model = get_model_from_file(modelpath)
    vocab = Wordlist(wordspath)
    w2v = load_vec(vocab.voc, model)
    newword2vector, _ = get_W(w2v, D)
    return newword2vector



newword2vector = get_tran_word2vec('./news_word2vec_model','./oneword_oneline_words.txt')

X,y = all_data('./data_index.csv')
X = np.array(X)
y = np.array(y)
print(X.shape)
print(y.shape)
print(X[1].shape)
print(newword2vector[X].shape)









