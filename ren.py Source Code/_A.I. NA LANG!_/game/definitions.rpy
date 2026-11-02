## game/definitions.rpy
## All character definitions, persistent variables, and image declarations.

default critical_thinking    = 50   # 0–100. Drops with AI, rises with effort.
default motivation           = 50   # 0–100. Drops with failure/shame, rises with wins.
default networking_grade     = 65   # Subject grade 0–100. INC if below 60 at finals.
default programming_grade    = 65
default cyber_grade          = 65
default ai_use_count         = 0    # Times player chose "Ask AI" during minigames.
default got_caught           = False  # True if Ms. Iva catches hallucinated citation.
default player_gender        = "male"   # Set in prologue character selection.
default player_bestfriend    = "carl"   # "carl" or "carly", set in prologue.
default player_name          = "Alex"   # Overwritten by name input in prologue.
default current_week         = 1        # Narrative week tracker (1–8).
default day_label            = "Day 1, Umaga"
default show_hud             = False    # Controlled manually; overlay re-shows every frame.
default _extras_target = None

transform farleft:
    xalign 0.02
transform farright:
    xalign 0.98

init python:

    def ct_change(delta):
        store.critical_thinking = max(0, min(100, store.critical_thinking + delta))

    def mot_change(delta):
        store.motivation = max(0, min(100, store.motivation + delta))

    def grade_change(subject, delta):
        if subject == "networking":
            store.networking_grade = max(0, min(100, store.networking_grade + delta))
        elif subject == "programming":
            store.programming_grade = max(0, min(100, store.programming_grade + delta))
        elif subject == "cyber":
            store.cyber_grade = max(0, min(100, store.cyber_grade + delta))

    def use_ai(subject=None, grade_boost=8):
        ct_change(-10)
        if subject:
            grade_change(subject, grade_boost)

    def letter_grade(score):
        if score >= 90: return "A"
        elif score >= 80: return "B"
        elif score >= 70: return "C"
        elif score >= 60: return "D"
        else: return "INC"

    def any_incomplete():
        return (store.networking_grade < 60 or
                store.programming_grade < 60 or
                store.cyber_grade < 60)

    def determine_ending():
        ng     = store.networking_grade
        pg     = store.programming_grade
        cg     = store.cyber_grade
        ct     = store.critical_thinking
        mot    = store.motivation
        ai     = store.ai_use_count
        caught = store.got_caught

        all_pass = (ng >= 60 and pg >= 60 and cg >= 60)
        all_high = (ng >= 85 and pg >= 85 and cg >= 85)

        if caught:
            return "ending_caught"
        if any_incomplete():
            if ct >= 45 and mot >= 45:
                return "ending_redemption"
            else:
                return "ending_bad"
        if all_high and ai == 0 and ct >= 75:
            return "ending_special_good"
        if all_pass and (ai > 3 or ct < 55):
            return "ending_good_guilt"
        if all_pass:
            return "ending_good_solid"
        return "ending_bad"

default tutorial_highlight = None

## Optional explicit question for the NEXT menu (shown in the choice screen's question card).
## Set it with  $ menu_q = _("...")  right before a menu; it clears itself on the next dialogue line.
default menu_q = None

## "mc" is set to mc_m or mc_f in the prologue; a default keeps Lint from flagging every mc line.
default mc = mc_m

init python:
    def clear_menu_q(event, **kwargs):
        if event == "begin" and store.menu_q is not None:
            store.menu_q = None
    config.all_character_callbacks.append(clear_menu_q)

define mc_m = Character("[player_name]",
    color="#ff5050" )

define mc_f = Character("[player_name]",
    color="#f825ff" )

define carl = Character("Carl",
    color="#7ee787" )

define carly = Character("Carly",
    color="#35fdaa" )

define gabby = Character("Gabby",
    color="#f78166" )

define kent = Character("Kent",
    color="#a450ff", )

define rey = Character("Rey",
    color="#ffa657", )

define mr_earns = Character("Mr. Earns",
    color="#23ffbd", )

define mr_kai = Character("Mr. Kai",
    color="#ff3e30", )

define ms_iva = Character("Ms. Iva",
    color="#2fff47", )

define narrator = Character(None,
    what_italic=True)

