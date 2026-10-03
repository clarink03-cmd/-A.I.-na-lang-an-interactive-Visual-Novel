## game/screens.rpy
## All screen definitions for A.I. na lang!
## CHOICE SCREEN 
default minigame_active = False
screen choice(items):
    zorder 150

    python:
        _is_small = renpy.variant("small")
        _btn_w = 680 if _is_small else 1100
        _txt_sz = int((34 if _is_small else 30) * persistent.text_scale)

    vbox:
        xalign 0.5
        yalign 0.78
        xsize _btn_w
        spacing 14

        for i in items:
            frame:
                xfill True
                background Solid("#C41230")
                padding (6, 0, 0, 0)

                textbutton i.caption:
                    action i.action
                    xfill True
                    background Solid("#FAF7F3F2")
                    hover_background Solid("#C4123022")
                    insensitive_background Solid("#FAF7F3AA")
                    padding (24, 14)
                    text_color "#1F1B19"
                    text_hover_color "#ffffff"
                    text_insensitive_color "#9C948C"
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
        background Solid("#E3DBD2")
        padding (3, 3)
        frame:
            xfill True
            yfill True
            background Solid("#C41230")
            padding (3, 3)
            frame:
                xfill True
                yfill True
                background Solid("#FAF7F3")
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
                background Solid("#FFFFFFE6")
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
                    text_color "#1F1B19"
                    text_hover_color "#ffffff"
                    text_size 34
                    text_bold True
                    text_xalign 0.15
init python:
    config.overlay_screens.append("quick_menu")
    config.overlay_screens.append("hud")
