#!/usr/bin/env python3
import requests

currencies = ['aud', 'cad', 'chf', 'cnh', 'cny', 'eur', 'gbp', 'hkd', 'ils',
              'inr', 'jpy', 'krw', 'mxn', 'nzd', 'rub', 'sek', 'sgd', 'usd']

def main(args):
    print('{:.2f} {}'.format(convert(args.value, args.fc, args.tc), args.tc))

def convert(value, fromcur, tocur):
    url = 'http://download.finance.yahoo.com/d/quotes.csv?s={}{}=X&f=l1'.format(fromcur, tocur)
    query = requests.get(url)
    rate = float(query.text)
    return value * rate

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(prog='concur', description='Accepted currencies: {}'.format(', '.join(currencies)))
    parser.add_argument('value', help='Value', type=float)
    parser.add_argument('fc', help='Currency to convert from.', choices=currencies)
    parser.add_argument('tc', help='Currency to convert to. Default: USD', choices=currencies, default='usd', nargs='?')
    args = parser.parse_args()
    args.fc = args.fc.upper()
    args.tc = args.tc.upper()

    main(args)
