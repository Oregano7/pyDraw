import tkinter as tk
from time import sleep

from utilities.color_picker import get_color_code

quads = [[1, 1], [-1, 1], [1, -1], [-1, -1]]


def DDA(p1, p2, c, s=5, t=0.1):
    x1, y1 = p1
    x2, y2 = p2
    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    xinc = float(dx) / steps
    yinc = float(dy) / steps
    x, y = p1
    for a in range(steps):
        x += xinc
        y += yinc
        sleep(t)
        canvas.create_rectangle(int(x) * s, int(y) * s, int(x + 1) * s, int(y + 1) * s, fill=c)
        root.update()


def octii(x, y, xc, yc, clr, s):
    for [a, b] in quads:
        xa1, yb1 = x * a + xc, y * b + yc
        xa2, yb2 = y * b + xc, x * a + yc
        canvas.create_rectangle(int(xa1) * s, int(yb1) * s, int(xa1 + 1) * s, int(yb1 + 1) * s, fill=clr)
        canvas.create_rectangle(int(xa2) * s, int(yb2) * s, int(xa2 + 1) * s, int(yb2 + 1) * s, fill=clr)


def Bresenham(c, r, clr, s=5, t=0.1, octii=octii):
    xc, yc = c
    p = 3 - 2 * r
    x, y = 0, r
    while x <= y:
        sleep(t)
        octii(x, y, xc, yc, clr, s=5)
        root.update()
        if p <= 0:
            p += (4 * x) + 6
        else:
            p += (4 * (x - y)) + 10
            y -= 1
        x += 1


def D_curve(x, y, xc, yc, clr, s):
    xa2, yb2 = xc + y, yc - x
    canvas.create_rectangle(int(xa2) * s, int(yb2) * s, int(xa2 + 1) * s, int(yb2 + 1) * s, fill=clr)
    xa2, yb2 = xc + x, yc + y
    canvas.create_rectangle(int(xa2) * s, int(yb2) * s, int(xa2 + 1) * s, int(yb2 + 1) * s, fill=clr)
    xa2, yb2 = xc + y, yc + x
    canvas.create_rectangle(int(xa2) * s, int(yb2) * s, int(xa2 + 1) * s, int(yb2 + 1) * s, fill=clr)
    xa2, yb2 = xc + x, yc - y
    canvas.create_rectangle(int(xa2) * s, int(yb2) * s, int(xa2 + 1) * s, int(yb2 + 1) * s, fill=clr)


def J_curve(x, y, xc, yc, clr, s):
    xa2, yb2 = xc + y, yc - x
    canvas.create_rectangle(int(xa2) * s, int(yb2) * s, int(xa2 + 1) * s, int(yb2 + 1) * s, fill=clr)
    xa2, yb2 = xc + x, yc + y
    canvas.create_rectangle(int(xa2) * s, int(yb2) * s, int(xa2 + 1) * s, int(yb2 + 1) * s, fill=clr)
    xa2, yb2 = xc + y, yc + x
    canvas.create_rectangle(int(xa2) * s, int(yb2) * s, int(xa2 + 1) * s, int(yb2 + 1) * s, fill=clr)
    xa2, yb2 = xc + x, yc - y
    canvas.create_rectangle(int(xa2) * s, int(yb2) * s, int(xa2 + 1) * s, int(yb2 + 1) * s, fill=clr)


def D_line(p1, p2, c, s=5):
    pmid = [(a + b) / 2.0 for (a, b) in zip(p1, p2)]
    # DDA(p1, pmid, c, s)
    # DDA(p2, pmid, c, s)
    x1, y1 = p1
    xmid, ymid = pmid
    x2, y2 = p2
    dx1 = x1 - xmid
    dy1 = y1 - ymid
    dx2 = x2 - xmid
    dy2 = y2 - ymid
    steps1 = max(abs(dx1), abs(dy1))
    steps2 = max(abs(dx2), abs(dy2))
    xinc1 = float(dx1) / steps1
    xinc2 = float(dx2) / steps2
    yinc1 = float(dy1) / steps1
    yinc2 = float(dy2) / steps2
    xa, ya = pmid
    xb, yb = pmid
    for a in range(int(min(steps1, steps2))):
        sleep(0.1)
        canvas.create_rectangle(int(xa) * s, int(ya) * s, int(xa + 1) * s, int(ya + 1) * s, fill=c)
        canvas.create_rectangle(int(xb) * s, int(yb) * s, int(xb + 1) * s, int(yb + 1) * s, fill=c)
        root.update()
        xa += xinc1
        ya += yinc1
        xb += xinc2
        yb += yinc2
    if steps1 > steps2:
        for a in range(int(steps1 - steps2)):
            sleep(0.1)
            canvas.create_rectangle(int(xa) * s, int(ya) * s, int(xa + 1) * s, int(ya + 1) * s, fill=c)
            root.update()
            xa += xinc1
            ya += yinc1
    else:
        for a in range(int(steps2 - steps1)):
            sleep(0.1)
            canvas.create_rectangle(int(xb) * s, int(yb) * s, int(xb + 1) * s, int(yb + 1) * s, fill=c)
            root.update()
            xb += xinc2
            yb += yinc2


def make_D(c, r, clr):
    D_line([c[0], c[1] - r], [c[0], c[1] + r], c=clr)
    Bresenham(c, r, octii=D_curve, clr=clr)
    Bresenham(c, r, octii=J_curve, clr=clr)


if __name__ == "__main__":
    root = tk.Tk()
    root.title(string="Bresenham")

    canvas = tk.Canvas(root)
    canvas.config(width=500, height=500)
    canvas.pack()

    c = get_color_code()

    make_D([20, 20], 10, clr=c)

    root.mainloop()
