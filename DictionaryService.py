# -*- coding: utf-8 -*-
import re

import mechanize
from BeautifulSoup import BeautifulSoup

from Word import Word
from config import DictionaryConfig


class DictionaryService:
    """Common base Dictionary Service"""

    fs = None
    regular_words = []
    proper_words = []
    phrases = []

    def __init__(self, fs):
        DictionaryService.fs = fs

    def get_regular_words(self):
        return DictionaryService.regular_words

    def get_proper_words(self):
        return DictionaryService.proper_words

    def get_phrases(self):
        return DictionaryService.phrases

    def request_page(self, page_uri):
        if DictionaryConfig.detailed_log:
            print 'page requesting...', page_uri
        br = mechanize.Browser()
        br.set_handle_robots(False)
        headers = [
            ('Content-type', 'text/html; charset=UTF-8')
        ]
        br.addheaders = headers
        if DictionaryConfig.use_proxy:
            br.set_proxies(DictionaryConfig.proxies)
        br._factory.encoding = 'utf-8'
        br._factory._forms_factory.encoding = 'utf-8'
        br._factory._links_factory._encoding = 'utf-8'
        res = br.open(page_uri).read()
        return res

    def handle_response(self, response):
        soup = BeautifulSoup(response.decode('utf-8', 'ignore'))

        table = soup.find('table', {'border': '1'})
        is_going_on = False
        for tr in table.findAll('tr'):
            is_going_on = True
            for td in tr.findAll('td'):
                td_value = str(td)
                word = re.search(r'(.*)kelime=(.+)&amp;c(.*)', td_value).group(2)

                is_letter = word.__len__() == 1
                is_proper_name = word[0].isupper()
                is_phrase = word.__contains__(' ')

                w = Word(word, is_letter, is_proper_name, is_phrase)

                if DictionaryConfig.detailed_log:
                    print 'word consumed #', DictionaryService.regular_words.__len__() + 1, ':', w.get_value()

                if w.is_regular():
                    DictionaryService.regular_words.append(w)
                elif w.is_proper_name:
                    DictionaryService.proper_words.append(w)
                elif w.is_phrase:
                    DictionaryService.phrases.append(w)

                DictionaryService.fs.write(w.formatted_value() + "\n")

        return is_going_on
