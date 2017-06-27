#!/usr/bin/env python3
import urllib.request

currencies = ['aud', 'cad', 'chf', 'cnh', 'cny', 'eur', 'gbp', 'hkd', 'ils',
              'inr', 'jpy', 'krw', 'mxn', 'nzd', 'rub', 'sek', 'sgd', 'usd']

def main(args):
    print('{:.2f} {}'.format(convert(args.value, args.fc, args.tc), args.tc))

def convert(value, fromcur, tocur):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
        'Accept': 'text/html'
    }

    url = 'http://download.finance.yahoo.com/d/quotes.csv?s={}{}=X&f=l1'.format(fromcur, tocur)
    req = urllib.request.Request(url, headers=headers)
    html = urllib.request.urlopen(req).read()
    rate = float(html)
    return value * rate

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(prog='concur', description='Accepted currencies: {}'.format(', '.join(currencies).upper()))
    parser.add_argument('value', help='Value', type=float)
    parser.add_argument('fc', help='Currency to convert from.', choices=currencies, metavar='from')
    parser.add_argument('tc', help='Currency to convert to. Default: USD', choices=currencies, default='usd', nargs='?', metavar='to')
    args = parser.parse_args()
    args.fc = args.fc.upper()
    args.tc = args.tc.upper()

    main(args)
