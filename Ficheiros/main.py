"""
ler e escrever em ficheiros de txt e bin

r - read
a- append
w - write
x - create

--------------

t - txt
b - bin

"""

file = open("ficheiros.txt", "w")

file.write("hello world\n")
file.write("hello world\n")
file.write("hello world2\n")
file.write("hello world3\n")

file.close()