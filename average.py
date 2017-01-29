from pip._vendor.distlib.compat import raw_input

fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"): continue
    index = line.find('0')
    line = line[index:]
    line = float(line)
    for line in [line]:
        total = total + line
    total = float(total)
    for line in [fh]:
        count = count + 1
    count = float(count)
    ave = total / count
print
"Average spam confidence:", ave
