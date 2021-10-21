https://github.com/digitapex/DerDieDas/blob/master/app/src/main/res/raw/list_nouns.txt

from googletrans import Translator

translator = Translator()

res = translator.translate('Tisch')
res.text



##########
import os
from gtts import gTTS
# speech = gTTS('der Zug, die Züge', lang='de', slow=True)
speech = gTTS('der Zug, die Züge', lang='de', slow=False)
speech.save("text.mp3")
os.system("mplayer text.mp3")


##############
http://api.corpora.uni-leipzig.de/ws/swagger-ui.html#/word-service
https://www.programmableweb.com/api/wortschatz


from libleipzig import * # might take some time initially
>>> r = Baseform(u"Schlangen")
>>> r # doctest: +NORMALIZE_WHITESPACE
[(Grundform: u'Schlange', Wortart: u'N'),
 (Grundform: u'Schlangen', Wortart: u'S')]
>>> r[0].Grundform
u'Schlange'
>>> help(Baseform) # doctest: +NORMALIZE_WHITESPACE
Help on function Baseform in module libleipzig.protocol:
Baseform(*vectors, **options)
    Baseform(Wort) -> Grundform, Wortart
        Return the lemmatized (base) form.




http://api.corpora.uni-leipzig.de/ws

curl -X GET "http://api.corpora.uni-leipzig.de/ws/sentences/deu_news_2012_1M/sentences/Tisch?limit=10" -H "accept: application/json"



export VENV=~/workspace/words/env/
python3 -m venv $VENV
$VENV/bin/pip install --upgrade pip setuptools
# uwsgi server waitress
$VENV/bin/pip install "pyramid==2.0" waitress


cd ..; cp -r package ini; cd ini
$VENV/bin/pip install -e .
$VENV/bin/pip install -e . or $VENV/bin/pip install -e ".[dev]"

https://docs.pylonsproject.org/projects/pyramid/en/latest/quick_tutorial/hello_world.html


$VENV/bin/cookiecutter gh:Pylons/pyramid-cookiecutter-starter --checkout 2.0-branch

# cookiecutter
$VENV/bin/pip install cookiecutter

Change directory into your newly created project.
    cd explainer

Create a Python virtual environment.
    python3 -m venv env

Upgrade packaging tools.
    env/bin/pip install --upgrade pip setuptools

Install the project in editable mode with its testing requirements.
    env/bin/pip install -e ".[testing]"

Run your project's tests.
    env/bin/pytest

Run your project.
    env/bin/pserve development.ini


###
env/bin/pserve development.ini --reload










export VENV=~/workspace/words/german_nouns/german_nouns/env
python3 -m venv $VENV
$VENV/bin/pip install --upgrade pip setuptools

########
from pprint import pprint
from explainer.nouns import NounDictionary

#nouns = NounDictionary('../nouns.csv')
nouns = NounDictionary('nouns.csv')


export VENV=~/workspace/words/explainer/env/
python3 -m venv $VENV
$VENV/bin/pip install --upgrade pip setuptools


[
  {'flexion': {
    'nominativ singular': 'Fahrrad', 
    'nominativ plural': 'Fahrräder', 
    'genitiv singular': 'Fahrrades', 
    'genitiv singular*': 'Fahrrads', 
    'genitiv plural': 'Fahrräder', 
    'dativ singular': 'Fahrrad', 
    'dativ singular*': 'Fahrrade', 
    'dativ plural': 'Fahrrädern', 
    'akkusativ singular': 'Fahrrad', 
    'akkusativ plural': 'Fahrräder'
  }, 
     'lemma': 'Fahrrad', 
     'pos': ['Substantiv'], 
     'genus': 'n'
  }
]

