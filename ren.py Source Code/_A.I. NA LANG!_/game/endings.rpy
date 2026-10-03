## game/endings.rpy
## All six endings for A.I. na lang!

screen ending_title(kind, ending_name, tagline):
    zorder 150
    on "show" action Play("sound", "audio/sfx/sfx_page_turn.ogg")

    python:
        _accent = "#166534" if kind == "good" else "#8C0E23"

    frame:
        xfill True
        yfill True
        background Solid("#FAF7F3")

        frame:
            xfill True
            ysize 5
            yalign 0.42
            background Solid(_accent)

        vbox:
            xalign 0.5
            yalign 0.45
            spacing 14

            text (_("MAGANDANG WAKAS") if kind == "good" else _("MASAKIT NA WAKAS")) size 26 color _accent xalign 0.5
            text ending_name size 62 color "#1F1B19" xalign 0.5 bold True outlines [(3, _accent, 0, 0)]
            text tagline size 30 color "#6B6259" xalign 0.5 italic True

        text "* Press any key to continue *" xalign 0.5 yalign 0.92 size 24 color "#E3DBD2"

    key "K_RETURN" action Return()
    key "K_SPACE"  action Return()
    button:
        xfill True
        yfill True
        action Return()
        background None

label ending_sequence:
    ## Calculate and jump to the correct ending
    $ ending_target = determine_ending()
    jump expression ending_target

# ══════════════════════════════════════════════════════════════════════════════
# ENDING 1: SPECIAL GOOD, "The Real Deal"
# Condition: All ≥ 85, ai_use_count == 0, CT ≥ 75
# ══════════════════════════════════════════════════════════════════════════════
label ending_special_good:
    $ persistent.last_ending = "The Real Deal"
    call screen ending_title("good", "The Real Deal", "Ang tunay na natutunan, hindi kayang kunin.")
    $ safe_play("music", "audio/bgm/bgm_good_ending.ogg", loop=True)
    scene black with dissolve

    narrator "TATLONG BUWAN ANG LUMIPAS."
    pause 1.5
    scene bg_classroom with dissolve

    show ms_iva thinking at left with moveinleft
    ms_iva "Gusto kong ipakita sa klase ang isang bagay ngayon."
    narrator "(Binuhat niya ang isang papel mula sa kanyang mesa. Hindi mo ito inaasahan.)"
    ms_iva "Ang essay na ito, tungkol sa cognitive debt. Binasa ko ito nang tatlong beses. Hindi dahil may mali, kundi dahil sa unang pagkakataon ngayong semester, may isang estudyante na hindi sumulat para lang sa grado."
    ms_iva "Sumulat siya dahil totoong may natutunan siya."
    if player_gender == "male":
        mc_m "(Naramdaman ko ang biglaang init sa dibdib ko.)"
    else:
        mc_f "(Naramdaman ko ang biglaang init sa dibdib ko.)"
    ms_iva "May mga bahagi na hindi perpekto ang grammar. May isang transition na awkward. Pero alam ba ninyo kung ano ang naroon?"
    narrator "(Tumigil siya. Tumingin sa iyo nang diretso.)"
    ms_iva "Ang tunay na pag-unawa. Hindi perpekto. Pero totoo. At may lakas, may dating, na hindi kayang gayahin ng kahit anong language model."
    ms_iva "Ito ang tunay na estudyanteng hindi kumuha ng shortcut. Hindi dahil bawal. Kundi dahil pinili niyang matuto."
    narrator "(Tahimik ang buong klase. Ilang segundo. Pakiramdam, mas matagal.)"
    ms_iva "Ipinagmamalaki ko kayo."
    if player_gender == "male":
        mc_m "(Nakilala ko ang sarili kong pangalan sa board. Hindi ako makapaniwala.)"
        mc_m "(Tiningnan ko ang papel. Binasa ko ang sarili kong mga salita.)"
        mc_m "(At sa unang pagkakataon sa mahabang panahon, naniwala ako.)"
    else:
        mc_f "(Nakilala ko ang sarili kong pangalan sa board. Hindi ako makapaniwala.)"
        mc_f "(Tiningnan ko ang papel. Binasa ko ang sarili kong mga salita.)"
        mc_f "(At sa unang pagkakataon sa mahabang panahon, naniwala ako.)"

    if player_gender == "male":
        mc_m "Hindi ito 'yung papel na gustong isulat ng 'dating' na ako. Pero pinaka-totoo ito sa lahat ng aking sinulat."
    else:
        mc_f "Ito ang pinaka-totoo na sinulat ko. Walang AI na nag-generate nito. Bawat salita, galing sa akin."

    hide ms_iva with dissolve

    scene bg_canteen with dissolve
    $ safe_play("music", "audio/bgm/bgm_good_ending.ogg", loop=True)

    show carl happy at left with moveinleft
    show gabby happy at right with moveinright
    show kent happy at center with dissolve
    show rey normal at right with dissolve

    narrator "(Grupo sa canteen. Extra rice para kay Carl. Tahimik na masaya si Kent. Si Gabby, nagnanakaw ng notes mo para sa susunod na semester.)"
    gabby "Pwede mo ba akong turuan? For real this time. 'Yung authentic na paraan."
    if player_gender == "male":
        mc_m "Oo. Pero i-review mo talaga. Sariling utak. Hindi AI."
    else:
        mc_f "Oo, pero sineseryoso ko. Sariling utak mo ang gamitin mo."
    gabby "Sige na, sige na!"
    kent "(bumubulong kay Rey) Miracle."
    rey "..."
    narrator "(Tahimik si Rey. Pero alam mo na, iyon ang kanyang paraan ng pagsabi na proud siya.)"

    hide carl with dissolve
    hide gabby with dissolve
    hide kent with dissolve
    hide rey with dissolve

    scene black with dissolve
    narrator "Hindi ka naging kung ano ang kinuha ng pandemic sa iyo."
    pause 1.0
    narrator "Naging isang bagay na hindi nito kayang kunin."
    pause 1.0
    narrator "Hindi shortcut. Ang mahabang daan. Ang landas mo."
    pause 1.5
    narrator "Graduated with honors, apat na semester pagkatapos."
    narrator "Ang AI chat window, nakasara."
    narrator "Hindi dahil ipinagbawal."
    narrator "Kundi dahil hindi mo na kailangan ito para mag-isip para sa iyo."
    pause 2.0

    scene black
    narrator "✦ SPECIAL GOOD ENDING, 'The Real Deal' ✦"
    pause 1.5
    narrator "Networking: [letter_grade(networking_grade)] | Programming: [letter_grade(programming_grade)] | Cybersecurity: [letter_grade(cyber_grade)]"
    narrator "Critical Thinking: [critical_thinking] / 100 | AI Uses: [ai_use_count]"
    call show_credits
    return

