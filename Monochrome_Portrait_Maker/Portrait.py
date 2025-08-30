import turtle
from tkinter import *
import csv

test_input = [
    (400,),
    (146,165,400),
    (146,165,400),
    (119,183,210,228,400),
    (119,183,210,228,400),
    (82,203,209,256,301,312,400),
    (82,203,209,256,301,312,400),
    (74,339,400),
    (74,339,400),
    (65,339,400),
    (65,339,400),
    (55,347,400),
    (55,347,400),
    (46,356,400),
    (46,356,400),
    (55,366,400),
    (55,366,400),
    (9,28,44,366,400),
    (9,28,44,366,400),
    (9,28,45,129,255,366,400),
    (9,28,45,129,255,366,400),
    (0,11,36,111,310,375,400),
    (0,11,36,111,310,375,400),
    (0,93,320,375,400),
    (0,93,320,375,400),
    (0,21,27,85,329,367,400),
    (0,21,27,85,329,367,400),
    (0,20,24,83,338,385,400),
    (0,20,24,83,338,385,400),
    (0,20,25,74,337,394,400),
    (0,20,25,74,337,394,400),
    (18,74,347),
    (18,74,347),
    (18,75,345),
    (18,75,345),
    (18,65,355),
    (18,65,355),
    (37,56,63,83,354),
    (37,56,63,83,354),
    (36,46,63,75,353),
    (36,46,63,75,353),
    (16,46,64,74,355),
    (16,46,64,74,355),
    (15,56,128,164,364),
    (15,56,128,164,364),
    (17,57,100,192,365),
    (17,57,100,192,365),
    (18,56,91,202,264,320,364),
    (18,56,91,202,264,320,364),
    (18,48,154,210,237,329,355),
    (18,48,154,210,237,329,355),
    (18,47,109,210,227,347,357),
    (18,47,109,210,227,347,357),
    (27,46,92,211,228,302,309,347,365,393,400),
    (27,46,92,211,228,302,309,347,365,393,400),
    (0,9,26,46,101,110,157,201,235,320,328,347,363,394,400),
    (0,9,26,46,101,110,157,201,235,320,328,347,363,394,400),
    (0,10,27,46,127,165,246,331,365,393,400),
    (0,10,27,46,127,165,246,331,365,393,400),
    (0,10,27,46,136,156,273,293,318,337,365,385,400),
    (0,10,27,46,136,156,273,293,318,337,365,385,400),
    (0,9,41,46,274,302,364,384,400),
    (0,9,41,46,274,302,364,384,400),
    (1,11,37,46,363,386),
    (1,11,37,46,363,386),
    (0,11,364,386),
    (0,11,364,386),
    (365,376),
    (365,376),
    (371,384),
    (371,384),
    (154,202,228,257,372,284),
    (154,202,228,257,372,284),
    (164,258),
    (164,258),
    (109,120,171,256),
    (109,120,171,256),
    (100,122,191,232),
    (100,122,191,232),
    (100,113,198,199),
    (100,113,198,199),
    (109,192,200,221,290,305),
    (109,192,200,221,290,305),
    (99,148,190,239,291,302),
    (99,148,190,239,291,302),
    (243,283,292,302,364,375),
    (243,283,292,302,364,375),
    (191,213,255,296,382,393),
    (191,213,255,296,382,393),
    (174,239,362,397),
    (174,239,362,397),
    (0,11,183,240,366),
    (0,11,183,240,366),
    (0,30,300,314,354),
    (0,30,300,314,354),
    (0,31,282,321,346),
    (0,31,282,321,346),
    (0,38,98,119,267,312,338),
    (0,38,98,119,267,312,338),
    (0,38,72,120,262,321,338),
    (0,38,72,120,262,321,338),
    (0,29,53,137,254),
    (0,29,53,137,254),
    (54,167,221),
    (54,167,221),
    (63,384),
    (63,384),
    (71,320),
    (71,320),
    (72,393),
    (72,393),
    (82,393),
    (82,393),
    (90,),
    (90,),
    (100,337),
    (100,337),
    (117,321,329,347,363,379,392),
    (117,321,329,347,363,379,392),
    (122,303,319,338,364),
    (122,303,319,338,364),
    (145,220,235,248,298,322,328,342,355),
    (145,220,235,248,298,322,328,342,355),
    (199,210,290,320,328),
    (199,210,290,320,328),
    (290,322,330),
    (290,322,330),
    (308,320,332),
    (308,320,332),
    (308,),
    (308,)
]

def read_csv(file_path):
    data = []
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                nums = tuple(int(x) for x in row if x.strip() != '')
                if nums:
                    data.append(nums)
    except Exception as e:
        print(f"Error reading CSV file: {e}")
    return data

