def points(games):
    b=0
    i=0
    while i<len(games):
        if games[i][0]>games[i][2]:
            b+=3
        elif games[i][0]<games[i][2]:
            b+=0
        elif games[i][0]==games[i][2]:
            b+=1
        i+=1
    return b
print(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']))
print(points(['1:1','2:2','3:3','4:4','2:2','3:3','4:4','3:3','4:4','4:4']))
print(points(['1:0','2:0','3:0','4:0','2:1','1:3','1:4','2:3','2:4','3:4']))
print(points(['1:0','2:0','3:0','4:4','2:2','3:3','1:4','2:3','2:4','3:4']))