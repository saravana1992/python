st = [1, 2, 3, 1, 2]
duplicate = []
for sts in st:
    if sts not in duplicate:
        duplicate.append(sts)
print(duplicate)

# sort a string or number in list

st.sort()
print(st)

# reserve a string

st.reverse()
print(st)

# string or number there or not

if 21 in st:
    print("its there")

# Copy

sts = st[:]
print(sts)

## or

sts= st.copy()
print(sts)

# Count

print(st.count(1))




