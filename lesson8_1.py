import re
from collections import Counter


with open('log_data.txt', 'r', encoding='UTF-8') as file:
    """ 1) строка должна начинаться с числа, буквы, символов </>, <.> или <:>
        2) этот набор может повториться произвольное количество раз
        3) затем может идти не более одной подстроки из символов < +> и произвольного количества цифр
        4) строка должна оканчиваться на < > или <]> и не на <(>, <А> или <y>"""

    result = (re.findall(r'[\d\w/.:]+(?: \+[\d]*)?(?=[ \]][^(Ay])', line) for line in file)

    print(next(result))  # Демонстрация строки

    max_spam_adr, max_spam = Counter(map(lambda x: x[0], result)).most_common(1)[0]

    print(f'Величайший спамер: {max_spam_adr} совершил {max_spam} атак')
