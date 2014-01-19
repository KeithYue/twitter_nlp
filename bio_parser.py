import re
import sys
import os
import subprocess

def ner_extract(tweet):
    ''' Return the BIO format str given a piece of tweet

    tweet: tweet str
    '''

    # subprocess.call(['export', 'TWITTER_NLP=./'], shell=True)
    ner_extration_popen = subprocess.Popen(args="echo '%s' | python $TWITTER_NLP/python/ner/extractEntities2.py --classify" % tweet, shell=True, stdout = subprocess.PIPE, stderr=subprocess.PIPE)

    bio_str, return_code = ner_extration_popen.communicate()
    print return_code

    return bio_parse(bio_str)


def bio_parse(sent):
    ''' Tokenize a sentence of conll 2002 format, return list of (entity, type)

    sent: the conll 2002 format sentences
    '''
    tokens = sent.strip().split(' ')
    tags = [('/'.join(token.split('/')[0:-1]), token.split('/')[-1]) for token in tokens]

    ne_tags = [] # tuple (word, type)
    current_ne = []
    # print tags
    # filter the tags
    for word, ne_type in tags:
        if ne_type == 'O':
            continue
        elif ne_type.startswith('B'):
            # new entity
            # add previous entity to ne_tags
            if current_ne != []:
                ne_tags.append(current_ne)
            # remove the content in current ne tag
            current_ne = []
            current_ne.append((word, ne_type))
        else:
            # The type is I
            current_ne.append((word, ne_type))
    # add the last ne to netags
    if current_ne != []:
        ne_tags.append(current_ne)
    # print ne_tags

    # get the chunks and their tags
    nes = []
    for entity in ne_tags:
        name, type_name = zip(*entity)[0], zip(*entity)[1]
        name = ' '.join(name)
        type_name = ' '.join(type_name[0].split('-')[1:])
        nes.append((name, type_name))

    return nes


if __name__ == '__main__':
    s = '''I/O posted/O 5/O photos/O on/O Facebook/B-company in/O the/O album/O "/O VersusSport/B-facility Event/I-facility -/O Carmelo/B-person vs/O ./O Kobe/O ":/O http://bit.ly/fw9wm/O'''

    print bio_parse(s)


