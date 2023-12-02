with open('day1/data/input1.txt', 'r') as f:
    data = [line.strip() for line in f.readlines()]

# get the calibration values
cal_vals=[]
for line in data:
   #traverse from left
    for ch in line:
        if ch.isdigit():
            ldigit = ch
            break
    
    for ch in reversed(line):
        if ch.isdigit():
            rdigit = ch
            break
    
    cal_vals.append(int(ldigit + rdigit))

print("Solution to part 1:")
print(sum(cal_vals)) 
    