# ══════════════════════════════════════════════════════════════════════════════
# ENDING 2: GOOD WITH GUILT, "At What Cost?"
# Condition: All ≥ 60, CT < 55 OR ai_use_count > 3
# ══════════════════════════════════════════════════════════════════════════════
label ending_good_guilt:
    $ persistent.last_ending = "At What Cost?"
    call screen ending_title("good", "At What Cost?", "Nakapasa ka. Pero may tanong na hindi pa nasasagot.")
    $ safe_play("music", "audio/bgm/bgm_good_ending.ogg", loop=True)
    scene bg_canteen with dissolve

    if player_bestfriend == "carl":
        show carl happy at right with dissolve
        carl "Uy! Lahat tayo nakapasa! Selebrasyon mamaya?"
    else:
        show carly happy at right with dissolve
        carly "Nakapasa tayo! Grabe, akala ko hindi na!"

    narrator "(Masarap ang pagkain. Tama ang grades. Nandoon ang mga numero sa report card.)"

    if player_gender == "male":
        mc_m "(Nakapasa ako. Tama ang resulta. Bakit parang walang masyadong nangyari?)"
    else:
        mc_f "(Nakapasa ako. Lahat ng subjects. Tapos... ganito lang pala ang pakiramdam?)"

    narrator "(Tinitingnan mo ang grade slip. Tapos ang bag mo. Tapos muli ang slip.)"

    if player_gender == "male":
        mc_m "(Anong matututunan ko sa susunod na semester? Kung paano gumawa ng mas magandang prompt?)"
    else:
        mc_f "(Kung tatanungin ako bukas kung ano ang pinag-aralan ko, anong sasabihin ko?)"

    if player_bestfriend == "carl":
        hide carl with dissolve
    else:
        hide carly with dissolve

    scene black with dissolve
    narrator "Nakapasa ka."
    pause 1.2
    narrator "Ang tanong ni Ms. Iva noong una, kailan nga ba nagiging crutch ang isang tool? Hanggang ngayon, hindi mo pa nasasagot."
    pause 1.0
    narrator "Sa susunod na semester, hindi nawawala ang tanong. Mas humihirap lang pag-isipan."
    pause 1.5

    scene black
    narrator "✦ GOOD ENDING, 'At What Cost?' ✦"
    pause 1.0
    narrator "Networking: [letter_grade(networking_grade)] | Programming: [letter_grade(programming_grade)] | Cybersecurity: [letter_grade(cyber_grade)]"
    narrator "Critical Thinking: [critical_thinking] / 100 | AI Uses: [ai_use_count]"
    narrator "(Pahiwatig: subukan muli nang may mas mataas na Critical Thinking at mas kaunting AI use para sa Special Good Ending.)"
    call show_credits
    return

