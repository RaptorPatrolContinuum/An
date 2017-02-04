m = 3
size = len(["A","B","C"]) ** 2
print("size is ",size)
for wtf in range(0,2):
    print("wtf??", wtf)
    #size = 2 ** size
    size = 1 << size
    print("enum size is", size)
    #size = 5
print("last size is", size)

