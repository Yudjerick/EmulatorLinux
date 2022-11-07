import sys
import zipfile

class TreeRoot:
    def __init__(file_name):
        self.children = []
        self.name = file_name

class Node:
    def __init__(file_name, parent):
        self.name = file_name
        self.children = []
        self.parent = parent
        parent.children.append(self)

class Emulator:

    def __init__(self, path):
        #self.wd = ' '
        self.img = path


    def execute(self, zipfile):
        namelist = zipfile.namelist()
        wd = namelist[0].split('/')[0] + '/'
        print(namelist)

        while(True):
            if('/' not in wd[:-1]):
                invite = '~'
            else:
                invite = wd.split('/')[len(wd.split('/'))-2]
            comand = input('root@localhost:'+ invite +' $ ')
            words = comand.split()
            if(len(words) == 0):
                break
                #continue
            elif words[0] == 'pwd':
                print('/' + wd[:-1])
            elif words[0] == 'ls':
                items = []
                for i in namelist:
                    if wd in i:
                        item = i[len(wd):].split('/')[0]
                        if(item not in items and item):
                            items.append(item)
                print(' '.join(items))
            elif words[0] == 'cat' and len(words) == 2:
                path = wd + words[1]
                if(path in namelist):
                    with zipfile.open(path) as myfile:
                        content = myfile.read()
                        print(content.decode('utf-8'))
            elif words[0] == 'cd' and len(words) == 2:
                if words[1] == '.':
                    continue
                elif words[1] == '..':
                    wd_splt = wd.split('/')
                    wd_splt.pop()
                    wd_splt.pop()
                    wd = '/'.join(wd_splt) + '/'
                if words[1][0] == '/':
                    nwd = words[1][1:] + '/'
                    if nwd in namelist:
                        wd = nwd
                else:
                    nwd = wd + words[1] + '/'
                    if nwd in namelist:
                        wd = nwd

    def run_emulation(self):
        try:
            with zipfile.ZipFile(self.img) as system:
                self.execute(system)
        except Exception as ex:
            print(ex)




if __name__ == '__main__':
    if len (sys.argv)!=2:
        print("Invalid argument")
    else:
        em = Emulator (sys.argv[1])
        em.run_emulation()
