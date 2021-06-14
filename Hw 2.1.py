my_list = [(-1 + 0j), 1, 2.2, True, None, 'Sring', [3, 4],
           (5, 6, 6.5), {7: 'sven', 8: 'eight'}, {9, 10},
           frozenset(), range(11), (b'twelve'), bytearray (b'thirteen'),
           zip(*[(14,15), (16, 17), ('a', 'b')]), TypeError]

for i, item in enumerate(my_list, 1):
    print(f"{i}) {item} - {type(item)}")

# print(list(map(type, my_list)))