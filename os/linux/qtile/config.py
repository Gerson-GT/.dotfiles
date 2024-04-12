import subprocess

from libqtile import hook

#! CONFIGURACIONES LOCALES
from settings.keys import mod, keys
from settings.groups import groups
from settings.layouts import layouts, floating_layout
from settings.mouse import mouse
from settings.path import qtile_path
from settings.screens import screens
from settings.widgets import widget_defaults, extension_defaults



from os import path
from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Key, Match, Screen

from libqtile.utils import guess_terminal
from libqtile.lazy import lazy


terminal = guess_terminal()





@hook.subscribe.startup_once
def autostart():
    subprocess.call([path.join(qtile_path, 'autostart.sh')])

main = None
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = True
auto_fullscreen = True
focus_on_window_activation = 'urgent'
wmname = 'LG3D'
