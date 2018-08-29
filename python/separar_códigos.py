import glob
import sys

file_ = sys.argv[1]

try:
    contents = open(file_, 'r').read().split('\n')
except OSError:
    print('File not found. Try again.')

line_to_sep = 66
sections = []
parts = 0

for i, line in enumerate(contents):
    if i % line_to_sep == 0:
        for j in range(5):
            if contents[i + j] == '\n':
                sections.append(contents[parts * line_to_sep:(parts+1) * line_to_sep + j])
                parts += 1
                print('Found one')
                break
            elif contents[i - j] == '\n':
                sections.append(contents[parts * line_to_sep:(parts+1) * line_to_sep - j])
                parts += 1
                print('Found one')
                break
        else:
            sections.append(contents[parts * line_to_sep:(parts+1) * line_to_sep])
            parts += 1
            print('Not found')

for i, section in enumerate(sections):
    dest = open(file_[:-4] + f'_parte{i}.py', 'w')
    dest.write('\n'.join(section))
    dest.close()

