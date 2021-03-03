#深さ優先探索(スタック)
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

def search(log):
    x,y=log[-1]
    if maze[x][y]==1:

        return len(log)-1

    depth=[999999]
    for move in d:
        if maze[x+move[0]][y+move[1]]!=9:
            if[x+move[0],y+move[1]] not in log:
                log.append([x+move[0],y+move[1]])

                depth.append(search(log))

                log.pop(-1)
    return min(depth)

print(search([[1,1]]))
