## game/sprites.rpy
## Sprite staging toolkit for A.I. na lang!  (movement + a sprite checker)
##
## Usage (all are normal Ren'Py `show` statements; nothing here touches dialogue):
##   show gabby happy at center, hop          # excited / greeting
##   show kent stressed at left, jitter       # nervous
##   show carl normal at right, nod           # agreement / "oo nga"
##   show rey normal at right, enter_right    # entrance (replaces `with dissolve`)
##   show carl normal at left, enter_left
##   show carl happy at right with quickfade  # smooth expression swap
## Re-showing a sprite that is already on screen with a new expression changes
## only the expression (and plays the movement); keep the same position word.

transform hop:
    easeout 0.12 yoffset -26
    easein  0.12 yoffset 0

transform jitter:
    linear 0.05 xoffset -7
    linear 0.05 xoffset 7
    linear 0.05 xoffset -7
    linear 0.05 xoffset 7
    linear 0.05 xoffset 0

transform nod:
    easeout 0.10 yoffset 10
    easein  0.10 yoffset 0
    easeout 0.10 yoffset 10
    easein  0.10 yoffset 0

transform enter_right:
    xoffset 380 alpha 0.0
    easeout 0.35 xoffset 0 alpha 1.0

transform enter_left:
    xoffset -380 alpha 0.0
    easeout 0.35 xoffset 0 alpha 1.0

define quickfade = Dissolve(0.15)

## Extra lanes for scenes with 4 characters (left / leftish / center / rightish / right)
transform leftish:
    xalign 0.25
transform rightish:
    xalign 0.75

## ── SPRITE CHECKER ───────────────────────────────────────────────────────────
## Developer tool. Open the console (Shift+O, needs config.developer) and type:
##     jump sprite_test
## It shows every sprite one by one, so a missing/broken file shows up here
## instead of in the middle of a chapter. Click through each one.
define sprite_test_list = [
    "mc normal", "mc happy", "mc stressed",
    "alex normal", "alex happy", "alex stressed",
    "alexa normal", "alexa happy", "alexa stressed",
    "carl normal", "carl happy", "carl stressed",
    "carly normal", "carly happy", "carly stressed",
    "gabby normal", "gabby happy", "gabby stressed",
    "kent normal", "kent happy", "kent stressed",
    "rey normal", "rey happy", "rey stressed",
    "mr_earns normal", "mr_earns thinking", "mr_earns disappointed",
    "mr_kai normal", "mr_kai thinking", "mr_kai disappointed",
    "ms_iva normal", "ms_iva thinking", "ms_iva disappointed",
]

label sprite_test:
    scene bg_classroom
    python:
        for _n in sprite_test_list:
            renpy.show(_n, at_list=[center])
            renpy.say(None, _n)
            renpy.hide(_n.split()[0])
    return
