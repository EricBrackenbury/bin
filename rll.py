#! /usr/bin/python3

from tkinter import *
from tkinter.ttk import *

from sys import argv
from os import execl

from multiprocessing import Process

from collections import OrderedDict

HOSTNAMES = ["gold",
             "garnet",
             "ottvob01",
             "rjrl1",
             "rjrl2",
             "rjrlap1",
             "rjrlap2",
             "rjrh1",
             "tripe.e-smith.com",
             "tux.oclug.on.ca",
             "enzo1",
             "limh1"]

SIZES      = ["40x7", "80x24", "80x39", "80x44"]

FGS        = ["none",
              "black",
              "white",
              "brown",
              "red",
              "orange",
              "yellow",
              "lightseagreen",
              "seagreen",
              "limegreen",
              "blue",
              "darkblue",
              "violet",
              "purple"]

FONTS      = ["10x20"] # TODO

COLOURS = [("red",
            [{"name": "t1_root"          , "bg": "pink"},
             {"name": "coral"            , "bg": "coral"},
             {"name": "palevioletred"    , "bg": "palevioletred"},
             {"name": "mistyrose"        , "bg": "mistyrose"},
             {"name": "t3_Thistle1"      , "bg": "Thistle1"},
             {"name": "t3_Thistle2"      , "bg": "Thistle2"},
             {"name": "t3_plum_1"        , "bg": "plum1"},
             {"name": "pink"             , "bg": "pink"},
             {"name": "pink_mod"         , "bg": "#ffaaaa"},
             {"name": "pink2"            , "bg": "pink2"},
             {"name": "t3_plum_2"        , "bg": "plum2"},
             {"name": "t3_orchid1"       , "bg": "orchid1"},
             {"name": "violet"           , "bg": "violet"},
             {"name": "red"              , "bg": "red"},
             {"name": "orangered"        , "bg": "orangered"},
             {"name": "tomato"           , "bg": "tomato"},
             {"name": "tomato_light1"    , "bg": "#ff8173"},
             {"name": "darkorange"       , "bg": "darkorange"},
             {"name": "orange"           , "bg": "orange"},
             {"name": "t3_lightsalmon"   , "bg": "lightsalmon"},
             {"name": "t3_darksalmon"    , "bg": "darksalmon"},
             {"name": "t3_palevioletred" , "bg": "palevioletred"}]),
           ("green",
            [{"name": "t1_remedy_2"      , "bg": "greenyellow"},
             {"name": "t3_LimeGreen"     , "bg": "LimeGreen"},
             {"name": "t3_DarkSeaGreen1" , "bg": "DarkSeaGreen1"},
             {"name": "t3_DarkSeaGreen2" , "bg": "DarkSeaGreen2"},
             {"name": "t3_PaleGreen"     , "bg": "PaleGreen"},
             {"name": "t3_LightGreen"    , "bg": "LightGreen"},
             {"name": "t3_MediumSpringGreen", "bg": "MediumSpringGreen"},
             {"name": "t3_LightSeaGreen" , "bg": "LightSeaGreen"},
             {"name": "Green"            , "bg": "Green"},
             {"name": "t1_remedy_3"      , "bg": "olivedrab"}]),
           ("blue",
            [{"name": "darkblue"         , "bg": "darkblue",         "fg": "white"},
             {"name": "blue"             , "bg": "blue"    ,         "fg": "white"},
             {"name": "violetblue1"      , "bg": "#9A88DC" ,         "fg": "white"},
             {"name": "violetblue2"      , "bg": "#6050B1" ,         "fg": "white"},
             {"name": "violetblue3"      , "bg": "#4C2CBE" ,         "fg": "white"},
             {"name": "teal"             , "bg": "#3A6EA5" ,         "fg": "white"},
             {"name": "t3_LightSkyBlue1" , "bg": "#B0E2FF" ,         "fg": "black"},
             {"name": "t3_DeepSkyBlue2"  , "bg": "#00B2EE" ,         "fg": "black"},
             {"name": "t3_lightblue00"   , "bg": "#F0F0F0" ,         "fg": "black"},
             {"name": "t3_lightblue0"    , "bg": "#E4F5FF" ,         "fg": "black"},
             {"name": "darkblue"         , "bg": "darkblue",         "fg": "white"},
             {"name": "darkblue"         , "bg": "darkblue",         "fg": "white"},
             {"name": "darkblue"         , "bg": "darkblue",         "fg": "white"},
             {"name": "blue"             , "bg": "blue",             "fg": "white"}]),
           ("yellow",
            [{"name": "yellow"           , "bg": "yellow"}]),
           ("misc",
            [{"name": "black"            , "bg": "black",            "fg": "white"}])]


