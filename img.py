import numpy as np
from PIL import Image
from tkinter import *
import math
import os

c = 0
w = 0
w1 = 0
r = 0


def qwer(w, w1, r, n, list1):
    import numpy as np
    
    i = 0
    b = 0
    if w > w1:
        pw = (w - w1) / n
        for j in range(len(list1)):
            for m in range(len(list1[0])):
                if list1[j][m] == 1:
                    i += np.sin(w - pw * j)
                elif list1[j][m] == 2:
                    b += np.sin(w - pw * j)
        t = (r**2)*(pw**2)*(i+b/2-1)
        return t
    else:
        pw = (w1 - w) / n
        for j in range(len(list1)):
            for m in range(len(list1[0])):
                if list1[j][m] == 1:
                    i += np.sin(w1 - pw * j)
                elif list1[j][m] == 2:
                    b += np.sin(w1 - pw * j)
        t = (r**2)*(pw**2)*(i+b/2-1)
        return t
    

    

def asdf():
    import numpy as np
    from PIL import Image
    import math
    
    global c
    global w
    global w1
    global r
    low = Image.open('asdf.png').convert("RGBA")
    low_size = low.size
    n = max(low_size)
    m = min(low_size)
    baseLayerSize = (n, n)
    img = Image.new("RGBA", baseLayerSize)

    img.paste(low)

    x = np.array(img)
    x1 = [[[0,0,0,0] for i in range(n)] for i in range(n)]

    for i in range(len(x)):
        for j in range(len(x[0])):
            for h in range(4):
                x1[i][j][h] = x[i][j][h]
                
        
    li = [[0 for i in range(n)] for i in range(n)]


    for i in range(len(x1)):
        m = 0
        m1 = 0
        m2 = 0
        m3 = 0
        for j in range(len(x1[0])):
            if j != len(x1[0])-1:
                if x1[i][j][3] == 0 and x1[i][j+1][3] != 0:
                    m += 1
                    if m % 2 == 1:
                        li[i][j+1] = 1
                if x1[j][i][3] == 0 and x1[j+1][i][3] != 0:
                    m3 += 1
                    if m3 % 2 == 1:
                        li[j+1][i] = 1
        for j in range(len(x1[0]) -1 , -1, -1):
            if j != 0:
                if x1[i][j][3] == 0 and x1[i][j-1][3] != 0:
                    m1 += 1
                    if m1 % 2 == 1:
                        li[i][j-1] = 1
                if x[j][i][3] == 0 and x1[j-1][i][3] != 0:
                    m2 += 1
                    if m2 % 2 == 1:
                        li[j-1][i] = 1
    
    p = 0
    p1 = 0
    for j in range(len(li)):
        if li[j].count(1) > 0:
            p1 = li[j].index(1)
            p = j
            break
    
    s = []
    i = 0
    j = 0

    if li[p+1][p1] == 0:
        li[p+1][p1] = 2
        i = p+1
        j = p1
        s.append((p+1, p1))
    elif li[p+1][p1+1] == 0:
        li[p+1][p1+1] = 2
        i = p+1
        j = p1+1
        s.append((p+1,p1+1))

    while len(s):
        if li[i][j] == 2 and li[i][j+1] == 0:
            li[i][j+1] = 2
            s.append((i, j+1))
        if li[i][j] == 2 and li[i][j-1] == 0:
            li[i][j-1] = 2
            s.append((i, j-1))
        if li[i][j] == 2 and li[i+1][j] == 0:
            li[i+1][j] = 2
            s.append((i+1, j))
        if li[i][j] == 2 and li[i-1][j] == 0:
            li[i-1][j] = 2
            s.append((i-1, j))
        i, j = s.pop(0)

    p1 = math.inf
    p0 = math.inf
    p2 = 0
    
    for j in range(len(li)):
        if li[j].count(1) > 0:
            if j < p1:
                p1 = li[j].index(1)
    for j in range(len(li)-1, -1,-1):
        if li[j].count(1) > 0:
            p2 = j
            break
    for j in range(len(li)-1, -1,-1):
        lis = li[j][::-1]
        if lis.count(1) > 0:
            if j < p0:
                p0 = li[j].index(1)
    n1 = p2 - p + 1
    m1 = p0 - p1 + 1
    list1 = [[0 for i in range(m1)] for i in range(n1)]

    v = 0
    for i in range(p, p2 + 1):
        v1 = 0
        for j in range(p1, p0 + 1):
            list1[v][v1] = li[i][j]
            v1 += 1
        v += 1

    op = qwer(w, w1, r, n1, list1)

    li1 = [[[255,255,255] for i in range(n)] for i in range(n)]

    for i in range(len(li)):
        for j in range(len(li[0])):
            if li[i][j] == 1:
                li1[i][j] = [255,0,0]
            elif li[i][j] == 2:
                li1[i][j] = [0,0,255]
    li2 = np.array(li1)
    img1 = Image.fromarray(li2.astype(np.uint8))
    img1.show()
    img1.save('asdf1.png', 'png')
    c = 0
    output.config(text=str(op))
    
window=Tk()

window.title("입력")
window.resizable(False, False)

id = StringVar()
id1 = StringVar()
id2 = StringVar()


def countUP():
    global c
    global w
    global w1
    global r
    c +=1
    w = int(id.get())
    w1 = int(id1.get())
    r = int(id2.get())
    entry.delete(0, END)
    entry1.delete(0, END)
    entry2.delete(0, END)
    if c == 1:
        asdf()

button = Button(window, overrelief="solid", width=15, text="입력", command=countUP, repeatdelay=10000, repeatinterval=100)
button.grid(row=3, column=1)

entry=Entry(window, textvariable=id)
entry.grid(row=0, column=1)

entry1=Entry(window, textvariable=id1)
entry1.grid(row=1, column=1)

entry2=Entry(window, textvariable=id2)
entry2.grid(row=2, column=1)

label=Label(window, text="시작점 위도")
label.grid(row=0, column=0)

label1=Label(window, text="끝점 위도")
label1.grid(row=1, column=0)

label2=Label(window, text="구의 반지름")
label2.grid(row=2, column=0)


output = Label(window, text='')
output.grid(row=5, column=1)

window.mainloop()