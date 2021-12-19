import sys
sys.path.append("..")
from packet import Packet, hex2bin

lines = [line.strip() for line in open("Day16.txt")]
# lines = list(map(int, list))
tr = lines[0]
tr = hex2bin(tr)

p = Packet(tr)
print(p.evaluate()[0])
