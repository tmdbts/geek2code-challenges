import itertools
import string

ascii_letters_lib = string.ascii_letters

int_lib = str(1234567890)

all = ascii_letters_lib + int_lib

k = int(input('Insert the length of the password '))

for s in itertools.product(all, repeat=k):
    print("".join(s))
