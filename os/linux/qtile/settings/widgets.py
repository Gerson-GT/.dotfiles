from libqtile import widget
from .theme import colors


def base(fg='text', bg='dark'): 
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)


def icon(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )


def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="", # Icon: nf-oct-triangle_left
        fontsize=37,
        padding=-2
    )


def workspaces(): 
    return [
        separator(),
        widget.GroupBox(
            **base(fg='light'),
            font='UbuntuMono Nerd Font',
            fontsize=26,
            margin_y=3,
            margin_x=12,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='text',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
        separator(),
        widget.WindowName(**base(fg='focus'), fontsize=14, padding=5),
        separator(),
    ]


primary_widgets = [
    *workspaces(),

    separator(),

        widget.Pomodoro(
                #background=colors['light'],
                length_pomodori= 30,
                length_short_break= 6,
                length_long_break= 25,
                prefix_inactive= 'Work',
                color_inactive= colors['active'],
                ),

    powerline('color4', 'dark'),



    icon(bg="color4", text=' '), # Icon: nf-fa-download
    
    widget.CheckUpdates(
        background=colors['color4'],
        colour_have_updates=colors['text'],
        colour_no_updates=colors['text'],
        no_update_string='0',
        display_format='{updates}',
        update_interval=1800,
        custom_command='checkupdates',
    ),

    powerline('color3', 'color4'),

        icon(bg="color4", text='  '), # Icon: nf-oct-cpu
        widget.ThermalSensor(
            background=colors['color4'],
            foreground=colors['text'],
            foreground_alert=colors['urgent'],
            tag_sensor='CPU',
            threshold= 66,
            #format='{temp:.0f}{unit}',
            fmt= 'CPU:{}'
        ),
    powerline('color3', 'color4'),

    icon(bg="color4", text='  '), # Icon: nf-oct-cpu
    widget.Memory(
            background=colors['color4'],
            foreground=colors['text'],
            measure_mem='G',
        ),


    powerline('color3', 'color4'),





    icon(bg="color3", text=' '),  # Icon: nf-fa-feed
    
    widget.Net(**base(bg='color3'),
               #interface='wlp0s20f3',
               interface='wg0-mullvad',
               format = '{interface}: {down:6.2f} Mbps ↓↑  {up:.2f} Mbps',
               scroll_fixed_width=True,
               #prefix="M",
               use_bits= True,
               #fmt = '<i>{}</i>'
               ),

    powerline('color2', 'color3'),
    

    widget.CurrentLayoutIcon(**base(bg='color2'), scale=0.65),

    widget.CurrentLayout(**base(bg='color2'), padding=5),

    widget.Systray( 
        **base(bg='color2'),
        icon_size= 18,
                padding= 7,),

    powerline('color1', 'color2'),

    #icon(bg="color1", fontsize=17, text=' '), # Icon: nf-mdi-calendar_clock

    widget.Clock(**base(bg='color1'), format='%H:%M '),

    powerline('dark', 'color1'),

    #widget.Systray(background=colors['dark'], padding=5),
]

secondary_widgets = [
    *workspaces(),

    separator(),

    powerline('color1', 'dark'),

    widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),

    widget.CurrentLayout(**base(bg='color1'), padding=5),

    powerline('color2', 'color1'),

    widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %H:%M '),

    powerline('dark', 'color2'),
]

widget_defaults = {
    'font': 'UbuntuMono Nerd Font',
    'fontsize': 14,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()
