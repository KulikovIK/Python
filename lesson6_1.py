from requests import get, utils
from collections import Counter


def data_converter(processing_record):
    """Функция-генератор кортежей (<URL>, <ВИД_ЗАПРОСА>, <ЗАПРАШИВАЕМАЯ_ИНФО>)"""
    converted_tuple = ()
    for item in processing_record:
        try:
            processing_url = item.split(' - - ')[0]
            processing_request = item.split('"')[1].split(' ')[:2]
            converted_tuple = (processing_url, processing_request[0], processing_request[1])
        except IndexError:
            pass
        yield converted_tuple


data_url = get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
if data_url.status_code == 200:

    encoding = utils.get_encoding_from_headers(data_url.headers)

    # Генератор последовательности строк с сайта
    processing_data = (item for item in data_url.content.decode(encoding=encoding).splitlines())

    # Вычисление главного спамера
    spammers = Counter(map(lambda item: item[0], data_converter(processing_data)))
    greatest_spammer, greatest_spammer_count = spammers.most_common(1)[0]

    print(f'Величайший спамер {greatest_spammer} совершил {greatest_spammer_count} обращений')

