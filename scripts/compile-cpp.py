# compile_cpp.py
# Script that compiles and executes a .cpp file with g++ compiler
# Usage:
# python compile_cpp.py -i <filename> (without .cpp extension)

import sys, os, getopt
from pyautogui import screenshot

def main(argv):
    cpp_file = ''
    exe_file = ''
    try:
        opts, args = getopt.getopt(argv, "hi:",["help",'ifile='])
    except getopt.GetoptError as err:
        # print help information and exit
        print(err)      
        usage()
        sys.exit(2)
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-i", "--ifile"):
            cpp_file = a + '.cpp'
            exe_file = a + '.exe'
            run(cpp_file, exe_file, a)


def usage():
    print('run_cpp.py -i <filename> (without .cpp extension)')

def run(cpp_file, exe_file, a):
    os.system("echo Compiling " + cpp_file)
    os.system('g++ ' + cpp_file + ' -o ' + exe_file)
    
    # Runs if the program compiled properly
    if not os.system('g++ ' + cpp_file + ' -o ' + exe_file):
        os.system("echo Compiled Successfully...")
        os.system("echo -------------------------------------")
        os.system("echo Running " + exe_file)
        os.system("echo -------------------------------------")
        os.system(exe_file)
    
    screenshot(imageFilename = a + '_output.png')

if __name__=='__main__':
    main(sys.argv[1:])
