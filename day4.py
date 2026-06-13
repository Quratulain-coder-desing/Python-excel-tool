classitems=["pen" , "copy" , "book", "bag", "scale"]
print(classitems)
print("total classitems", len(classitems))
classitems.append("eraser")
print("new list", classitems)
for cheez in  classitems:
 if "o" in cheez:
    print("cheez", cheez)
for i in range(len(classitems)):  
 print(i+1, ".", classitems[i])
classitems.sort()
print("list after sort", classitems)
classitems.reverse()
print("list after reverse", classitems)
