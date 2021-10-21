import os
import pyramid.httpexceptions as exc
from functools import cache
import requests
from pyramid.view import view_config
from googletrans import Translator
from gtts import gTTS
from explainer.nouns import NounDictionary


class ExplainerViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='index', renderer='explainer:templates/index.jinja2')
    def index(self):
        return {
            'project': 'Explainer',
        }

    @view_config(route_name='keyword', renderer='explainer:templates/word.jinja2')
    def keyword_page(self):
        #import pdb; pdb.set_trace()
        word = self.request.matchdict['keyword'].capitalize()
        #say_it(word)
        # import pdb; pdb.set_trace()
        return {
            'word': word,
            'en_word': translation(word),
            'google': get_google_contents(word),
            'project': 'Explainer',
            'singular_plural': get_singular_plural(word),
            'singular_declination': get_singular_declination(word),
            'sentences': get_sentences(word),
        }

    @view_config(route_name='post', renderer='explainer:templates/word.jinja2')
    def post_page(self):
        word = self.request.params.get('word', 'Nichts')  # self.request.matchdict['word']
        import pdb; pdb.set_trace()
        raise exc.HTTPFound(self.request.route_url("keyword", keyword=word.lower()))


def translation(word):
    translator = Translator()
    res = translator.translate(word, dest='en', src='de')
    return res.text


def say_it(word):
    # speech = gTTS('der Zug, die Züge', lang='de', slow=True)
    to_say = get_singular_plural(word)
    speech = gTTS(to_say, lang='de', slow=False)
    speech.save("text.mp3")
    os.system("mplayer text.mp3")

def get_google_contents(word):
    headers = {'User-agent': 'Chrome'}
    url = 'https://www.google.com/search?q=%s&tbm=isch' % word
    response  = requests.get(url, headers = headers)
    
    html_file = open("explainer/static/google/%s.html" % word,"w")
    html_file.write(response.text)
    html_file.close()

    return response.text


def get_sentences(word):
    # curl -X GET "http://api.corpora.uni-leipzig.de/ws/sentences/deu_news_2012_1M/sentences/Tisch?limit=10" -H "accept: application/json"
    headers = {'Accept': 'application/json'}
    url = "http://api.corpora.uni-leipzig.de/ws/sentences/deu_news_2012_1M/sentences/%s?limit=10" % word
    response  = requests.get(url, headers = headers).json()
    sentences = [
        element['sentence']
        for element in response['sentences']
    ]
    return set(sentences)


NOUN_GENUS = {
    'm': 'der',
    'f': 'die',
    'n': 'das',
}

@cache
def get_nouns():
    nouns = NounDictionary('explainer/nouns/nouns.csv')
    return nouns

@cache
def get_word_forms(word):
    nouns = get_nouns()
    word_entry = nouns[word][0]
    return word_entry

def get_singular_plural(word):
    #import pdb; pdb.set_trace()
    word_forms = get_word_forms(word)
    artikel = NOUN_GENUS[word_forms['genus']]
    singular = word_forms['flexion']['nominativ singular']
    plural = word_forms['flexion']['nominativ plural']
    result = f"{artikel} {singular}, die {plural}"

    return result

DECLINATION = {
    'der': {
        'genitiv': 'des',
        'dativ': 'dem',
        'akkusativ': 'den',
    }, 
    'die': {
        'genitiv': 'der',
        'dativ': 'der',
        'akkusativ': 'die',
    },
    'das': {
        'genitiv': 'des',
        'dativ': 'dem',
        'akkusativ': 'das',
    },
}


def get_singular_declination(word):
    word_forms = get_word_forms(word)
    artikel = NOUN_GENUS[word_forms['genus']]
    
    nominativ = artikel + ' ' + word_forms['flexion']['nominativ singular']
    genitiv = DECLINATION[artikel]['genitiv'] + ' ' + word_forms['flexion']['genitiv singular']
    if word_forms['flexion'].get('genitiv singular*'):
        genitiv = genitiv + ' (' + word_forms['flexion']['genitiv singular*'] + ')'
    dativ = DECLINATION[artikel]['dativ'] + ' ' + word_forms['flexion']['dativ singular']
    akkusativ = DECLINATION[artikel]['akkusativ'] + ' ' + word_forms['flexion']['akkusativ singular']
    
    result = f"{nominativ}, {genitiv}, {dativ}, {akkusativ}"

    return result
# [
#   {'flexion': {
#     'nominativ singular': 'Fahrrad', 
#     'nominativ plural': 'Fahrräder', 
#     'genitiv singular': 'Fahrrades', 
#     'genitiv singular*': 'Fahrrads', 
#     'genitiv plural': 'Fahrräder', 
#     'dativ singular': 'Fahrrad', 
#     'dativ singular*': 'Fahrrade', 
#     'dativ plural': 'Fahrrädern', 
#     'akkusativ singular': 'Fahrrad', 
#     'akkusativ plural': 'Fahrräder'
#   }, 
#      'lemma': 'Fahrrad', 
#      'pos': ['Substantiv'], 
#      'genus': 'n'
#   }
# ]






