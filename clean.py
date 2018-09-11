import string
import json
import re
import collections
import nltk
import string
from gensim.models import Word2Vec
from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from collections import Counter


# save list to file
def save_list(tokens, filename):
    # convert tokens to a single blob of text
    data = '\n'.join(tokens) + "\n"
    # open file
    file = open(filename,'a')
    # write text
    file.write(data)
    # close file
    file.close()



def preprocess_text(preprocess_text):
    # Remove punctuation
    exclude = set(string.punctuation)
    preprocess_text = ''.join(ch for ch in preprocess_text if ch not in exclude)                          #
    # preprocess_text = preprocess_text.strip('\'"?!,.():;')
    # Convert more than 2 letter repetitions to 2 letter
    # funnnnny --> funny
    preprocess_text = re.sub(r'(.)\1+', r'\1\1', preprocess_text)
    # Remove - & '
    preprocess_text = re.sub(r'(-|\')', '', preprocess_text)
    # Replaces #hashtag with hashtag
    preprocess_text = re.sub(r'#(\S+)', r' \1 ', preprocess_text)
    # Replace 2+ dots with space
    preprocess_text = re.sub(r'\.{2,}', ' ', preprocess_text)
    # Strip space, " and ' from text
    preprocess_text = preprocess_text.strip(' "\'')
    # Replace @handle with the word USER_MENTION
    preprocess_text = re.sub(r'@[\S]+', 'USER_MENTION', preprocess_text)
    # Replaces URLs with the word URL
    preprocess_text = re.sub(r'((www\.[\S]+)|(https://[\S]+))', ' URL ', preprocess_text)
    # Replace multiple spaces with a single space
    preprocess_text = re.sub(r'\s+', ' ', preprocess_text)
    # removing http/url
    preprocess_text = re.sub(r'http', '', preprocess_text)
    preprocess_text = re.sub(r'url', '', preprocess_text)
    preprocess_text = re.sub(r'ensuffix', '', preprocess_text)
    
    return preprocess_text





