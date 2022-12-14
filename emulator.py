import sys
import zipfile

def execute(zipfile):
    namelist = zipfile.namelist()
    for i in range(len(namelist)):
        namelist[i] = '/' + namelist[i]
    wd = '/' + namelist[0].split('/')[1] + '/'
    namelist.append(wd)
    namelist.append('/')
    root_lvl = '/'
    #print(namelist)
    #print(wd)
    while(True):
        if(wd ==  '/'):
            invite = '/'
        elif('/' not in wd[1:-1]):
            invite = '~'
        else:
            invite = wd.split('/')[len(wd.split('/'))-2]
        comand = input('root@localhost:'+ invite +' $ ')
        words = comand.split()
        if(len(words) == 0):
            break
        elif words[0] == 'pwd':
            if(wd == '/'):
                print(wd)
            else:
                print(wd[:-1])
        elif words[0] == 'ls':
            items = []
            for i in namelist:
                if wd in i:
                    item = i[len(wd):].split('/')[0]
                    if(item not in items and item):
                        items.append(item)
            print(' '.join(items))
        elif words[0] == 'cat' and len(words) == 2:
            path, pathtype = parse_path(words[1],wd[:-1],namelist)
            if(pathtype == 'file'):
                with zipfile.open(path[1:]) as myfile:
                    content = myfile.read()
                    print(content.decode('utf-8'))
            elif(pathtype == 'directory'):
                print('cat:' + path + ': it is not file')
            else:
                print('cat:' + words[1] + ': no such file or directory')
        elif words[0] == 'cd' and len(words) == 2:
            if words[1][0] == '/':
                path, pathtype = parse_path(words[1][1:],'',namelist)
            else:
                path, pathtype = parse_path(words[1],wd[:-1],namelist)
            if(pathtype == 'directory'):
                wd = path + '/'
            elif(pathtype == 'file'):
                print('cd:' + path + ': it is not directory')
            else:
                print('cd:' + words[1] + ': no such file or directory')
        else:
            print('not a command')
            
def parse_path(path, wd, namelist):
    #print('path: '+ path+' wd: ' + wd)   
    if path == '':
        if wd + '/' in namelist :
            return wd,'directory'
        elif wd in namelist:
            return wd, 'file'
        else:
            return 'x',''
    command = path.split('/')[0]
    #print('command= ' + command)
    if command == '.' :
        None
    elif command == '..':
        try:
            wd = wd[:wd.rindex('/')]
        except:
            return wd, 'directory'
    else:
        wd += '/' + command
    if wd + '/' in namelist or wd in namelist:
        if path.find('/') == -1:
            path = ''
        else:
            path = path[path.find('/')+1:]
        return parse_path(path, wd, namelist)
    else:
        return 'n',''

def run_emulation(archive):
    try:
        with zipfile.ZipFile(archive) as system:
            execute(system)
    except Exception as ex:
        print(ex)

#run_emulation('fs.zip')


if __name__ == '__main__':
    if len (sys.argv)!=2:
        print("Invalid argument")
    else:
        run_emulation(sys.argv[1])