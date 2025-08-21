M_list = []

for i in range(9):
    a = int(input())
    M_list.append(a)

print(max(M_list))
print(M_list.index(max(M_list))+1)
