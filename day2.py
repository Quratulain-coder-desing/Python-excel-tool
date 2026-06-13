classitems=["pen" , "copy" , "book", "bag", "scale"]
cheez=["pen" , "copy" , "book", "bag", "scale"]
print(classitems)
classitems.append("eraser")
print("new list", classitems)

for i in range(len(classitems)):
 print(i+1, ".",classitems[i])
   
classitems.sort()
print("list after sort", classitems)
classitems.reverse()
print("list after reverse", classitems)
