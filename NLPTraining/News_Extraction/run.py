
from News_Extraction.ltp_tool import sentence_embedding,LTP
from gensim.models import Word2Vec


ltp = LTP()
model = Word2Vec.load('./final_model')
sentence_embedding = sentence_embedding(model,'./words.txt',0.001)


# result = open('./news_extraction.csv','w',encoding='utf-8')


line = '李连杰突然宣布，波兰国家安全局当天逮捕了一名中国公民和一名波兰公民，' \
       '指控他们从事间谍活动。随后，波兰媒体披露，被捕中国籍高管名叫Weijing Wu，是华为在波兰分' \
       '公司负责销售的管理人员，而波兰工程师 Piotr D，曾是就职国家安全局的高官。西方媒体普遍添加的一' \
       '个背景是， 这是华为CFO孟晚舟被加拿大方面拘押后，第二位华为高管在外国被逮捕。这一次， 罪名更加严重，间谍罪！'
line = str(line.strip())
wordslist = ltp.cut(line)
keywords_index, postags, arcs = ltp.get_dependtree_root_index(wordslist)
print(keywords_index)
keyword = wordslist[keywords_index]
main_index = ltp.get_sbv_id(postags, arcs,keywords_index)
main = wordslist[main_index]
content = ltp.find_content(wordslist,keywords_index)
# sentences = ltp.keyword_senteces(wordslist,postags,keywords_index)
# content = sentence_embedding.get_final_sents(sentences)
# result.write(str(main) + '-->' + str(keyword) + '-->' + str(content))
print(str(main) + '-->' + str(keyword) + '-->' + str(content))























