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
    wd = ""

    def __init__(self, path):
        self.wd = ''
        self.img = path


    def execute(self, zipfile):
       sys_files = zipfile.namelist()
       print(sys_files)

    def build_hierarchy_tree():
        print()

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
