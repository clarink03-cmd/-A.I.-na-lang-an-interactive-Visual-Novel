## game/colorblind.rpy
## Colorblind mode for A.I. na lang!
##
## Three modes, saved in persistent so the choice survives restarts:
##   "off" - original palette (nothing changes)
##   "rg"  - red-green safe (protanopia / deuteranopia)  -> Okabe-Ito based
##   "by"  - blue-yellow safe (tritanopia)
##
## Anywhere the game used color to carry meaning, this file supplies a safe
## color AND (in the HUD) a numeric readout so color is never the only cue.
## All text colors were checked for >= 4.5:1 contrast on the cream (#FAF7F3) UI.

default persistent.colorblind_mode = "off"

init -1 python:

    CB_EMPTY_SEG = "#E3DBD2"

    cb_palettes = {

        "off": {
            "night": "#4A5578", "day": "#E0A836", "special": "#C41230",
            "ct0": "#b91c1c", "ct1": "#b45309", "ct2": "#854d0e",
            "ct3": "#166534", "ct4": "#15803d",
            "motivation": "#f43f5e",
            "grade_net": "#e3b341", "grade_prog": "#ff7b72", "grade_cyber": "#56d364",
            "end_good": "#166534", "end_bad": "#8C0E23", "end_neutral": "#6B6259",
            "ai_text": "#7ee787",
        },

        ## Red-green safe: blue <-> vermillion/orange carry the good/bad axis.
        "rg": {
            "night": "#0072B2", "day": "#E69F00", "special": "#CC79A7",
            "ct0": "#D55E00", "ct1": "#E69F00", "ct2": "#8C8C8C",
            "ct3": "#56B4E9", "ct4": "#0072B2",
            "motivation": "#0072B2",
            "grade_net": "#8A5A00", "grade_prog": "#005A9C", "grade_cyber": "#8E3B7A",
            "end_good": "#0072B2", "end_bad": "#B34700",
            "ai_text": "#00695C",
            "who_mc_m": "#A84300", "who_mc_f": "#8E3B7A", "who_carl": "#005A9C",
            "who_carly": "#8A5A00", "who_gabby": "#A3306B", "who_kent": "#4B3F9E",
            "who_rey": "#6B6B00", "who_mr_earns": "#555555", "who_mr_kai": "#A84300",
            "who_ms_iva": "#00695C", "who_groupchat": "#555555", "who_ai": "#005A9C",
        },

        ## Blue-yellow safe: red <-> teal/gray carry the good/bad axis.
        "by": {
            "night": "#333333", "day": "#D55E00", "special": "#009E73",
            "ct0": "#B91C1C", "ct1": "#D55E00", "ct2": "#8C8C8C",
            "ct3": "#009E9E", "ct4": "#006D77",
            "motivation": "#D55E00",
            "grade_net": "#B33F00", "grade_prog": "#007A66", "grade_cyber": "#555555",
            "end_good": "#006D5B", "end_bad": "#B01E3C",
            "ai_text": "#00695C",
            "who_mc_m": "#B01E3C", "who_mc_f": "#A84300", "who_carl": "#00695C",
            "who_carly": "#555555", "who_gabby": "#A3306B", "who_kent": "#8A5A00",
            "who_rey": "#B33F00", "who_mr_earns": "#333333", "who_mr_kai": "#B01E3C",
            "who_ms_iva": "#006D77", "who_groupchat": "#555555", "who_ai": "#333333",
        },
    }

    cb_who_keys = {
        "Carl": "carl", "Carly": "carly", "Gabby": "gabby", "Kent": "kent",
        "Rey": "rey", "Mr. Earns": "mr_earns", "Mr. Kai": "mr_kai",
        "Ms. Iva": "ms_iva", "GROUP CHAT": "groupchat", "AI": "ai",
    }

    def cb_on():
        return persistent.colorblind_mode in ("rg", "by")

    def cb(key):
        pal = cb_palettes.get(persistent.colorblind_mode, cb_palettes["off"])
        return pal.get(key) or cb_palettes["off"].get(key, "#C41230")

    def cb_ct_seg(i, filled):
        ## i = 0..9 (segment index). Tier = 0..4, same buckets as before.
        return cb("ct%d" % (i // 2)) if filled else CB_EMPTY_SEG

    def cb_who(who):
        ## Speaker-name recolor for the say screen. Returns `who` untouched
        ## when the mode is off, so the original look is preserved exactly.
        if not who or not cb_on():
            return who
        if who == store.player_name:
            key = "mc_m" if store.player_gender == "male" else "mc_f"
        else:
            key = cb_who_keys.get(who)
        if key is None:
            return who
        return "{color=%s}%s{/color}" % (cb("who_" + key), who)
