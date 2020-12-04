import re

# group each passport to a single consecutive string
# removes the new lines
def group_all_passports(passport_file):
    all_passports = ['']
    
    for line in passport_file:
        line = line.rstrip()
        if len(line) == 0:
            all_passports.append('')
        all_passports[-1] += ' ' + line

    return all_passports
        

def validate_passport(fields):
    if len(fields) < 7 or len(fields) == 7 and 'cid' in fields:
        return False

    for identifier, value in fields.items():
        if identifier == 'byr':
            birth_year = int(value)
            if not (1920 <= birth_year <= 2002):
                return False
        elif identifier == 'iyr':
            issue_year = int(value)
            if not (2010 <= issue_year <= 2020):
                return False                
        elif identifier == 'eyr':
            expiration_year = int(value)
            if not (2020 <= expiration_year <= 2030):
                return False
        elif identifier == 'hgt':
            height = re.findall('\d+|\w+', value)
            if len(height) != 2:
                return False
            unit = height[1]
            height = int(height[0])
            if unit == 'cm':
                if not (150 <= height <= 193):
                    return False
            elif unit == 'in':
                if not (59 <= height <= 76):
                    return False
        elif identifier == 'hcl':
            if not re.search('^#(?:[0-9a-fA-F]{3}){1,2}$', value):
                return False
        elif identifier == 'ecl':
            if value not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                return False
        elif identifier == 'pid':
            if len(value) != 9 or not re.search('^\d{9}', value):   
                return False
            print(identifier, value)

    return True            
        
                
def count_valid_passports(passports):
    valid_passports_count = 0

    for passport in passports:
        split_fields = passport.split(' ')
        fields = {}
        for field in split_fields:
            if not field:
                continue
            identifier, value = field.split(':')
            fields[identifier] = value

        if validate_passport(fields):
            valid_passports_count += 1        

    return valid_passports_count

#passport_file = open('input_4_small.txt', 'r')
passport_file = open('input_4.txt', 'r')

all_passports = group_all_passports(passport_file)
valid_passports_count = count_valid_passports(all_passports)
print(valid_passports_count)
    
