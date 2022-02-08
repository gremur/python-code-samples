# -*- coding: utf-8 -*-

"""
List of stopwords related with calendar units like 'today, half year, quartile, week and etc.' for russian language

Integrated preprocess:
1. removes duplicates if any take place by mistake
2. sorts in alphabetical order
3. sorts by word length

Notes:
1. Sorting by length is required in order to completely remove long phrases before short ones,
otherwise parts of long phases may not be removed
"""

RU_CALENDAR_UNITS = sorted(sorted(list(filter(None, list(set(
    """
сегодня вчера позавчера завтра 

день дня дню днём днем дне дни дней дням днями днях дн 

неделя недели неделе неделю неделей неделею недель неделям неделями неделях нед 

декада декады декаде декаду декадой декадою декад декадам декадами декадах 

месяц месяца месяцу месяцем месяце месяцы месяцев месяцам месяцами месяцах месяц-два месяц-полтора мес 

квартал квартала кварталу кварталом квартале кварталы кварталов кварталам кварталами кварталах кв 

полугодие полугодье полугодия полугодья полугодию полугодью полугодием полугодьем полугодье полугодии полугодьи 
полугодий полугодиям полугодьям полугодиями полугодьями полугодиях полугодьях полгода 

год года году годом году годе года годы годов лет годам годами годах лет год-два год-полтора год-три года-двух гг 

век века веку веком веков векам веками веках веке 

столетие столетия столетию столетием столетье столетий столетиям столетиями столетиях  столетье  столетья  столетью  
столетьем  столетии  столетьям  столетьями  столетьях  столетьи
""".split()))))), key=len, reverse=True)
