def fetcher(obj, index):
    return obj[index]

if __name__ == '__main__':
    x = 'spam'

    print(fetcher(x, 3))

    try:
        fetcher(x, 4)

    except IndexError:
        print('got exception')

    print('continuing')

    try:
        raise IndexError
    except IndexError:
        print('got exception')
