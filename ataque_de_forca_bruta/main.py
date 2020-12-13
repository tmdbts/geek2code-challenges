import itertools

lower_char_lib = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                  'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

upper_char_lib = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                  'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

int_lib = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

all = upper_char_lib + lower_char_lib + int_lib

for r in range(1, 8):
    for s in itertools.product(all, repeat=r):
        print("".join(s))