# ══════════════════════════════════════════════════════════════════════════════
# ENDING 3: GOOD SOLID, "Solid Enough"
# Condition: All ≥ 60, not Special Good, not Good Guilt
# ══════════════════════════════════
label ending_good_solid:
    $ persistent.last_ending = "Solid Enough"
    call screen ending_title("good", "Solid Enough", "Hindi perpekto. Pero earned.")
    $ safe_play("music", "audio/bgm/bgm_good_ending.ogg", loop=True)
    scene bg_canteen with dissolve

    if player_bestfriend == "carl":
        show carl happy at right with dissolve
    else:
        show carly happy at right with dissolve

    narrator "(Nakalusot. Hindi lahat perpekto, may ilang grade na medyo mababa.)"
    narrator "(Pero nakalusot. At alam mo kung saan nanggaling ang bawat puntos.)"

    show mr_kai thinking at left with dissolve
    mr_kai "Ang coding output mo, may ilang inefficiency, pero sarili mo ang logic. 'Yan ang pinakamahalaga."
    hide mr_kai with dissolve

    if player_gender == "male":
        mc_m "Hindi perpekto ang grades ko. Pero 'yung linya na sinulat ko sa essay ni Ms. Iva, 'yun talaga galing sa akin."
    else:
        mc_f "Hindi perpekto ang lahat. Pero lahat ay earned. Lahat, sarili ko."

    if player_bestfriend == "carl":
        hide carl with dissolve
    else:
        hide carly with dissolve

    scene black with dissolve
    narrator "Hindi perpekto. Pero earned."
    pause 1.0
    narrator "Bawat grade na nakuha ay paalala na nandoon ka, presente, nagsisikap, paminsan-minsang nagkakamali sa paraang nagtuturo ng isang bagay."
    pause 1.5
    narrator "Kita-kita sa susunod na semester."
    pause 2.0

    scene black
    narrator "✦ GOOD ENDING, 'Solid Enough' ✦"
    pause 1.0
    narrator "Networking: [letter_grade(networking_grade)] | Programming: [letter_grade(programming_grade)] | Cybersecurity: [letter_grade(cyber_grade)]"
    narrator "Critical Thinking: [critical_thinking] / 100 | AI Uses: [ai_use_count]"
    call show_credits
    return

# ══════════════════════════════════════════════════════════════════════════════
# ENDING 4: REDEMPTION, "Not Yet, But Getting There"
# Condition: Any INC, CT ≥ 45 and motivation ≥ 45
# ══════════════════════════════════════════════════════════════════════════════
label ending_redemption:
    $ persistent.last_ending = "Not Yet, But Getting There"
    call screen ending_title("good", "Not Yet, But Getting There", "Nagsimula sa INC. Natapos nang wala.")

    $ safe_play("music", "audio/bgm/bgm_sad.ogg", loop=True)
    scene bg_hallway with dissolve

    narrator "(Lumabas ang grades. Isa o dalawang INC.)"
    narrator "(Nakatayo ka sa harapan ng bulletin board. Hindi ka umiiyak. Pero hindi ka rin nagsasalita.)"

    if player_gender == "male":
        mc_m "INC."
    else:
        mc_f "INC."

    if player_bestfriend == "carl":
        show carl normal at right with moveinright
        carl "Okay ka lang ba?"
        if player_gender == "male":
            mc_m "...Okay lang. Alam ko na kung bakit. 'Yun na ang difference."
        else:
            mc_f "Alam ko kung bakit nangyari ito. 'Yun ang mahalaga ngayon."
        carl "(mababa) May completion exam. Kent ang nagsabi."
        hide carl with dissolve
    else:
        show carly normal at right with moveinright
        carly "Huy. Okay ka lang ba?"
        if player_gender == "male":
            mc_m "...Okay lang. Alam ko na kung bakit. 'Yun na ang difference."
        else:
            mc_f "Hindi okay, pero alam ko kung saan nagkamali. At 'yun na ang simula ng pagbabago."
        carly "May completion exam. Handa ka ba?"
        hide carly with dissolve

    show kent happy at left with dissolve
    kent "May completion exam. Chineck ko na ang schedule. Pwede nating i-prepare."
    hide kent with dissolve

    scene bg_canteen with dissolve
    $ safe_play("music", "audio/bgm/bgm_campus.ogg", loop=True)

    narrator "(Completion exam montage. Sariling sulat na notes. Walang AI sa syntax drills.)"
    narrator "(Si Kent, nagtu-tutor sa canteen. Si Rey, tahimik na nanonood, paminsan-minsang nagko-correct ng isang mali.)"
    narrator "(Dumating ang araw ng completion exam.)"
    if player_gender == "male":
        mc_m "(Pumasok ako nang may kumpiyansa na hindi nanggaling sa shortcuts. Kumpiyansang kinita.)"
    else:
        mc_f "(Pumasok ako nang may kumpiyansa na hindi nanggaling sa shortcuts. Kumpiyansang kinita.)"

    scene black with dissolve
    narrator "(Lumabas ang revised grade. INC, removed. Passing mark.)"
    pause 1.5
    narrator "Mas matagal. Pero ngayon, kapag may nagtatanong tungkol sa VLAN configuration, o Python scope errors, o RA 10173,"
    pause 1.0
    narrator "alam mo na ang sagot."
    pause 1.0
    narrator "Alam mo, dahil ikaw mismo ang naglagay nito doon."
    pause 2.0

    scene black
    narrator "✦ REDEMPTION ENDING, 'Not Yet, But Getting There' ✦"
    pause 1.0
    narrator "Critical Thinking: [critical_thinking] / 100 | Motivation: [motivation] / 100"
    narrator "(Nagsimula sa INC. Natapos nang wala. Ganoon ang redemption.)"
    call show_credits
    return

