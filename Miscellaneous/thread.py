#
# This example shows how the high level threading module can be run tasks in
# background while the main program continues to run.
#

import threading
import zipfile


class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)


if __name__ == '__main__':
    import sys

    def usage():
        print('Usage: python thread.py infile outfile')
        print('\tinfile : input file to be process.')
        print('\toutfile: processed output file')

    if len(sys.argv) == 3:
        background = AsyncZip(sys.argv[1], sys.argv[2])
        background.start()
        print('The main program continues to run in foreground.')

        background.join()
        print('Main program waited until background was done.')
    else:
        usage()
