import re
rawpassports=(
'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\n',
'byr:1937 iyr:2017 cid:147 hgt:183cm\n',
'\n',
'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884\n',
'hcl:#cfa07d byr:1929\n',
'\n',
'hcl:#ae17e1 iyr:2013\n',
'eyr:2024\n',
'ecl:brn pid:760753108 byr:1931\n',
'hgt:179cm\n',
'\n',
'hcl:#cfa07d eyr:2025 pid:166559648\n',
'iyr:2011 ecl:brn hgt:59in\n')

def hgt_valid(hgt):
    if hgt[-2:]=="cm" and int(hgt[:-2])>=150 and int(hgt[:-2])<=193:
        return True
    if hgt[-2:]=="in" and int(hgt[:-2])>=59 and int(hgt[:-2])<=76:
        return True
    else:
        return False

def hcl_valid(hcl):
    cond=re.match('^#[0-9a-f]{6}',hcl)
    if cond:
        return True
    else:
        return False

def ecl_valid(ecl):
    valid_colors=('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
    if ecl in valid_colors:
        return True
    else:
        return False

def pid_valid(pid):
    cond=re.match('^[0-9]{9}$',pid)
    if cond:
        return True
    else:
        return False
    

fname=open("C://Users/Mark/Documents/Advent of Code/2020/input_day4.txt")
rawpassports = fname.readlines()
fname.close()

passports=list(rawpassports)
passports.append('\n')


dataset={}
count=0
for entry in passports:
    a=entry.split()
    if a:
        #print(a)
        for field in a:
            pair=field.split(':')
            key=pair[0]
            value=pair[1]
            dataset[key]=value
            #print(dataset)
        
    if not a:
        if 'byr' in dataset and 'iyr' in dataset and 'eyr' in dataset and 'hgt' in dataset and 'hcl' in dataset and 'ecl' in dataset and 'pid' in dataset:
            byrvalid=int(dataset['byr'])>=1920 and int(dataset['byr'])<=2002
            iyrvalid=int(dataset['iyr'])>=2010 and int(dataset['iyr'])<=2020
            eyrvalid=int(dataset['eyr'])>=2020 and int(dataset['eyr'])<=2030
            hgtvalid=hgt_valid(dataset['hgt'])
            hclvalid=hcl_valid(dataset['hcl'])
            eclvalid=ecl_valid(dataset['ecl'])
            pidvalid=pid_valid(dataset['pid'])
            #print('byrvalid',byrvalid, dataset['byr'])
            #print('iyrvalid',iyrvalid, dataset['iyr'])
            #print('eyrvalid',eyrvalid, dataset['eyr'])
            #print('hgtvalid',hgtvalid, dataset['hgt'])
            #print('hclvalid',hclvalid, dataset['hcl'])
            #print('eclvalid',eclvalid, dataset['ecl'])
            #print('pidvalid',pidvalid, dataset['pid'])
            if byrvalid and iyrvalid and eyrvalid and hgtvalid and hclvalid and eclvalid and pidvalid:
                print(dataset)
                print('Valid passport')
                count=count+1
                print(count)
        #    else:
        #        print(dataset)
        #        print('Invalid passport')
        #else:
        #    print(dataset)
        #    print('Invalid passport')
        #print("New Record")
        dataset.clear()

print('Number of valid passports is',count)
