import sys

print {'big': 'BigEndian', 'little': 'LittleEndian'}.get(sys.byteorder)