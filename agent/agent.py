import sys
import requests
import urllib.parse


print(str(sys.argv[1]))
file1 = open(str(sys.argv[1]), 'r')
for line in file1:
    urllib.parse.quote(line)
    r = requests.post('http://127.0.0.1:8000',data = line, verify=False)