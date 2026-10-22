################################################################################
## THEME - dark / light switch
##
## Every colour literal inside a screen is wrapped as tc("#...") (fills, backgrounds,
## bars) or tx("#...") (text). In the light theme both return the colour unchanged, so
## the light look is exactly the original. In the dark theme they look the colour up in
## the maps below. Change a dark colour here and it changes everywhere.
##
## Dark palette (from the suggested swatch):  #181A2F  #242E49  #37415C  #FDA481  #B4182D  #541628
################################################################################

default persistent.theme = "dark"

init -2 python:

    ## light colour -> dark colour, for FILLS (backgrounds, bars, tracks). Alpha is kept.
    THEME_FILL = {
        "#FAF7F3": "#242E49",   # card / panel surface
        "#F3EFEA": "#37415C",   # inset surface: fields, option rows, buttons
        "#FFFFFF": "#242E49",   # white overlays
        "#E3DBD2": "#37415C",   # borders and bar tracks
        "#D9D0C6": "#4B587A",   # empty progress segments
        "#B8AFA6": "#56648A",
        "#E8EEF3": "#2F3B5C",   # tip / hint boxes
        "#C8D8E6": "#475577",   # hint hover
        "#FFE3E7": "#541628",   # pale pink highlight -> wine
        "#14110F": "#0B0D1C",   # dimming overlays
        "#1F1B19": "#12142A",   # dark cards on top of scenes
        "#2B2624": "#12142A",   # dark chips
    }

    ## light colour -> dark colour, for TEXT
    THEME_TEXT = {
        "#2B2624": "#F4EEE8",
        "#1F1B19": "#F4EEE8",
        "#0E0E0E": "#F4EEE8",
        "#6B6259": "#AEB6CC",   # muted text
        "#9C948C": "#7C86A0",   # disabled text
        "#C41230": "#FDA481",   # crimson text -> peach (crimson is too dark on navy)
        "#8C0E23": "#FFC9B4",
        "#005A9C": "#8CC4FF",
        "#B8AFA6": "#AEB6CC",
        "#3D3730": "#D3D9E8",   # sidebar tab text
        "#202020": "#F4EEE8",   # chapter card subtitle
        "#3D3D3D": "#AEB6CC",   # chapter card hint
    }

    def theme_dark():
        return persistent.theme == "dark"

    def _theme_map(c, table):
        if persistent.theme != "dark":
            return c
        base = c[:7].upper()
        return table.get(base, c[:7]) + c[7:]

    def tc(c):
        """Theme colour for a fill / background."""
        return _theme_map(c, THEME_FILL)

    def tx(c):
        """Theme colour for text."""
        return _theme_map(c, THEME_TEXT)

    def theme_img(name):
        """gui/<name>.png in light, gui/<name>_dark.png in dark."""
        return "gui/%s_dark.png" % name if persistent.theme == "dark" else "gui/%s.png" % name

    def theme_textbox():
        return theme_img("textbox")

    def theme_scrollbar_style():
        return "prefs_vscrollbar_dark" if persistent.theme == "dark" else "prefs_vscrollbar"

style prefs_vscrollbar_dark is vscrollbar:
    xsize 18
    base_bar Solid("#37415C")
    thumb Solid("#FDA481")
    unscrollable "hide"