# ══════════════════════════════════════════════════════════════════════════════
# ENDING 5: BAD, "See You Next Year"
# Condition: Any INC, CT < 45 or motivation < 45
# ════════════════════════════
label ending_bad:
    $ persistent.last_ending = "See You Next Year"
    call screen ending_title("bad", "See You Next Year", "May isa pang taon. May isa pang pagkakataon.")

    $ safe_play("music", "audio/bgm/bgm_bad_ending.ogg", loop=True)
    scene bg_hallway with dissolve

    narrator "(Ang grades screen. Isa o higit pang incomplete. Naka-flag ang enrollment system.)"
    if player_gender == "male":
        mc_m "..."
    else:
        mc_f "..."

    scene bg_canteen with dissolve
    narrator "(Nandoon ang grupo. Pero parang malayo ang usapan, kahit magkatabi lang kayo.)"
    narrator "(Tumatawa si Gabby sa isang bagay. Nagche-check ng phone si Carl. Nagdi-discuss sina Kent at Rey.)"
    if player_gender == "male":
        mc_m "(Umupo ako sa mesa. Wala akong nasabi sa buong tanghalian.)"
    else:
        mc_f "(Umupo ako sa mesa. Wala akong nasabi sa buong tanghalian.)"

    if player_gender == "male":
        mc_m "(Alam ko naman ang magiging mangyayari. Alam ko na noong simula pa lang.)"
    else:
        mc_f "(Alam ko naman. Alam ko na habang ginagawa ko ang bawat shortcut. Alam ko.)"

    narrator "(Walang tumingin sa'yo nang masama. Hindi 'yun ang sumakit. Ang sumakit, walang gustong itanong pa.)"

    scene black with dissolve
    narrator "\"See you next year.\""
    pause 2.0
    narrator "Sapat na ang kinuha ng pandemic sa iyo."
    pause 1.0
    narrator "Huwag mong hayaang umulit ang nangyari."
    pause 1.5
    narrator "May isa pang taon. May isa pang pagkakataon."
    pause 1.5

    scene black
    narrator "✦ BAD ENDING, 'See You Next Year' ✦"
    pause 1.0
    narrator "Critical Thinking: [critical_thinking] / 100 | AI Uses: [ai_use_count]"

    menu:
        "Try again. (Return to Chapter 6, sagutin nang tapat si Ms. Iva)":
            jump chapter6
        "Finish the game. (Accept the ending)":
            call show_credits
            return

    call show_credits   
    return

# ENDING 6: CAUGHT, "Academic Integrity Issue"
# Condition: got_caught == True

