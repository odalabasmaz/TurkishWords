# -*- coding: utf-8 -*-

# DictionaryServer
# Server uri example
# 'http://www.tdk.gov.tr/index.php?option=com_yazimkilavuzu&view=yazimkilavuzu&kategori1=yazim_listeli&ayn1=bas&kelime1=a&sayfa1=0'
server_uri_base = 'http://www.tdk.gov.tr/index.php?option=com_yazimkilavuzu&view=yazimkilavuzu&kategori1=yazim_listeli&ayn1=bas'

# output file path
output_file_path = 'output/words.out'

# proxy settings
use_proxy = False
proxies = {"http": "username:password@proxy-ip:proxy-port",
           "https": "username:password@proxy-ip:proxy-port"
           }

# Alphabet
turkish_letters = ['a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'h', 'ı', 'i',
                   'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'r', 's', 'ş',
                   't', 'u', 'ü', 'v', 'y', 'z']

# Log level
detailed_log = False
