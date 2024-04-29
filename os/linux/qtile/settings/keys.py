from libqtile.config import Key
from libqtile.lazy import lazy

mod = "mod4"

keys = [

    #? MOVER LA VENTANA HACIA  DISTINTAS DIRECCIONES <^>
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),

    #? MODIFICAR LAS DIMENSIONES DE LA VENTANA EN DISTINTAS DIRECCIONES <^>
    Key([mod, "control"], "h", lazy.layout.grow_left()),
    Key([mod, "control"], "l", lazy.layout.grow_right()),
    Key([mod, "control"], "j", lazy.layout.grow_down()),
    Key([mod, "control"], "k", lazy.layout.grow_up()),
    Key([mod], "n", lazy.layout.normalize(), desc=" Restablecer las dimensiones"),

    #? FULL SCREEN COLUMNA/FULL/LAYOUT
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),
    Key([mod], "Tab", lazy.next_layout()),

    #! LANZAR PROGRAMAS
    Key([mod], "m", lazy.spawn("rofi -show drun")),
    Key([mod], "b", lazy.spawn("brave")),
    Key([mod], "c", lazy.spawn("code")),
    Key([mod, "control"], "f", lazy.spawn("firefox")),
    Key([mod], "g", lazy.spawn("github-desktop")),
    Key([mod], "o", lazy.spawn("p3x-onenote")),
    Key([mod], "x", lazy.spawn("keepassxc")),
    Key([mod, "shift"], "t", lazy.spawn("thunar")),
    Key([mod], "Return", lazy.spawn("alacritty")),
    Key([mod], "p", lazy.spawn("postman")),
    Key([mod, "control"], "d", lazy.spawn("docker-desktop")),
    #Key([mod], "u", lazy.spawn("sudo gufw")),


    #? CERRAR VENTANA ENFOCADA
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    #? REINICIAR - RECARGAR / QTILE
    Key([mod], "r", lazy.spawncmd()),
    Key([mod, "control"], "r", lazy.reload_config()),

    #? CERRAR SESION
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile, o cerrar sesion"),

    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),

    #? CONTROL DE VOLUMEN
    Key([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    Key([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),

     #? CONTROL DE BRILLO DE VENTANA
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),

    #? CAPTURA DE PANTALLA
    Key([mod], "s", lazy.spawn("scrot")),
    Key([mod, "shift"], "s", lazy.spawn("scrot -s")),
   
]