label ending_caught:
    $ persistent.last_ending = "Academic Integrity Issue"
    $ safe_play("music", "audio/bgm/bgm_bad_ending.ogg", loop=True)
    scene bg_classroom with pixellate

    show ms_iva disappointed at center with dissolve
    ms_iva "Ang academic integrity ay hindi lang isang patakaran. \nIto ay isang kasunduan, sa institusyon, sa mga kaklase mo, at sa sarili mo."
    ms_iva "Binigyan kita ng pagkakataon na maging tapat. Pinili mong hindi."
    hide ms_iva with dissolve

    scene bg_hallway with dissolve
    narrator "(Mas mabigat ang pakiramdam ng hallway habang lumalabas ka.)"
    narrator "(Hindi nagtatanong si Carl. Alam na niya kung may nangyari.)"
    narrator "(Mabilis lumayo si Gabby. Si Kent, tinitingnan ka, pero hindi nagsasalita.)"
    narrator "(Si Rey, lumakad palayo nang walang kibo.)"

    if player_gender == "male":
        mc_m "(Hindi naman kita nalinlang, Ms. Iva. Niloko ko lang ang sarili ko.)"
    else:
        mc_f "(Hindi kita nalinlang, Ma'am. Niloko ko ang sarili ko. Matagal na.)"

    scene black with dissolve
    narrator "\"Kailan nagiging crutch ang isang tool?\""
    pause 1.5
    narrator "Mayroon ka na palaging sagot."
    pause 1.0
    narrator "Ang problema, hindi mo ito inamin sa tamang oras."
    pause 1.5
    narrator "May susunod na pagkakataon. Hindi 'to 'yun."
    pause 2.0

    scene black
    narrator "✦ CAUGHT ENDING, 'Academic Integrity Issue' ✦"
    pause 1.0
    narrator "got_caught: True | Critical Thinking: [critical_thinking] / 100"

    menu:
        "Try again (Go back to Chapter 5, make different choices to avoid INCs)":
            jump chapter5
        "Finish the game. (Accept this ending)":
            call show_credits
            return

transform credits_scroll(duration):
    yoffset 900
    linear duration yoffset -2700

screen credits_roll(ending_name):
    modal True
    zorder 300

    frame:
        xfill True
        yfill True
        background Solid("#FAF7F3")

    vbox at credits_scroll(34.0):
        xalign 0.5
        spacing 36
        xmaximum 900

        text "[config.name!t]" size 56 color "#1F1B19" bold True xalign 0.5

        null height 20
        text "NAKAMIT MO" size 24 color "#C41230" xalign 0.5
        text "[ending_name]" size 46 color "#1F1B19" bold True xalign 0.5

        null height 50
        text "FINAL NA RESULTA" size 24 color "#C41230" xalign 0.5
        text "Networking: [letter_grade(networking_grade)]     Programming: [letter_grade(programming_grade)]     Cybersecurity: [letter_grade(cyber_grade)]" size 26 color "#2B2624" xalign 0.5
        text "Critical Thinking: [critical_thinking]/100     Motivation: [motivation]/100     AI Uses: [ai_use_count]" size 26 color "#2B2624" xalign 0.5

        null height 70
        text "Project by Group 8:" size 24 color "#C41230" xalign 0.5
        text "Clarin, Kylle Benedict" size 30 color "#2B2624" xalign 0.5
        text "Cecilio, Neil Ayangel C." size 30 color "#2B2624" xalign 0.5
        text "Morgan, Christian David F." size 30 color "#2B2624" xalign 0.5

        null height 50
        text "TECHNICAL ADVISER" size 22 color "#C41230" xalign 0.5
        text "Engr. Ernie Lee E. Pineda, MIT" size 28 color "#2B2624" xalign 0.5

        text "CAPSTONE INSTRUCTOR / DEAN, ICS" size 22 color "#C41230" xalign 0.5
        text "Engr. Dennis L. Tacadena, DIT" size 28 color "#2B2624" xalign 0.5

        null height 50
        text "Mabalacat City College" size 26 color "#6B6259" xalign 0.5
        text "Institute of Computing Studies, 2026" size 26 color "#6B6259" xalign 0.5

        null height 90
        text "{i}Salamat sa paglalaro. Sana, kahit konti, may natutunan ka rin.{/i}" size 28 color "#1F1B19" xalign 0.5

        null height 250

    text "I-click o pindutin ang kahit anong key para mag-skip" xalign 0.5 yalign 0.95 size 20 color "#E3DBD2"

    timer 36.0 action Return()

    key "K_RETURN" action Return()
    key "K_SPACE"  action Return()
    key "K_ESCAPE" action Return()
    button:
        xfill True
        yfill True
        action Return()
        background None

label show_credits:
    scene black with dissolve
    $ show_hud = False
    call screen credits_roll(persistent.last_ending)
    return