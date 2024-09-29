# my_bytes = bytes([num for num in range(256)])
# print(list(my_bytes))
# print(my_bytes)
printable_bytes = bytes([num for num in range(32,127)])
print(printable_bytes)
print(printable_bytes[45])
# b' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

my_ba = bytearray([num for num in range(32,127)])
print(my_ba)  # Output: bytearray(b'ABC')
my_ba[0] = 68  # Modify the first byte
print(my_ba)  # Output: bytearray(b'DBC')
print(my_ba[45])


