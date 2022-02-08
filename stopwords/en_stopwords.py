# -*- coding: utf-8 -*-

"""
List of stopwords for english language

Integrated preprocess:
1. removes duplicates if any take place by mistake
2. sorts in alphabetical order
3. sorts by word length

Notes:
1. Sorting by length is required in order to completely remove long phrases before short ones,
otherwise parts of long phases may not be removed
"""


EN_STOPWORDS = sorted(sorted(list(filter(None, list(set(
    """
a about above after again against all am an and any are as at ain aren aren't 

b be because been before being below between both but by 

c can could can't could't couldn couldn't

d did do does doing don down during don't did't doi didn didn't doesn doesn't

e each etc. etc 

f few for from further 

g 

h had has have having he her here hers herself him himself his how hadn hadn't hasn hasn't haven haven't

i if in into is it its itself isn isn't it's 

j just 

k kind

l ll

m me more most my myself mail ma mightn mightn't mustn mustn't 

n no nor not now needn needn't 

o ok of off on once only or other our ours ourselves out over own 

p 

q 

r rather re 

s same she should so some such something shan shan't she's should've shouldn shouldn't 

t than that the their theirs them themselves then there these they this those through to too that'll

u under until up upon unto until unless unlike  under underneath 

v very ve 

w was we were what when where which while who whom why will with would would't woulds wasn wasn't weren 
weren't won won't wouldn wouldn't 

x 

y you your yours yourself yourselves ye yet you'd you'll you're you've 

z
""".split()))))), key=len, reverse=True)
