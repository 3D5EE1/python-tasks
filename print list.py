# question: list = [1, 2, 3, 4, 'q', '{', 'r', 'T', ']', 'nhg', '1r#', ]
# result: 1, 2, 3, 4, q, {, r, T, ], nhg, 1r#.

list_ = [1, 2, 3, 4, 'q', '{', 'r', 'T', ']', 'nhg', '1r#', ]

print(*list_[:-1], str(list_[-1]) + '.', sep=', ')
