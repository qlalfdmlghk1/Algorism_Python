word = input()
alpha = ["dz=", "lj", "nj", "c=", "c-", "d-", "s=", "z="]
alpha2 = []

for a in alpha :
    word = word.replace(a,"*")
    # print(word)

# for a2 in alpha2 :
#     word = word.replace(a2,"**")

print(len(word))
