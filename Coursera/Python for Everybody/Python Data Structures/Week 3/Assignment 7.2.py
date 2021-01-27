# Use the file name mbox-short.txt as the file name
import re
fname = "text.txt"
list_number = []
count = 0
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    try:
        number = re.match('(X-DSPAM-Confidence:\s*)(\d*.\d*)', line)
        list_number.append(number.group(2))
        count += 1
        print(line)
    except Exception as e:
        print("error occurred")
new_list = []
for i in list_number:
    i = float(i)
    new_list.append(i)
print(sum(new_list)/len(new_list))
print(count)
