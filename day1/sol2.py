with open('day1/data/input1.txt', 'r') as f:
    data = [line.strip() for line in f.readlines()]


valid_str_digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

# get the calibration values
cal_vals=[]
for line in data:
    ldigit = None
    rdigit = None
   #traverse from left
    lsub_str = ""
    rsub_str = ""
    for ch in line:
        if ch.isdigit():
            ldigit = ch
            break
        
        lsub_str += ch
        for str_digit in valid_str_digits:
            if str_digit in lsub_str:
                ldigit = str(valid_str_digits[str_digit])
                break

        if ldigit:
            break
    
    for ch in reversed(line):
        if ch.isdigit():
            rdigit = ch
            break
        
        rsub_str = ch + rsub_str
        for str_digit in valid_str_digits:
            if str_digit in rsub_str:
                rdigit = str(valid_str_digits[str_digit])
                break
        
        if rdigit:
            break

    cal_vals.append(int(ldigit + rdigit))

print("Solution to part 2:")
print(sum(cal_vals)) 