#!/usr/bin/env python3

"""currency.py: This module provides methods to calculate the amount of money you can exchange.

__author__ = "Liuziyu"
__pkuid__  = "1700011766"
__email__  = "1700011766@pku.edu.cn"
"""

import string
from urllib.request import urlopen


def make_up(a, b, c):
    """This function uses the given parameters to make up the url address needed
    """
    d = 'http://cs1110.cs.cornell.edu/2016fa/a1server.php?from={}&to={}&amt={}'.format(a, b, c)
    return d


def get_from(f):
    """This function uses the given parameter to get the corresponding string from the website
    """
    doc = urlopen(f)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    return jstr


def results(g):
    """This function uses the given parameter to get the results for this exchange
    """
    h = g.split('"')
    l = [h[3], h[7], h[10], h[13]]
    if l[2] == ' : false, ':
        j = l[3]
    else:
        j = 'You can get ' + l[1] + ' with ' + l[0]
    return j


def exchange(currency_from, currency_to, amount_from):
    """Returns: amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in currency currency_from to the currency currency_to. The value returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code

    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""
    url = make_up(currency_from, currency_to, amount_from)
    strings_ = get_from(url)
    feedback = results(strings_)
    return feedback


def test_make_up():
    """This function provides tests for the function make_up.
    """
    a = 'USD'
    b = 'EUR'
    c = '2.5'
    assert(make_up(a, b, c) == 'http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=USD&to=EUR&amt=2.5')
    assert(make_up(b, a, c) == 'http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=EUR&to=USD&amt=2.5')
    assert(make_up(c, a, b) == 'http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=2.5&to=USD&amt=EUR')
    return True


def test_get_from():
    """This function provides tests for the function get_from.
    """
    f = 'http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=USD&to=EUR&amt=2.5'
    assert(get_from(f) == '{ "from" : "2.5 United States Dollars", "to" : "2.0952375 Euros", "success" : true, "error" : "" }')
    f = 'http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=asd&to=EUR&amt=2.5'
    assert(get_from(f) == '{ "from" : "", "to" : "", "success" : false, "error" : "Source currency code is invalid." }')
    f = 'http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=USD&to=RMB&amt=2.5'
    assert(get_from(f) == '{ "from" : "", "to" : "", "success" : false, "error" : "Exchange currency code is invalid." }')
    f = 'http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=USD&to=EUR&amt=x'
    assert(get_from(f) == '{ "from" : "", "to" : "", "success" : false, "error" : "Currency amount is invalid." }')
    return True


def test_results():
    """This funcion provides tests for the function results.
    """
    g = '{ "from" : "", "to" : "", "success" : false, "error" : "Source currency code is invalid." }'
    assert(results(g) == 'Source currency code is invalid.')
    g = '{ "from" : "", "to" : "", "success" : false, "error" : "Exchange currency code is invalid." }'
    assert(results(g) == 'Exchange currency code is invalid.')
    g = '{ "from" : "2.5 United States Dollars", "to" : "2.0952375 Euros", "success" : true, "error" : "" }'
    assert(results(g) == 'You can get 2.0952375 Euros with 2.5 United States Dollars')
    g = '{ "from" : "", "to" : "", "success" : false, "error" : "Currency amount is invalid." }'
    assert(results(g) == 'Currency amount is invalid.')
    return True


def test_exchange():
    """This function provides tests for the function exchange.
    """
    (A, B, C) = ('USD', 'EUR', '2.5')
    assert(exchange(A, B, C) == 'You can get 2.0952375 Euros with 2.5 United States Dollars')
    (A, B, C) = ('RMB', 'EUR', '2.5')
    assert(exchange(A, B, C) == 'Source currency code is invalid.')
    (A, B, C) = ('USD', 'RMB', '2.5')
    assert(exchange(A, B, C) == 'Exchange currency code is invalid.')
    (A, B, C) = ('USD', 'EUR', 'X')
    assert(exchange(A, B, C) == 'Currency amount is invalid.')
    return True


def testall():
    """Test all cases.
    """
    test_make_up()
    test_get_from()
    test_results()
    test_exchange()
    print('All tests passed.')
    return True


def main():
    """main module
    """
    testall()
    currency_from = input('Please input the currency you have : ', )
    currency_to = input('Please input the currency you want to convert to : ', )
    amount_from = input('Please input the amount of the currency you want to convert : ',)
    last_results = exchange(currency_from, currency_to, amount_from)
    print(last_results)


if __name__ == '__main__':
    main()
