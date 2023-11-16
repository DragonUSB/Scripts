from random import shuffle, randrange, randint

def make_maze(w = 16, h = 16):
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    ver = [["|  "] * w + ['|'] for _ in range(h)] + [[]]
    hor = [["+--"] * w + ['+'] for _ in range(h + 1)]

    # Definir el Comienzo
    c = randint(1, 4)
    d = randint(0, 1)
    if c == 1:
        if d == 0:
            hor[1][0] = "+  "
            vis[0][1] = 1
            vis[1][0] = 1
        else:
            ver[0][1] = "   "
            vis[0][1] = 1
            vis[1][0] = 1
    elif c ==2:
        if d == 0:
            hor[1][w - 1] = "+  "
            vis[1][w - 1] = 1
            vis[0][w - 1] = 1
        else:
            ver[0][w - 1] = "   "
            vis[0][w - 1] = 1
            vis[1][w - 1] = 1
    elif c ==3:
        if d == 0:
            hor[h - 1][w - 1] = "+  "
            vis[h - 1][w - 1] = 1
        else:
            ver[h - 1][w - 1] = "   "
            vis[h - 1][w - 1] = 1
    else:
        if d == 0:
            hor[h - 1][0] = "+  "
            vis[h - 1][0] = 1
            vis[h - 1][1] = 1
        else:
            ver[h - 1][1] = "   "
            vis[h - 1][1] = 1
            vis[h - 1][0] = 1
        

    # ver[0][1] = "   "
    # hor[1][0] = "+  "
    # ver[0][2] = "   "
    # hor[1][1] = "+  "
    # ver[1][1] = "   "

    # vis[1][2] = 1
    # vis[2][0] = 1
    # vis[2][1] = 1

    # si = ""
    # for (a, b) in zip(hor, ver):
    #     si += ''.join(a + ['\n'] + b + ['\n'])
    # print(si)

    def walk(x, y):
        vis[y][x] = 1

        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]: continue
            if xx == x: hor[max(y, yy)][x] = "+  "
            if yy == y: ver[y][max(x, xx)] = "   "
            walk(xx, yy)

    walk(randrange(w), randrange(h))

    s = ""
    for (a, b) in zip(hor, ver):
        s += ''.join(a + ['\n'] + b + ['\n'])
    return s

if __name__ == '__main__':
    print(make_maze())