## HUD
screen hud():
    zorder 5
    if show_hud:
        python:
            _is_small = renpy.variant("small")
            _bar_h = 100 if _is_small else 92
            _pad = 20 if _is_small else 36

            _dl = day_label.lower()
            if "gabi" in _dl:
                _day_color = "#4A5578"   # night
            elif "umaga" in _dl or "tanghali" in _dl or "hapon" in _dl:
                _day_color = "#E0A836"   # day
            else:
                _day_color = "#C41230"   # special / event day (exam, submission, etc.)

        vbox:
            xfill True
            yalign 0.0
            spacing 0

            frame:
                xfill True
                ysize _bar_h
                background Solid("#FFFFFFF5")
                padding (_pad, 0)

                frame:
                    xfill True
                    ysize 3
                    yalign 1.0
                    background Solid("#C41230")

                if _is_small:
                    hbox:
                        xfill True
                        yfill True
                        yalign 0.5
                        spacing 24
                        frame:
                            background Frame("gui/whitediamond.png", Borders(40, 0, 60, 0))
                            padding (36, 16)
                            hbox:
                                spacing 14
                                yalign 0.5
                                frame:
                                    xsize 18
                                    ysize 18
                                    yalign 0.5
                                    background Solid(_day_color)
                                text "[day_label]" size 34 color "#1F1B19" bold True yalign 0.5

                        frame:
                            xsize 2
                            ysize 44
                            yalign 0.5
                            background Solid("#00000014")

                        frame:
                            background Solid("#F3EFEA")
                            padding (18, 10)
                            vbox:
                                spacing 6
                                text "CRITICAL THINKING" size 17 color "#C41230" bold True
                                hbox:
                                    spacing 4
                                    for i in range(10):
                                        python:
                                            filled = (critical_thinking // 10) > i
                                            if   i < 2: seg_color = "#b91c1c" if filled else "#E3DBD2"
                                            elif i < 4: seg_color = "#b45309" if filled else "#E3DBD2"
                                            elif i < 6: seg_color = "#854d0e" if filled else "#E3DBD2"
                                            elif i < 8: seg_color = "#166534" if filled else "#E3DBD2"
                                            else:       seg_color = "#15803d" if filled else "#E3DBD2"
                                        frame:
                                            xsize 44
                                            ysize 18
                                            background Solid(seg_color)

                        frame:
                            xsize 2
                            ysize 44
                            yalign 0.5
                            background Solid("#00000014")

                        frame:
                            background Solid("#F3EFEA")
                            padding (18, 10)
                            vbox:
                                spacing 6
                                hbox:
                                    spacing 8
                                    yalign 0.5
                                    text "♥" size 28 color "#f43f5e" yalign 0.5
                                    text "MOTIVATION" size 17 color "#C41230" bold True yalign 0.5
                                bar:
                                    value motivation
                                    range 100
                                    xsize 200
                                    ysize 18
                                    left_bar  Solid("#f43f5e")
                                    right_bar Solid("#B8AFA6")

                        null width True

                        frame:
                            background Solid("#C41230")
                            padding (20, 12)
                            yalign 0.5
                            textbutton _("Tingnan ang Grades"):
                                action Show("grade_results")
                                background None
                                hover_background None
                                text_color "#FFFFFF"
                                text_hover_color "#FFE3E7"
                                text_size 22
                                text_bold True

                else:
                    hbox:
                        xfill True
                        yfill True
                        yalign 0.5
                        spacing 24
                        frame:
                            background Frame("gui/whitediamond.png", Borders(40, 0, 60, 0))
                            padding (36, 16)
                            hbox:
                                spacing 14
                                yalign 0.5
                                frame:
                                    xsize 18
                                    ysize 18
                                    yalign 0.5
                                    background Solid(_day_color)
                                text "[day_label]" size 34 color "#1F1B19" bold True yalign 0.5

                        frame:
                            xsize 2
                            ysize 44
                            yalign 0.5
                            background Solid("#00000014")

                        frame:
                            background Solid("#F3EFEA")
                            padding (18, 10)
                            vbox:
                                spacing 6
                                text "CRITICAL THINKING" size 17 color "#C41230" bold True
                                hbox:
                                    spacing 4
                                    for i in range(10):
                                        python:
                                            filled = (critical_thinking // 10) > i
                                            if   i < 2: seg_color = "#b91c1c" if filled else "#E3DBD2"
                                            elif i < 4: seg_color = "#b45309" if filled else "#E3DBD2"
                                            elif i < 6: seg_color = "#854d0e" if filled else "#E3DBD2"
                                            elif i < 8: seg_color = "#166534" if filled else "#E3DBD2"
                                            else:       seg_color = "#15803d" if filled else "#E3DBD2"
                                        frame:
                                            xsize 44
                                            ysize 18
                                            background Solid(seg_color)

                        frame:
                            xsize 2
                            ysize 44
                            yalign 0.5
                            background Solid("#00000014")

                        frame:
                            background Solid("#F3EFEA")
                            padding (18, 10)
                            vbox:
                                spacing 6
                                hbox:
                                    spacing 8
                                    yalign 0.5
                                    text "♥" size 28 color "#f43f5e" yalign 0.5
                                    text "MOTIVATION" size 17 color "#C41230" bold True yalign 0.5
                                bar:
                                    value motivation
                                    range 100
                                    xsize 200
                                    ysize 18
                                    left_bar  Solid("#f43f5e")
                                    right_bar Solid("#B8AFA6")

                        null width True

                        frame:
                            background Solid("#C41230")
                            padding (20, 12)
                            yalign 0.5
                            textbutton _("Tingnan ang Grades"):
                                action Show("grade_results")
                                background None
                                hover_background None
                                text_color "#FFFFFF"
                                text_hover_color "#FFE3E7"
                                text_size 22
                                text_bold True

            ## Soft shadow so the bar lifts off the scene instead of cutting off hard
            frame:
                xfill True
                ysize 10
                background Solid("#00000022")
            frame:
                xfill True
                ysize 6
                background Solid("#00000014")
            frame:
                xfill True
                ysize 3
                background Solid("#0000000A")
## QUICK MENU — HUd

screen quick_menu():
    zorder 100

    if show_hud:
        frame:
            xfill True
            ysize 64
            yalign 1.0
            background None
            padding (16, 0)

            hbox:
                xfill True
                yalign 0.5

                ## ── Left cluster: Back / History / Skip / Auto ──
                hbox:
                    yalign 0.5
                    spacing 4

                    textbutton _("Back"):
                        action Rollback()
                        xsize 100
                        ysize 48
                        background Solid("#F3EFEA")
                        hover_background Solid("#C41230")
                        text_color "#6B6259"
                        text_hover_color "#fff"
                        text_size 22
                        text_xalign 0.5
                        text_yalign 0.5

                    textbutton _("History"):
                        action ShowMenu("history")
                        xsize 120
                        ysize 48
                        background Solid("#F3EFEA")
                        hover_background Solid("#C41230")
                        text_color "#6B6259"
                        text_hover_color "#fff"
                        text_size 22
                        text_xalign 0.5
                        text_yalign 0.5

                    textbutton _("Skip"):
                        action [Preference("skip", "all"), Skip()]
                        sensitive (not minigame_active)
                        xsize 100
                        ysize 48
                        background Solid("#F3EFEA")
                        hover_background Solid("#C41230")
                        text_color "#6B6259"
                        text_hover_color "#fff"
                        text_size 22
                        text_xalign 0.5
                        text_yalign 0.5

                    textbutton _("Auto"):
                        action Preference("auto-forward", "toggle")
                        selected (_preferences.afm_enable)
                        selected_background Solid("#C41230")
                        xsize 100
                        ysize 48
                        background Solid("#F3EFEA")
                        hover_background Solid("#C41230")
                        text_color "#6B6259"
                        text_hover_color "#fff"
                        text_size 22
                        text_xalign 0.5
                        text_yalign 0.5

                ## ── Center: phone / AI access only usable during a quiz 
                null width True
                if minigame_active:
                    textbutton _("📱  Browse Social Media"):
                        action Function(show_phone_ai)
                        xsize 300
                        ysize 48
                        background Solid("#C4123022")
                        hover_background Solid("#C41230")
                        text_color "#E5677A"
                        text_hover_color "#fff"
                        text_size 22
                        text_xalign 0.5
                        text_yalign 0.5
                else:
                    null width 300
                null width True
                ## ── Right cluster: Save / Load / Prefs ──
                hbox:
                    yalign 0.5
                    spacing 4

                    textbutton _("Save"):
                        action ShowMenu("save")
                        xsize 100
                        ysize 48
                        background Solid("#F3EFEA")
                        hover_background Solid("#C41230")
                        text_color "#6B6259"
                        text_hover_color "#fff"
                        text_size 22
                        text_xalign 0.5
                        text_yalign 0.5

                    textbutton _("Load"):
                        action ShowMenu("load")
                        xsize 100
                        ysize 48
                        background Solid("#F3EFEA")
                        hover_background Solid("#C41230")
                        text_color "#6B6259"
                        text_hover_color "#fff"
                        text_size 22
                        text_xalign 0.5
                        text_yalign 0.5

                    textbutton _("Prefs"):
                        action ShowMenu("preferences")
                        xsize 100
                        ysize 48
                        background Solid("#F3EFEA")
                        hover_background Solid("#C41230")
                        text_color "#6B6259"
                        text_hover_color "#fff"
                        text_size 22
                        text_xalign 0.5
                        text_yalign 0.5

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
        background Solid("#FAF7F3F4")
        padding (30, 30)

        vbox:
            spacing 20
            text "Phone ni [player_name]" size 34 color "#E5677A" xalign 0.5
            text "Naka-open ang AI app..." size 28 color "#6B6259" xalign 0.5
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
                background Solid("#F3EFEA")
                text_color "#7ee787"
                text_size 30
                text_xalign 0.5
                text_yalign 0.5

            text "CT: [critical_thinking]/100  |  AI uses: [ai_use_count]" size 24 color "#6B6259" xalign 0.5

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
    frame at notify_slide:
        xalign 0.98
        yalign 0.06
        xsize 420
        ysize 64
        background Solid("#FFFFFFEE")

        hbox:
            xfill True
            yfill True
            frame:
                xsize 5
                ysize 64
                background Solid("#C41230")
            frame:
                xfill True
                yfill True
                background None
                padding (16, 0)
                text message size 22 color "#E5677A" yalign 0.5 xalign 0.0

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

            text "[config.name!t]  v[config.version]" xalign 0.97 yalign 0.97 size 22 color "#ffffff80"
## CHAPTER SELECT — replaces the old Extras -> Week Select chain
screen chapter_select():
    tag menu
    use base_menu(_("Chapter Select")):
        vbox:
            xalign 0.5
            yalign 0.05
            spacing 12
            xmaximum 760

            text "Direktang pumunta sa kahit anong bahagi ng laro." size 24 color "#6B6259" xalign 0.5
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
                    background Solid("#F3EFEA")
                    hover_background Solid("#C41230")
                    text_color "#2B2624"
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
        background Solid("#FAF7F3F8")

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
            text "[subtitle]" size 40 color "#202020" xalign 0.5 italic True

        text "Click anything to continue" xalign 0.5 yalign 0.92 size 40 color "#3d3d3d"

    key "K_RETURN" action Return()
    key "K_SPACE"  action Return()
    button:
        xfill True
        yfill True
        action Return()
        background None
screen minigame(title, question, options, correct_idx, subject, ct_reward=8, grade_reward=10, correct_label="minigame_correct", wrong_label="minigame_wrong"):
    modal True
    zorder 180
    on "show" action [SetVariable("minigame_active", True), Function(stop_skipping)]
    on "hide" action SetVariable("minigame_active", False)

    python:
        _is_small = renpy.variant("small")
        _card_w = 720 if _is_small else 1200
        _btn_h  = 100 if _is_small else 78
        _txt_sz = 30  if _is_small else 26
        _q_sz   = 30  if _is_small else 28

    ## Dim backdrop
    frame:
        xfill True
        yfill True
        background Solid("#FAF7F3F2")

        ## Card — sized ONLY by its own content. No viewport, no fixed
        ## heights, no nested border frames. This cannot collapse to zero.
        frame:
            xalign 0.5
            yalign 0.5
            xsize _card_w
            background Solid("#FAF7F3")
            padding (0, 0)

            vbox:
                xfill True
                spacing 0

                ## Top accent bar
                frame:
                    xfill True
                    ysize 6
                    background Solid("#C41230")

                ## Header
                frame:
                    xfill True
                    ysize 64
                    background Solid("#C41230")
                    padding (24, 0)
                    hbox:
                        yalign 0.5
                        spacing 20
                        text title size 30 color "#FFFFFF" bold True
                        null width True
                        text "CT [critical_thinking]/100" size 22 color "#F3EFEA" yalign 0.5

                ## Question
                frame:
                    xfill True
                    background Solid("#FFFFFFAA")
                    padding (22, 20)
                    text question size _q_sz color "#2B2624"

                null height 16

                ## Answer options
                vbox:
                    xfill True
                    spacing 12

                    $ __minigame_correct = correct_idx
                    for idx in range(len(options)):
                        python:
                            _opt = options[idx]
                            _letter = chr(65 + idx)
                            _is_correct = (idx == __minigame_correct)
                            _jump = Jump(correct_label) if _is_correct else Jump(wrong_label)

                        hbox:
                            xfill True
                            ysize _btn_h
                            spacing 14

                            frame:
                                xsize 52
                                ysize 52
                                yalign 0.5
                                background Solid("#C41230")
                                text _letter size 26 color "#ffffff" bold True xalign 0.5 yalign 0.5

                            textbutton _opt:
                                action [
                                    Function(ct_change, ct_reward if _is_correct else -5),
                                    Function(grade_change, subject, grade_reward if _is_correct else -5),
                                    Hide("minigame"),
                                    _jump
                                ]
                                xfill True
                                yfill True
                                background Solid("#F3EFEA")
                                hover_background Solid("#C4123033")
                                padding (20, 8)
                                text_color "#2B2624"
                                text_hover_color "#C41230"
                                text_size _txt_sz
                                text_xalign 0.0
                                text_yalign 0.5

                null height 16

                ## AI shortcut
                frame:
                    xfill True
                    background Solid("#C4123015")
                    padding (20, 16)
                    hbox:
                        spacing 20
                        yalign 0.5
                        vbox:
                            yalign 0.5
                            spacing 4
                            text "Itanong sa AI" size _txt_sz color "#C41230" bold True
                            text ("CT -10  |  Grade +" + str(grade_reward) + "  (pero walang naiintindihan)") size 18 color "#6B6259"
                        null width True
                        textbutton _("Gamitin"):
                            action [
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

                null height 6

## GRADE RESULTS SCREEN
screen grade_results():
    modal True
    zorder 170

    ## Dim backdrop — hides the scene, HUD, and dialogue behind the card
    frame:
        xfill True
        yfill True
        background Solid("#FAF7F3F2")

    frame:
        xsize 900
        yalign 0.5
        xalign 0.5
        background Solid("#FFFFFFF8")

        vbox:
            xfill True
            spacing 0

            ## Top accent bar, matches minigame()'s card treatment
            frame:
                xfill True
                ysize 6
                background Solid("#C41230")

            vbox:
                xalign 0.5
                xmaximum 820
                spacing 24

                null height 30
                text "RESULTA NG GRADES" size 38 color "#E5677A" xalign 0.5 bold True
                null height 6

                hbox:
                    xalign 0.5
                    spacing 60
                    vbox:
                        spacing 10
                        text "Networking"   size 28 color "#e3b341" xalign 0.5
                        text "[networking_grade]  ([letter_grade(networking_grade)])" size 34 color "#1F1B19" xalign 0.5 bold True
                    vbox:
                        spacing 10
                        text "Programming"  size 28 color "#ff7b72" xalign 0.5
                        text "[programming_grade]  ([letter_grade(programming_grade)])" size 34 color "#1F1B19" xalign 0.5 bold True
                    vbox:
                        spacing 10
                        text "Cybersecurity" size 28 color "#56d364" xalign 0.5
                        text "[cyber_grade]  ([letter_grade(cyber_grade)])" size 34 color "#1F1B19" xalign 0.5 bold True

                null height 4
                frame:
                    xfill True
                    ysize 1
                    background Solid("#ffffff14")
                null height 4

                text "Critical Thinking: [critical_thinking]/100" size 26 color "#6B6259" xalign 0.5
                text "Motivation: [motivation]/100"               size 26 color "#6B6259" xalign 0.5
                text "AI Uses: [ai_use_count]"                   size 26 color "#6B6259" xalign 0.5

                null height 6
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
screen say(who, what):
    style_prefix "say"

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
            background Frame("gui/textbox.png", Borders(0, 0, 0, 0))
            padding (30, 30, 30, 70)

            vbox:
                xfill True
                spacing 8

                if who:
                    vbox:
                        xfill True
                        spacing 6
                        text who:
                            id "who"
                            size tsz(40)
                            color "#C41230"
                            bold True
                            xalign 0.5
                        fixed:
                            xfill True
                            ysize 18
                            frame:
                                xfill True
                                ysize 1
                                yalign 0.5
                                background Solid("#00000033")
                            frame:
                                xalign 0.5
                                yalign 0.5
                                background Solid("#FAF7F3")
                                padding (6, 0)
                                text "":
                                    size 16
                                    color "#C41230"

                text what:
                    id "what"
                    size tsz(40)
                    color "#0e0e0e"
                    xalign 0.5
                    text_align 0.5
                    xmaximum 1700

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
                            color ("#C41230" if device == _dev else "#6B6259")
                            hover_color "#C41230"
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
                text _desc size 22 color "#6B6259" xsize 900 text_align 0.5

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
                text _desc size 22 color "#6B6259" xsize 900 text_align 0.5


################################################################################
## GAME MENU — overlay base (save/load/prefs/about/return)
################################################################################
screen base_menu(title, scroll=None, yinitial=0.0):
    style_prefix "game_menu"
    tag menu

    frame:
        xfill True
        yfill True
        background Solid("#FAF7F3F2")

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
                    text title size 36 color "#1F1B19" bold True yalign 0.5
                    null width True
                    textbutton _("Bumalik"):
                        action Return()
                        yalign 0.5
                        xsize 200
                        ysize 64
                        background Solid("#F3EFEA")
                        hover_background Solid("#C41230")
                        text_color "#2B2624"
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
        background Solid("#FAF7F3F2")

        hbox:
            xfill True
            yfill True
            spacing 0

            ## ── LEFT: persistent sidebar, same on every tab ──
            frame:
                xsize _sb_w
                yfill True
                background Solid("#FFFFFF")
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
                        background Solid("#F3EFEA")
                        hover_background Solid("#b91c1c")
                        text_color "#6B6259"
                        text_hover_color "#fff"
                        text_size _sb_txt
                        text_xalign 0.5
                        text_yalign 0.5

                    textbutton _("← Bumalik"):

                        action Return()
                        xfill True
                        ysize 60
                        background Solid("#F3EFEA")
                        hover_background Solid("#C41230")
                        text_color "#6B6259"
                        text_hover_color "#fff"
                        text_size _sb_txt
                        text_xalign 0.5
                        text_yalign 0.5

            ## ── RIGHT: content panel swaps per tab ──
            frame:
                xfill True
                yfill True
                background Solid("#FAF7F3")

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
        background (Solid("#C41230") if _is_active else Solid("#F3EFEA"))
        hover_background Solid("#C41230")
        padding (18, 12)
        text_color ("#FFFFFF" if _is_active else "#3D3730")
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
                            background Solid("#F3EFEA")
                            hover_background Solid("#E3DBD2")
                            padding (3, 3)

                            add Transform(FileScreenshot(slot), xysize=(414, 230)):
                                xalign 0.5
                                yalign 0.5

                        text FileTime(slot, format=_("%b %d, %H:%M"), empty=_("Walang laman")):
                            size 20
                            color "#6B6259"
                            xalign 0.5

                        textbutton _("Burahin"):
                            action FileDelete(slot)
                            sensitive FileLoadable(slot)
                            xfill True
                            ysize 44
                            background Solid("#8e1a1a")
                            hover_background Solid("#b91c1c")
                            insensitive_background Solid("#F3EFEA55")
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
            background Frame("gui/nvl.png", Borders(0, 0, 0, 0))

            vbox:
                spacing 20
                xalign 0.5
                xmaximum 860

                null height 24

                if not renpy.variant("web") and not renpy.variant("small"):
                    use settings_card(_("Display")):
                        hbox:
                            spacing 40
                            use pref_tick_option(_("Fullscreen"), _preferences.fullscreen, Preference("display", "fullscreen"))
                            use pref_tick_option(_("Window"), not _preferences.fullscreen, Preference("display", "window"))

                use settings_card(_("Wika / Language")):
                    hbox:
                        spacing 40
                        use pref_tick_option(_("Tagalog"), _preferences.language is None, Language(None))
                        use pref_tick_option(_("English"), _preferences.language == "english", Language("english"))

                use settings_card(_("Bilis ng Teksto / Text Speed")):
                    bar:
                        value Preference("text speed")
                        xfill True
                        ysize 36
                        left_bar Solid("#C41230")
                        right_bar Solid("#E3DBD2")

                use settings_card(_("Laki ng Teksto / Text Size")):
                    hbox:
                        spacing 40
                        use pref_tick_option(_("Maliit"), persistent.text_scale == 0.85, SetField(persistent, "text_scale", 0.85))
                        use pref_tick_option(_("Normal"), persistent.text_scale == 1.0, SetField(persistent, "text_scale", 1.0))
                        use pref_tick_option(_("Malaki"), persistent.text_scale == 1.2, SetField(persistent, "text_scale", 1.2))

                use settings_card(_("Bilis ng Auto-Forward")):
                    bar:
                        value Preference("auto-forward time")
                        xfill True
                        ysize 36
                        left_bar Solid("#C41230")
                        right_bar Solid("#E3DBD2")

                    use settings_card(_("Musika / Music")):
                        bar:
                            value Preference("music volume")
                            xfill True
                            ysize 36
                            left_bar Solid("#56d364")
                            right_bar Solid("#E3DBD2")

                    use settings_card(_("Tunog / Sound")):
                        bar:
                            value Preference("sound volume")
                            xfill True
                            ysize 36
                            left_bar Solid("#e3b341")
                            right_bar Solid("#E3DBD2")

                    null height 40

## Reusable bordered card wrapper for a single settings row.
screen settings_card(label):
    frame:
        xfill True
        background Solid("#E3DBD2")
        padding (1, 1)

        frame:
            xfill True
            background Solid("#FFFFFF")
            padding (24, 18)

            vbox:
                xfill True
                spacing 14
                text label size 24 color "#C41230" bold True
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
                color ("#C41230" if is_selected else "#6B6259")
                hover_color "#C41230"
                bold is_selected
                yalign 0.5

screen preferences():
    tag menu
    use mcc_menu_hub("preferences")
        
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
            text _("Kasaysayan") size 36 color "#1F1B19" bold True yalign 0.5

        vbox:
            xfill True
            yfill True
            spacing 4

            null height 16

            python:
                _hist = list(reversed(_history_list)) if _history_list else []

            if not _hist:
                text "Walang kasaysayan pa." size 28 color "#6B6259" xalign 0.5

            for h in _hist:
                python:
                    _who_text  = h.who  if h.who  else None
                    _what_text = h.what if h.what else ""

                if _who_text or _what_text.strip():
                    frame:
                        xfill True
                        background Solid("#F3EFEA")
                        padding (20, 14)
                        bottom_margin 4

                        vbox:
                            spacing 6
                            if _who_text:
                                text _who_text size 26 color "#E5677A" bold True
                            text _what_text size 28 color "#2B2624" substitute False

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

            text "[config.name!t]" size 42 color "#1F1B19" bold True xalign 0.5
            text "Version [config.version]" size 28 color "#6B6259" xalign 0.5
            null height 20

            text "Project began in development in June by:" size 30 color "#E5677A" xalign 0.5
            text "Lead/Main Developer: Clarin, Kylle Benedict" size 27 color "#6B6259" xalign 0.5
            text "3D Sprites Artist: Morgan, Christian David F." size 26 color "#6B6259" xalign 0.5
            text "Landing Page Designer: Cecilio, Neil Ayangel C." size 26 color "#6B6259" xalign 0.5
            null height 12

            text "Technical Adviser: Engr. Ernie Lee Pineda, MIT" size 24 color "#6B6259" xalign 0.5
            text "Capstone Instructor: Engr. Dennis L. Tacadena, MIT" size 24 color "#6B6259" xalign 0.5
            null height 12

            text "Mabalacat City College" size 24 color "#6B6259" xalign 0.5
            text "Institute of Computing Studies, 2026" size 24 color "#6B6259" xalign 0.5
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
        background Solid("#FFFFFFF8")
        padding (40, 40)

        vbox:
            spacing 30
            xfill True

            text message:
                size 30
                color "#2B2624"
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
                    background Solid("#F3EFEA")
                    hover_background Solid("#E3DBD2")
                    text_color "#2B2624"
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
        background Frame("gui/skip.png", Borders(0, 0, 0, 0))
        padding (20, 15)
        text _(">> Nilalaktawan...") size 40 color "#C41230"
style button:
    activate_sound "audio/sfx/sfx_click.ogg"