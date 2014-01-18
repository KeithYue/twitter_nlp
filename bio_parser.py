import re
import sys
import os
import subprocess

def ner_extract(tweet):
    ''' Return the BIO format str given a piece of tweet

    tweet: tweet str
    '''

    bio_str = subprocess.check_output(['cat %s |python ./python/ner/extractEntities2.py' % (tweet,),
        '--classify'])
    return bio_str

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

    # get the chunks and their tags
    nes = []
    for entity in ne_tags:
        name, type_name = zip(*entity)[0], zip(*entity)[1]
        name = ' '.join(name)
        type_name = ' '.join(type_name[0].split('-')[1:])
        nes.append((name, type_name))

    return nes


if __name__ == '__main__':
    s = 'Spotted/O :/O Kanye/B-person West/I-person Celebrates/O LAMB/B-product With/O Gwen/B-person Stefani/I-person :/O New/B-other York/I-other Fashion/I-other Week/I-other is/O coming/O to/O a/O close/O ,/O but/O not/O before/O .../O http://bit.ly/cSyZUi/O'

    print ner_extract(s)

