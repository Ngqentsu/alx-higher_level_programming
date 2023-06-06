#!/usr/bin/python3
toggle_n = 0
for char in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(char - toggle_n)), end="")
    toggle_n = 32 if toggle_n == 0 else 0
