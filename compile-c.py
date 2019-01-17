# compile_c.py
# Script that compiles and executes a .cpp file with g++ compiler
# Usage:
# python compile_c.py -i <filename> (without .c extension)

import sys, os, getopt
from pyautogui import screenshot

def main(argv):
    c_file = ''
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
            c_file = a + '.c'
            exe_file = a + '.exe'
            run(c_file, exe_file, a)

def usage():
    print('compile-c.py -i <filename> (without .c extension)')

def run(c_file, exe_file, a):
    os.system("echo Compiling " + c_file)
    os.system('gcc ' + c_file + ' -o ' + exe_file)
    
    # Runs if the program compiled properly
    if not os.system('gcc ' + c_file + ' -o ' + exe_file):
        os.system("echo Compiled Successfully...")
        os.system("echo -------------------------------------")
        os.system("echo Running " + exe_file)
        os.system("echo -------------------------------------")
        os.system(exe_file)
    
    screenshot(imageFilename = a + '_output.png')

if __name__=='__main__':
    main(sys.argv[1:])
