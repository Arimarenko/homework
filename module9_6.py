def all_variants(text):
    for x in range(len(text)):
        for l in range(len(text) - x):
            yield text[l:l + x + 1]


a = all_variants("abc")
for i in a:
    print(i)
