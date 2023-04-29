import os 

data = ''
dsy = input('File Name: ')
ic = input('Icon: ')
fi = input('Onefile: [Y/N]')

if fi.upper() == 'Y':
    fi = '--onefile'
else:
    fi = ''

if ic != '':
    ic = '--icon=' + ic
c = input('Console: [Y/N]')
while True:
    dat = input('Data: [Enter To No Data]')

    if dat != '':
        if data != '':
            data = f'{data} --add-data "{dat};."'
        else:
            data = f'--add-data "{dat};."'
    else:
        break


c = c.upper()

if c == 'Y':
    c = ''
else:
    c = '--noconsole'

#os.system('pyinstaller --onefile --icon=' + ic + ' ' +  dsy)

command = f'pyinstaller {fi} {c} {ic} {data} {dsy}'
command = command.replace('  ', ' ')
command = command.replace('  ', ' ')

print(command)

os.system(command)

if dsy.endswith('.py'):
    folder = dsy.replace('.py', '')
else:
    folder = dsy.replace('.pyw', '')

for file in os.listdir():
    if file.endswith('.spec'):
        print(file)
        os.remove(file)
    if file == 'build':
        cw = os.getcwd()
        os.chdir('build')
        cwd = os.getcwd()
        os.chdir(folder)

        cwdd = os.getcwd() #saved location of file named folder
        os.chdir('localpycs')
        for file in os.listdir():
            os.remove(file)
        
        os.chdir(cwdd)
        print(os.listdir())
        os.rmdir('localpycs')

        for file in os.listdir():
            os.remove(file)
        os.chdir(cwd)
        os.rmdir(folder)
        os.chdir(cw)
        os.rmdir('build')

input('Completed. Enter To Quit')