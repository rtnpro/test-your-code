import sys


def fizzbuzz(n):
    """Time to play fizzbuzz.

    >>> fizzbuzz(1)
    '1'
    >>> fizzbuzz(0)
    Traceback (most recent call last):
      ...
    ValueError: Value of zero is undefined
    """
    if n == 0:
        raise ValueError('Value of zero is undefined')
    result = ''
    if n % 3 == 0:
        result += 'Fizz'
    if n % 5 == 0:
        result += 'Buzz'
    return result or str(n)


def main(output=sys.stdout):
    for n in range(1, 101):
        output.write('%s\n' % fizzbuzz(n))


if __name__ == '__main__':
    main()

