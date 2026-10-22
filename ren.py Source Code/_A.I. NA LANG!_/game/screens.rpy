## game/screens.rpy
## All screen definitions for A.I. na lang!
## CHOICE SCREEN 
default minigame_active = False
screen choice(items):
    zorder 150

    python:
        _is_small = renpy.variant("small")
        _btn_w = 1300 if _is_small else 1100
        _txt_sz = int((40 if _is_small else 30) * persistent.text_scale)
        _q_sz = int((40 if _is_small else 32) * persistent.text_scale)

        ## context for the decision: the line that was just shown (the question / situation).
        ## "[" is doubled so the text is not interpolated a second time.
        _ls = renpy.last_say()
        _q = menu_q if menu_q else (_ls.what if (_ls is not None and _ls.what) else "")
        _q = _q.replace("[", "[[")

    vbox:
        xalign 0.5
        yalign 0.78
        xsize _btn_w
        spacing 14

        if _q:
            frame:
                xfill True
                background Solid("#C41230")
                padding (6, 0, 0, 0)
                frame:
                    xfill True
                    background Solid(tc("#1F1B19EC"))
                    padding (28, 20)
                    text _q:
                        size _q_sz
                        color "#FAF7F3"
                        xalign 0.5
                        text_align 0.5
            null height 12

        for i in items:
            frame:
                xfill True
                background Solid("#C41230")
                padding (6, 0, 0, 0)

                textbutton i.caption:
                    action i.action
                    xfill True
                    background Solid(tc("#FAF7F3F2"))
                    hover_background Solid("#C4123022")
                    insensitive_background Solid(tc("#FAF7F3AA"))
                    padding (24, 14)
                    text_color tx("#1F1B19")
                    text_hover_color "#ffffff"
                    text_insensitive_color tx("#9C948C")
                    text_size _txt_sz
                    text_xalign 0.0
                    text_yalign 0.5

style default:
    font gui.default_font

style button_text:
    font gui.interface_font

style label_text:
    font gui.interface_font

transform grades_pulse:
    linear 0.9 zoom 1.07
    linear 0.9 zoom 1.0
    repeat

transform tutorial_pulse:
    alpha 1.0
    linear 0.5 alpha 0.45
    linear 0.5 alpha 1.0
    repeat

transform hud_idle:
    pass

screen bordered_frame():
    frame:
        xfill True
        yfill True
        background Solid(tc("#E3DBD2"))
        padding (3, 3)
        frame:
            xfill True
            yfill True
            background Solid("#C41230")
            padding (3, 3)
            frame:
                xfill True
                yfill True
                background Solid(tc("#FAF7F3"))
                transclude

screen menu_button(label, action, accent="#C41230"):
    fixed:
        xsize 390
        ysize 76

        frame:
            xoffset 4
            yoffset 4
            xsize 380
            ysize 72
            background Solid("#00000033")

        hbox at menu_button_hover:
            xsize 380
            ysize 72

            frame:
                xsize 6
                yfill True
                background accent

            frame:
                xfill True
                yfill True
                background Solid(tc("#FFFFFFE6"))
                frame:
                    xfill True
                    ysize 1
                    background Solid("#00000014")

                textbutton label:
                    action action
                    xfill True
                    yfill True
                    background None
                    hover_background Solid("#C41230")
                    text_color tx("#1F1B19")
                    text_hover_color "#ffffff"
                    text_size 34
                    text_bold True
                    text_xalign 0.15
init python:
    config.overlay_screens.append("quick_menu")
    config.overlay_screens.append("hud")
## HUD
## TUTORIAL SPOTLIGHT - wraps one HUD element. While `on` is true it gets a pulsing blue
## outline and a small tag underneath; the element itself never fades.
screen tut_glow(active, lbl, ya=0.0):
    fixed:
        fit_first True
        yalign ya
        transclude
        if active:
            fixed at tutorial_pulse:
                xfill True
                yfill True
                frame:
                    xfill True
                    ysize 5
                    yalign 0.0
                    background Solid("#58A6FF")
                frame:
                    xfill True
                    ysize 5
                    yalign 1.0
                    background Solid("#58A6FF")
                frame:
                    xsize 5
                    yfill True
                    xalign 0.0
                    background Solid("#58A6FF")
                frame:
                    xsize 5
                    yfill True
                    xalign 1.0
                    background Solid("#58A6FF")
            frame:
                xalign 0.5
                ypos 1.0
                yoffset 8
                background Solid("#58A6FF")
                padding (16, 6)
                text ("↑ " + lbl) size 30 color "#FFFFFF" bold True

transform stat_warn:
    alpha 1.0
    easeout 0.45 alpha 0.35
    easein 0.45 alpha 1.0
    repeat

transform stat_still:
    alpha 1.0

transform stat_cue_pop:
    alpha 0.0 yoffset -18
    easein 0.22 alpha 1.0 yoffset 0
    pause 1.9
    easeout 0.5 alpha 0.0

