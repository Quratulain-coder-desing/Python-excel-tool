color=("pink" , "blue" , "yellow" , "red")
print(color)
print("color:", len(color))
for colo in color:
    if "o" in colo:
        print("color", colo)
for i in range(len(color)):
   print(i+1, ".", color[i])
fir=list(color)
fir.reverse()
print("reverse list", fir)
ulta=color[:: -1]
print("sort list", ulta)
print("list", color[-2])
fir=list(color)
fir.sort()
print("sorted list", fir)
