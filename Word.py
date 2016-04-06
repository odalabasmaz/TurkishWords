# -*- coding: utf-8 -*-
class Word:
    value = None
    is_letter = None
    is_proper_name = None
    is_phrase = None
    DISCRIMINATOR = '#'

    def __init__(self, value, is_letter, is_proper_name, is_phrase):
        Word.value = value
        Word.is_letter = is_letter
        Word.is_proper_name = is_proper_name
        Word.is_phrase = is_phrase

    def __str__(self):
        return Word.value + " " + str(Word.is_letter) + " " + str(Word.is_proper_name) + " " + str(Word.is_phrase)

    def get_value(self):
        return Word.value

    def formatted_value(self):
        return Word.value + \
               Word.DISCRIMINATOR + str(Word.is_letter) + \
               Word.DISCRIMINATOR + str(Word.is_proper_name) + \
               Word.DISCRIMINATOR + str(Word.is_phrase)

    def is_regular(self):
        return not Word.is_letter and not Word.is_proper_name and not Word.is_phrase
