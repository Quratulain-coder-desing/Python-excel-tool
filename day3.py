classitems=["pen" , "copy" , "book", "bag", "scale"]

print(classitems)

 
for cheez in  classitems:
 if "o" in cheez:
    print("cheez", cheez)
 
classitems.sort()
print("list after sort", classitems)
classitems.reverse()
print("list after reverse", classitems)
