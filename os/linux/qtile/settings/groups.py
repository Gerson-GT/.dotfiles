
from libqtile.config import Key, Group
from libqtile.command import lazy
from .keys import mod, keys


groups = [Group(i) for i in ["󰣇", "", "󰨞", "", "󱂪", "", "󰟌", "󱠇"] ]

for i, group in enumerate(groups):
    windows = str(i+1)
    keys.extend(
        [

            Key([mod], windows, lazy.group[group.name].toscreen()),
            # mod1 + shift + group number = switch to & move focused window to group
            Key([mod, "shift"], windows, lazy.window.togroup(group.name, switch_group=True)),
        ]
    )