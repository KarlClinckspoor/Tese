        # ... continuação
        elif append == '2':
            oldlist = open('INPUT.LIS', 'r')  # todo: check for file missing
            contents = [line.strip() for line in oldlist]
            oldlength = int(contents[0])
            del (contents[0]) # removes the counter at the beginning of the file.
            newlength = oldlength + len(files)
            oldlist.close()

            newlist = open('INPUT.LIS', 'w')
            newlist.write(' ' + str(newlength) + '\n')
            for line in contents:
                newlist.write(' ' + line + '\n')
            for file in files:
                newlist.write(' ' + file + '\n')
            newlist.close()
            sys.exit()
        else:
            print('I did not understand.')
            sys.exit()

    if choice == '2':
        fname = input('What is the file name of the file/series you want to convert? ')
        try:
            file = open(fname, 'r')
        except FileNotFoundError:
            print('File not found. Try again.')
            sys.exit()
        content_list = list(line.rstrip() for line in file)[1:]  # Ignores the q int err line of the file.
        file.close()
        dest_filename = input('What will the destination filename be? No extension, it will be saved to .dat.' +
                              'Only 8 characters, please!').strip()
        dest_filename = dest_filename[:8] + '.dat'  # Trims to 8 characters
        convert_file(content_list, dest_filename, multiple=False)
    else:
        fname = input('What is the file name of the file/series you want to convert? ')
        files = glob.glob('*{}*'.format(fname))
        counter = 1
        filename = input('What will the destination filename be? Must have space for 2 numerals' +
                         ' (6 chars total): ').strip()
        filename = filename[:7]
        for file in files:
            dest_filename = filename + str(counter).zfill(2) + '.dat'
            fhand = open(file, 'r')
            content_list = list(line.rstrip() for line in fhand)[1:]  # Ignores the first line.
            convert_file(content_list, dest_filename)
            print('Converted {} to {}'.format(file, dest_filename))
            counter += 1
    print('Done!')