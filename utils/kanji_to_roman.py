# -*- coding: utf-8 -*-
from pykakasi import kakasi

kakasi_ = kakasi()
kakasi_.setMode('H', 'a') # H(Hiragana) to a(roman)
kakasi_.setMode('K', 'a') # K(Katakana) to a(roman)
kakasi_.setMode('J', 'a') # J(Kanji) to a(roman)

conv = kakasi_.getConverter()
filename = '本日は晴天ナリ'

print(type(filename))
print(filename)
print(conv.do(filename))