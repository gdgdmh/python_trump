#!/usr/bin/env python
"""エントリーポイント"""
from python_trump import trump


def main():
    print('main')
    trump_test = trump.Trump(trump.Trump.SPADE, 2)
    trump_test.print_string()


if __name__ == '__main__':
    main()
