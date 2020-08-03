class cell():
    def __init__(self):
        self.forRank= None
        self.fill = 0
        self.dir_name = None
        self.dir_x = 0
        self.dir_y = 0
        self.last = False
        self.turn = None

    def __str__(self):
        fill = str(int(round(self.fill * 10, 0)))
        if fill.__len__() == 1:
            fill = '0' + fill
        rank = str(self.forRank)
        if self.forRank == 10:
            rank = '0'
        # return rank + '/' + fill
        return self.turn

from Data.getDataSpec import getTop10
import itertools

class loc():
    def __init__(self, rank, cellmap):
        self.x = 0
        self.y = rank - 1

        self.rank = rank
        self.cellmap = cellmap
        dirList = [(1,0, 'right'),(0,1,'down'),(-1,0,'left'),(0,-1,'up')]
        self.dir_cycle = itertools.cycle(dirList)
        dt = next(self.dir_cycle)
        self.dir_x = dt[0]
        self.dir_y = dt[1]
        self.dir_name = dt[2]
        self.turn_id = None

    def turn(self):
        dt = next(self.dir_cycle)
        self.dir_x = dt[0]
        self.dir_y = dt[1]
        self.dir_name = dt[2]

    def go(self):
        self.x += self.dir_x
        self.y += self.dir_y

    def hit_wall(self):
        right = 26-self.rank
        bottom = 11-self.rank
        top = 4
        if self.rank == 1:
            left = 15
        elif self.rank == 2:
            left = 19
        else:
            left = 0

        nextx = self.x + self.dir_x
        nexty = self.y + self.dir_y
        if self.dir_name == 'right' and nextx >= right:
            return True
        if self.dir_name == 'down' and nexty >= bottom:
            return True
        if self.dir_name == 'left' and nextx <= left:
            return True
        if self.dir_name == 'up' and nexty <= top:
            return True
        if self.cellmap[nexty][nextx] is not None:
            return True
        else:
            return False

    def next_loc(self):
        if self.hit_wall():
            ls = self.dir_name
            self.turn()
            self.turn_id = ls + '_' + self.dir_name
            if self.hit_wall():
                print('no way')
                self.turn_id = ls
                return False

            self.go()
            return True
        else:
            self.go()
            self.turn_id = self.dir_name
            return True



class poly():
    def __init__(self, key='confirmed'):
        self.t = getTop10(keyword = key)
        t = self.t
        length = 25
        unit = t[3][1] / (length - 2 + 5)
        unit2 = t[2][1] / (length - 1 + 7 + 3 + 6)
        self.pad = 0.1
        self.width = 0.8
        self.unit = max(unit, unit2)
        self.cells = [[None for _ in range(25)] for _ in range(10)]
        self.lastMap = {}

        #FILL CELL
        for i in range(10, 0 ,-1):

            thisLength = t[i][1] / self.unit
            #y,x
            thisloc = loc(i, self.cells)

            while thisLength > 0:
                c = cell()
                c.forRank = i
                c.fill = 1
                if thisLength <= 1:
                    c.fill = thisLength
                    c.last = True
                thisLength -= 1
                self.cells[thisloc.y][thisloc.x] = c
                # if (thisloc.x, thisloc.y) == (18,6):
                #     print('go up: ', thisLength)
                #     c.last = True
                #     break
                #get next cell
                r = thisloc.next_loc()
                c.dir_name = thisloc.dir_name
                c.dir_x = thisloc.dir_x
                c.dir_y = thisloc.dir_y
                c.turn = thisloc.turn_id
                if not r:
                    c.last = True
                    print(i,' go up: ', thisLength)
                    self.lastMap[c.forRank] = thisLength
                    break
                #print(self)
    def __str__(self):
        str = ''
        for i in self.cells:
            str += [x.__str__() for x in i].__str__()
            str += '\n'
        return str


    def getPoly(self):
        def addpoly(cell, left, right, top, y):
            if cell.turn == 'right':
                left.append((x + cell.fill, top - y - self.pad))
                right.append((x + cell.fill, top - y - 1 + self.pad))
            if cell.turn == 'down':
                right.append((x + self.pad, top - y - cell.fill))
                left.append((x + 1 - self.pad, top - y - cell.fill))
            if cell.turn == 'left':
                right.append((x + 1 - cell.fill, top - y - self.pad))
                left.append((x + 1 - cell.fill, top - y - 1 + self.pad))
            if cell.turn == 'up':
                left.append((x + self.pad, top - y - 1 + cell.fill))
                right.append((x + 1 - self.pad, top - y - 1 + cell.fill))
            if cell.turn == 'right_down':
                left.append((x + 1 - self.pad, top - y - self.pad))
                right.append((x + self.pad, top - y - 1 + self.pad))
                left.append((x + 1 - self.pad, top - y - 1))
                right.append((x + self.pad, top - y - 1))
            if cell.turn == 'down_left':
                left.append((x + 1 - self.pad, top - y - 1 + self.pad))
                right.append((x + self.pad, top - y - self.pad))
                right.append((x, top - y - self.pad))
                left.append((x, top - y - 1 + self.pad))
            if cell.turn == 'left_up':
                left.append((x + self.pad, top - y - 1 + self.pad))
                right.append((x + 1 - self.pad, top - y - self.pad))
                left.append((x + self.pad, top - y))
                right.append((x + 1 - self.pad, top - y))
            if cell.turn == 'up_right':
                left.append((x + self.pad, top - y - self.pad))
                right.append((x + 1 - self.pad, top - y - 1 + self.pad))
                left.append((x + 1, top - y - self.pad))
                right.append((x + 1, top - y - 1 + self.pad))


        res = []
        for i in range(10):
            top = 10
            left = [(0,top - i-self.pad)]
            right = [(0,top - i -1 + self.pad)]
            x = 0
            y = i
            while True:
                cell = self.cells[y][x]
                addpoly(cell, left,right,top, y)
                if cell.last:
                    break

                #next
                x += cell.dir_x
                y += cell.dir_y

            #cell = self.cells[y][x]
            # if cell:
            #     addpoly(cell, left, right, top)


            right.reverse()
            res.append(left+right)
        return res

    def getUpLength(self):
        return self.lastMap[1]

    def getpolyUp(self):
        res = []
        for i in self.lastMap:
            if i == 1:
                l = 18.9
                r = 18.1
                leng = self.lastMap[i]
                #z = 2
                res.append( [(18.9,0),(18.1,0),(18.1,leng),(18.9,leng)])

        return res





if __name__ == '__main__':

    a = poly()
    print(a)
    print(a.getPoly())






#



