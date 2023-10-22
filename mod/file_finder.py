import os, socket

class file_browse:
    def __init__(self):
        self.path = os.getcwd()

        print(self.path)
    
    def start(self):
        running = True
        while running:
            print("\x1B[2J\x1B[1;1H")
            cur_js = self.list_files()

            print("[  FILE NAME  ]---[  DIR  ]")
            for file in cur_js:
                print(file, " -> ", cur_js[file]["dir"])

            print("[ESC:Back Dir]-[*FILE/DIR*:select]")
            inp = input("╭─DISPUTE@"+socket.gethostname()+" ("+self.path+")\n╰─$")
            if inp.lower() == "esc":
                self.path = self.back_dir()
            else:
                for i in cur_js:
                    if cur_js[i]["file"] == inp:
                        if cur_js[i]["dir"] == True:
                            self.path = self.path + "/" + inp
                        else:
                            txt = "[Y/N] Use -> ", i, "-? "
                            chk = input(txt)
                            if "y" in chk.lower():
                                return self.path+"/"+i
                            


    def list_files(self):
        js = {}
        for file in os.listdir(self.path):
            js[file] = {"path": self.path, "dir": self.chk_dir(self.path+"/"+file), "file": str(file)}
        
        return js

    def chk_dir(self, file) -> bool:
        if os.path.isdir(file):
            return True
        return False
    
    def back_dir(self):
        path = self.path
        path = path.split("/")
        _ = path.pop()

        return "/".join(path)