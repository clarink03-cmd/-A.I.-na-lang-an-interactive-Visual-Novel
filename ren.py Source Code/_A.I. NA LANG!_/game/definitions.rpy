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
        store.ai_use_count += 1
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
        if all_pass and ai > 3 and ct < 55:
            return "ending_good_guilt"
        if all_pass:
            return "ending_good_solid"
        return "ending_bad"

default tutorial_highlight = None

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


image alex normal = Transform("images/sprites/alex_normal.webp", zoom=0.3)
image alex happy = Transform("images/sprites/alex_happy.webp", zoom=0.3)
image alex stressed = Transform("images/sprites/alex_stressed.webp", zoom=0.3)
image alexa normal = Transform("images/sprites/alexa_normal.webp", zoom=0.3)
image alexa happy = Transform("images/sprites/alexa_happy.webp", zoom=0.3)
image alexa stressed = Transform("images/sprites/alexa_stressed.webp", zoom=0.3)
image carl normal = Transform("images/sprites/carl_normal.webp", zoom=0.3)
image carl happy = Transform("images/sprites/carl_happy.webp", zoom=0.3)
image carl stressed = Transform("images/sprites/carl_stressed.webp", zoom=0.3)
image carly normal = Transform("images/sprites/carly_normal.webp", zoom=0.3)
image carly happy = Transform("images/sprites/carly_happy.webp", zoom=0.3)
image carly stressed = Transform("images/sprites/carly_stressed.webp", zoom=0.3)
image gabby normal = Transform("images/sprites/gabby_normal.webp", zoom=0.4)
image gabby happy = Transform("images/sprites/gabby_happy.webp", zoom=0.4)
image gabby stressed = Transform("images/sprites/gabby_stressed.webp", zoom=0.3)
image kent normal = Transform("images/sprites/kent_normal.webp", zoom=0.3)
image kent happy = Transform("images/sprites/kent_happy.webp", zoom=0.3)
image kent stressed = Transform("images/sprites/kent_stressed.webp", zoom=0.3)
image rey normal = Transform("images/sprites/rey_normal.webp", zoom=0.4)
image rey happy = Transform("images/sprites/rey_happy.webp", zoom=0.4)
image rey stressed = Transform("images/sprites/rey_stressed.webp", zoom=0.4)

image mr_earns normal = Transform("images/sprites/mr_earns_normal.webp", zoom=0.5)
image mr_earns thinking = Transform("images/sprites/mr_earns_thinking.webp", zoom=0.5)
image mr_earns disappointed = Transform("images/sprites/mr_earns_disappointed.webp", zoom=0.5)
image mr_kai normal = Transform("images/sprites/mr_kai_normal.webp", zoom=0.3)
image mr_kai thinking = Transform("images/sprites/mr_kai_thinking.webp", zoom=0.3)
image mr_kai disappointed = Transform("images/sprites/mr_kai_disappointed.webp", zoom=0.3)
image ms_iva normal = Transform("images/sprites/ms_iva_normal.webp", zoom=0.3)
image ms_iva thinking = Transform("images/sprites/ms_iva_thinking.webp", zoom=0.3)
image ms_iva disappointed = Transform("images/sprites/ms_iva_disappointed.webp", zoom=0.3)
image bg_campus_night = "images/backgrounds/bg_zoom.webp"
image cg_ai_chat = Solid("#0d1117")
## Backgrounds
image bg_classroom = "images/backgrounds/bg_classroom.webp"
image bg_canteen   = "images/backgrounds/bg_canteen.webp"
image bg_hallway   = "images/backgrounds/bg_hallway.webp"
image bg_bedroom   = "images/backgrounds/bg_bedroom.webp"
image bg_lab       = "images/backgrounds/bg_lab.webp"
image bg_campus    = "images/backgrounds/bg_campus.webp"
image bg_campus_night = "images/backgrounds/bg_zoom.webp"

init python:
    renpy.image("mc normal", ConditionSwitch(
        "player_gender == 'male'", Transform("images/sprites/alex_normal.webp", zoom=0.3),
        "True", Transform("images/sprites/alexa_normal.webp", zoom=0.3)
    ))
    renpy.image("mc happy", ConditionSwitch(
        "player_gender == 'male'", Transform("images/sprites/alex_happy.webp", zoom=0.3),
        "True", Transform("images/sprites/alexa_happy.webp", zoom=0.3)
    ))
    renpy.image("mc stressed", ConditionSwitch(
        "player_gender == 'male'", Transform("images/sprites/alex_stressed.webp", zoom=0.3),
        "True", Transform("images/sprites/alexa_stressed.webp", zoom=0.3)
    ))
    renpy.image("bestfriend normal", ConditionSwitch(
        "player_bestfriend == 'carl'", Transform("images/sprites/carl_normal.webp", zoom=0.3),
        "True", Transform("images/sprites/carly_normal.webp", zoom=0.3)
    ))
    renpy.image("bestfriend happy", ConditionSwitch(
        "player_bestfriend == 'carl'", Transform("images/sprites/carl_happy.webp", zoom=0.3),
        "True", Transform("images/sprites/carly_happy.webp", zoom=0.3)
    ))
    renpy.image("bestfriend stressed", ConditionSwitch(
        "player_bestfriend == 'carl'", Transform("images/sprites/carl_stressed.webp", zoom=0.3),
        "True", Transform("images/sprites/carly_stressed.webp", zoom=0.3)
    ))