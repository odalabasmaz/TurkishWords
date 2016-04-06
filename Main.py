# -*- coding: utf-8 -*-
from DictionaryService import DictionaryService
from config import DictionaryConfig
from config.DictionaryConfig import turkish_letters

if __name__ == '__main__':
    print 'Fetching words in dictionary...'
    fs = open(DictionaryConfig.output_file_path, 'w')

    service = DictionaryService(fs)
    page_uri_base = DictionaryConfig.server_uri_base

    page_count = 0
    for letter in turkish_letters:
        while True:
            page_uri = page_uri_base + "&kelime1=" + letter + "&sayfa1=" + str(page_count)
            response = service.request_page(page_uri)
            should_continue = service.handle_response(response)
            page_count += 60
            if not should_continue:
                page_count = 0
                break

    fs.close()

    print 'Fetching is done...'
    print 'Results:'
    print '-- Regular Words: ', str(service.get_regular_words().__len__())
    print '-- Proper Words: ', str(service.get_proper_words().__len__())
    print '-- Phrases: ', str(service.get_phrases().__len__())
