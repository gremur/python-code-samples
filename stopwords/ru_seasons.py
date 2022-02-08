# -*- coding: utf-8 -*-

"""
List of stopwords related with seasons like 'winter, summer and etc.' for russian language

Integrated preprocess:
1. removes duplicates if any take place by mistake
2. sorts in alphabetical order
3. sorts by word length

Notes:
1. Sorting by length is required in order to completely remove long phrases before short ones,
otherwise parts of long phases may not be removed
"""

RU_SEASON = sorted(sorted(list(filter(None, list(set(
    """
зима зимы зиме зиму зимой зим зимам зимами зимах зимою 

весна весны весне весну весной вёсны вёсен вёснам вёснами вёснах весною 

лето лета лету летом лете летах 

осень осени осенью осеней осеням осенями осенях
""".split()))))), key=len, reverse=True)
