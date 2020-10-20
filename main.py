import requests
import logging


url = 'https://api.coindesk.com/v1/bpi/currentprice/usd.json'
log_level = logging.ERROR
logging.basicConfig(filename='btc-messages.log',
                    filemode='a',
                    format='%(levelname)s %(asctime)s - %(message)s',
                    level=log_level)


def convert(num_of_btc):
    if not is_valid_num(num_of_btc):
        print(f'"{num_of_btc}" is an invalid number, please try again\n')
        return None
    resp = api_call()
    btc_price = parse_resp(resp)
    total_in_usd = btc_to_usd(num_of_btc, btc_price)
    return_value = print_total(total_in_usd)
    print(return_value)
    return return_value


def is_valid_num(num):
    test_num = None
    try:
        test_num = float(num) > 0
    except Exception as e:
        logging.error(e)
    return test_num


def api_call():
    api_response = None
    try:
        api_response = requests.get(url).json()
    except Exception as e:
        print(f'Error- {e}')
        logging.error(e)
    return api_response


def parse_resp(resp):
    parsed = None
    try:
        parsed = float(resp['bpi']['USD']['rate_float'])
    except Exception as e:
        print(f'Error- {e}')
        logging.error(e)
    return parsed


def btc_to_usd(btc, price):
    calculation = None
    try:
        calculation = float(btc) * price
    except Exception as e:
        logging.error(e)
        print(f'Error- {e}')
    return calculation


def print_total(total):
    return_total = None
    try:
        return_total = f'${str(round(total, 2))}'
    except Exception as e:
        logging.error(e)
    return return_total


if __name__ == '__main__':
    user_input = input('Please enter the number of BTC:\n').strip()
    convert(user_input)
