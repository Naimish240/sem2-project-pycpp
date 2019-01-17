# compile.py
# Script that compiles and executes a .c or a .cpp file with gcc or g++ compiler
# Usage:
# python compiler.py -v <compiler> (1 for c, 2 for cpp) -i <filename> (without .c/.cpp extension) 

try:
    import sys, os, getopt, subprocess
    from pyautogui import screenshot
except:
    l = ['sys', 'os','getopt', 'pyautogui']
    for i in l:
        os.system('pip install '+ i)

def main(argv):
    # list of args[1:]
    d = {}
    code_file = ''
    exe_file = ''
    compiler = ''

    for i in range(0,len(argv),2):
        d[argv[i]] = argv[i+1]
    
    if '-v' in d.keys():
        ch = d['-v']
        if ch == 1:
            compiler = 'gcc'
        elif ch == 2:
            compiler = 'g++'
    
    if '-i' in d.keys():
        if compiler == 'gcc':
            code_file = d['-i'] + '.c'
            exe_file = d['-i'] + '.exe'
        elif compiler == 'g++':
            code_file = d['-i'] + '.cpp'
            exe_file = d['-i'] + '.exe'
    
    if '-h' in d.keys():
        usage()
    print(d)
    run(code_file, exe_file, compiler, d['-i'])
        
def usage():
    print('python compiler.py -v <compiler> (1 for c, 2 for cpp) -i <filename> (without .c/.cpp extension) ')

def run(code_file, exe_file, compiler, a):
    os.system("echo Compiling " + code_file)
    #os.system(compiler + ' ' + code_file) # + ' -o ' + exe_file)
    comm = compiler + ' ' + code_file
    subprocess.call(comm)
    # Runs if the program compiled properly
    if not os.system(compiler + ' ' + code_file): # + ' -o ' + exe_file):
        os.system("echo Compiled Successfully...")
        os.system("echo -------------------------------------")
        os.system("echo Running " + exe_file)
        os.system("echo -------------------------------------")
        subprocess.call('a.exe')
    
    screenshot(imageFilename = a + '_output.png')

if __name__=='__main__':
    print(sys.argv[1:])
    main(sys.argv[1:])