def Portrait(color='white', coords_list=None, scan_mode='normal'):
    if coords_list is None:
        coords_list = test_input

    p = turtle.Turtle()
    p.color('black')
    p.pensize(5)
    p.shape('classic')
    p.screen.setup(650, 700)
    turtle.color(color)
    turtle.hideturtle()
    style = ('Arial', 15, 'italic')
    turtle.write('Happy Birthday Sachin Sir!', font=style, align='right')
    turtle.Screen().bgcolor('black')

    # Margin
    p.penup()
    p.backward(300)
    p.left(90)
    p.forward(340)
    p.right(90)
    p.pendown()

    def gap(n):
        p.penup()
        p.forward(n)
        p.pendown()

    def east(e):
        p.forward(e)

    def right(R):
        p.right(R)

    def left(L):
        p.left(L)

    def z(*args):
        pts = args
        p.penup()
        p.setx(x_start)
        p.pendown()

        for i in range(len(pts)-1):
            distance = pts[i+1] - pts[i]
            p.forward(distance)
        p.penup()
        p.sety(p.ycor() - line_height)
        p.pendown()

    p.pensize(5)
    p.speed(10)
    p.color(color)
    p.forward(400)
    p.right(90)
    p.forward(650)
    p.right(90)
    p.forward(400)
    p.right(90)
    p.forward(650)
    p.right(90)

    # Parameters for positioning
    x_start = -300      # Fixed left margin start (adjust as needed)
    x_end = x_start + 400
    y_start = 340       # Starting vertical position (top)
    line_height = 5     # Vertical spacing between lines, adjust for your portrait scale


    line_width = 400  # Total width of line, adjust as per your scale

    if scan_mode == 'normal':
        for i, coords in enumerate(coords_list):
            p.penup()
            p.setx(x_start)
            p.sety(y_start - i * line_height)

            is_draw = True  # Alternate between not drawing (pen up) and drawing (pen down)
            for x_offset in coords:
                cur_x = x_start + x_offset
                if is_draw:
                    p.pendown()
                    p.setx(cur_x)
                    p.penup()
                else:
                    p.penup()
                    p.setx(cur_x)
                is_draw = not is_draw
    else:
        for i, coords in enumerate(coords_list):
            p.penup()
            p.sety(y_start - i * line_height)

            if i % 2 == 0:
                # Even lines: left to right
                p.setx(x_start)
                segment_coords = coords
            else:
                # Odd lines: right to left
                p.setx(x_start + line_width)
                segment_coords = coords[::-1]

            is_draw = False  # Consistent pen state, start with drawing

            for x_offset in segment_coords:
                if i % 2 == 0:
                    cur_x = x_start + x_offset
                    is_draw = not is_draw
                else:
                    cur_x = x_start + line_width - x_offset
                    is_draw = not is_draw

                if is_draw:
                    p.pendown()
                    p.setx(cur_x)
                    p.penup()
                else:
                    p.penup()
                    p.setx(cur_x)


    def B():
        p=turtle.Turtle()
        p.color('white')
        p.hideturtle()
        p.up()
        p.forward(275)
        p.left(90)
        p.backward(300)
        p.left(90)
        p.down()
        p.color('turquoise')
        p.pensize(5)
        p.forward(100)
        p.right(90)
        p.forward(10)
        p.color('darkgreen')
        for i in range(20):
            p.right(3)
            p.forward(2)
        p.color('red')
        for i in range(40):
            p.right(3)
            p.forward(1)
        p.forward(20)
        p.right(180)
        p.color('green')
        for i in range(25):
            p.right(3)
            p.forward(2.1)
        p.color('violet')
        for i in range(40):
            p.right(3)
            p.forward(1)
        p.color('yellow')
        p.forward(20)
        p.left(195)

    def e():
        p=turtle.Turtle()
        p.color('white')
        p.hideturtle()
        p.pensize(5)
        p.up()
        p.forward(260)
        p.left(90)
        p.backward(235)
        p.left(90)
        p.forward(20)
        p.right(90)
        p.down()
        p.color('green')
        p.forward(30)
        p.color('red')
        for i in range(30):
            p.left(4)
            p.forward(1)
        p.left(20)
        p.color('yellow')
        for i in range(30):
            p.left(3.2)
            p.forward(1)
        p.forward(20)
        p.color('red')
        for i in range(34):
            p.left(5)
            p.forward(2)


    def H():
        p=turtle.Turtle()
        p.color('white')
        p.hideturtle()
        p.pensize(5)
        p.up()
        p.forward(220)
        p.left(90)
        p.backward(100)
        p.left(90)
        p.down()
        p.color('yellow')
        p.up()
        p.forward(60)
        p.down()
        p.backward(120)
        p.up()
        p.forward(60)
        p.down()
        p.color('red')
        p.right(90)
        p.forward(50)
        p.left(90)
        p.up()
        p.forward(60)
        p.down()
        p.color('lightgreen')
        p.backward(120)
        p.up()
        p.forward(60)
        p.down()
    def a():
        p=turtle.Turtle()
        p.color('white')
        p.hideturtle()
        p.pensize(5)
        p.up()
        p.forward(220)
        p.left(90)
        p.backward(30)
        p.left(90)
        p.down()
        p.color('yellow')
        for i in range(10):
            p.right(4)
            p.forward(1)
        p.color('blue')
        for i in range(47):
            p.right(3)
            p.forward(1)
        p.color('red')
        p.forward(40)
        p.color('brown')
        for i in range(10):
            p.left(5)
            p.forward(1)
        p.up()
        for i in range(10):
            p.right(5)
            p.backward(1)
        p.backward(25)
        p.color('turquoise')
        p.down()
        p.right(90)
        p.forward(20)
        p.color('magenta')
        for i in range(35):
            p.left(3)
            p.forward(1)
        p.color('purple')
        for i in range(9):
            p.left(9)
            p.forward(1) 
        p.color('lightgreen')
        p.forward(27)

    def p(n):
        p=turtle.Turtle()
        p.color('white')
        p.hideturtle()
        p.pensize(5)
        p.up()
        p.forward(290)
        p.left(90)
        p.forward(n)
        p.down()
        for i in range(5):
            p.left(18)
            p.forward(1)
        p.color('green')
        p.forward(80)
        p.color('red')
        p.right(90)
        p.forward(20)
        for i in range(18):
            p.right(10)
            p.forward(3)
        p.color('cyan')
        p.forward(15)
    def y():
        p=turtle.Turtle()
        p.hideturtle()
        p.color('white')
        p.pensize(5)
        p.speed(0)
        p.up()
        p.forward(220)
        p.left(90)
        p.forward(130)
        p.down()
        p.color('orange')
        p.forward(3)
        p.color("blue")
        p.right(60)
        p.forward(50)
        p.left(120)
        p.color('red')
        p.forward(50)
        p.up()
        p.backward(50)
        p.down()
        p.color('chocolate')
        p.backward(50)
        p.color('yellow')
        for i in range(6):
            p.right(18)
            p.backward(1)


    B()
    e()
    H()
    a()
    p(30)
    p(75)
    y()


    q=turtle.Turtle()
    q.hideturtle()
    q.color('orange')
    q.speed(0)
    q.pensize(10)
    q.up()
    q.forward(220)
    q.left(90)
    q.forward(320)
    q.right(90)
    def curve():
        for i in range(15):
            q.right(1)
            q.forward(1)
        q.down()
        for i in range(150):
            if i%5==0:
                q.color('blue')
            elif i%2==0:
                q.color('red')
            else:
                q.color('orange')
            q.right(1)
            q.forward(1)
        q.up()
        for i in range(15):
            q.right(1)
            q.forward(1)
        q.down()
        q.color('orange')
    curve()
    q.right(90)
    q.penup()
    q.forward(35)
    q.pendown()
    q.pensize(20)
    q.shape('circle')
    q.forward(1)
    q.penup()
    q.forward(35)
    q.pendown()
    q.pensize(20)
    q.shape('circle')
    q.forward(1)
    q.penup()
    q.shape('arrow')
    q.forward(40)


