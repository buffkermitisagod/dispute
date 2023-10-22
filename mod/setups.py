import json, os


class setup:
    def __init__(self) -> None:
        self.stat = {
            "install": " ",
            "port": " ",
            "ip": " ",

        }
        self.config = {
            "setup": True,
            "server": {
                "port": 8080,
                "ip": "127.0.0.1",
                "version": "V0.1",
            }
        }
    def run(self):
        self.install_commands()
        self.port()
        self.ip()

        file = open("config.json", "w")
        file.write(json.dumps(self.config, indent=4))
        file.close()
    def install_commands(self):
        self.print_menu()
        os.system("sudo apt install python3-pip")
        os.system("pip3 install flask")
        self.stat["install"] = "X"
    def print_menu(self):
        print("""
\x1B[2J\x1B[1;1H
                    [CONFIG]      
        Welcome to file home setup
            
        Setup:
            ["""+self.stat["install"]+"""] Install
            ["""+self.stat["port"]+"""] Port - """, self.config["server"]["port"],"""
            ["""+self.stat["ip"]+"""] Ip - """+self.config["server"]["ip"]+"""

        """)
    def port(self):
        self.print_menu()
        run = True
        while run:
            port = input("Please enter a port to run on (999 - 9999) : ")
            try:
                if int(port) < 999:
                    print("are you sure? this will require root preivliges? ")
                    chk = input("[Y/N] : ")
                    if chk.lower() == "y" or "yes":
                        run = False
                        self.config["server"]["port"] = int(port)
                elif int(port) > 9999:
                    print("Must be below 9999!")
                else:
                    run = False
                    self.config["server"]["port"] = int(port)
            except ValueError:
                print("Must be a number!")
        
        self.stat["port"] = "X"
    def ip(self):
        self.print_menu()

        run = True
        while run:
            ip = input("1) no internet [127.0.0.1]\n2) internet [0.0.0.0]\n -> ")
            if ip == "1":
                run = False
                self.stat["ip"] = "X"
                self.config["server"]["ip"] = "127.0.0.1"
            elif ip == "2":
                run = False
                self.stat["ip"] = "X"
                self.config["server"]["ip"] = "0.0.0.0"
            else:
                print("please enter an option")
    def users(self):
        self.print_menu()
        
        run = True
        while run:
            print("User maker (this will repeat until you type 'quit')")
            name = input("Please enter username: ")
            if name == "quit":
                print("Setup complete!")
                print("starting...")
                run = False
            elif name in os.listdir("files/data/user"):
                print("name already in use!")
            else:
                pas = input("Please enter password: ")
                js = {
                    "pas": pas,
                    "coc": ""
                }
                file = open("files/data/user/"+name+".json", "x+")
                file.write(json.dumps(js, indent=4))
                file.close()
            
    def return_config(self):
        return json.loads(open("config.json", "r").read())["server"]

