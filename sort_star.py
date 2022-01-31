def sort_star(array):
    array.sort()
    print()
    i=0
    b=""
    while i<len(array[0]):
        a=array[0][i]+"***"
        b=b+a
        i+=1
    print(b[0:-3])
sort_star(["bitcoin","take","over","the","world","maybe","who","knows","perhaps"])
sort_star(["turns", "out", "random", "test", "cases", "are", "easier",
"than", "writing", "out", "basic", "ones"])
sort_star(["lets", "talk", "about", "javascript", "the", "best", "language"])
sort_star(["i", "want", "to", "travel", "the", "world", "writing", "code", "one", "day"])
sort_star(["Lets", "all", "go", "on", "holiday", "somewhere", "very", "cold"])
