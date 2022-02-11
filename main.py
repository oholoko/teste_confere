import sys
import serialize_data


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Please send the -h argument if you need help.')
    elif '-h' in sys.argv:
        print('USAGE:')
        print('python3 main.py [FLAG]')
        print('FLAGS:')
        print('--output [FILENAME]\t\tWrite the output to [FILENAME]')
        print('--allfiles\t\t\tWrite the output to all files')
        print('--onscreenresult\t\tWrite the result screen')
        print('--onscreenlog\t\t\tWrite the log screen')
    else:
        elog = False
        log = False
        if '--onscreenlog' in sys.argv:
            elog = True
        if '--output' in sys.argv:
            if sys.argv[sys.argv.index('--output')+1] not in ('--output', '--allfiles', '--onscreenlog'):
                file = sys.argv[sys.argv.index('--output')+1]
            else:
                print('File name invalid')
        a = serialize_data.confere_data(elog=elog)
        if '--onscreenresult' in sys.argv:
            a.to_stdout()
        if '--allfiles' in sys.argv:
            a.all_files()
        if '--output' in sys.argv:
            a.all_files(file, multiple=False)
