# This script allows you to compute url content code for Odyssey.
# It does this by first hashing the url's contents and then 
# summing up the hash in decimal. Please put the identical url
# that you are using for the job website, as the only argument to
# the python code. If the code is 484 that means an error occured,
# check website and try again.
#
# Best of Luck,
# Willie McClinton

import os
from hashlib import sha256
import sys

try:
    assert len(sys.argv) == 2
except AssertionError:
    raise Exception("Missing website url try running: python url2code.py {webiste-url}")

url = sys.argv[1]
output_stream = os.popen("curl " + url)
urlcontent = output_stream.read()
hex = sha256(urlcontent.encode('utf-8')).hexdigest()
print(hex)

hex_sum = 0
for c in hex:
    hex_sum += int(c, 16)
print("If code is 484 please check website and try again.")
print("URL content code:", hex_sum)
