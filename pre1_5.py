#幅優先探索(キュー)
maze=[
[9]*9,
[9,0,0,0,9,9,0,9,9],
[9,0,9,9,0,0,0,0,9],
[9,0,0,0,0,9,9,9,9],
[9,9,0,9,0,9,0,1,9],
[9,0,0,9,0,0,0,9,9],
[9]*9
]

d=[[0,-1],[-1,0],[0,1],[1,0]]
log=[[1,1]]

queue=[[1,1,0]]

while len(queue)>0:
    x,y,depth=queue.pop(0)
    for move in d:
        xd,yd=x+move[0],y+move[1]
        if maze[xd][yd]==1:

            print(depth+1)
            exit
        elif maze[xd][yd]!=9:
            if [xd,yd] not in log:

                log.append([xd,yd])
                queue.append([xd,yd,depth+1])
