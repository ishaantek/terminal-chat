import os
os.system("nc -lk 12345 | nc $(ipconfig getifaddr en0) 12345")