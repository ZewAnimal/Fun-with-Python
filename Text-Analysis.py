import pandas as pd


wordsContainer = []


def calcWords(text):
    words = text.split()
    for word in words:
        addflag = True
        for schema in wordsContainer:
            if schema['word'] == word:
                schema['count'] += 1
                addflag = False
                break
        if addflag:
            d = {'word': word,
                 'count': 1}
            wordsContainer.append(d)


df = pd.read_csv('mydocs_ML_data.csv', dtype='str', encoding='latin1')
df['text'].apply(calcWords)     # create copy dataframe with no whitespace, punctuation, etc
df['char_count'] = df['text'].apply(len)    # improve to strip whitespace, punctuation before calling
df['word_count'] = df['text'].apply(lambda x: len(x.split()))
df['word_density'] = df['char_count'] / (df['word_count']+1)


max = 1
max_word = ''
for item in wordsContainer:
    if item['word'] == 'the':
        continue
    else:
        if item['count'] > max:
            max = item['count']
            max_word = item['word']
