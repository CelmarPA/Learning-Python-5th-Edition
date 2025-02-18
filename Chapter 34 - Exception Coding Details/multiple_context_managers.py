with open('data') as fin, open('res', 'w') as fout:
    for line in fin:
        if 'some key' in line:
            fout.write(line)

with open('script1.py') as f1, open('script2.py') as f2:
    for pair in zip(f1, f2):
        print(pair)

with open('script1.py') as f1, open('script2.py') as f2:
    for (linenum, (line1, line2)) in enumerate(zip(f1, f2)):
        if line1 != line2:
            print('%s\n%r\n%r' % (linenum, line1, line2))

for pair in zip(open('script1.py'), open('script2.py')):            # Same effect, auto close
    print(pair)

with open('script2.py') as fin, open('upper.txt', 'w') as fout:
    for line in fin:
        fout.write(line.upper())

print(open('upper.txt').read())

fin = open('script2.py')
fout = open('upper.txt', 'w')

for line in fin:                            # Same effect as preceding code, auto close
    fout.write(line.upper())

fin = open('script2.py')
fout = open('upper.txt', 'w')

try:                                        # Same effect but explicit close on error
    for line in fin:
        fout.write(line.upper())
finally:
    fin.close()
    fout.close()
