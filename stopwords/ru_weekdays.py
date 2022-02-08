# -*- coding: utf-8 -*-

"""
List of stopwords related with weekdays like 'sunday, monday and etc.' for russian language

Integrated preprocess:
1. removes duplicates if any take place by mistake
2. sorts in alphabetical order
3. sorts by word length

Notes:
1. Sorting by length is required in order to completely remove long phrases before short ones,
otherwise parts of long phases may not be removed
"""


RU_WEEKDAYS = sorted(sorted(list(filter(None, list(set(
    """
понедельник понедельника понедельникам понедельниками понедельниках понедельнике понедельники понедельников 
понедельником понедельнику 

вторник вторника вторникам вторниками вторниках вторнике вторники вторников вторником вторнику 

среда средам средами средах среде средой среду среды 

четверг четверга четвергам четвергами четвергах четверге четверги четвергов четвергом четвергу 

пятница пятниц пятницам пятницами пятницах пятнице пятницей пятницею пятницу пятницы 

суббота суббот субботам субботами субботах субботе субботой субботою субботу субботы 

воскресенье воскресений воскресеньем воскресенью воскресенья воскресеньям воскресеньями воскресеньях
""".split()))))), key=len, reverse=True)
