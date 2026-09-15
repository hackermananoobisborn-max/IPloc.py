# IPloc.py

IPLoc is a terminal based,lightweight program, built to integrate with an ip2location.io API key to interface their backend for location enumeration of IP addresses 
Features 
* Light and portable 
* Generates a link for satellite view of the target ip
* Accepts target as link, ip4 and domain names 
* Two modes of input single mode and batch mode for scanning multiple targets in a file
* Creates a  simple log file to store your scanned Targets named Log.txt 
 * stores your api key so you don't have to manually input it after first run

#How to install

Gitclone the repo into any directory of your choice you would like to run this program from and then the install its only dependency python3
Link to install python3: https://www.python.org/downloads/

#How to use 

for api key storeage create apikey.txt in the current gitcloned directory 
then simple run the program against python3 as so 

Python3 iploc.py 
and input your target and api key,
for batch mode run the program against python3 and your txt file containing a list of targets with no indentations and then input the api key to be stored if not done already,you can give a list of links,ips or domain names
e.g python3 IPloc.py target.txt
Note that to get an ip2location api key you need to sign up to their website  and then you will receive a free key for use.
Link to get api key: www.ip2location.io
