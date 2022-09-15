from random import choice


def get_joke(number, repeat=False):
    """Функция принимающая количество шуток и возможность повторения слов в них
    Параметр repeat = True говорит, что повторяться нельзя"""

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    for i in range(number):  # Генератор
        if repeat:  # уникальных шуток
            try:
                noun = nouns.pop(nouns.index(choice(nouns)))
                adverb = adverbs.pop(adverbs.index(choice(adverbs)))
                adjective = adjectives.pop(adjectives.index(choice(adjectives)))
                print(f'{noun} {adverb} {adjective}')

            except IndexError:
                print('Шутки закончились')
                break

        else:  # повторяющихся
            print(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')


get_joke(9, repeat=True)
