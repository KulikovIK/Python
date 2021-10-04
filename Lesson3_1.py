def num_translate_adv(adv_en_num=None):
    """Переводит числительные от 0 до 10 с английского нужном регистре"""

    '''Для выполнения данной задачи лучше весего подойдет словарь
    объявленный в теле функции. Так как обратиться к нему напрямую
    из тела основной программы сложно, то и сложнее сломать 
    логику работы программы'''

    translate_dict = {'zero': 'ноль',
                      'one': 'один',
                      'two': 'два',
                      'three': 'три',
                      'four': 'четыре',
                      'five': 'пять',
                      'six': 'шесть',
                      'seven': 'семь',
                      'eight': 'восемь',
                      'nine': 'девять',
                      'ten': 'десять'}

    if 64 < ord(adv_en_num[0]) < 91 and adv_en_num.lower() in translate_dict:
        print(f'{str(translate_dict[adv_en_num.lower()]).capitalize()}')
    elif adv_en_num in translate_dict:
        print(f'{translate_dict[adv_en_num]}')
    else:
        print(None)


num_translate_adv('Six')    # Шесть
num_translate_adv('Два')    # None
num_translate_adv('Two')    # Два