# Tkinter GUI setup
root = Tk()
root.geometry("300x180")
root.title("Birthday Wish")

color_var = StringVar(value='#FFFFFF')

scan_mode_var = StringVar(value='normal')  # default scanning mode

Label(root, text="Select Scanning Mode:").grid(row=2, column=0, padx=10, pady=(10,0))

Radiobutton(root, text="Normal", variable=scan_mode_var, value='normal').grid(row=3, column=0, sticky='w', padx=30)
Radiobutton(root, text="Snake", variable=scan_mode_var, value='snake').grid(row=4, column=0, sticky='w', padx=30)

Label(root, text="Enter Hex Color (#RRGGBB):").grid(row=0, column=0, padx=10, pady=5)
color_entry = Entry(root, textvariable=color_var)
color_entry.grid(row=1, column=0, padx=10, pady=5)

coords_from_csv = []

def run_portrait():
    coords = coords_from_csv if coords_from_csv else test_input
    col = color_var.get().strip()
    if not (len(col) == 7 and col.startswith('#')):
        col = '#FFFFFF'
    mode = scan_mode_var.get()
    Portrait(color=col, coords_list=coords, scan_mode=mode)

def load_csv():
    import tkinter.filedialog as fd
    filename = fd.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if filename:
        global coords_from_csv
        coords_from_csv = read_csv(filename)

Button(root, text="Draw Portrait", command=run_portrait).grid(row=20, column=0, padx=30, pady=5)
Button(root, text="Load Coordinates CSV", command=load_csv).grid(row=21, column=0, padx=30, pady=5)
Button(root, text="Close", command=root.destroy).grid(row=22, column=0, padx=30, pady=5)

root.mainloop()
