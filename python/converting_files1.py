import glob
import sys

def convert_file(list_contents, dest_filename, multiple=True):
    """Gets the file contents as a list and writes two dummy headers, the number of points and then closes the \
    destination file. By default it will do a series of files and not ask the the comment lines."""
    fdest = open(dest_filename, 'w', encoding='utf-8')
    if multiple:
        comm1 = 'nothing special'
        comm2 = 'nothing special'
    else:
        comm1 = input('What is the first line of comments?')
        comm2 = input('What is the second line of comments?')

    length = len(list_contents)
    fdest.write(comm1 + '\n')
    fdest.write(comm2 + '\n')
    fdest.write(str(length) + '\n')
    for line in list_contents:
        fdest.write(line + '\n')
    fdest.close()
    return


# todo: find out the max length of the list and warn the user. Is it 59?
if __name__ == '__main__':
    choice = input('Do you want to convert a series of experiments [1, def] or a single one [2]?'
                   + '\nYou can also [list] all files in the directory'
                   + '\nAnd create a list file to [batch] treatment\nChoice: ')
    if choice == 'list:':
        files = glob.glob('*.*')
        print(*files)
    if choice == 'batch':  # todo: do not insert directories into the input.lis
        append = input('Do you want to [1] create a new list or [2] append to a new one?')
        fname = input('What is the file name of the file/series you want to batch treat? ')
        files = glob.glob('*{}*'.format(fname))
        if append == '1':
            newlist = open('INPUT.LIS', 'w')
            newlist.write(' ' + str(len(files)) + '\n')
            for file in files:
                newlist.write(' ' + file + '\n')
            newlist.close()
            sys.exit()
            # ... continua