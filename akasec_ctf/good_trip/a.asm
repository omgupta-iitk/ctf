section .text
    global _start

_start:
    mov rax, 1          ; syscall number for sys_write
    mov rdi, 1          ; file descriptor 1 (stdout)
    mov rsi, message    ; pointer to message
    mov rdx, 13         ; length of message
    syscall             ; invoke the kernel

    mov rax, 60         ; syscall number for sys_exit
    xor rdi, rdi        ; exit code 0
    syscall             ; invoke the kernel

section .data
message db 'Hello, world!', 0xA  ; the message with a newline character
