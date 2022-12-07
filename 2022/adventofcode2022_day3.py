fname="day3_example.txt"
fname="input_day3.txt"
with open(fname) as fp: data = fp.read().splitlines()

score="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

prioritytotal=0

for record in data:
    rucksack1=record[:len(record)//2]
    rucksack2=record[-len(record)//2:]
    for letter in set(rucksack1):
        if letter in rucksack2:
            priority=score.index(letter)+1
            prioritytotal+=priority
            
print("Part 1 solution is",prioritytotal)


prioritytotal=0

for i in range(0,len(data),3):
    for letter in set(data[i]):
        if letter in data[i+1] and letter in data[i+2]:
            priority=score.index(letter)+1
            prioritytotal+=priority

print("Part 2 solution is",prioritytotal)
