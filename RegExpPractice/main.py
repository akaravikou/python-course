import re

# def find_three_con(text):
#    mo = re.search(r'\d\d\d', text)
#    if mo is None:
#        return 'Not Found'
#    else:
#        return mo.group()


# text = 'My phone number is: 756-891-3522'
# print(find_three_con(text))

# phone_number_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# mo = phone_number_regex.search(text)
# print(mo.group(0))

# dis_regex = re.compile(r'dis(agree|allow|array)')
# text = "I was disconnect, and after disarray"
# print(dis_regex.search(text))

# regex = re.compile(r'a?pple')
# mo = regex.search('pinple')
# print(mo)

# def match(text):
#    regex = re.compile(r'AB*')
#    mo = regex.search(text)
#    if mo is None:
#        return 'Not matched'
#    else:
#        return 'Matched'


# print(match('A'))
# print(match('AB'))
# print(match('ABBC'))


# def match(text):
#     regex = re.compile(r'AB{2,3}')
#     mo = regex.search(text)
#     if mo is None:
#         return 'Not matched'
#     else:
#         return 'Matched'
#
#
# print(match('A'))
# print(match('AB'))
# print(match('ABBC'))

# text = '''Lovers in love
# Lovers in love
# Love, love, love, love, love
# Love, love, love, love, love
# Love, love, love, love, love
# Love, love, love, love, love
# Lovers loving love just like these lovers are loving love in love
# Lovers loving love just like these lovers are loving love in love'''


# def text_match(text):
#     regex = re.compile(r'(L|l)ove(rs)?')
#     mo_list = regex.findall(text)
#     return len(mo_list)
#
#
# print(text_match(text))

# text = '''What’s New In Python 3.10
# Release 3.10.1
# Date January 10, 2022
# Editor Pablo Galindo Salgado
# This article explains the new features in Python 3.10, compared to 3.9.'''
#
# regex = re.compile(r'3\S+')
# mo = regex.findall(text)
# print(mo)

url = 'https://www.apmillers.com/news/daily/wp/2022/02/02/regular-expressions-patterns/'


def extract_date(url):
    regex = re.compile(r'\d')
    mo = regex.findall(url)
    return mo


print(extract_date(url))
