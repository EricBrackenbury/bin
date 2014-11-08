#! /usr/bin/python3

from os import execl, execlp
from sys import argv
from tkinter import *
from tkinter.ttk import *
from multiprocessing import Process


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

# TODO
FONTS      = ["Terminess Powerline:pixelsize=26:antialias=false:hint=true",
              "Terminus",
              "10x20"]

TERMINALS = ["st", "xterm"]

COLOURS = [("red",
            [{"name": "t1_root"          , "bg": "pink",             "fg": "black"},
             {"name": "coral"            , "bg": "coral",            "fg": "black"},
             {"name": "palevioletred"    , "bg": "#DB7093",          "fg": "black"},
             {"name": "mistyrose"        , "bg": "mistyrose",        "fg": "black"},
             {"name": "t3_Thistle1"      , "bg": "Thistle1",         "fg": "black"},
             {"name": "t3_Thistle2"      , "bg": "Thistle2",         "fg": "black"},
             {"name": "t3_plum_1"        , "bg": "plum1",            "fg": "black"},
             {"name": "pink"             , "bg": "pink",             "fg": "black"},
             {"name": "pink_mod"         , "bg": "#ffaaaa",          "fg": "black"},
             {"name": "pink2"            , "bg": "pink2",            "fg": "black"},
             {"name": "t3_plum_2"        , "bg": "plum2",            "fg": "black"},
             {"name": "t3_orchid1"       , "bg": "orchid1",          "fg": "black"},
             {"name": "violet"           , "bg": "violet",           "fg": "black"},
             {"name": "red"              , "bg": "red",              "fg": "black"},
             {"name": "orangered"        , "bg": "orangered",        "fg": "black"},
             {"name": "tomato"           , "bg": "tomato",           "fg": "black"},
             {"name": "tomato_light1"    , "bg": "#ff8173",          "fg": "black"},
             {"name": "darkorange"       , "bg": "darkorange",       "fg": "black"},
             {"name": "orange"           , "bg": "orange",           "fg": "black"},
             {"name": "t3_lightsalmon"   , "bg": "lightsalmon",      "fg": "black"},
             {"name": "t3_darksalmon"    , "bg": "darksalmon",       "fg": "black"},
             {"name": "t3_palevioletred" , "bg": "palevioletred",    "fg": "black"}]),
           ("green",
            [{"name": "t1_remedy_2"      , "bg": "greenyellow",      "fg": "black"},
             {"name": "t3_LimeGreen"     , "bg": "LimeGreen",        "fg": "black"},
             {"name": "t3_DarkSeaGreen1" , "bg": "DarkSeaGreen1",    "fg": "black"},
             {"name": "t3_DarkSeaGreen2" , "bg": "DarkSeaGreen2",    "fg": "black"},
             {"name": "t3_PaleGreen"     , "bg": "PaleGreen",        "fg": "black"},
             {"name": "t3_LightGreen"    , "bg": "LightGreen",       "fg": "black"},
             {"name": "t3_MediumSpringGreen", "bg": "#00FA9A",       "fg": "black"},
             {"name": "t3_LightSeaGreen" , "bg": "LightSeaGreen",    "fg": "black"},
             {"name": "Green"            , "bg": "Green",            "fg": "black"},
             {"name": "DarkSoftGreen"    , "bg": "#245032",          "fg": "#E1FFB8"},
             {"name": "t1_remedy_3"      , "bg": "olivedrab",        "fg": "black"}]),
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
             {"name": "blue"             , "bg": "blue",             "fg": "white"}]),
           ("yellow",
            [{"name": "yellow"           , "bg": "#FFFF00" ,         "fg": "black"},
             {"name": "t1_ccase1"        , "bg": "#FEFF7D" ,         "fg": "black"},
             {"name": "t1_ccase2"        , "bg": "#FDFF52" ,         "fg": "black"},
             {"name": "t1_perl"          , "bg": "#EEE8AA" ,         "fg": "black"},
             {"name": "t1_perl2"         , "bg": "#F0E68C" ,         "fg": "black"},
             {"name": "t1_perl3"         , "bg": "#EEDD82" ,         "fg": "black"},
             {"name": "t3_yellow_orange1", "bg": "#FFEFAC" ,         "fg": "black"},
             {"name": "t3_yellow_orange2", "bg": "#FFE683" ,         "fg": "black"},
             {"name": "t3_yellow_orange3", "bg": "#FFDB4A" ,         "fg": "black"},
             {"name": "t3_yellow0"       , "bg": "#FFFFCC" ,         "fg": "black"},
             {"name": "t3_yellow1"       , "bg": "#FFFFAF" ,         "fg": "black"},
             {"name": "t3_yellow2"       , "bg": "#FFFF9D" ,         "fg": "black"},
             {"name": "t3_yellow3"       , "bg": "#FFFF92" ,         "fg": "black"},
             {"name": "t3_yellow3a"      , "bg": "#FFF399" ,         "fg": "black"},
             {"name": "t3_yellow4"       , "bg": "#FEFF7D" ,         "fg": "black"},
             {"name": "t3_yellow5"       , "bg": "#FFFF88" ,         "fg": "black"},
             {"name": "t3_yellow6"       , "bg": "#FDFF52" ,         "fg": "black"},
             {"name": "t3_yellow7"       , "bg": "#FFFF2C" ,         "fg": "black"},
             {"name": "t3_yellow8"       , "bg": "#F5F500" ,         "fg": "black"},
             {"name": "t3_yellow9"       , "bg": "#EFF079" ,         "fg": "black"},
             {"name": "t3_gold1"         , "bg": "#FFD700" ,         "fg": "black"},
             {"name": "t3_gold2"         , "bg": "#EEC900" ,         "fg": "black"},
             {"name": "t3_gold3"         , "bg": "#CDAD00" ,         "fg": "black"},
             {"name": "goldenrod"        , "bg": "#DAA520" ,         "fg": "black"},
             {"name": "wheat_brown"      , "bg": "#F5DEB3" ,         "fg": "brown"},
             {"name": "wheat"            , "bg": "#F5DEB3" ,         "fg": "black"},
             {"name": "wheat2"           , "bg": "#F5DEB3" ,         "fg": "black"}]),
           ("misc",
            [{"name": "black_lightblue"  , "bg": "black",            "fg": "lightblue"},
             {"name": "black_yellow"     , "bg": "black",            "fg": "yellow"},
             {"name": "black_orange"     , "bg": "black",            "fg": "orange"},
             {"name": "black_green"      , "bg": "black",            "fg": "green"},
             {"name": "black_pink"       , "bg": "black",            "fg": "pink"},
             {"name": "black"            , "bg": "black",            "fg": "white"}])]


