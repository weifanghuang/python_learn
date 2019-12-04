def story(**kwds):
    return 'Once upon a time, there was a ' \
           '{job} called {name}.'.format_map(kwds)


def power(x, y, *others):
    if others:
        print('Received redundant parameters:', others)
    return pow(x, y)


def interval(start, stop=None, step=1):
    'Imittes rang() for step > 0'
    if stop is none:
        start, stop = 0, start
    result = []

    i = start
    while i < stop:
        resule.append(i)
        i += step
    return result


print(story(job='king', name='Gumby'))
