from champs_desc_dict import CHAMPS_DESC
import re
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

stopwords = set(STOPWORDS)
stopwords.update(['now','new','the'])
champ_desc = CHAMPS_DESC

def cleaner():
    str = ''
    count = 0
    for count in range(len(champ_desc['desc'])):
        str = str + ' ' + champ_desc['desc'][count]

    words = re.split(r'\W+',str)
    newWords = map(lambda x: x.lower(),words)
    newWords = list(newWords)
    text = " ".join(newWords)
    return text

def gen(text):
    wordcloud = WordCloud(stopwords=stopwords,max_words=150, background_color="white",max_font_size=50,width=500, height=400).generate(text)
    plt.imshow(wordcloud,interpolation='bilinear')
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    gen(cleaner())
