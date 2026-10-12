## game/ui_polish.rpy
## UI polish for the defense build:
##   - tr(): IMMEDIATE translation. _() only marks a string and Ren'Py translates the
##     whole displayed text, so any string that is joined to something else or edited
##     before it is shown (like "TANONG 3" or a quiz option with its "A. " removed)
##     must go through tr() or it stays in Tagalog.
##   - say_fit_size: keeps dialogue inside the box (name sits inside the box)
##   - quiz_hint: plain-language hints for non-IT players (text lives in quiz_hints.rpy)
##   - ai_used_overlay: the moment the player lets the AI answer (the core mechanic)

init python:
    import re

    def tr(s):
        return renpy.translate_string(s)

    def say_fit_size(what, base, width=1480, height=200, line_h=1.3, char_w=0.6):
        ## Rough fit: estimate the wrapped line count at a font size and shrink
        ## (never below 26) until the text fits the box height.
        plain = re.sub(r"\{[^}]*\}", "", what)
        size = base
        while size > 26:
            cpl = max(10, int(width / (char_w * size)))
            lines = 0
            for part in plain.split("\n"):
                lines += max(1, -(-len(part) // cpl))
            if lines * line_h * size <= height:
                break
            size -= 2
        return size

    def quiz_fb_color(kind):
        if kind == "correct":
            return cb("end_good")
        if kind == "wrong":
            return cb("end_bad")
        return "#C41230"

    def quiz_fb_heading(kind):
        if kind == "correct":
            return tr("TAMA ANG SAGOT!")
        if kind == "wrong":
            return tr("MALI. SUBUKAN ULIT.")
        return tr("SAGOT NG AI")

    _acr_state = {}

    def quiz_expand(text, skip=None, short_only=False):
        ## Writes abbreviations out in full, e.g. "CFAA" -> "Computer Fraud and Abuse
        ## Act (CFAA)". Returns (new_text, set_of_abbreviations_explained).
        ## short_only: for answer options, only when the option is short, and never
        ## for abbreviations the question already explained.
        skip = set(skip or [])
        done = set()
        if short_only and len(text.split()) > 8:
            return text, done
        if "re" not in _acr_state:
            keys = sorted(quiz_glossary.keys(), key=len, reverse=True)
            _acr_state["re"] = re.compile(r"\b(" + "|".join(keys) + r")(s?)\b")
        def sub(m):
            acr = m.group(1)
            plural = m.group(2)
            if acr in skip or acr in done:
                return m.group(0)
            full = quiz_glossary[acr]
            s0, e0 = m.start(), m.end()
            if s0 > 0 and text[s0 - 1] == "(" and e0 < len(text) and text[e0] == ")":
                done.add(acr)
                return m.group(0)
            if full.lower() in text.lower():
                done.add(acr)
                return m.group(0)
            done.add(acr)
            return full + plural + " (" + acr + plural + ")"
        return _acr_state["re"].sub(sub, text), done

    def quiz_hint(question):
        h = quiz_hints.get(question)
        if h:
            return tr(h)
        return None

    def ai_warning(n):
        if n <= 1:
            return tr("Isang beses lang naman. Hindi na mauulit.")
        if n <= 3:
            return tr("Nagiging ugali na.")
        if n <= 6:
            return tr("Hindi mo na kailangang mag-isip. Iyon ang problema.")
        return tr("Kaya mo pa bang sagutin ito nang mag-isa?")

transform ai_pop:
    zoom 1.3 alpha 0.0
    easeout 0.22 zoom 1.0 alpha 1.0
    linear 0.04 xoffset -10
    linear 0.04 xoffset 10
    linear 0.04 xoffset -6
    linear 0.04 xoffset 0

screen ai_used_overlay():
    modal True
    zorder 195
    default can_skip = False
    timer 1.2 action SetScreenVariable("can_skip", True)
    timer 6.0 action Return()
    if can_skip:
        key "dismiss" action Return()

    frame:
        xfill True
        yfill True
        background Solid("#14110FEE")

        vbox:
            xalign 0.5
            yalign 0.5
            xsize 1100
            spacing 28

            frame:
                at ai_pop
                xalign 0.5
                background Solid("#C41230")
                padding (56, 20)
                text _("AI ANG SUMAGOT") size 72 color "#FFFFFF" bold True xalign 0.5

            text _("Mabilis. Tama. Walang pinag-isipan.") size 34 color "#F3EFEA" xalign 0.5 text_align 0.5

            frame:
                xalign 0.5
                xsize 760
                background Solid("#FFFFFF14")
                padding (28, 22)
                vbox:
                    spacing 14
                    fixed:
                        xfill True
                        ysize 32
                        text "CRITICAL THINKING" size 24 color "#F3EFEA" bold True xalign 0.0
                        text (str(critical_thinking) + " / 100") size 24 color "#FFFFFF" bold True xalign 1.0
                    bar:
                        value StaticValue(critical_thinking, 100)
                        xfill True
                        ysize 16
                        thumb None
                        left_bar Solid("#C41230")
                        right_bar Solid("#FFFFFF33")
                    fixed:
                        xfill True
                        ysize 44
                        text "AI ANSWERS" size 24 color "#F3EFEA" bold True xalign 0.0 yalign 0.5
                        frame:
                            xalign 1.0
                            yalign 0.5
                            background Solid("#C41230")
                            padding (20, 4)
                            text str(ai_use_count) size 26 color "#FFFFFF" bold True

            text ai_warning(ai_use_count) size 30 color "#FFB4BF" xalign 0.5 text_align 0.5

            if can_skip:
                text _("I-click para magpatuloy") size 22 color "#B8AFA6" xalign 0.5
