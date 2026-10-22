################################################################################
## ON-SCREEN KEYBOARD (phones / touch, web build)
##
## On a touch device in a web build, Ren'Py always draws its own keyboard screen,
## "_touch_keyboard" (the native phone keyboard cannot be used from a canvas game).
## The stock one is a huge 60%-transparent A-Z grid over the WHOLE screen, which hid
## the rename card. This replaces it with a compact, themed QWERTY keyboard that sits
## along the bottom, so the rename card (placed at the top on phones) stays visible.
##
## It reuses Ren'Py's own input actions, so typing, backspace and Enter behave exactly
## like the stock keyboard. Same screen name + no parameters = drop-in override.
################################################################################

default kb_caps = False        # one-shot shift: next letter is a capital

screen kb_key(label, act, w=150, sel=False):
    textbutton label:
        action act
        selected sel
        xsize w
        ysize 104
        background Solid(tc("#F3EFEA"))
        hover_background Solid("#C41230")
        selected_background Solid("#C41230")
        text_color tx("#2B2624")
        text_hover_color "#FFFFFF"
        text_selected_color "#FFFFFF"
        text_size 46
        text_xalign 0.5
        text_yalign 0.5

screen _touch_keyboard():
    layer config.interface_layer
    zorder 1100

    python:
        _kb_rows = ["qwertyuiop", "asdfghjklñ", "zxcvbnm"]

    frame:
        xfill True
        yalign 1.0
        background Solid(tc("#FFFFFFF8"))
        padding (20, 14)

        vbox:
            xalign 0.5
            spacing 10

            for r in range(2):
                hbox:
                    xalign 0.5
                    spacing 10
                    for ch in _kb_rows[r]:
                        python:
                            _c = ch.upper() if kb_caps else ch
                        use kb_key(_c, [_TouchKeyboardTextInput(_c), SetVariable("kb_caps", False)])

            hbox:
                xalign 0.5
                spacing 10
                use kb_key("Aa", ToggleVariable("kb_caps"), 190, kb_caps)
                for ch in _kb_rows[2]:
                    python:
                        _c = ch.upper() if kb_caps else ch
                    use kb_key(_c, [_TouchKeyboardTextInput(_c), SetVariable("kb_caps", False)])
                use kb_key("←", _TouchKeyboardBackspace(), 190)

            hbox:
                xalign 0.5
                spacing 10
                use kb_key("'", _TouchKeyboardTextInput("'"))
                use kb_key("-", _TouchKeyboardTextInput("-"))
                use kb_key(".", _TouchKeyboardTextInput("."))
                use kb_key(_("Space"), _TouchKeyboardTextInput(" "), 640)
                use kb_key(_("OK"), _TouchKeyboardReturn(), 270)
