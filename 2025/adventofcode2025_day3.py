fname='input_day3.txt'
# fname='example_day3.txt'

with open(fname) as fp: data = fp.read().splitlines()

total=0
total2=0
for bank in data:
    first = max(bank[:-1])
    firstidx = bank.index(first)
    second = max(bank[firstidx+1:])
    total+=int(first+second)

    tomatch=12
    joltage=''
    test=bank
    while tomatch>1:
        largest = max(test[:-tomatch+1])
        largestidx = test.index(largest)
        test=test[largestidx+1:]
        joltage=joltage+largest
        tomatch-=1
    joltage=joltage+max(test)
    total2+=int(joltage)

print('Part 1 is', total)
print('Part 2 is', total2)