DEFAULT_FOREGROUND = "black"
DEFAULT_BACKGROUND = "sand"
DEFAULT_FONT       = FONTS[0]
DEFAULT_TERMINAL   = TERMINALS[0]
DEFAULT_GEOMETRY   = "80x39"
DEFAULT_CLASS      = None

def spawn_st(label,
             foreground=DEFAULT_FOREGROUND,
             background=DEFAULT_BACKGROUND,
             geometry=DEFAULT_GEOMETRY,
             font=DEFAULT_FONT,
             wm_class=DEFAULT_CLASS):
    # TODO: wm_class, wm_instance
    Process(target=execlp, args=["st",
                                "st",
                                "-C", "fg:" + foreground,
                                "-C", "bg:" + background,
                                "-g", geometry,
                                "-f", font,
                                "-t", label]).start()

def spawn_xterm(label,
                foreground=DEFAULT_FOREGROUND,
                background=DEFAULT_BACKGROUND,
                geometry=DEFAULT_GEOMETRY,
                font=DEFAULT_FONT):
    # TODO: -n
    Process(target=execlp, args=["xterm",
                                "xterm",
                                "-s",  # asynchronous scrolling
                                "+sb", # no scrollbars
                                "-ut", # don't write to UTMP
                                "-fg", foreground,
                                "-bg", background,
                                "-geometry", geometry,
                                "-fn", font,
                                "-n", label]).start()

if __name__ == "__main__":
    root = Tk()

    for key in "<Control-c>", "<Control-d>", "<Escape>", "q":
        root.bind(key, lambda e: root.destroy())
    for key in "<Control-z>", "i":
        root.bind(key, lambda e: root.iconify())
    root.bind("<Alt-r>", lambda e: execl("/proc/self/exe", argv[0], *argv))

    # Create the various buttons and fields at the top
    # TODO: What does this do, since we can just read the value of fg_text directly?
    fg_button   = Button(root, text="fg")
    size_button = Button(root, text="size")
    term_button = Button(root, text="term")
    # FIXME: size and host buttons not displayed nor used
    host_button = Button(root, text="remote host")
    ssh_button  = Button(root, text="ssh")
    exit_button = Button(root, text="exit", command=root.destroy)

    fg_text = StringVar()
    size_text = StringVar()
    host_text = StringVar()
    term_text = StringVar()
    fg_field   = Combobox(root, textvariable=fg_text,   values=FGS)
    size_field = Combobox(root, textvariable=size_text, values=SIZES)
    host_field = Combobox(root, textvariable=host_text, values=HOSTNAMES)
    term_field = Combobox(root, textvariable=term_text, values=TERMINALS)

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
                                   [(term_button, (E,)), (term_field, (W,E))],
                                   [(exit_button, (N,E,S,))],
                                   [(tabs,        (W,E))]]):
        for column, (widget, sticky) in enumerate(widgets):
            widget.grid(row=row,
                        column=column,
                        sticky=sticky + (N,S),
                        columnspan={1:2, 2:1}[len(widgets)])

    root.mainloop()