def coded_emojis(processed_text):
    
    #--------------------------------
    #--------------\ud83d\ude----------
    
    happy_emoji = re.compile(u"(\ud83d[\ude00-\ude09])" "+", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d[\ude17-\ude19])" "+", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d[\ude42-\ude43])" "+", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d[\ude47-\ude49])" "+", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d[\ude38-\ude39])" "+", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d\ude0a)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d\ude0c)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d\ude0d)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d\ude1a)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d\ude0b)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d\ude1c)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d\ude1d)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d\ude1b)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d\ude0e)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d\ude2c)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d\ude3a)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d\ude3b)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d\ude3c)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d\ude3d)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d\ude4b)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d\ude4e)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d\ude4a)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d\ude47\u200d\u2640)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d\ude46\u200d\u2642)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d\ude4b\u200d\u2642)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d\ude4e\u200d\u2642)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d\udeb4\u200d\u2640)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d\udeb5\u200d\u2640)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d\udeb5\u200d\u2640)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    
    #----------------
    
    sad_emoji = re.compile(u"(\ud83d[\ude13-\ude16])" "+", flags=re.UNICODE)
    processed_text = sad_emoji.sub(r' EMO_NEG ', processed_text)
    
    sad_emoji = re.compile(u"(\ud83d[\ude10-\ude12])" "+", flags=re.UNICODE)
    processed_text = sad_emoji.sub(r' EMO_NEG ', processed_text)
    
    sad_emoji = re.compile(u"(\ud83d[\ude20-\ude37])" "+", flags=re.UNICODE)
    processed_text = sad_emoji.sub(r' EMO_NEG ', processed_text)
    
    sad_emoji = re.compile(u"(\ud83d[\ude40-\ude41])" "+", flags=re.UNICODE)
    processed_text = sad_emoji.sub(r' EMO_NEG ', processed_text)
    
    sad_emoji = re.compile(u"(\ud83d[\ude44-\ude45])" "+", flags=re.UNICODE)
    processed_text = sad_emoji.sub(r' EMO_NEG ', processed_text)
    
    sad_emoji = re.compile(u"(\ud83d\ude4d\u200d\u2642)", flags=re.UNICODE)
    processed_text = sad_emoji.sub(r' EMO_NEG ', processed_text)
    
    sad_emoji = re.compile(u"(\ud83d\ude0f)", flags=re.UNICODE)
    processed_text = sad_emoji.sub(r' EMO_NEG ', processed_text)
    
    sad_emoji = re.compile(u"(\ud83d\ude1e)", flags=re.UNICODE)
    processed_text = sad_emoji.sub(r' EMO_NEG ', processed_text)
    
    sad_emoji = re.compile(u"(\ud83d\ude1f)", flags=re.UNICODE)
    processed_text = sad_emoji.sub(r' EMO_NEG ', processed_text)
    
    sad_emoji = re.compile(u"(\ud83d\ude2b)", flags=re.UNICODE)
    processed_text = sad_emoji.sub(r' EMO_NEG ', processed_text)
    
    sad_emoji = re.compile(u"(\ud83d\ude2f)", flags=re.UNICODE)
    processed_text = sad_emoji.sub(r' EMO_NEG ', processed_text)
    
    sad_emoji = re.compile(u"(\ud83d\ude2e)", flags=re.UNICODE)
    processed_text = sad_emoji.sub(r' EMO_NEG ', processed_text)
    
    sad_emoji = re.compile(u"(\ud83d\ude3f)", flags=re.UNICODE)
    processed_text = sad_emoji.sub(r' EMO_NEG ', processed_text)
    
    sad_emoji = re.compile(u"(\ud83d\ude2d)", flags=re.UNICODE)
    processed_text = sad_emoji.sub(r' EMO_NEG ', processed_text)
    
    sad_emoji = re.compile(u"(\ud83d\ude2a)", flags=re.UNICODE)
    processed_text = sad_emoji.sub(r' EMO_NEG ', processed_text)
    
    sad_emoji = re.compile(u"(\ud83d\ude3e)", flags=re.UNICODE)
    processed_text = sad_emoji.sub(r' EMO_NEG ', processed_text)
    
    
    #------------------------------
    #--------------\ud83e\udd----------
    
    
    happy_emoji = re.compile(u"(\ud83e[\udd16-\udd19])" "+", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83e[\udd20-\udd21])" "+", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83e[\udd23-\udd24])" "+", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83e[\udd33-\udd36])" "+", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83e\udd11)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83e\udd13)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83e\udd1e)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83e\udd1d)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83e\udd1a)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83e\udd30)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83e\udd81)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83e\udd84)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83e\udd8b)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    
    
    #--------
    
    
    sad_emoji = re.compile(u"(\ud83e[\udd14-\udd15])" "+", flags=re.UNICODE)
    processed_text = sad_emoji.sub(r' EMO_NEG ', processed_text)
    
    sad_emoji = re.compile(u"(\ud83e[\udd47-\udd49])" "+", flags=re.UNICODE)
    processed_text = sad_emoji.sub(r' EMO_NEG ', processed_text)
    
    sad_emoji = re.compile(u"(\ud83e[\udd24-\udd25])" "+", flags=re.UNICODE)
    processed_text = sad_emoji.sub(r' EMO_NEG ', processed_text)
    
    sad_emoji = re.compile(u"(\ud83e[\udd90-\udd91])" "+", flags=re.UNICODE)
    processed_text = sad_emoji.sub(r' EMO_NEG ', processed_text)
    
    sad_emoji = re.compile(u"(\ud83e[\udd87-\udd89])" "+", flags=re.UNICODE)
    processed_text = sad_emoji.sub(r' EMO_NEG ', processed_text)
    
    sad_emoji = re.compile(u"(\ud83e\udd26\u200d\u2640)", flags=re.UNICODE)
    processed_text = sad_emoji.sub(r' EMO_NEG ', processed_text)
    
    sad_emoji = re.compile(u"(\ud83e\udd26\u200d\u2642)", flags=re.UNICODE)
    processed_text = sad_emoji.sub(r' EMO_NEG ', processed_text)
    
    sad_emoji = re.compile(u"(\ud83e\udd37\u200d\u2640)", flags=re.UNICODE)
    processed_text = sad_emoji.sub(r' EMO_NEG ', processed_text)
    
    sad_emoji = re.compile(u"(\ud83e\udd37\u200d\u2642)", flags=re.UNICODE)
    processed_text = sad_emoji.sub(r' EMO_NEG ', processed_text)
    
    sad_emoji = re.compile(u"(\ud83e\udd10)", flags=re.UNICODE)
    processed_text = sad_emoji.sub(r' EMO_NEG ', processed_text)
    
    sad_emoji = re.compile(u"(\ud83e\udd22)", flags=re.UNICODE)
    processed_text = sad_emoji.sub(r' EMO_NEG ', processed_text)
    
    sad_emoji = re.compile(u"(\ud83e\udd27)", flags=re.UNICODE)
    processed_text = sad_emoji.sub(r' EMO_NEG ', processed_text)
    
    sad_emoji = re.compile(u"(\ud83e\udd12)", flags=re.UNICODE)
    processed_text = sad_emoji.sub(r' EMO_NEG ', processed_text)
    
    sad_emoji = re.compile(u"(\ud83e\udd1b)", flags=re.UNICODE)
    processed_text = sad_emoji.sub(r' EMO_NEG ', processed_text)
    
    sad_emoji = re.compile(u"(\ud83e\udd1c)", flags=re.UNICODE)
    processed_text = sad_emoji.sub(r' EMO_NEG ', processed_text)
    
    sad_emoji = re.compile(u"(\ud83e\udd8a)", flags=re.UNICODE)
    processed_text = sad_emoji.sub(r' EMO_NEG ', processed_text)
    
    sad_emoji = re.compile(u"(\ud83e\udd8c)", flags=re.UNICODE)
    processed_text = sad_emoji.sub(r' EMO_NEG ', processed_text)
    
    sad_emoji = re.compile(u"(\ud83e\udd8e)", flags=re.UNICODE)
    processed_text = sad_emoji.sub(r' EMO_NEG ', processed_text)
    
    sad_emoji = re.compile(u"(\ud83e\udd82)", flags=re.UNICODE)
    processed_text = sad_emoji.sub(r' EMO_NEG ', processed_text)
    
    sad_emoji = re.compile(u"(\ud83e\udd80)", flags=re.UNICODE)
    processed_text = sad_emoji.sub(r' EMO_NEG ', processed_text)
    
    #-----------------------------------------
    #--------------\u263a\----
    
    happy_emoji = re.compile(u"(\u263a\ufe0f)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    #-----------------------------------------
    #--------------\u2639\----
    
    sad_emoji = re.compile(u"(\u2639\ufe0f)", flags=re.UNICODE)
    processed_text = sad_emoji.sub(r' EMO_NEG ', processed_text)
    
    #-----------------------------------------
    #--------------\ud83d\udc----
    
    
    happy_emoji = re.compile(u"(\ud83d\udc4f)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d\udc4d)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d\udc4c)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d\udc4b)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d\udcaa)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d\udc85)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d\udc8d)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d\udc84)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d\udc8b)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d\udc44)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d\udc76)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d\udc78)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d\udc70)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d\udc7c)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d\udc83)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d\udc6f)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d\udc6f\u200d\u2642)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d\udc6b)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d\udc6d)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    
    happy_emoji = re.compile(u"(\ud83d\udc91)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d\udc69\u200d\u2764\ufe0f\u200d\ud83d\udc69)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d\udc68\u200d\u2764\ufe0f\u200d\ud83d\udc68)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d\udc8f)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d\udc69\u200d\u2764\ufe0f\u200d\ud83d\udc8b\u200d\ud83d\udc69)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d\udc68\u200d\u2764\ufe0f\u200d\ud83d\udc8b\u200d\ud83d\udc68)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d\udc6a)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d\udc68\u200d\ud83d\udc69\u200d\ud83d\udc67)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d\udc68\u200d\ud83d\udc69\u200d\ud83d\udc67\u200d\ud83d\udc66)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d\udc68\u200d\ud83d\udc69\u200d\ud83d\udc66\u200d\ud83d\udc66)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d\udc68\u200d\ud83d\udc69\u200d\ud83d\udc67\u200d\ud83d\udc67)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d\udc69\u200d\ud83d\udc69\u200d\ud83d\udc66)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    happy_emoji = re.compile(u"(\ud83d\udc69\u200d\ud83d\udc69\u200d\ud83d\udc67)", flags=re.UNICODE)
    processed_text = happy_emoji.sub(r' EMO_POS ', processed_text)
    
    #------------------
    
    sad_emoji = re.compile(u"(\ud83d\udc45)", flags=re.UNICODE)
    processed_text = sad_emoji.sub(r' EMO_NEG ', processed_text)
    
    sad_emoji = re.compile(u"(\ud83d\udc79)", flags=re.UNICODE)
    processed_text = sad_emoji.sub(r' EMO_NEG ', processed_text)
    
    sad_emoji = re.compile(u"(\ud83d\udc7a)", flags=re.UNICODE)
    processed_text = sad_emoji.sub(r' EMO_NEG ', processed_text)
    
    sad_emoji = re.compile(u"(\ud83d\udca9)", flags=re.UNICODE)
    processed_text = sad_emoji.sub(r' EMO_NEG ', processed_text)
    
    sad_emoji = re.compile(u"(\ud83d\udc7b)", flags=re.UNICODE)
    processed_text = sad_emoji.sub(r' EMO_NEG ', processed_text)
    
    sad_emoji = re.compile(u"(\ud83d\udc80)", flags=re.UNICODE)
    processed_text = sad_emoji.sub(r' EMO_NEG ', processed_text)
    
    sad_emoji = re.compile(u"(\ud83d\udc7d)", flags=re.UNICODE)
    processed_text = sad_emoji.sub(r' EMO_NEG ', processed_text)
    
    sad_emoji = re.compile(u"(\ud83d\udc7e)", flags=re.UNICODE)
    processed_text = sad_emoji.sub(r' EMO_NEG ', processed_text)
    
    sad_emoji = re.compile(u"(\ud83d\udc4e)", flags=re.UNICODE)
    processed_text = sad_emoji.sub(r' EMO_NEG ', processed_text)
    
    sad_emoji = re.compile(u"(\ud83d\udc4a)", flags=re.UNICODE)
    processed_text = sad_emoji.sub(r' EMO_NEG ', processed_text)
    
    
    return processed_text



def handle_emojis(text):
    
    # shock_emoji = re.compile("[" u"\ud83d\ude31" "]+", flags=re.UNICODE)
    # text = emoji_pattern.sub(r' EMO_NEG ', text)
    # Smile -- :), : ), :-), (:, ( :, (-:, :')
    text = re.sub(r'(:\)|:-\)|\(\s:|\(-:|:\'\))', ' EMO_POS ', text)
    # Laugh -- :D, : D, :-D, xD, x-D, XD, X-D, :-d, :d
    text = re.sub(r'(:D|:-D|x-D|X-D|:-d|:d)', ' EMO_POS ', text)
    # Love -- <3, :*
    text = re.sub(r'(<3|:\*)', ' EMO_POS ', text)
    # Wink -- ;-), ;), ;-D, ;D, (;,  (-;
    text = re.sub(r'(;-\)|;-D|\(-;)', ' EMO_POS ', text)
    # Sad -- :-(, : (, :(, ):, )-:, -_-
    text = re.sub(r'(:\(|:-\(|\)\s:|\)-:|-_-)', ' EMO_NEG ', text)
    # Cry -- :,(, :'(, :"(
    text = re.sub(r'(:,\(|:\'\(|:"\()', ' EMO_NEG ', text)
    # Shout -- :@
    text = re.sub(r'(:\@)', ' EMO_NEG ' , text)
    text = coded_emojis(text)
    
    return text



def build_vocab(text):
    try:
        # split into tokens by white space
        # tokens = text.split()
        lower_text = text.lower()
        # turn a doc into clean tokens
        processed_text = handle_emojis(lower_text)
        final_text = preprocess_text(processed_text)
        #tokenize
        tokenizer = RegexpTokenizer(r'\w+')
        tokens = tokenizer.tokenize(final_text)
        # remove remaining tokens that are not alphabetic
        tokens = [word for word in tokens if word.isalpha()]
        # filter out stop words
        stop_words = set(stopwords.words('english'))
        tokens = [w for w in tokens if not w in stop_words]
        
        # write to txt file
        save_list(tokens, 'testvocab.txt')
    
    except Exception as inst:
        print inst
        pass

# load the document

with open('HN-EN_train.json') as json_data:
    d = json.load(json_data)

for text in d:
    text = text["text"]
    tokens = build_vocab(text)

