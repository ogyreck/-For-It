import re
import nltk
import string


from nltk.tokenize import sent_tokenize
from collections import defaultdict
import pymorphy2

morph = pymorphy2.MorphAnalyzer()
nltk.download('stopwords')


frequency = {}
document_text = open('data.txt', 'r')
text_string = document_text.read().lower()











stop_words = set(nltk.corpus.stopwords.words('english'))
#устанавливаем словарь русских стоп-слов и выводим его


tmp = text_string.split()

filtred = ''

for i in range(0,len(tmp)):
    #обрабатываем список слов при помощи цикла
    if not tmp[i] in stop_words:
        #записываем слово в переменную filtred, если оно не находитя в словаре стоп-слов
        filtred = filtred + tmp[i]+ " "

match_pattern = re.findall(r"\b[a-z]{3,15}\b", filtred)

for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1

names_top_10 = sorted(frequency.items(),
                      key=lambda name_and_count: name_and_count[1],
                      reverse=True)[:10]

print(names_top_10)

word_itoge = []

for word_c in names_top_10:
    word_itoge.append(word_c[0])
#--------------------------------------------------



def get_book_text(path_to_file):
    with open(path_to_file, encoding='utf-8') as opened_file:
        text = opened_file.read()
    return text

book_file_name = 'data.txt'
book_text = get_book_text(book_file_name) #str

key_words_contexts = defaultdict(list)

def lemmatize_words_list(words_list):
    words_lemmas = []
    for word in words_list:
        lemma = morph.parse(word)[0].normal_form
        words_lemmas.append(lemma)
    return words_lemmas

key_word = lemmatize_words_list(word_itoge)