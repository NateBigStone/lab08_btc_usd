import requests
import logging


url = 'https://api.coindesk.com/v1/bpi/currentprice/usd.json'
log_level = logging.ERROR
logging.basicConfig(filename='btc-messages.log',
                    filemode='a',
                    format='%(levelname)s %(asctime)s - %(message)s',
                    level=log_level)


def convert():
    num_of_btc = input('Please enter the number of BTC:\n').lower().strip()
    if is_valid_num(num_of_btc):
        btc_price = api_call()
        total_in_usd = btc_to_usd(num_of_btc, btc_price)
        return_value = print_total(total_in_usd)
        print(return_value)
        return return_value
    else:
        print(f'"{num_of_btc}" is an invalid number, please try again\n')
        convert()


def is_valid_num(num):
    try:
        test_num = float(num) > 0
        return test_num
    except Exception as e:
        print(f'{e}\n')
        logging.error(e)


def api_call():
    price = None
    try:
        resp = requests.get(url).json()
        price = float(resp['bpi']['USD']['rate_float'])
    except Exception as e:
        print(f'Error- {e}')
        logging.error(e)
    return price


def btc_to_usd(btc, price):
    return float(btc) * price


def print_total(total):
    return f'${str(round(total, 2))}'


if __name__ == '__main__':
    convert()
