# compile.py
# Script that compiles and executes a .c or a .cpp file with gcc or g++ compiler
# Usage:
# python compiler.py -v <compiler> (1 for c, 2 for cpp) -i <filename> (without .c/.cpp extension) 

import sys, os, getopt
from pyautogui import screenshot

# Installs all dependencies
def setup_stuff():
    l = ['sys', 'os','getopt', 'pyautogui']
    for i in l:
        os.system('pip install '+ i)

def main(argv):
    code_file = ''
    exe_file = ''
    compiler = ''
    try:
        opts, args = getopt.getopt(argv, "hi:",["help",'ifile='])
    except getopt.GetoptError as err:
        # print help information and exit
        print(err)      
        usage()
        sys.exit(2)
    for o, a in opts:
        # Prints help menu
        if o in ("-h", "--help"):
            usage()
            sys.exit()

        # Gives compiler to use    
        elif o in ("-v", "--vfile"):
            if a == 1:
                compiler = 'gcc'
            elif a == 2:
                compiler = 'g++'

        # Compiles and executes the code        
        elif o in ("-i", "--ifile"):
            code_file = a + '.cpp'
            exe_file = a + '.exe'
            run(code_file, exe_file,compiler, a)


def usage():
    print('python compiler.py -v <compiler> (1 for c, 2 for cpp) -i <filename> (without .c/.cpp extension) ')

def run(code_file, exe_file, a, compiler):
    os.system("echo Compiling " + code_file)
    os.system(compiler + code_file + ' -o ' + exe_file)
    
    # Runs if the program compiled properly
    if not os.system(compiler + code_file + ' -o ' + exe_file):
        os.system("echo Compiled Successfully...")
        os.system("echo -------------------------------------")
        os.system("echo Running " + exe_file)
        os.system("echo -------------------------------------")
        os.system(exe_file)
    
    screenshot(imageFilename = a + '_output.png')

if __name__=='__main__':
    print(sys.argv)
    main(sys.argv[1:])
