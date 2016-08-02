def genPrimes():
    primes = []   # primes generated so far
    last = 1      # last number tried
    while last < 50:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            yield last