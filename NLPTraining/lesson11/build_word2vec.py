from gensim.models import word2vec
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence


# model_file_name = './news_cutted_words.txt'
# sentences = word2vec.Text8Corpus(model_file_name)
# model = word2vec.Word2Vec(sentences, size=50)
# model.wv.save_word2vec_format( './corpus.model.bin', binary=True)





word2vec_model = Word2Vec(LineSentence('./news_cutted_words.txt'), min_count=10, size=50)
word2vec_model.save('./news_word2vec_model')











