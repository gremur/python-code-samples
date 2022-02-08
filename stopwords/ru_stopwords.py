# -*- coding: utf-8 -*-

"""
List of stopwords for russian language

Integrated preprocess:
1. removes duplicates if any take place by mistake
2. sorts in alphabetical order
3. sorts by word length

Notes:
1. 'не', 'ни' excluded from stopwords to keep negative meaning of words
2. Sorting by length is required in order to completely remove long phrases before short ones,
otherwise parts of long phases may not be removed
"""


RU_STOPWORDS = sorted(sorted(list(filter(None, list(set(
    """
а а-ля ага аж аа ааа агу ау ах авось ай али алло ао авторизуйтесь акцентировал акцентировала акцентирует акцентирую 
ахнули 

б будем будет будете будешь буду будут будучи будь будьте бы был была были было быть без будто благо благодаря более 
больше буль-буль более-менее бац бишь близко бывает ближайшие безусловно будем будет будете будешь буду будут будь 
будьте бывает бывала бывали бываю бывают был была были было было-то бытует 

в вам вами вас весь во вот все всё всего всей всем всём всеми всему всех всею всея всю вся вы вне вряд ведь вновь 
вроде вернее впрямь всякий всякой вчеред взаимно включая вначале вопреки вправду впрочем всякого все-таки во-вторых 
во-первых вдобавок воистину вперекор вресноту взаправду вместо вдруг всегда везде всюду всячески вот-вот всего-навсего 
всего-то все-все-все всё-таки внакладе вправе ваш вечер важная важное важные важный ваша ваше ваши вверх вдали 
видно вишь вниз внизу вокруг вон вообще вчера времени время вполне выглядит выступает возможно вплоть важно вовсе 
важнее вcем выскажется выскажут высказал высказала высказалась высказали высказались высказало высказался высказывает 
высказывается высказывайте высказывал высказывали высказывались высказывался высказывают высказываются 

г где-то где-либо где-нибудь где гав-гав говорил говорит говорится говорить говоря говорят гораздо говорил говорила 
говорили говорилось говорим говорит говорите говорится 

д да для до дабы доколе доколь должно должный даже другой другая другое других другими данунах дану два двое двоих 
двоим двоими давным-давно довольно-таки для-де да-с да-да де долго-долго данный день давно далеко дальше даром
действительно дел довольно долго другие должен должна должны добиться дополнительно давайте думаю думает думать думала 
другим данная данного данное данной данном данному данные данных далее 

е его едим едят ее её ей еле ем ему емъ если ест есть ешь еще ещё ею едва едва-едва еле-еле ей-де ей-же-ей ей-богу 
ежели 

ё ёпрст ёпэрэсэтэ ёмаё 

ж же жизнь 

з за зачем затем здесь зачем-то зато зэий зсный занят занята занято заняты значит зарегистрироваться заявил заявила
заметил заметила замечает заявили зависит зачитал зао зря 

и из или им ими имъ их ибо итак иначе из-за именно исключая иными иным иногда из-под ишь извинять изволить иль иметь
имя имеет имел имело имела имени источник информирует 

й 

к как кем ко когда кого кому которая которого которое которой котором которому которою которую которые который которым 
которыми которых кто какой какою кроме какими какого как-то кое-как кой-как конечно как-либо какой-то какою-то 
как-никак какого-то как-нибудь какой-либо какой-нибудь какой-никакого какой-никакой какою-нибудь которой-нибудь 
которою-нибудь который-нибудь касательно какими-то какою-то каких-то какая куда кто-то когда-то кое-где кое-куда 
куда-либо куда-нибудь куда-то кое-какими кое-какой кое-кто кое-чем кое-что кой-какой кой-куда кто-нибудь каков 
когда-нибудь кое-когда как-будто короче кстати ку кто-кто кто-либо ка каждый какой кабы каждая каждое каждые кажется
кой коли коль ком кругом казаться комментариями комментарий комментирует какие-то какие контакты каким-либо какому 
каким кем-нибудь кем-то кого-либо кого-нибудь кого-то кое-кем кому-кому кому-то казалась казались казалось казался 
комментировал комментировала комментирует комментируют прокомментировал прокомментировала прокомментировали 
крутится-вертится 

л лишь либо ли лучше лучший лучшего лучших лучшая линк люди любой любом любых любого любыми любую любое любая 

м меня мне мной мною мог моги могите могла могли могло могу могут можно мое моё моего моей моем моём моему моею можем 
может можете можешь мои мой моим моими моих мочь мою моя мы между много мало-мальски мало-помалу много-много мм му 
многие многое мы-то мол меж мало менее меньше мимо мира многочисленная многочисленное многочисленные многочисленный 
многого многом многому мог могла могли могло могу могут можем может можете можешь 

н на ну нам нами нас наса наш наша наше нашего нашей нашем нашему нашею наши нашим нашими наших нашу него нее 
неё ней нем нём нему нет нею ним ними них но ныне нынче навряд насилу насчет наоборот накануне например напротив 
начихать начхать нынешнее наверняка наизворот наизнанку наперекор навыворот наипаче наперед начхать неважно над надо 
наконец нельзя нибудь никогда ничего негде незачем некогда некуда нигде никак никуда ниоткуда нипочем не-а ну-тка 
нет-нет ням-ням наподобие наконец-то некто немногие нечего нечто никто ничто нате неужели неоткуда нет-то нету нужно 
ночь наверху назад наиболее начала недавно недалеко немного непрерывно нередко несколько нешто ниже низко некоторый 
никакой нужный нужная нужные нужных нужного напомним некоторые некоторый некоторая находиться настоящее нынешних 
наметилась нынешней надеясь необходимые напоминает напомнил напрямую начале необходимо некоторых необходимым 
необходимости напоминать настоящая настоящие настоящий некем некому немногим нечем нечему никем никого никому ничем
ничему 

о об один одна одни одним одними одних одно одного одной одном одному одною одну он она оне они оно от около опять 
однако оттого отчего отчему особенно отнелижа отнелиже оттот-то оттого-то опять-таки откуда откуда-то отовсюду 
оттуда отчего-то ого-го о-го-го она-де очень-очень очень-то особо-то ого ой оп ох они-то он-то окей общий-то оба
обычно однажды отсюда очень оказаться остаться ответить отмечает отмечают отметил оправданно оправдано определяет 
ожидать обсуждалось осуществления осуществлении осваивают опубликовала опубликовал отметили отметила озвучено 
объяснил объяснила объясняет объясняет ответил отвечает обратил объясняют обсудили отмечены напрямую объяснили 
очевидно особые ооо оао общую особую осветила ожидают оценили отмечается оный 

п по при под пока почти поколе поколь покуда помимо понеже посему потому почему прежде притом почитай поэтому подавно 
подобно поелику пожалуй понятие понятье поистине покамест покудова поскольку потого-то потому-то потомушта 
перво-наперво посредством перефразируй перефразируя перед после потом про по-всякому по-другому по-иному почему-то 
по-разному по-вашему по-моему по-настоящему по-нашему по-новому по-прежнему по-своему по-старому по-твоему по-хорошему 
по-человечески просто-напросто прямо-таки по-видимому поди-ка по-за по-над по-пустому по-любому по-одному по-особому 
прочее просто прям пусть пусть-ка причем подобный подобные подобного подобных подобным подобная пор пускай поди 
позволять позже пора посреди право пред прекрасно против процентов подталкивает появился паче предлагает потребует 
позволяет потребуется принимают полученная проводятся прочими понимать появляться предпочитают постоянный 
применяться появляться появляется поделился поделилась поделились подчеркнул подчеркнула подчеркнули прокомментировали 
предоставлено примени проведенного пожалуйста пояснил прим.ред. пояснила подписывайтесь поделиться подчеркивает 
подытожил полагает получается понятно пояснили поясняет пояснял приводит продолжает прокомментировал прокомментировала 
показал предлагают представлять пишет пишут показав похожем присоединяйтесь проще подробная подробный подробные 
поприще прочего прочему 

р раз разве ради рано раньше ранее рядом ранее рассказал рассказали рассказать рассматривать рассчитывать рассмотрены 
резюмирует резюмировала резюмировал рассуждает рассуждала рассуждали рассказала рассказывает рублей рассказала 
расскажут рассказывать рассказываем рассказывает рассказывал рассказывала рассказывали рассказывают резюмировал 
резюмировала резюмировали резюмирует резюмируют рекламирует рекламирую 

с со сам сама сами самим самими самих самых само самого самом самому саму свое своё своего своей своем своём своему 
свои свой своим своими своих свою своя себе себя собой собою снова стало сперва сначала спокону сызнова случайно своею 
согласно созвучно собственно соответственно сейчас совсем сколько-нибудь сколько-то сколь-нибудь сейчас-то сие сверх 
свыше сквозь спустя среди сродни сей сих ссылка ссылку ссылке ссылкам соответствующий следующем соответствующая 
соответствующего соответствующих самой самый сегодня сказал сказала сказать сколько слишком слышь спасибо стал суть 
стать сразу случай считает сможет скачать сообщил сообщало считает связанные состоится сообщается смогут слышим 
стараются соответствующей сообщает соотнеся самое самая следует скорее сказали сказано сообщила сообщили считаю считают 
скоро се сего сей сообщаем сообщает сообщается сообщал сообщала сообщали сообщало сообщалось сообщаю сообщают 
сообщил сообщила сообщили сообщило сообщит сообщите 

т та так такая такие таким такими таких такого такое такой таком такому такою такую те тебе тебя тем теми тех то тобой 
тобою того той только лько тому тот тою ту ты типа точно так-таки таки-да таки-нет только-только тел. тел тел./факс 
тел/факс там теперь тогда тоже три трое троих троим тут туда туда-сюда таки-так т.д. т.п. также таков там-то тогда-то 
туда-обратно таки так-то твой твоя твоё твоя твоих твоим такова тот том тотчас тьфу твои тысяч требуется 

у уж уже увы ура ух утро уметь уж убежден уверен утверждает уточнил уточнила уточнили уточняет уверена удк 
утверждает утверждается утверждал утверждала утверждали утверждало утверждалось утверждают уточнил уточнила 
уточнили уточнило уточним уточняем уточняет уточняется уточнял уточнялось уточняют уточняются упоминает упоминается 
упоминаешь упоминали упоминался упоминают упоминаются упомянул упомянула упомянули упомянуло 

ф факс фу фото 

х хорошо хоть ха-ха-ха худо-бедно хотя ха хе хлоп хотеть хочешь хотел хотелось хотела хуже хочу 

ц цап цок цитирует цитируют цитировал цитирует цитируете цитируют 

ч чего чем чём чему что чтобы чуть чтоб через чей-то чхать чуть-чуть что-то что-де чао что-либо что-нибудь чей чьё 
чьим чьих чай часто чаще человек черт час часть чему-то чего-либо чего-то чем-нибудь чем-то чё читайте 

ш ша шире 

щ ща щас 

ь 

ъ 

э эта эти этим этими этих это этого этой этом этому этот этою эту этак эдак эй эх эка экий эдакий этакий  

ю 

я яко ясно якоже якобы являюсь являясь является явилась явных являются являлся явилась явились явилось явился явится 
явленияй являемся являетесь является являлась являлись являлось являлся являюсь являются 
""".split()))))), key=len, reverse=True)


# hyphened stopwords like "так-то" with hyphen "-" in order to have one single token ['так-то']
# and prevent separate tokenization like ['так', '-', 'то']
# single token like ['так-то'] can be early filtered out as a stopword

RU_HYPHEN_STOPWORDS = [item for item in RU_STOPWORDS if '-' in ''.join(item)]