## HUD - one layout for desktop and phone (sizes change, structure does not).
## Both stat blocks always show their number, are tappable (tap = what this stat means),
## and pulse when the stat is low.
screen hud():
    zorder 5
    if show_hud:
        python:
            _ph = renpy.variant(["touch", "small", "mobile"])
            _bar_h = 124 if _ph else 100
            _pad = 24 if _ph else 36
            _lab = 24 if _ph else 20          # stat label size
            _val = 38 if _ph else 30          # stat number size
            _seg_w = 38 if _ph else 40
            _seg_h = 26 if _ph else 20
            _ct_w = 10 * _seg_w + 9 * 4       # width of the 10-segment row
            _mot_w = 270 if _ph else 230
            _btn_t = 28 if _ph else 22
            _long = len(day_label) >= 24
            _dsz = (30 if _long else 36) if _ph else (26 if _long else 30)
            _ct_col = cb("ct%d" % min(4, critical_thinking // 20))
            _ct_warn = critical_thinking < 25
            _mot_warn = motivation < 25

            _dl = day_label.lower()
            if "gabi" in _dl:
                _day_color = cb("night")
            elif "umaga" in _dl or "tanghali" in _dl or "hapon" in _dl:
                _day_color = cb("day")
            else:
                _day_color = cb("special")

        vbox:
            xfill True
            yalign 0.0
            spacing 0

            frame:
                xfill True
                ysize _bar_h
                background Solid(tc("#FFFFFFF5"))
                padding (_pad, 0)

                frame:
                    xfill True
                    ysize 3
                    yalign 1.0
                    background Solid("#C41230")

                hbox:
                    xfill True
                    yfill True
                    spacing 24

                    ## day / week chip
                    frame:
                        yalign 0.5
                        background Frame(theme_img("whitediamond"), Borders(40, 0, 60, 0))
                        padding (36, 16)
                        hbox:
                            spacing 14
                            yalign 0.5
                            frame:
                                xsize 18
                                ysize 18
                                yalign 0.5
                                background Solid(_day_color)
                            text "[day_label]" size _dsz color tx("#1F1B19") bold True yalign 0.5

                    frame:
                        xsize 2
                        ysize 52
                        yalign 0.5
                        background Solid("#00000014")

                    ## Critical Thinking
                    use tut_glow(tutorial_highlight in ("ct", "all"), "Critical Thinking", 0.5):
                        button:
                            action Function(toggle_stat_info, "ct")
                            background Solid(tc("#F3EFEA"))
                            hover_background Solid(tc("#E8EEF3"))
                            padding (20, 10)
                            vbox:
                                spacing 6
                                fixed:
                                    xsize _ct_w
                                    ysize (_val + 6)
                                    text "CRITICAL THINKING" size _lab color tx("#C41230") yalign 0.5
                                    text str(critical_thinking) size _val color _ct_col bold True xalign 1.0 yalign 0.5 at (stat_warn if _ct_warn else stat_still)
                                hbox:
                                    spacing 4
                                    for i in range(10):
                                        python:
                                            filled = (critical_thinking // 10) > i
                                            seg_color = cb_ct_seg(i, filled)
                                        frame:
                                            xsize _seg_w
                                            ysize _seg_h
                                            background Solid(seg_color)

                    frame:
                        xsize 2
                        ysize 52
                        yalign 0.5
                        background Solid("#00000014")

                    ## Motivation
                    use tut_glow(tutorial_highlight in ("mot", "all"), "Motivation", 0.5):
                        button:
                            action Function(toggle_stat_info, "mot")
                            background Solid(tc("#F3EFEA"))
                            hover_background Solid(tc("#E8EEF3"))
                            padding (20, 10)
                            vbox:
                                spacing 6
                                fixed:
                                    xsize _mot_w
                                    ysize (_val + 6)
                                    hbox:
                                        spacing 8
                                        yalign 0.5
                                        text "♥" size (_lab + 6) color cb("motivation") yalign 0.5 at (stat_warn if _mot_warn else stat_still)
                                        text "MOTIVATION" size _lab color tx("#C41230") bold True yalign 0.5
                                    text str(motivation) size _val color cb("motivation") bold True xalign 1.0 yalign 0.5 at (stat_warn if _mot_warn else stat_still)
                                bar:
                                    value motivation
                                    range 100
                                    xsize _mot_w
                                    ysize _seg_h
                                    left_bar  Solid(cb("motivation"))
                                    right_bar Solid(tc("#B8AFA6"))

                    null width True

                    use tut_glow(tutorial_highlight == "all", "Grades", 0.5):
                        frame:
                            background Solid("#C41230")
                            padding (24, 14)
                            textbutton _("Tingnan ang Grades"):
                                action Show("grade_results")
                                background None
                                hover_background None
                                text_color "#FFFFFF"
                                text_hover_color "#FFE3E7"
                                text_size _btn_t
                                text_bold True

## Tap a HUD stat to see what it means. Tap anywhere (or wait) to close.
screen hud_info(stat):
    modal True
    zorder 40

    python:
        _ph = renpy.variant(["touch", "small", "mobile"])
        if stat == "ct":
            _title = "Critical Thinking"
            _value = critical_thinking
            _col = cb("ct%d" % min(4, critical_thinking // 20))
            _body = _("Bumababa tuwing binibigay mo sa AI ang pag-iisip. Tumataas kapag ikaw talaga ang gumawa.")
        else:
            _title = "Motivation"
            _value = motivation
            _col = cb("motivation")
            _body = _("Bumababa sa panic o guilt. Tumataas kapag may confidence ka sa sarili mo.")

    button:
        action Hide("hud_info")
        xfill True
        yfill True
        background None

    frame:
        xalign 0.5
        ypos (150 if _ph else 126)
        xsize (1200 if _ph else 920)
        background Solid(tc("#FFFFFFF8"))
        padding (0, 0)

        vbox:
            xfill True
            frame:
                xfill True
                ysize 8
                background Solid(_col)
            vbox:
                xalign 0.5
                xsize (1100 if _ph else 840)
                spacing 12
                null height 10
                hbox:
                    xfill True
                    spacing 20
                    text _title size (40 if _ph else 32) color tx("#C41230") bold True yalign 0.5
                    text (str(_value) + " / 100") size (40 if _ph else 32) color _col bold True yalign 0.5
                text _body size (32 if _ph else 26) color tx("#2B2624")
                text _("Pindutin kahit saan para isara.") size (26 if _ph else 20) color tx("#6B6259")
                null height 10

    key "game_menu" action Hide("hud_info")
    timer 9.0 action Hide("hud_info")

## A short pop-up whenever Critical Thinking or Motivation changes (shown by stat_cue()).
screen stat_cue(stat, amount):
    zorder 30

    python:
        _ph = renpy.variant(["touch", "small", "mobile"])
        _gain = amount > 0
        _name = "Critical Thinking" if stat == "ct" else "Motivation"
        _col = "#56D364" if _gain else "#E5677A"
        _txt = ("+" if _gain else "") + str(amount)
        _sz = 38 if _ph else 30

    frame at stat_cue_pop:
        xalign 0.5
        ypos (170 if _ph else 150)
        background Solid(tc("#FFFFFFF2"))
        padding (0, 0)

        hbox:
            frame:
                xsize 8
                ysize (_sz * 2)
                background Solid(_col)
            hbox:
                spacing 16
                yalign 0.5
                null width 8
                text ("↑" if _gain else "↓") size _sz color _col bold True yalign 0.5
                text _name size _sz color tx("#2B2624") yalign 0.5
                text _txt size (_sz + 6) color _col bold True yalign 0.5
                null width 8

    timer 2.7 action Hide("stat_cue_" + stat)


## One quick-menu button (sizes follow phone / desktop).
screen qm_button(label, act, w, sens=True):
    python:
        _qs = renpy.variant(["touch", "small", "mobile"])
        _qh = 72 if _qs else 48
        _qt = 32 if _qs else 22

    textbutton label:
        action act
        sensitive sens
        xsize w
        ysize _qh
        background Solid(tc("#F3EFEA"))
        hover_background Solid("#C41230")
        selected_background Solid("#C41230")
        text_color tx("#6B6259")
        text_hover_color "#FFFFFF"
        text_selected_color "#FFFFFF"
        text_insensitive_color tx("#9C948C")
        text_size _qt
        text_xalign 0.5
        text_yalign 0.5

## The small speed chip next to Skip / Auto: tap to cycle 1x, 2x, 4x ...
screen qm_chip(label, act):
    python:
        _qs = renpy.variant(["touch", "small", "mobile"])
        _qh = 72 if _qs else 48
        _qt = 28 if _qs else 20

    textbutton label:
        action act
        xsize (96 if _qs else 64)
        ysize _qh
        background Solid(tc("#E3DBD2"))
        hover_background Solid("#8C0E23")
        text_color tx("#C41230")
        text_hover_color "#FFFFFF"
        text_size _qt
        text_bold True
        text_xalign 0.5
        text_yalign 0.5

screen quick_menu():
    zorder 100

    python:
        _qs = renpy.variant(["touch", "small", "mobile"])
        _qbar = 88 if _qs else 64
        _qw = 150 if _qs else 100
        _qw_h = 190 if _qs else 120
        _qw_b = 420 if _qs else 300
        _qsp = 6 if _qs else 4

    if show_hud:
        frame:
            xfill True
            ysize _qbar
            yalign 1.0
            background None
            padding (16, 0)

            hbox:
                xfill True
                yalign 0.5

                ## left: Back / History / Skip + speed / Auto + speed
                hbox:
                    yalign 0.5
                    spacing _qsp

                    use qm_button(_("Back"), Rollback(), _qw)
                    use qm_button(_("History"), ShowMenu("history"), _qw_h)

                    hbox:
                        spacing 2
                        use qm_button(_("Skip"), [Preference("skip", "all"), Skip()], _qw, (not minigame_active))
                        use qm_chip(SKIP_LABELS[persistent.skip_speed], Function(cycle_skip_speed))

                    hbox:
                        spacing 2
                        use qm_button(_("Auto"), Preference("auto-forward", "toggle"), _qw)
                        use qm_chip(AUTO_LABELS[persistent.auto_speed], Function(cycle_auto_speed))

                ## center: phone / AI access, only usable during a quiz
                null width True
                if minigame_active:
                    textbutton _("📱  Browse Social Media"):
                        action Function(show_phone_ai)
                        xsize _qw_b
                        ysize (72 if _qs else 48)
                        background Solid("#C4123022")
                        hover_background Solid("#C41230")
                        text_color "#E5677A"
                        text_hover_color "#FFFFFF"
                        text_size (32 if _qs else 22)
                        text_xalign 0.5
                        text_yalign 0.5
                else:
                    null width _qw_b
                null width True

                ## right: Save / Load / Prefs
                hbox:
                    yalign 0.5
                    spacing _qsp

                    use qm_button(_("Save"), ShowMenu("save"), _qw)
                    use qm_button(_("Load"), ShowMenu("load"), _qw)
                    use qm_button(_("Prefs"), ShowMenu("preferences"), _qw)


## PHONE AI OVERLAY

init python:
    def show_phone_ai():
        renpy.show_screen("phone_ai_overlay")

screen phone_ai_overlay():
    modal True
    zorder 200
    on "show" action Play("sound", "audio/sfx/sfx_phone.ogg")
    frame:
        xsize 680
        ysize 480
        xalign 0.5
        yalign 0.4
        background Solid(tc("#FAF7F3F4"))
        padding (30, 30)

        vbox:
            spacing 20
            text "Phone ni [player_name]" size 34 color "#E5677A" xalign 0.5
            text "Naka-open ang AI app..." size 28 color tx("#6B6259") xalign 0.5
            null height 10

            textbutton _("Itanong sa AI ang sagot"):
                action [
                    Function(ct_change, -10),
                    Function(mot_change, -3),
                    Hide("phone_ai_overlay"),
                    Call("ai_used_result")
                ]
                xfill True
                ysize 80
                background Solid("#C41230")
                text_color "#ffffff"
                text_size 30
                text_xalign 0.5
                text_yalign 0.5

            textbutton _("Hindi na. Sariling gawa na lang!"):
                action [
                    Function(ct_change, +5),
                    Hide("phone_ai_overlay")
                ]
                xfill True
                ysize 80
                background Solid(tc("#F3EFEA"))
                text_color cb("ai_text")
                text_size 30
                text_xalign 0.5
                text_yalign 0.5

            text "CT: [critical_thinking]/100  |  AI uses: [ai_use_count]" size 24 color tx("#6B6259") xalign 0.5

## MAIN MENU 

transform title_pulse:
    alpha 0.7
    easein 2.5 alpha 1.0
    easeout 2.5 alpha 0.7
    repeat

transform menu_slide_in(delay_time):
    xoffset 50 alpha 0.0
    pause delay_time
    easein 0.6 xoffset 0 alpha 1.0

transform notify_slide:
    xoffset 80 alpha 0.0
    easein 0.3 xoffset 0 alpha 1.0

screen notify(message):
    zorder 250

    python:
        ## below the HUD bar (and its tutorial tags); bigger text/box on phones
        _ns = renpy.variant(["touch", "small", "mobile"])
        _nw = 700 if _ns else 460
        _nh = 84 if _ns else 64
        _nt = 32 if _ns else 24

    frame at notify_slide:
        xalign 0.98
        ypos 250
        xsize _nw
        ysize _nh
        background Solid(tc("#FFFFFFEE"))

        hbox:
            xfill True
            yfill True
            frame:
                xsize 5
                ysize _nh
                background Solid("#C41230")
            frame:
                xfill True
                yfill True
                background None
                padding (16, 0)
                text message size _nt color "#E5677A" yalign 0.5 xalign 0.0

    timer 3.25 action Hide("notify")

# ── MAIN MENU SCREEN
transform menu_button_hover:
    on hover:
        linear 0.15 xoffset 6
    on idle:
        linear 0.15 xoffset 0

screen main_menu():
    tag menu
    style_prefix "main_menu"

    use bordered_frame():

        add Transform("images/backgrounds/main_menu.webp", fit="cover", xalign=0.5, yalign=0.5)
        frame:
            xfill True
            yfill True
            background Solid("#1a111400")
        frame:
            xfill True
            yfill True
            background Solid("#c4123000")
    if renpy.variant("small"):
        fixed:
            xfill True
            yfill True

            vbox at title_pulse:
                xpos 60
                xanchor 0.0
                yalign 0.10
                xmaximum 900
                spacing 5
                text "A.I. NA LANG!" font "gui/fonts/Marmelad-Regular.ttf" size 100 color "#ffffff" bold True outlines [(7, "#000000", 0, 0), (3, "#ff002b", 0, 0)] xalign 0.0
                text "A Web-Based Interactive Visual Novel by Group 8" size 30 color "#ffffff" xalign 0.0 outlines [(1, "#000000", 0, 0)]
                text "-Clarin" size 10 color "#0abbd2" xalign 0.0 outlines [(1, "#ffffff", 2, 2)]

            vbox:
                xalign 0.90
                yalign 0.38
                spacing 0

                null height 70

                vbox:
                    xalign 1.0
                    spacing 18

                    fixed:
                        xsize 380
                        ysize 68
                        at menu_slide_in(0.1)
                        use menu_button(_("Simulan/New game"), Start(), "#C41230")

                    fixed:
                        xsize 380
                        ysize 68
                        at menu_slide_in(0.2)
                        use menu_button(_("Ipagpatuloy/Load"), ShowMenu("load"), "#C41230")

                    fixed:
                        xsize 380
                        ysize 68
                        at menu_slide_in(0.3)
                        use menu_button(_("Mga Settings"), ShowMenu("preferences"), "#C41230")

                    fixed:
                        xsize 380
                        ysize 68
                        at menu_slide_in(0.35)
                        use menu_button(_("Chapter Select"), ShowMenu("chapter_select"), "#C41230")
                    fixed:
                        xsize 380
                        ysize 68
                        at menu_slide_in(0.4)
                        use menu_button(_("Credits"), ShowMenu("about"), "#C41230")

                    fixed:
                        xsize 380
                        ysize 68
                        at menu_slide_in(0.45)
                        use menu_button(_("Tulong"), ShowMenu("help"), "#C41230")

                    if not renpy.variant("web"):
                        fixed:
                            xsize 380
                            ysize 68
                            at menu_slide_in(0.5)
                            use menu_button(_("Umalis"), Quit(confirm=not main_menu), "#C41230")
    else:
        fixed:
            xfill True
            yfill True

            vbox at title_pulse:
                xpos 60
                xanchor 0.0
                yalign 0.14
                xmaximum 900
                spacing 5
                text "A.I. NA LANG!" font "gui/fonts/Marmelad-Regular.ttf" size 100 color "#ffffff" bold True outlines [(7, "#000000", 0, 0), (3, "#C41230", 0, 0)] xalign 0.0
                text "A Web-Based Interactive Visual Novel by Group 8" size 30 color "#ffffff" xalign 0.0 outlines [(1, "#070707", 0, 0)]
                text "-Clarin" size 10 color "#0abbd2" xalign 0.0 outlines [(1, "#ffffff", 2, 2)]

            vbox:
                xalign 1.0
                xoffset -60
                yalign 0.38

                null height 70

                vbox:
                    xalign 1.0
                    spacing 18

                    fixed:
                        xsize 380
                        ysize 68
                        at menu_slide_in(0.1)
                        use menu_button(_("Simulan/New game"), Start(), "#C41230")

                    fixed:
                        xsize 380
                        ysize 68
                        at menu_slide_in(0.2)
                        use menu_button(_("Ipagpatuloy/Load"), ShowMenu("load"), "#C41230")

                    fixed:
                        xsize 380
                        ysize 68
                        at menu_slide_in(0.3)
                        use menu_button(_("Mga Settings"), ShowMenu("preferences"), "#C41230")

                    fixed:
                        xsize 380
                        ysize 68
                        at menu_slide_in(0.35)
                        use menu_button(_("Chapter Select"), ShowMenu("chapter_select"), "#C41230")

                    fixed:
                        xsize 380
                        ysize 68
                        at menu_slide_in(0.4)
                        use menu_button(_("Credits"), ShowMenu("about"), "#C41230")

                    fixed:
                        xsize 380
                        ysize 68
                        at menu_slide_in(0.45)
                        use menu_button(_("Tulong"), ShowMenu("help"), "#C41230")

                    if not renpy.variant("web"):
                        fixed:
                            xsize 380
                            ysize 68
                            at menu_slide_in(0.5)
                            use menu_button(_("Umalis"), Quit(confirm=not main_menu), "#b91c1c")

            vbox:
                xalign 0.97
                yalign 0.97
                spacing 4
                text "[config.name!t]  [config.version]" size 24 xalign 1.0 color "#ffffffB0"
                text build_label size 22 xalign 1.0 color "#ffffff80"
## CHAPTER SELECT — replaces the old Extras -> Week Select chain
screen chapter_select():
    tag menu
    use base_menu(_("Chapter Select")):
        vbox:
            xalign 0.5
            yalign 0.05
            spacing 12
            xmaximum 760

            text "Direktang pumunta sa kahit anong bahagi ng laro." size 24 color tx("#6B6259") xalign 0.5
            null height 10

            $ _weeks = [
                ("Chapter 1  Day One Vibes", "chapter1"),
                ("Chapter 2  Laro Muna!", "chapter2"),
                ("Chapter 3  Submit Mo Na Lang", "chapter3"),
                ("Chapter 4  May Test Bukas", "chapter4"),
                ("Chapter 5  Incomplete?", "chapter5"),
                ("Chapter 6  Busted", "chapter6"),
                ("Chapter 7  Last Chance Na", "chapter7"),
                ("Chapter 8  Finals", "chapter8"),
            ]

            for _label, _target in _weeks:
                textbutton _label:
                    action [SetVariable("_extras_target", _target), Start("extras_setup")]
                    xfill True
                    ysize 56
                    background Solid(tc("#F3EFEA"))
                    hover_background Solid("#C41230")
                    text_color tx("#2B2624")
                    text_hover_color "#ffffff"
                    text_size 24
                    text_xalign 0.0
                    padding (24, 0)

## CHAPTER TITLE CARD
screen chapter_title(chapter_num, chapter_name, subtitle):
    zorder 150
    on "show" action Play("sound", "audio/sfx/sfx_page_turn.ogg")

    frame:
        xfill True
        yfill True
        background Solid(tc("#FAF7F3F8"))

        frame:
            xfill True
            ysize 5
            yalign 0.42
            background Solid("#C41230")

        vbox:
            xalign 0.5
            yalign 0.45
            spacing 14

            text "CHAPTER [chapter_num]" size 35 color "#E5677A" xalign 0.5
            text "[chapter_name]" size 70 color "#ffffff" xalign 0.5 bold True outlines [(2, "#C41230", 0, 0)]
            text "[subtitle]" size 40 color tx("#202020") xalign 0.5 italic True

        text "Click anything to continue" xalign 0.5 yalign 0.92 size 40 color tx("#3d3d3d")

    key "K_RETURN" action Return()
    key "K_SPACE"  action Return()
    button:
        xfill True
        yfill True
        action Return()
        background None
## ── QUIZ CARD (redesigned for the defense build) ───────────────────────────
## Same behaviour as before (same arguments, same labels, shuffled answers,
## AI shortcut). New: category chip, topic, progress bar, CT meter, question
## number, hover motion, a Hint button for non-IT players, and a one-time tip.
## NOTE: _() only MARKS a string; tr() (ui_polish.rpy) translates immediately,
## which is needed whenever a string is joined to another or edited before display.
default quiz_tip_seen = False

transform quiz_card_in:
    alpha 0.0 yoffset 26
    easeout 0.28 alpha 1.0 yoffset 0

transform quiz_option_hover:
    on idle:
        easein 0.12 xoffset 0
    on hover:
        easeout 0.12 xoffset 10

screen quiz_hint_popup(hint_text):
    modal True
    zorder 190

    frame:
        xfill True
        yfill True
        background Solid(tc("#14110F99"))

    frame:
        at quiz_card_in
        xalign 0.5
        yalign 0.5
        xsize 960
        background Solid(tc("#FAF7F3"))
        padding (0, 0)

        vbox:
            xfill True
            frame:
                xfill True
                ysize 8
                background Solid("#0072B2")
            vbox:
                xalign 0.5
                xsize 880
                spacing 18
                null height 22
                text "HINT" size 34 color tx("#005A9C") bold True
                text hint_text size 30 color tx("#2B2624")
                text tr("Ito ay paliwanag ng ideya, hindi ng sagot.") size 20 color tx("#6B6259")
                textbutton tr("Sige, balik sa tanong"):
                    action Hide("quiz_hint_popup")
                    xalign 0.5
                    xsize 360
                    ysize 64
                    background Solid("#005A9C")
                    hover_background Solid("#003F6E")
                    text_color "#FFFFFF"
                    text_size 26
                    text_xalign 0.5
                    text_yalign 0.5
                null height 24

init python:
    def quiz_est_lines(text, size, width):
        ## rough line count for a text block: explicit newlines plus wrapping at ~0.52 em/char
        per = max(8, int(width / max(1.0, size * 0.52)))
        n = 0
        for ln in str(text).split("\n"):
            n += max(1, -(-len(ln) // per))
        return n

screen minigame(title, question, options, correct_idx, subject, ct_reward=8, grade_reward=10, correct_label="minigame_correct", wrong_label="minigame_wrong"):
    modal True
    zorder 180
    on "show" action [SetVariable("minigame_active", True), SetVariable("quiz_fb", None), Function(stop_skipping)]
    on "hide" action SetVariable("minigame_active", False)

    python:
        _is_small = renpy.variant("small")
        ## phones: wide two-column card (question left, answers + AI shortcut right) so even
        ## the long multi-line IOS-command questions fit in 1080 px without scrolling
        _card_w = 1700 if _is_small else 1200
        _left_w = 760
        _right_w = 940
        _btn_h  = 84  if _is_small else 78
        _txt_sz = 30  if _is_small else 26
        _q_sz   = 32  if _is_small else 28
        _f_s    = 24  if _is_small else 18
        _f_m    = 26  if _is_small else 20
        _gap    = 12
        _ai_h   = 120 if _is_small else 60
        _q_t, _explained = quiz_expand(tr(question))
        _cat, _topic, _note, _qi, _qn = mg_parse_title(tr(title))
        _accent = quiz_accent(subject)
        _hint = quiz_hint(question)

    ## Dim backdrop
    frame:
        xfill True
        yfill True
        background Solid(tc("#FAF7F3F2"))

        frame:
            at quiz_card_in
            xalign 0.5
            yalign 0.5
            xsize _card_w
            background Solid(tc("#FAF7F3"))
            padding (0, 0)

            vbox:
                xfill True
                spacing 0

                ## Accent bar in the subject colour
                frame:
                    xfill True
                    ysize 8
                    background Solid(_accent)

                ## Header: category chip + topic on the left, CT meter on the right
                frame:
                    xfill True
                    ysize 72
                    background Solid("#C41230")
                    padding (24, 0)
                    fixed:
                        hbox:
                            yalign 0.5
                            spacing 16
                            frame:
                                yalign 0.5
                                background Solid(tc("#2B2624"))
                                padding (14, 6)
                                text _cat.upper() size _f_m color "#FFFFFF" bold True
                            text _topic size (30 if _is_small else 28) color "#FFFFFF" bold True yalign 0.5
                        if not _is_small:
                            vbox:
                                xalign 1.0
                                yalign 0.5
                                spacing 4
                                text "Critical Thinking [critical_thinking]/100" size 20 color "#F3EFEA" xalign 1.0
                                bar:
                                    value StaticValue(critical_thinking, 100)
                                    xsize 150
                                    ysize 8
                                    thumb None
                                    left_bar Solid("#FFFFFF")
                                    right_bar Solid("#FFFFFF55")

                ## Progress segments (only when the title has a counter like (3/7))
                if _qn > 0:
                    frame:
                        xfill True
                        background Solid(tc("#F3EFEA"))
                        padding (24, 10)
                        hbox:
                            spacing 8
                            yalign 0.5
                            text (str(_qi) + " / " + str(_qn)) size _f_m color tx("#6B6259") yalign 0.5
                            for _k in range(_qn):
                                frame:
                                    xsize (28 if _is_small else 44)
                                    ysize 8
                                    yalign 0.5
                                    background Solid("#C41230" if _k < (_qi - 1) else (_accent if _k == (_qi - 1) else tc("#D9D0C6")))

                if _is_small:
                    hbox:
                        vbox:
                            xsize _left_w
                            use quiz_question_block(_qi, _hint, _note, _q_t, _q_sz, _f_s, _f_m)
                            if not quiz_tip_seen:
                                null height 12
                                use quiz_tip_block(_f_m)
                        vbox:
                            xsize _right_w
                            use quiz_answers_block(question, options, correct_idx, subject, ct_reward, grade_reward, correct_label, wrong_label, _explained, _right_w - 66, _btn_h, _txt_sz, _gap)
                            null height 12
                            use quiz_ai_block(subject, grade_reward, _txt_sz, _f_s, _ai_h, _right_w - 224)
                            null height 12
                else:
                    use quiz_question_block(_qi, _hint, _note, _q_t, _q_sz, _f_s, _f_m)
                    null height 16
                    use quiz_answers_block(question, options, correct_idx, subject, ct_reward, grade_reward, correct_label, wrong_label, _explained, _card_w - 78, _btn_h, _txt_sz, _gap)
                    null height 16
                    if not quiz_tip_seen:
                        use quiz_tip_block(_f_m)
                        null height 12
                    use quiz_ai_block(subject, grade_reward, _txt_sz, _f_s, _ai_h, _card_w - 224)
                    null height 6

screen quiz_question_block(qi, hint, note, q_t, q_sz, f_s, f_m):
    frame:
        xfill True
        background Solid(tc("#FFFFFFAA"))
        padding (22, 20)
        vbox:
            spacing 8
            fixed:
                xfill True
                ysize (int(f_s * 1.45) + 12)
                text (tr("TANONG") + ((" " + str(qi)) if qi else "")) size f_s color tx("#C41230") bold True yalign 0.5
                if hint:
                    textbutton tr("Hint (para sa hindi IT)"):
                        action [SetVariable("quiz_tip_seen", True), Show("quiz_hint_popup", hint_text=hint)]
                        xalign 1.0
                        yalign 0.5
                        background Solid(tc("#E8EEF3"))
                        hover_background Solid(tc("#C8D8E6"))
                        padding (16, 6)
                        text_color tx("#005A9C")
                        text_size f_m
            text q_t size q_sz color tx("#2B2624")
            if note:
                text note size f_s color tx("#6B6259")

screen quiz_answers_block(question, options, correct_idx, subject, ct_reward, grade_reward, correct_label, wrong_label, explained, opt_w, btn_h, txt_sz, gap):
    vbox:
        xfill True
        spacing gap
        python:
            _mg_order = mg_order(question, len(options))
        for idx in range(len(options)):
            python:
                _src = _mg_order[idx]
                _opt, _x = quiz_expand(mg_strip(tr(options[_src])), explained, True)
                _letter = chr(65 + idx)
                _is_correct = (_src == correct_idx)
                _jump = Jump(correct_label) if _is_correct else Jump(wrong_label)
                _row_h = max(btn_h, int(quiz_est_lines(_opt, txt_sz, opt_w - 40) * txt_sz * 1.45) + 24)
            hbox:
                xfill True
                ysize _row_h
                spacing 14
                frame:
                    xsize 52
                    ysize 52
                    yalign 0.5
                    background Solid("#C41230")
                    text _letter size 26 color "#ffffff" bold True xalign 0.5 yalign 0.5
                textbutton _opt:
                    at quiz_option_hover
                    action [
                        SetVariable("quiz_tip_seen", True),
                        SetVariable("quiz_fb", "correct" if _is_correct else "wrong"),
                        SetVariable("quiz_last_ct", ct_reward if _is_correct else -5),
                        SetVariable("quiz_last_grade", ((grade_reward if _is_correct else -5) if subject else 0)),
                        Function(ct_change, ct_reward if _is_correct else -5),
                        Function(grade_change, subject, grade_reward if _is_correct else -5),
                        Hide("minigame"),
                        _jump
                    ]
                    xsize opt_w
                    yfill True
                    background Solid(tc("#F3EFEA"))
                    hover_background Solid("#C4123033")
                    padding (20, 8)
                    text_color tx("#2B2624")
                    text_hover_color tx("#C41230")
                    text_size txt_sz
                    text_xalign 0.0
                    text_yalign 0.5

screen quiz_tip_block(f_m):
    frame:
        xfill True
        background Solid(tc("#E8EEF3"))
        padding (20, 12)
        text _("Walang IT background? Okay lang. Pindutin ang Hint kung kailangan. Pag-isipan muna, saka pumili.") size f_m color tx("#2B2624")

screen quiz_ai_block(subject, grade_reward, txt_sz, f_s, ai_h, ai_w):
    frame:
        xfill True
        background Solid("#C4123015")
        padding (20, 16)
        fixed:
            ysize ai_h
            vbox:
                yalign 0.5
                spacing 4
                xmaximum ai_w
                text tr("Itanong sa AI") size txt_sz color tx("#C41230") bold True
                if subject:
                    text ("Critical Thinking -10  |  Grade +" + str(grade_reward) + "  " + tr("(pero walang naiintindihan)")) size f_s color tx("#6B6259")
                else:
                    text ("Critical Thinking -10  |  " + tr("(pero walang naiintindihan)")) size f_s color tx("#6B6259")
            textbutton _("Gamitin"):
                xalign 1.0
                yalign 0.5
                action [
                    SetVariable("quiz_tip_seen", True),
                    SetVariable("quiz_fb", "ai"),
                    SetVariable("quiz_last_ct", -10),
                    SetVariable("quiz_last_grade", (grade_reward if subject else 0)),
                    Function(use_ai, subject, grade_reward),
                    Hide("minigame"),
                    Call("ai_used_result")
                ]
                background Solid("#C41230")
                hover_background Solid("#8C0E23")
                ysize 56
                xsize 160
                text_color "#fff"
                text_size 24
                text_xalign 0.5
                text_yalign 0.5

## GRADE RESULTS SCREEN
screen grade_results():
    modal True
    zorder 170

    python:
        _subjects = [
            ("Networking", networking_grade, cb("grade_net")),
            ("Programming", programming_grade, cb("grade_prog")),
            ("Cybersecurity", cyber_grade, cb("grade_cyber")),
        ]
        _meters = [
            ("CRITICAL THINKING", critical_thinking, cb("ct4")),
            ("MOTIVATION", motivation, cb("motivation")),
        ]

    ## Backdrop: hides the scene, HUD, and dialogue behind the card
    frame:
        xfill True
        yfill True
        background Solid(tc("#FAF7F3F2"))

    frame:
        at quiz_card_in
        xsize 1120
        yalign 0.5
        xalign 0.5
        background Solid(tc("#FFFFFFF8"))
        padding (0, 0)

        vbox:
            xfill True
            spacing 0

            frame:
                xfill True
                ysize 8
                background Solid("#C41230")

            vbox:
                xalign 0.5
                xsize 1040
                spacing 22

                null height 24
                vbox:
                    spacing 4
                    text _("RESULTA NG GRADES") size 42 color tx("#C41230") xalign 0.5 bold True
                    text day_label size 22 color tx("#6B6259") xalign 0.5

                ## One card per subject: grade, letter, bar, and a status word
                hbox:
                    xalign 0.5
                    spacing 24
                    for _name, _score, _col in _subjects:
                        $ _pass = _score >= 60
                        frame:
                            xsize 320
                            background Solid(tc("#F3EFEA"))
                            padding (0, 0)
                            vbox:
                                spacing 12
                                frame:
                                    xfill True
                                    ysize 8
                                    background Solid(_col)
                                vbox:
                                    xalign 0.5
                                    xsize 280
                                    spacing 12
                                    text _name size 28 color tx("#2B2624") bold True xalign 0.5
                                    frame:
                                        xalign 0.5
                                        xsize 120
                                        ysize 120
                                        background Solid(tc("#2B2624") if _pass else "#C41230")
                                        text letter_grade(_score) size (72 if _pass else 48) color "#FFFFFF" bold True xalign 0.5 yalign 0.5
                                    text (str(_score) + " / 100") size 30 color tx("#2B2624") bold True xalign 0.5
                                    bar:
                                        value StaticValue(_score, 100)
                                        xfill True
                                        ysize 14
                                        thumb None
                                        left_bar Solid(tc("#2B2624") if _pass else "#C41230")
                                        right_bar Solid(tc("#D9D0C6"))
                                    frame:
                                        xalign 0.5
                                        background Solid(tc("#2B2624") if _pass else "#C41230")
                                        padding (16, 4)
                                        text ("PASSED" if _pass else "INCOMPLETE") size 20 color "#FFFFFF" bold True
                                    null height 14

                ## Critical Thinking, Motivation, and the AI counter (the core mechanic)
                frame:
                    xfill True
                    background Solid(tc("#F3EFEA"))
                    padding (28, 20)
                    vbox:
                        spacing 14
                        for _label, _val, _col in _meters:
                            vbox:
                                spacing 6
                                fixed:
                                    xfill True
                                    ysize 30
                                    text _label size 22 color tx("#2B2624") bold True xalign 0.0
                                    text (str(_val) + " / 100") size 22 color tx("#2B2624") bold True xalign 1.0
                                bar:
                                    value StaticValue(_val, 100)
                                    xfill True
                                    ysize 14
                                    thumb None
                                    left_bar Solid(_col)
                                    right_bar Solid(tc("#D9D0C6"))
                        fixed:
                            xfill True
                            ysize 40
                            text "AI ANSWERS" size 22 color tx("#2B2624") bold True xalign 0.0 yalign 0.5
                            frame:
                                xalign 1.0
                                yalign 0.5
                                background Solid("#C41230" if ai_use_count > 0 else tc("#2B2624"))
                                padding (18, 4)
                                text str(ai_use_count) size 24 color "#FFFFFF" bold True
                        text (tr("Bawat sagot ng AI ay bawas sa Critical Thinking mo.") if ai_use_count > 0 else tr("Walang AI. Lahat ay sarili mong pag-iisip.")) size 20 color tx("#6B6259")

                textbutton _("Magpatuloy"):
                    action Hide("grade_results")
                    xalign 0.5
                    xsize 300
                    ysize 70
                    background Solid("#C41230")
                    hover_background Solid("#8C0E23")
                    text_color "#fff"
                    text_size 30
                    text_xalign 0.5
                    text_yalign 0.5
                null height 30

################################################################################
## SAY SCREEN — dialogue textbox
################################################################################
default quiz_fb = None
default quiz_last_ct = 0
default quiz_last_grade = 0

screen say(who, what):
    style_prefix "say"

    if quiz_fb:
        ## Quiz feedback (correct / wrong / AI answer): the explanation line is shown
        ## as a card, like the "AI answered" screen. quiz_fb is cleared by a
        ## "$ quiz_fb = None" line placed right after that first line in each label.
        python:
            _fb_col = quiz_fb_color(quiz_fb)
            _fb_head = quiz_fb_heading(quiz_fb)
            _fb_sz = say_fit_size(what, 36, width=960, height=250)

        window:
            id "window"
            xfill True
            yfill True
            background Solid(tc("#14110FB3"))

            frame:
                at quiz_card_in
                xalign 0.5
                yalign 0.5
                xsize 1100
                background Solid(tc("#FAF7F3"))
                padding (0, 0)
                vbox:
                    xfill True
                    frame:
                        xfill True
                        ysize 10
                        background Solid(_fb_col)
                    vbox:
                        xalign 0.5
                        xsize 980
                        spacing 24
                        null height 26
                        frame:
                            xalign 0.5
                            background Solid(_fb_col)
                            padding (48, 12)
                            text _fb_head size 56 color "#FFFFFF" bold True xalign 0.5
                        text what:
                            id "what"
                            size _fb_sz
                            color tx("#2B2624")
                            xalign 0.5
                            text_align 0.5
                            xmaximum 960
                        hbox:
                            xalign 0.5
                            spacing 16
                            frame:
                                background Solid(tc("#2B2624"))
                                padding (18, 6)
                                text ("Critical Thinking " + ("%+d" % quiz_last_ct)) size 24 color "#FFFFFF" bold True
                            if quiz_last_grade != 0:
                                frame:
                                    background Solid(tc("#2B2624"))
                                    padding (18, 6)
                                    text ("Grade " + ("%+d" % quiz_last_grade)) size 24 color "#FFFFFF" bold True
                        text tr("I-click para magpatuloy") size 22 color tx("#6B6259") xalign 0.5
                        null height 24

    else:
        python:
            ## the name plate is tsz(40); the dialogue gets the height that is left in the
            ## 206 px content area of the box (same budget as before at normal text size)
            _who_sz = tsz(40)
            _say_h = (206 - 4 - int(_who_sz * 1.45) - 4) if who else 200
            _say_sz = say_fit_size(what, tsz(40), height=max(90, _say_h))

        window:
            id "window"
            xfill True
            yalign 1.0
            ysize 420
            background None

            frame:
                xfill True
                yalign 1.0
                ysize 300
                background Frame(theme_textbox(), Borders(0, 0, 0, 0))
                padding (30, 24, 30, 70)

                vbox:
                    xfill True
                    spacing 4

                    ## The speaker's name sits inside the box, small, with a dark outline so
                    ## bright character colours stay readable on the light box
                    if who:
                        text cb_who(who):
                            id "who"
                            size _who_sz
                            bold True
                            xalign 0.5
                            outlines [ (2, "#2B2624", 0, 0) ]

                    ## 1480 wide keeps the text clear of the dark fades at both ends of the box
                    text what:
                        id "what"
                        size _say_sz
                        color tx("#0e0e0e")
                        xalign 0.5
                        text_align 0.5
                        xmaximum 1480

style say_window:
    xfill True
    background None

style say_label:
    color "#C41230"
    size 32
    bold True

style say_dialogue:
    size 30
    color "#1F1B19"

################################################################################
## HELP SCREEN — controls reference, plain-text sub-tabs (Keyboard / Mouse)
################################################################################
screen help():
    tag menu
    default device = "keyboard"

    use base_menu(_("Tulong")):

        vbox:
            xfill True
            spacing 30
            ## Plain text sub-nav tabs, not boxed buttons
            hbox:
                xalign 0.5
                spacing 60

                for _dev, _label in [("keyboard", _("Keyboard")), ("mouse", _("Mouse"))]:
                    button:
                        action SetScreenVariable("device", _dev)
                        background None
                        hover_background None
                        padding (6, 6)

                        text _label:
                            size 32
                            color (tx("#C41230") if device == _dev else tx("#6B6259"))
                            hover_color tx("#C41230")
                            bold (device == _dev)

            if device == "keyboard":
                use help_keyboard_rows
            elif device == "mouse":
                use help_mouse_rows
style help_row_label:
    xsize 260
    right_padding 20

style help_row_label_text:
    size 26
    color "#E5677A"
    bold True
    xalign 0.0
    text_align 0.0

style help_row_text:
    size 24
    color "#6B6259"

screen help_keyboard_rows():
    vbox:
        xalign 0.5
        xsize 900
        spacing 24

        for _key, _desc in [
            (_("Enter"),      _("Nagpapatuloy ng dayalogo at ina-activate ang interface.")),
            (_("Space"),      _("Nagpapatuloy ng dayalogo nang hindi pumipili ng choices.")),
            (_("Arrow Keys"), _("Mag-navigate sa interface.")),
            (_("Escape"),     _("Binubuksan ang pause menu.")),
            (_("Ctrl"),       _("Nagski-skip ng dayalogo habang pinipindot.")),
            (_("Page Up"),    _("Bumabalik sa nakaraang dayalogo.")),
        ]:
            vbox:
                spacing 4
                text _key size 26 color "#E5677A" bold True xsize 900 text_align 0.5
                text _desc size 22 color tx("#6B6259") xsize 900 text_align 0.5

screen help_mouse_rows():
    vbox:
        xalign 0.5
        xsize 900
        spacing 24

        for _key, _desc in [
            (_("Left Click"),  _("Nagpapatuloy ng dayalogo at ina-activate ang interface.")),
            (_("Mouse Wheel"), _("Bumabalik o pumapasulong sa dayalogo.")),
        ]:
            vbox:
                spacing 4
                text _key size 26 color "#E5677A" bold True xsize 900 text_align 0.5
                text _desc size 22 color tx("#6B6259") xsize 900 text_align 0.5


################################################################################
## GAME MENU — overlay base (save/load/prefs/about/return)
################################################################################
screen base_menu(title, scroll=None, yinitial=0.0):
    style_prefix "game_menu"
    tag menu

    frame:
        xfill True
        yfill True
        background Solid(tc("#FAF7F3F2"))

        vbox:
            xfill True
            yfill True
            spacing 0

            frame:
                xfill True
                ysize 90
                background Solid("#C41230")
                padding (30, 0)
                hbox:
                    xfill True
                    yalign 0.5
                    spacing 20
                    text title size 36 color tx("#1F1B19") bold True yalign 0.5
                    null width True
                    textbutton _("Bumalik"):
                        action Return()
                        yalign 0.5
                        xsize 200
                        ysize 64
                        background Solid(tc("#F3EFEA"))
                        hover_background Solid("#C41230")
                        text_color tx("#2B2624")
                        text_hover_color "#fff"
                        text_size 28
                        text_xalign 0.5
                        text_yalign 0.5

            if scroll == "viewport":
                viewport:
                    id "viewport"
                    xfill True
                    yfill True
                    yinitial yinitial
                    scrollbars "vertical"
                    mousewheel True
                    draggable True

                    vbox:
                        id "viewport_content"
                        xfill True
                        spacing 0
                        transclude

            elif scroll == "vpgrid":
                vpgrid:
                    id "viewport"
                    cols 1
                    xfill True
                    yinitial yinitial
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    transclude

            else:
                transclude

style game_menu_frame:
    background Solid("#FAF7F3F2")
################################################################################
## MCC MENU HUB — unified icon-sidebar layout for Save / Load / Settings / History
## Sidebar tabs call ShowMenu(tab_id); since save/load/preferences/history all
## carry "tag menu", Ren'Py's own tag-swap does the navigating for us — no
## extra state variable needed. The individual screens below stay as thin
## wrappers so ShowMenu("save"), keyboard shortcuts, and the main menu buttons
## all keep working exactly as before.
################################################################################

define mcc_menu_tabs = [
    ("save",        _("I-save")),
    ("load",        _("Mag-load")),
    ("preferences", _("Mga Settings")),
    ("history",     _("Kasaysayan")),
]

screen mcc_menu_hub(active_tab):

    python:
        _sb_w   = 300 if renpy.variant("small") else 300
        _sb_txt = 25  if renpy.variant("small") else 24

    frame:
        xfill True
        yfill True
        background Solid(tc("#FAF7F3F2"))

        hbox:
            xfill True
            yfill True
            spacing 0

            ## ── LEFT: persistent sidebar, same on every tab ──
            frame:
                xsize _sb_w
                yfill True
                background Solid(tc("#FFFFFF"))
                padding (8, 24, 8, 16)

                vbox:
                    xfill True
                    yfill True
                    spacing 10

                    for _tab_id, _tab_label in mcc_menu_tabs:
                        use mcc_sidebar_tab(_tab_id, _tab_label, active_tab, _sb_txt)

                    null height True

                    textbutton _("Bumalik sa Main Menu"):
                        action MainMenu()
                        xfill True
                        ysize 60
                        background Solid(tc("#F3EFEA"))
                        hover_background Solid("#b91c1c")
                        text_color tx("#6B6259")
                        text_hover_color "#fff"
                        text_size _sb_txt
                        text_xalign 0.5
                        text_yalign 0.5

                    textbutton _("← Bumalik"):

                        action Return()
                        xfill True
                        ysize 60
                        background Solid(tc("#F3EFEA"))
                        hover_background Solid("#C41230")
                        text_color tx("#6B6259")
                        text_hover_color "#fff"
                        text_size _sb_txt
                        text_xalign 0.5
                        text_yalign 0.5

            ## ── RIGHT: content panel swaps per tab ──
            frame:
                xfill True
                yfill True
                background Solid(tc("#FAF7F3"))

                if active_tab == "save":
                    use mcc_content_save()
                elif active_tab == "load":
                    use mcc_content_load()
                elif active_tab == "preferences":
                    use mcc_content_preferences()
                elif active_tab == "history":
                    use mcc_content_history()

screen mcc_sidebar_tab(tab_id, label, active_tab, txt_size):
    python:
        _is_active = (tab_id == active_tab)

    textbutton label:
        action (NullAction() if _is_active else ShowMenu(tab_id))
        selected _is_active
        xfill True
        yminimum (64 if renpy.variant("small") else 56)
        background (Solid("#C41230") if _is_active else Solid(tc("#F3EFEA")))
        hover_background Solid("#C41230")
        padding (18, 12)
        text_color ("#FFFFFF" if _is_active else tx("#3D3730"))
        text_hover_color "#FFFFFF"
        text_size txt_size
        text_xalign 0.0
        text_yalign 0.5
        text_bold _is_active


## SAVE / LOAD content panels + thin screen wrappers

screen save():
    tag menu
    use mcc_menu_hub("save")

screen load():
    tag menu
    use mcc_menu_hub("load")

screen mcc_content_save():
    use mcc_file_slots(_("I-save"))

screen mcc_content_load():
    use mcc_file_slots(_("Mag-load"))

screen mcc_file_slots(title):

    vbox:
        xfill True
        yfill True
        spacing 0

        frame:
            xfill True
            ysize 90
            background Solid("#C41230")
            padding (30, 0)
            text title size 36 color "#ffffff" bold True yalign 0.5

        frame:
            xfill True
            yfill True
            background None

            grid 3 2:
                xalign 0.5
                yalign 0.5
                spacing 30

                for i in range(1, 7):
                    $ slot = i

                    vbox:
                        xsize 420
                        spacing 12

                        button:
                            action FileAction(slot)
                            xsize 420
                            ysize 236
                            background Solid(tc("#F3EFEA"))
                            hover_background Solid(tc("#E3DBD2"))
                            padding (3, 3)

                            add Transform(FileScreenshot(slot), xysize=(414, 230)):
                                xalign 0.5
                                yalign 0.5

                        text FileTime(slot, format=_("%b %d, %H:%M"), empty=_("Walang laman")):
                            size 20
                            color tx("#6B6259")
                            xalign 0.5

                        textbutton _("Burahin"):
                            action FileDelete(slot)
                            sensitive FileLoadable(slot)
                            xfill True
                            ysize 44
                            background Solid("#8e1a1a")
                            hover_background Solid("#b91c1c")
                            insensitive_background Solid(tc("#F3EFEA55"))
                            text_color "#fff"
                            text_size 20
                            text_xalign 0.5
                            text_yalign 0.5

## PREFERENCES SCREEN — content panel + thin wrapper
screen mcc_content_preferences():

    vbox:
        xfill True
        yfill True
        spacing 0

        frame:
            xfill True
            ysize 90
            background Solid("#C41230")
            padding (30, 0)
            text _("Mga Settings") size 36 color "#ffffff" bold True yalign 0.5

        frame:
            xfill True
            yfill True
            background Frame(theme_img("nvl"), Borders(0, 0, 0, 0))

            side "c r":
                xfill True
                yfill True

                viewport:
                    id "prefs_vp"
                    xfill True
                    mousewheel True
                    draggable True

                    vbox:
                        xfill True

                        vbox:
                            spacing 20
                            xalign 0.5
                            xmaximum 860

                            null height 24

                            if not renpy.variant("web") and not renpy.variant("small"):
                                use pref_dropdown("display", _("Display"), (_("Fullscreen") if _preferences.fullscreen else _("Window"))):
                                    use pref_chip(_("Fullscreen"), _preferences.fullscreen, Preference("display", "fullscreen"))
                                    use pref_chip(_("Window"), not _preferences.fullscreen, Preference("display", "window"))

                            use pref_dropdown("lang", _("Wika / Language"), (_("Tagalog") if _preferences.language is None else _("English"))):
                                use pref_chip(_("Tagalog"), _preferences.language is None, Language(None))
                                use pref_chip(_("English"), _preferences.language == "english", Language("english"))

                            use pref_dropdown("theme", _("Tema / Theme"), (_("Ambient") if persistent.theme == "dark" else _("Light"))):
                                use pref_chip(_("Ambient"), persistent.theme == "dark", SetField(persistent, "theme", "dark"))
                                use pref_chip(_("Light"), persistent.theme == "light", SetField(persistent, "theme", "light"))

                            use pref_dropdown("size", _("Laki ng Teksto / Text Size"), (_("Maliit") if persistent.text_scale == 0.85 else (_("Malaki") if persistent.text_scale == 1.2 else _("Normal")))):
                                use pref_chip(_("Maliit"), persistent.text_scale == 0.85, SetField(persistent, "text_scale", 0.85))
                                use pref_chip(_("Normal"), persistent.text_scale == 1.0, SetField(persistent, "text_scale", 1.0))
                                use pref_chip(_("Malaki"), persistent.text_scale == 1.2, SetField(persistent, "text_scale", 1.2))

                            use pref_dropdown("cb", _("Colorblind Mode"), (_("Red-Green") if persistent.colorblind_mode == "rg" else (_("Blue-Yellow") if persistent.colorblind_mode == "by" else _("Off")))):
                                use pref_chip(_("Off"), persistent.colorblind_mode == "off", SetField(persistent, "colorblind_mode", "off"))
                                use pref_chip(_("Red-Green"), persistent.colorblind_mode == "rg", SetField(persistent, "colorblind_mode", "rg"))
                                use pref_chip(_("Blue-Yellow"), persistent.colorblind_mode == "by", SetField(persistent, "colorblind_mode", "by"))
                            text _("Red-Green: protanopia / deuteranopia.  Blue-Yellow: tritanopia. Also shows numbers on the HUD bars.") size 20 color tx("#6B6259")

                            use pref_slider(_("Bilis ng Teksto / Text Speed"), "text speed", "#C41230")
                            use pref_steps(_("Bilis ng Auto-Forward"), AUTO_LABELS, persistent.auto_speed, set_auto_speed)
                            use pref_steps(_("Bilis ng Skip / Skip Speed"), SKIP_LABELS, persistent.skip_speed, set_skip_speed)
                            use pref_slider(_("Musika / Music"), "music volume", "#56d364")
                            use pref_slider(_("Tunog / Sound"), "sound volume", "#e3b341")

                            null height 40

                vbar:
                    value YScrollValue("prefs_vp")
                    style theme_scrollbar_style()


## SETTINGS ROWS - Hoyoverse-style. Every setting is ONE line: the label on the left and the
## current value as a pill on the right. Tapping the row expands the choices underneath it;
## picking one collapses it again. Sliders stay on one row with their bar.
default pref_open = None

screen pref_dropdown(key, label, value):
    python:
        _po = (pref_open == key)
        _pm = renpy.variant(["touch", "small", "mobile"])
        _prh = 96 if _pm else 80
        _pls = 32 if _pm else 28

    frame:
        xfill True
        background Solid(tx("#C41230") if _po else tc("#E3DBD2"))
        padding (2, 2)

        vbox:
            xfill True

            button:
                action SetVariable("pref_open", None if _po else key)
                xfill True
                ysize _prh
                background Solid(tc("#FFFFFF"))
                hover_background Solid(tc("#E8EEF3"))
                padding (28, 0)

                fixed:
                    xfill True
                    yfill True
                    text label size _pls color tx("#2B2624") yalign 0.5
                    frame:
                        xalign 1.0
                        yalign 0.5
                        background Solid(tc("#F3EFEA"))
                        padding (22, 8)
                        hbox:
                            spacing 14
                            text value size (_pls - 2) color tx("#C41230") bold True yalign 0.5
                            text ("↑" if _po else "↓") size _pls color tx("#6B6259") yalign 0.5

            if _po:
                frame:
                    xfill True
                    background Solid(tc("#F3EFEA"))
                    padding (28, 20)

                    hbox:
                        xfill True
                        box_wrap True
                        spacing 16
                        transclude

## One choice inside an expanded row. Picking it applies it and collapses the row.
screen pref_chip(label, is_selected, act):
    python:
        _pm = renpy.variant(["touch", "small", "mobile"])

    button:
        action [act, SetVariable("pref_open", None)]
        background (Solid("#C41230") if is_selected else Solid(tc("#FFFFFF")))
        hover_background Solid("#8C0E23")
        padding (30, 0)
        ysize (72 if _pm else 60)

        text label:
            size (30 if _pm else 26)
            color ("#FFFFFF" if is_selected else tx("#6B6259"))
            hover_color "#FFFFFF"
            bold is_selected
            yalign 0.5

## A labelled step bar: tap a segment to pick that speed. Segments are explicit equal widths.
screen pref_steps(label, labels, idx, setter):
    python:
        _pm = renpy.variant(["touch", "small", "mobile"])
        _n = len(labels)
        _sw = (800 - 8 * (_n - 1)) // _n
        _ls = 32 if _pm else 28

    frame:
        xfill True
        background Solid(tc("#E3DBD2"))
        padding (2, 2)

        frame:
            xfill True
            background Solid(tc("#FFFFFF"))
            padding (28, 20)

            vbox:
                xfill True
                spacing 10

                fixed:
                    xfill True
                    ysize (_ls + 14)
                    text label size _ls color tx("#2B2624") yalign 0.5
                    text labels[idx] size _ls color tx("#C41230") bold True xalign 1.0 yalign 0.5

                hbox:
                    spacing 8
                    for i in range(_n):
                        button:
                            action Function(setter, i)
                            xsize _sw
                            ysize (96 if _pm else 84)
                            background None
                            hover_background None
                            padding (0, 0)

                            vbox:
                                spacing 8
                                frame:
                                    xsize _sw
                                    ysize (36 if _pm else 30)
                                    background Solid("#C41230" if i <= idx else tc("#E3DBD2"))
                                text labels[i]:
                                    size (28 if _pm else 24)
                                    color (tx("#C41230") if i == idx else tx("#6B6259"))
                                    hover_color tx("#C41230")
                                    bold (i == idx)
                                    xalign 0.5

## A one-row slider setting.
screen pref_slider(label, pref, fill):
    python:
        _pm = renpy.variant(["touch", "small", "mobile"])

    frame:
        xfill True
        background Solid(tc("#E3DBD2"))
        padding (2, 2)

        frame:
            xfill True
            background Solid(tc("#FFFFFF"))
            padding (28, 20)

            vbox:
                xfill True
                spacing 14
                text label size (32 if _pm else 28) color tx("#2B2624")
                bar:
                    value Preference(pref)
                    xfill True
                    ysize (44 if _pm else 36)
                    left_bar Solid(fill)
                    right_bar Solid(tc("#E3DBD2"))

## Reusable bordered card wrapper for a single settings row.
screen settings_card(label):
    frame:
        xfill True
        background Solid(tc("#E3DBD2"))
        padding (1, 1)

        frame:
            xfill True
            background Solid(tc("#FFFFFF"))
            padding (24, 18)

            vbox:
                xfill True
                spacing 14
                text label size 24 color tx("#C41230") bold True
                transclude

## Plain-text option with a small left tick when selected, ErinsLight-style.
screen pref_tick_option(label, is_selected, act):
    button:
        action act
        background None
        hover_background None
        padding (10, 4)

        hbox:
            spacing 8
            yalign 0.5
            frame:
                xsize 3
                ysize 28
                background (Solid("#C41230") if is_selected else None)
            text label:
                size 26
                color (tx("#C41230") if is_selected else tx("#6B6259"))
                hover_color tx("#C41230")
                bold is_selected
                yalign 0.5

## Scrollbar for the Settings tab (matches the red/cream theme).
style prefs_vscrollbar is vscrollbar:
    xsize 18
    base_bar Solid("#E3DBD2")
    thumb Solid("#C41230")
    unscrollable "hide"

screen preferences():
    tag menu
    on "show" action SetVariable("pref_open", None)
    on "replace" action SetVariable("pref_open", None)
    use mcc_menu_hub("preferences")
        
################################################################################
## NAME ENTRY - typed-name prompt WITH an on-screen button.
## renpy.input has no button, and on phones there is often no usable Enter key.
## Returns the typed text. Blank is fine: the caller keeps the default name.
################################################################################
screen name_entry(prompt, default_name=""):
    modal True
    zorder 200
    default name_buf = default_name

    python:
        ## phones: the on-screen keyboard covers the lower half of the screen, so the whole
        ## card sits at the top and the field + button share one row.
        _nc = renpy.variant(["touch", "small", "mobile"])

    frame:
        xfill True
        yfill True
        background Solid(tc("#14110FCC"))

    frame:
        xalign 0.5
        ypos (24 if _nc else 0.42)
        yanchor (0.0 if _nc else 0.42)
        xsize (1500 if _nc else 1100)
        background Solid(tc("#FAF7F3"))
        padding (0, 0)

        vbox:
            xfill True
            frame:
                xfill True
                ysize 8
                background Solid("#C41230")

            if _nc:
                vbox:
                    xalign 0.5
                    xsize 1400
                    spacing 14
                    null height 6
                    text prompt size 36 color tx("#2B2624") xalign 0.5 text_align 0.5
                    hbox:
                        xalign 0.5
                        spacing 20
                        frame:
                            xsize 1040
                            ysize 88
                            background Solid(tc("#F3EFEA"))
                            padding (24, 0)
                            input:
                                value ScreenVariableInputValue("name_buf", returnable=True)
                                length 20
                                size 46
                                color tx("#2B2624")
                                yalign 0.5
                        textbutton _("Tuloy"):
                            action Return(name_buf)
                            xsize 340
                            ysize 88
                            background Solid("#C41230")
                            hover_background Solid("#8C0E23")
                            text_color "#FFFFFF"
                            text_size 40
                            text_bold True
                            text_xalign 0.5
                            text_yalign 0.5
                    text _("Kung blangko, gagamitin ang \"[default_name]\".") size 26 color tx("#6B6259") xalign 0.5
                    null height 10
            else:
                vbox:
                    xalign 0.5
                    xsize 980
                    spacing 24
                    null height 20
                    text prompt size 40 color tx("#2B2624") xalign 0.5 text_align 0.5
                    frame:
                        xfill True
                        ysize 96
                        background Solid(tc("#F3EFEA"))
                        padding (24, 0)
                        input:
                            value ScreenVariableInputValue("name_buf", returnable=True)
                            length 20
                            size 48
                            color tx("#2B2624")
                            yalign 0.5
                    text _("Kung blangko, gagamitin ang \"[default_name]\".") size 26 color tx("#6B6259") xalign 0.5
                    textbutton _("Tuloy"):
                        action Return(name_buf)
                        xalign 0.5
                        xsize 420
                        ysize 88
                        background Solid("#C41230")
                        hover_background Solid("#8C0E23")
                        text_color "#FFFFFF"
                        text_size 40
                        text_bold True
                        text_xalign 0.5
                        text_yalign 0.5
                    null height 24

screen input(prompt):
    style_prefix "input"

    frame:
        xalign 0.5
        yalign 0.5
        xpadding 40
        ypadding 40

        vbox:
            xalign 0.5
            spacing 20

            text prompt:
                xalign 0.5
                size 60

            input id "input":
                xalign 0.5
                size 60

################################################################################
## HISTORY SCREEN — content panel + thin wrapper
################################################################################
screen mcc_content_history():

    vbox:
        xfill True
        yfill True
        spacing 0

        frame:
            xfill True
            ysize 90
            background Solid("#C41230")
            padding (15, 0)
            text _("Kasaysayan") size 36 color tx("#1F1B19") bold True yalign 0.5

        vbox:
            xfill True
            yfill True
            spacing 4

            null height 16

            python:
                _hist = list(reversed(_history_list)) if _history_list else []

            if not _hist:
                text "Walang kasaysayan pa." size 28 color tx("#6B6259") xalign 0.5

            for h in _hist:
                python:
                    _who_text  = h.who  if h.who  else None
                    _what_text = h.what if h.what else ""

                if _who_text or _what_text.strip():
                    frame:
                        xfill True
                        background Solid(tc("#F3EFEA"))
                        padding (20, 14)
                        bottom_margin 4

                        vbox:
                            spacing 6
                            if _who_text:
                                text _who_text size 26 color "#E5677A" bold True
                            text _what_text size 28 color tx("#2B2624") substitute False

screen history():
    tag menu
    use mcc_menu_hub("history")

## ABOUT / CREDITS SCREEN
screen about():
    tag menu
    use base_menu(_("Credits")):

        vbox:
            xalign 0.5
            spacing 20
            xmaximum 700
            yalign 0.3

            text "[config.name!t]" size 42 color tx("#1F1B19") bold True xalign 0.5
            text "Version [config.version]" size 28 color tx("#6B6259") xalign 0.5
            null height 20

            text "Project began in development in June by:" size 30 color "#E5677A" xalign 0.5
            text "Lead/Main Developer: Clarin, Kylle Benedict" size 27 color tx("#6B6259") xalign 0.5
            text "3D Sprites Artist: Morgan, Christian David F." size 26 color tx("#6B6259") xalign 0.5
            text "Landing Page Designer: Cecilio, Neil Ayangel C." size 26 color tx("#6B6259") xalign 0.5
            null height 12

            text "Technical Adviser: Engr. Ernie Lee Pineda, MIT" size 24 color tx("#6B6259") xalign 0.5
            text "Capstone Instructor: Engr. Dennis L. Tacadena, MIT" size 24 color tx("#6B6259") xalign 0.5
            null height 12

            text "Mabalacat City College" size 24 color tx("#6B6259") xalign 0.5
            text "Institute of Computing Studies, 2026" size 24 color tx("#6B6259") xalign 0.5
            null height 32


## CONFIRM DIALOG

screen confirm(message, yes_action, no_action=Return()):
    modal True
    zorder 300

    frame:
        xsize 640
        ysize 320
        xalign 0.5
        yalign 0.45
        background Solid(tc("#FFFFFFF8"))
        padding (40, 40)

        vbox:
            spacing 30
            xfill True

            text message:
                size 30
                color tx("#2B2624")
                xalign 0.5
                text_align 0.5

            hbox:
                xalign 0.5
                spacing 40

                textbutton _("Oo"):
                    action yes_action
                    xsize 220
                    ysize 72
                    background Solid("#b91c1c")
                    hover_background Solid("#dc2626")
                    text_color "#fff"
                    text_size 30
                    text_xalign 0.5
                    text_yalign 0.5

                textbutton _("Hindi"):
                    action no_action
                    xsize 220
                    ysize 72
                    background Solid(tc("#F3EFEA"))
                    hover_background Solid(tc("#E3DBD2"))
                    text_color tx("#2B2624")
                    text_size 30
                    text_xalign 0.5
                    text_yalign 0.5

## SKIP INDICATOR
screen skip_indicator():
    zorder 100

    frame:
        xalign 1.0
        yalign 0.0
        xoffset -10
        yoffset 100
        background Frame(theme_img("skip"), Borders(0, 0, 0, 0))
        padding (20, 15)
        text _(">> Nilalaktawan...") size 40 color tx("#C41230")
style button:
    activate_sound "audio/sfx/sfx_click.ogg"