define sys_voice = Character(None,
    what_italic=True,
    what_slow_sound="audio/sfx/blip/sfx_blip_digital.ogg")

define groupchat = Character("GROUP CHAT",
    color="#8b949e",
    what_italic=True,
    what_slow_sound="audio/sfx/sfx_chat.ogg")

define ai_voice = Character("AI",
    color="#58a6ff",
    what_italic=False,
    what_slow_sound="audio/sfx/blip/sfx_blip_digital.ogg")


image alex normal = "images/sprites/alex_normal.webp"
image alex happy = "images/sprites/alex_happy.webp"
image alex stressed = "images/sprites/alex_stressed.webp"
image alexa normal = "images/sprites/alexa_normal.webp"
image alexa happy = "images/sprites/alexa_happy.webp"
image alexa stressed = "images/sprites/alexa_stressed.webp"
image carl normal = "images/sprites/carl_normal.webp"
image carl happy = "images/sprites/carl_happy.webp"
image carl stressed = "images/sprites/carl_stressed.webp"
image carly normal = "images/sprites/carly_normal.webp"
image carly happy = "images/sprites/carly_happy.webp"
image carly stressed = "images/sprites/carly_stressed.webp"
image gabby normal = "images/sprites/gabby_normal.webp"
image gabby happy = "images/sprites/gabby_happy.webp"
image gabby stressed = "images/sprites/gabby_stressed.webp"
image kent normal = "images/sprites/kent_normal.webp"
image kent happy = "images/sprites/kent_happy.webp"
image kent stressed = "images/sprites/kent_stressed.webp"
image rey normal = "images/sprites/rey_normal.webp"
image rey happy = "images/sprites/rey_happy.webp"
image rey stressed = "images/sprites/rey_stressed.webp"

image mr_earns normal = "images/sprites/mr_earns_normal.webp"
image mr_earns thinking = "images/sprites/mr_earns_thinking.webp"
image mr_earns disappointed = "images/sprites/mr_earns_disappointed.webp"
image mr_kai normal = "images/sprites/mr_kai_normal.webp"
image mr_kai thinking = "images/sprites/mr_kai_thinking.webp"
image mr_kai disappointed = "images/sprites/mr_kai_disappointed.webp"
image ms_iva normal = "images/sprites/ms_iva_normal.webp"
image ms_iva thinking = "images/sprites/ms_iva_thinking.webp"
image ms_iva disappointed = "images/sprites/ms_iva_disappointed.webp"
image bg_campus_night = "images/backgrounds/bg_zoom.webp"
image cg_ai_chat = Solid("#0d1117")
## Backgrounds
image bg_classroom = "images/backgrounds/bg_classroom.webp"
image bg_canteen   = "images/backgrounds/bg_canteen.webp"
image bg_hallway   = "images/backgrounds/bg_hallway.webp"
image bg_bedroom   = "images/backgrounds/bg_bedroom.webp"
image bg_lab       = "images/backgrounds/bg_lab.webp"
image bg_campus    = "images/backgrounds/bg_campus.webp"

init python:
    renpy.image("mc normal", ConditionSwitch(
        "player_gender == 'male'", "images/sprites/alex_normal.webp",
        "True", "images/sprites/alexa_normal.webp"
    ))
    renpy.image("mc happy", ConditionSwitch(
        "player_gender == 'male'", "images/sprites/alex_happy.webp",
        "True", "images/sprites/alexa_happy.webp"
    ))
    renpy.image("mc stressed", ConditionSwitch(
        "player_gender == 'male'", "images/sprites/alex_stressed.webp",
        "True", "images/sprites/alexa_stressed.webp"
    ))
    renpy.image("bestfriend normal", ConditionSwitch(
        "player_bestfriend == 'carl'", "images/sprites/carl_normal.webp",
        "True", "images/sprites/carly_normal.webp"
    ))
    renpy.image("bestfriend happy", ConditionSwitch(
        "player_bestfriend == 'carl'", "images/sprites/carl_happy.webp",
        "True", "images/sprites/carly_happy.webp"
    ))
    renpy.image("bestfriend stressed", ConditionSwitch(
        "player_bestfriend == 'carl'", "images/sprites/carl_stressed.webp",
        "True", "images/sprites/carly_stressed.webp"
    ))