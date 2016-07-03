def radiationExposure(start, stop, step):
    def frange2(start, end=None, inc=None):
        "A range function, that does accept float increments..."

        if end == None:
            end = start + 0.0
            start = 0.0
        else:
            start += 0.0  # force it to be a float

        if inc == None:
            inc = 1.0

        count = int((end - start) / inc)
        if start + count * inc != end:
            # need to adjust the count.
            # AFAIKT, it always comes up one short.
            count += 1

        L = [None, ] * count
        for i in xrange(count):
            L[i] = start + i * inc

        return L

    sum = 0
    for i in frange2(start,stop,step):
        sum += f(i) * step
    return sum
