from requests import get, utils


def currency_rates(tiket):
    """Функция формирования информации о курсе выбранной валюты по отношению к рублю"""

    target_url = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(target_url.headers)
    server_date = target_url.headers['Set-Cookie'].split(',')[1]
    print(f'Дата сервера: {server_date}')

    target_content = target_url.content.decode(encoding=encodings)

    key_words = ['Nominal', 'Name', 'Value']  # Список ключевых тегов XML для поиска требуемых параметров

    target_str = target_content[target_content.find(str(tiket).upper()):]  # Поиск валюты в общем списке

    if len(target_str) > 2:
        target_str = target_str[:target_str.find('</Valute>')]  # Формирование целевой строки с информацией о валюте

        # Формирование списка информации о фалюте по тегам XML и приведение их к нужному типу

        currency_info = list(map(lambda x: str(target_str.split(x)[1])[1:-2], key_words))
        currency_info[0] = int(currency_info[0])
        currency_info[2] = float('.'.join(currency_info[2].split(',')))

        print(f'За {currency_info[0]} {currency_info[1]} дают {currency_info[2]} Рублей')
    else:
        print(None)


if __name__ == "__main__":
    currency_rates(input('Введите тикет нужной валюты: '))