DEFAULT_FOREGROUND = "black"
DEFAULT_BACKGROUND = "sand"
DEFAULT_FONT       = "10x20"
DEFAULT_GEOMETRY   = "80x39"

def spawn_xterm(label,
                foreground=DEFAULT_FOREGROUND,
                background=DEFAULT_BACKGROUND,
                geometry=DEFAULT_GEOMETRY,
                font=DEFAULT_FONT):
    # TODO: -n
    Process(target=execl, args=["/usr/bin/xterm",
                                "xterm",
                                "-s",  # asynchronous scrolling
                                "+sb", # no scrollbars
                                "-ut", # don't write to UTMP
                                "-fg", foreground,
                                "-bg", background,
                                "-geometry", geometry,
                                "-fn", font,
                                "-n", label]).start()

root = Tk()

for key in "<Control-c>", "<Control-d>", "q":
    root.bind(key, lambda e: root.destroy())
for key in "<Control-z>", "i":
    root.bind(key, lambda e: root.iconify())
root.bind("<Alt-r>", lambda e: execl("/proc/self/exe", argv[0], *argv))

# Create the various buttons and fields at the top
# TODO: What does this do, since we can just read the value of fg_text directly?
fg_button   = Button(root, text="fg")
size_button = Button(root, text="size")
host_button = Button(root, text="remote host")
ssh_button  = Button(root, text="ssh")
exit_button = Button(root, text="exit", command=root.destroy)

fg_text, size_text, host_text = StringVar(), StringVar(), StringVar()
fg_field   = Combobox(root, textvariable=fg_text,   values=FGS)
size_field = Combobox(root, textvariable=size_text, values=SIZES)
host_field = Combobox(root, textvariable=host_text, values=HOSTNAMES)

# Create the tab set, and the frames for each tab
tabs = Notebook(root)
for tabname, subcolours in COLOURS:
    f = Frame(tabs)
    column = 0
    row = 0
    for options in subcolours:
        name = options["name"]
        fg = fg_text.get() if fg_text.get() else options.get("fg", DEFAULT_FOREGROUND)
        bg = options.get("bg", DEFAULT_BACKGROUND)
        gy = size_text.get() if size_text.get() else DEFAULT_GEOMETRY
        # Create new derived style for button, with only overriden background
        # colour.
        s = Style()
        s.configure(name + ".TButton", background=bg, foreground=fg)

        b = Button(f,
                   text=name,
                   style=name + ".TButton",
                   command=lambda label=name, bg=bg, fg=fg: spawn_xterm(label=label,
                                                                        foreground=fg,
                                                                        background=bg,
                                                                        geometry=gy))
        b.grid(row=row, column=column, sticky=(N,E,S,W))

        column += 1
        if column == 3: # 3x… grid
            column = 0
            row += 1

    tabs.add(f, text=tabname)

for row, widgets in enumerate([[(fg_button,   (E,)), (fg_field, (W,E))],
                               [(size_button, (E,)), (size_field, (W,E))],
                               [(exit_button, (E,))],
                               [(tabs,        (W,E))]]):
    for column, (widget, sticky) in enumerate(widgets):
        widget.grid(row=row,
                    column=column,
                    sticky=sticky + (N,S),
                    columnspan={1:2, 2:1}[len(widgets)])
exit_button.grid(row=2, column=0, columnspan=2, sticky=(N,E,S))

root.mainloop()
