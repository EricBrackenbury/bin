#! /usr/bin/python3

from os import execl, execlp
from sys import argv
from signal import signal, SIGINT, SIG_DFL
from multiprocessing import Process

import tkinter as tk
from tkinter import ttk


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
             wm_class=DEFAULT_CLASS,
             command=None):
    # TODO: wm_class, wm_instance
    Process(target=execlp, args=["st",
                                 "st",
                                 "-C", "fg:" + foreground,
                                 "-C", "bg:" + background,
                                 "-g", geometry,
                                 "-f", font,
                                 "-t", label] +
                                 ((["-e"] + command) if command is not None else [])).start()


def spawn_xterm(label,
                foreground=DEFAULT_FOREGROUND,
                background=DEFAULT_BACKGROUND,
                geometry=DEFAULT_GEOMETRY,
                font=DEFAULT_FONT,
                command=None):
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
                                 "-n", label] +
                                 ((["-e"] + command) if command is not None else [])).start()


def spawn_term(term, *args, **kwargs):
    {"st": spawn_st,
     "xterm": spawn_xterm}[term](*args, **kwargs)


class TkRll(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Create the various buttons and fields at the top
        fg_label   = ttk.Label(self, text="fg: ")
        size_label = ttk.Label(self, text="size: ")
        term_label = ttk.Label(self, text="term: ")
        ssh_bool    = tk.BooleanVar()
        ssh_button  = ttk.Checkbutton(self, text="ssh: ",
                                      style="Toolbutton",
                                      variable=ssh_bool)
        # FIXME: Figure out cleanest way of exiting.
        exit_button = ttk.Button(self, text="exit", command=self.destroy)

        fg_text   = tk.StringVar()
        size_text = tk.StringVar()
        term_text = tk.StringVar()
        ssh_text  = tk.StringVar()
        fg_field   = ttk.Combobox(self, textvariable=fg_text,   values=FGS)
        size_field = ttk.Combobox(self, textvariable=size_text, values=SIZES)
        term_field = ttk.Combobox(self, textvariable=term_text, values=TERMINALS)
        ssh_field  = ttk.Combobox(self, textvariable=ssh_text,  values=HOSTNAMES)

        # Create the tab set, and the frames for each tab
        tabs = ttk.Notebook(self)
        for tabname, subcolours in COLOURS:
            f = ttk.Frame(tabs)
            column = 0
            row = 0
            for options in subcolours:
                name = options["name"]
                # Using closures to keep a reference to this environment when
                # calling later.
                fg = lambda os=options: fg_text.get() if fg_text.get() else os.get("fg", DEFAULT_FOREGROUND)
                bg = lambda os=options: os.get("bg", DEFAULT_BACKGROUND)
                gy = lambda: size_text.get() if size_text.get() else DEFAULT_GEOMETRY
                te = lambda: term_text.get() if term_text.get() else DEFAULT_TERMINAL
                # TODO: port specifiation
                cl = lambda: ["ssh", ssh_text.get()] if ssh_bool.get() and ssh_text.get() else None
                # Create new derived style for button, with only overriden background
                # colour.
                s = ttk.Style()
                s.configure(name + ".TButton", background=bg(), foreground=fg())

                b = ttk.Button(f,
                           text=name,
                           style=name + ".TButton",
                           command=lambda label=name, bg=bg, fg=fg, te=te, cl=cl: \
                                       spawn_term(te(),
                                                  label=label,
                                                  foreground=fg(),
                                                  background=bg(),
                                                  geometry=gy(),
                                                  command=cl()))
                b.grid(row=row, column=column, sticky=(tk.N, tk.E, tk.S, tk.W))

                column += 1
                if column == 3: # 3x… grid
                    column = 0
                    row += 1

            tabs.add(f, text=tabname)

        for row, widgets in enumerate([[(fg_label,    (tk.E,)),
                                        (fg_field,    (tk.W, tk.E))],
                                       [(size_label,  (tk.E,)),
                                        (size_field,  (tk.W, tk.E))],
                                       [(term_label,  (tk.E,)),
                                        (term_field,  (tk.W, tk.E))],
                                       [(ssh_button,  (tk.E,)),
                                        (ssh_field,   (tk.W, tk.E))],
                                       [(exit_button, (tk.N, tk.E, tk.S))],
                                       [(tabs,        (tk.W, tk.E))]]):
            for column, (widget, sticky) in enumerate(widgets):
                widget.grid(row=row,
                            column=column,
                            sticky=sticky + (tk.N, tk.S),
                            columnspan={1:2, 2:1}[len(widgets)])

def _tk_main():
    root = tk.Tk()

    for key in "<Control-c>", "<Control-d>", "<Escape>", "q":
        root.bind(key, lambda e: root.destroy())
    for key in "<Control-z>", "i":
        root.bind(key, lambda e: root.iconify())
    root.bind("<Alt-r>", lambda e: execl("/proc/self/exe", argv[0], *argv))

    TkRll(root).pack()

    root.mainloop()


try:
    from gi.repository import Gtk, Gdk
except ImportError:
    _gtk_main = None
else:
    # TODO: set_urgency, set_wm_class, set_default
    # http://lazka.github.io/pgi-docs/Gtk-3.0/classes/
    # https://developer.gnome.org/gtk3/stable/ch03.html
    # http://python-gtk-3-tutorial.readthedocs.org/en/latest/index.html
    class GtkRll(Gtk.Window):
        def __init__(self):
            super().__init__(title="Gtk rll")

            ctrl = Gdk.ModifierType.CONTROL_MASK
            alt = Gdk.ModifierType.MOD1_MASK
            self._bindings = [({(ctrl, Gdk.KEY_c),
                                (ctrl, Gdk.KEY_d),
                                (None, Gdk.KEY_Escape),
                                (None, Gdk.KEY_q)},
                               self.destroy),
                              ({(ctrl, Gdk.KEY_z),
                                (None, Gdk.KEY_i)},
                               self.iconify),
                              ({(alt, Gdk.KEY_r)},
                                  lambda: execl("/proc/self/exe",
                                                argv[0], *argv))]
            self.connect("key-release-event", self._key_pressed)

            box = Gtk.VBox()

            def choose(title, combobox):
                def callback(widget):
                    dialog = Gtk.ColorSelectionDialog(title=title)
                    dialog.set_transient_for(self)
                    selection = dialog.get_color_selection()
                    rgba = Gdk.RGBA()
                    if rgba.parse(combobox.get_active_text()):
                        selection.set_current_rgba(rgba)
                    if dialog.run():
                        rgba = selection.get_current_rgba()
                        fmt = "#{:02x}{:02x}{:02x}".format(int(rgba.red * 255),
                                                           int(rgba.green * 255),
                                                           int(rgba.blue * 255))
                        combobox.get_child().set_text(fmt)
                    dialog.destroy()
                return callback

            self._foreground = Gtk.ComboBoxText(hexpand=True, has_entry=True)
            self._foreground.set_tooltip_text("Choose terminal foreground text")
            for fg in FGS:
                self._foreground.append_text(fg)
            fgchooser = Gtk.Button(label="Foreground: ")
            fgchooser.set_tooltip_text("Choose terminal foreground text")
            fgchooser.connect("clicked", choose("Foreground", self._foreground))

            self._background = Gtk.ComboBoxText(hexpand=True, has_entry=True)
            self._background.set_tooltip_text("Choose terminal background text")
            for bg in FGS:
                self._background.append_text(bg)
            bgchooser = Gtk.Button(label="Background:" )
            bgchooser.set_tooltip_text("Choose terminal background text")
            bgchooser.connect("clicked", choose("Background", self._background))

            self._size = Gtk.ComboBoxText(hexpand=True, has_entry=True)
            self._size.set_tooltip_text("Choose terminal size")
            for size in SIZES:
                self._size.append_text(size)

            self._term = Gtk.ComboBoxText(hexpand=True, has_entry=True)
            self._term.set_tooltip_text("Choose terminal to spawn")
            for terminal in TERMINALS:
                self._term.append_text(terminal)

            self._ssh = Gtk.ComboBoxText(hexpand=True, has_entry=True)
            self._ssh.set_tooltip_text("Choose SSH host (one word) or command "
                                       "line to run")
            for hostname in HOSTNAMES:
                self._ssh.append_text(hostname)

            grid = Gtk.Grid(valign=Gtk.Align.START, vexpand=False)
            for rowno, row in enumerate([(fgchooser, self._foreground),
                                         (bgchooser, self._background),
                                         (Gtk.Label(label="Size: ",
                                                    halign=Gtk.Align.START),
                                          self._size),
                                         (Gtk.Label(label="Terminal: ",
                                                    halign=Gtk.Align.START),
                                          self._term),
                                         (Gtk.Label(label="SSH: ",
                                                    halign=Gtk.Align.START),
                                          self._ssh)]):
                for colno, col in enumerate(row):
                    grid.attach(col, left=colno, top=rowno, width=1, height=1)
            box.add(grid)

            notebook = Gtk.Notebook(valign=Gtk.Align.START)
            for tabname, colours in COLOURS:
                #scrolled = Gtk.ScrolledWindow()
                #scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
                # TODO: Make all button vertical sizes the same across flowboxes
                flowbox = Gtk.FlowBox(vexpand=False)
                flowbox.set_selection_mode(Gtk.SelectionMode.NONE)
                for colour in colours:
                    # TODO: set button colour
                    fc = Gdk.RGBA()
                    bc = Gdk.RGBA()
                    if not fc.parse(colour["fg"]) or not bc.parse(colour["bg"]):
                        continue
                    def clicked(colour):
                        def callback(widget):
                            fg = self._foreground.get_active_text() or colour["fg"]
                            bg = self._background.get_active_text() or colour["bg"]
                            te = self._term.get_active_text() or DEFAULT_TERMINAL
                            gy = self._size.get_active_text() or DEFAULT_GEOMETRY
                            ssh = self._ssh.get_active_text().split()
                            if len(ssh) > 1:
                                cl = ssh
                            elif len(ssh) == 1:
                                cl = ["ssh", self._ssh.get_active_text()]
                            else:
                                cl = None
                            spawn_term(te,
                                       label=colour["name"],
                                       foreground=fg,
                                       background=bg,
                                       geometry=gy,
                                       command=cl)
                        return callback

                    button = Gtk.Button(label=colour["name"],
                                        vexpand=False)
                    button.set_tooltip_text(' '.join(["Spawn a",
                                                      colour["name"],
                                                      "terminal"]))
                    button.override_background_color(Gtk.StateFlags.NORMAL, bc)
                    button.override_color(Gtk.StateFlags.NORMAL, fc)
                    button.override_color(Gtk.StateFlags.PRELIGHT, bc)
                    # FIXME: Mouse over (PRELIGHT) background colour doesn't
                    #        take effect.
                    #button.override_background_color(Gtk.StateFlags.PRELIGHT, Gdk.RGBA(1, 0, 0, 1))
                    #button.connect("enter", lambda widget: print(widget.get_style_context().get_background_color(Gtk.StateFlags.PRELIGHT)))
                    button.set_relief(Gtk.ReliefStyle.NONE)
                    button.connect("clicked", clicked(colour))
                    flowbox.add(button)

                #scrolled.add(flowbox)
                notebook.append_page(flowbox, Gtk.Label(tabname))
            box.add(notebook)

            exit = Gtk.Button(label="Exit", expand=False,
                              halign=Gtk.Align.END, valign=Gtk.Align.END)
            exit.connect("clicked", lambda widget: self.destroy())
            box.add(exit)

            self.add(box)


        def _key_pressed(self, widget, event):
            if event.type == Gdk.EventType.KEY_RELEASE:
                for keys, callback in self._bindings:
                    for mask, key in keys:
                        if event.keyval == key:
                            if mask is not None:
                                if event.state & mask:
                                    callback()
                            else:
                                callback()


    def _gtk_main():
        gui = GtkRll()
        gui.connect("delete-event", Gtk.main_quit)
        signal(SIGINT, SIG_DFL)
        gui.show_all()
        # FIXME: KeyboardInterrupt here hangs it.
        Gtk.main()


if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser(description="Roland's <TODO> <TODO>")
    toolkit = parser.add_mutually_exclusive_group()
    toolkit.add_argument("--tk", action='store_const', const=_tk_main,
                         dest="toolkit",
                         default=_tk_main)
    toolkit.add_argument("--gtk", action='store_const', const=_gtk_main,
                         dest="toolkit")
    args = parser.parse_args()

    if args.toolkit is None:
        error("specified widget toolkit not available")
    else:
        args.toolkit()
