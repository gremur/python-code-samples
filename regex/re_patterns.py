# -*- coding: utf-8 -*-
# Collection of compiled regex patterns for sustainable reuse from single source.
# re.I == re.IGNORECASE

import re
from typing import Pattern


RE_HTML_TAG: Pattern = re.compile(r'<.*?>')

RE_EMAIL: Pattern = re.compile(r'([а-яa-z0-9_.-]+@[а-яa-z0-9-]+\.[а-яa-z0-9-.]+\b)', re.I)

RE_URL_VALID: Pattern = re.compile(r'(https?:\s?//[^\s]+[^.,()\]:\\;\r\n\s"]+)', re.I)

RE_URL_LIKE: Pattern = re.compile(r'''\b((?:https?://|www\d{0,3}\.|[a-z0-9.\-]+\.[a-z]{2,4}/)'''
                                  r'''(?:[^\s()<>]+|\((?:[^\s()<>]+|(?:\([^\s()<>]+\)))*\))'''
                                  r'''+(?:\((?:[^\s()<>]+|(?:\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''',
                                  re.I)

# source: https://gist.github.com/dperini/729294
RE_URL_COMPLEX: Pattern = re.compile(
    r"(?:^|(?<![\w/.]))"
    # protocol identifier
    # r"(?:(?:https?|ftp)://)"  <-- alt?
    r"(?:https?://|ftp://|www\d{0,3}\.)"
    # user:pass authentication
    r"(?:\S+(?::\S*)?@)?"
    r"(?:"
    # IP address exclusion
    # private & local networks
    r"(?!(?:10|127)(?:\.\d{1,3}){3})"
    r"(?!(?:169\.254|192\.168)(?:\.\d{1,3}){2})"
    r"(?!172\.(?:1[6-9]|2\d|3[0-1])(?:\.\d{1,3}){2})"
    # IP address dotted notation octets
    # excludes loopback network 0.0.0.0
    # excludes reserved space >= 224.0.0.0
    # excludes network & broadcast addresses
    # (first & last IP address of each class)
    r"(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])"
    r"(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}"
    r"(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))"
    r"|"
    # host name
    r"(?:(?:[a-z\u00a1-\uffff0-9]-?)*[a-z\u00a1-\uffff0-9]+)"
    # domain name
    r"(?:\.(?:[a-z\u00a1-\uffff0-9]-?)*[a-z\u00a1-\uffff0-9]+)*"
    # TLD identifier
    r"(?:\.(?:[a-z\u00a1-\uffff]{2,}))"
    r")"
    # port number
    r"(?::\d{2,5})?"
    # resource path
    r"(?:/\S*)?"
    r"(?:$|(?![\w?!+&/]))",
    re.I)

# numbers in square brackets like '[10]', '[10:30]' and etc.
RE_NUMBERS_SQ_BRACKETS: Pattern = re.compile(r"\[[0-9\-.,:;]*]")

RE_FILE_NAME: Pattern = re.compile(
    r'\b[0-9a-z\-_]+\.'
    r'(?:avi|mpeg|mp4|mpg|mp3|'
    r'doc|docx|xls|xlsx|csv|pdf|ppt|pptx|txt|'
    r'gif|webp|png|svg|jpeg|jpg|jfif|pjpeg|pjp|ico|'
    r'exe|'
    r'zip|rar|tar)\b', re.I)

RE_TIMESTAMP: Pattern = re.compile(
    r'((?:^|\s)'
    r'('
    r'(?:(?:(?:[0-2][0-3])|(?:[0][4-9])|(?:[1][2-9])|[0-9])[:-][0-5][0-9](?:[:][0-5][0-9])?)'
    r'(?:-?(?:(?:[0-2][0-3])|(?:[0][4-9])|(?:[1][2-9])|[0-9])[:-][0-5][0-9](?:[:][0-5][0-9])?)?'
    r')'
    r'(?:$|\s|.|,|:|;))'
    r'|'
    r'('
    r'(?:^|\s)'
    r'(\d{2}(?::\d{2})?-\d{2}:\d{2})'
    r'(?:$|\s)'
    r')')

RE_QUOTES: Pattern = re.compile(r'[\u0022\u00AB\u00BB\u2018\u2019\u201A\u201B\u201C\u201D\u201E\u201F\u2039\u203A'
                                r'\u275B\u276E\u2E42\u301D\u301E\u301F\u0301]+', re.U)

RE_BULLETS: Pattern = re.compile(r'[\u00B7\u2022\u2023\u2043\u204C\u204D\u2219\u23FA\u25AA\u25CF\u25E6\u26AB'
                                 r'\u29BE\u29BF\u30FB]+', re.U)

RE_HYPHENS: Pattern = re.compile(r'[\u1806\uFE63\uFF0D\u2212\u00AD\u2010\u2011\u2043\u2012\u2013\u2014\u2015\u4E00]+',
                                 re.U)

RE_HYPHENATED_WORD: Pattern = re.compile(r'(\w{2,}(?<!\d))¬\s+((?!\d)\w{2,})', re.I)

RE_CURRENCY_SYMBOL: Pattern = re.compile(r"[₽€$¢£¤¥ƒ֏؋৲৳૱௹฿៛ℳ元円圆圓﷼]+|[\u20A0-\u20C0]+", re.U)

RE_MENTION: Pattern = re.compile(r"(?:^|(?<![\w@.]))@\w+", re.I)

RE_HASHTAG: Pattern = re.compile(r"(?:^|(?<![\w#＃.]))[#＃](?!\d)\w+", re.I)
