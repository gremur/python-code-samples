# -*- coding: utf-8 -*-

"""
List of stopwords related with months like 'january, jan and etc.' for russian language

Integrated preprocess:
1. removes duplicates if any take place by mistake
2. sorts in alphabetical order
3. sorts by word length

Notes:
1. Sorting by length is required in order to completely remove long phrases before short ones,
otherwise parts of long phases may not be removed
"""


RU_MONTHS = sorted(sorted(list(filter(None, list(set(
    """
январь январе январей январём январи январю января январям январями январях янв 

февраль феврале февралей февралём феврали февралю февраля февралям февралями февралях фев 

март марта мартам мартами мартах марте мартов мартом марту марты мар

апрель апреле апрелей апрелем апрели апрелю апреля апрелям апрелями апрелях апр 

май маю мая мае маем 

июнь июне июней июнем июни июню июня июням июнями июнях июн

июль июле июлей июлем июли июлю июля июлям июлями июлях июл 

август августа августам августами августах августе августов августом августы авг 

сентябрь сентябре сентябрей сентябрём сентябри сентябрю сентября сентябрям сентябрями сентябрях сен сент 

октябрь октябре октябрей октябрём октябри октябрю октября октябрям октябрями октябрях окт 

ноябрь ноябре ноябрей ноябрём ноябри ноябрю ноября ноябрям ноябрями ноябрях ноя нояб

декабрь декабре декабрей декабрём декабри декабрю декабря декабрям декабрями декабрях дек
""".split()))))), key=len, reverse=True)
