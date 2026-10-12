label splashscreen:
    $ renpy.music.stop(fadeout=0.0)
    scene black
    pause 0.5

    play sound "audio/sfx/sfx_phone.ogg"
    show text "{color=#C41230}{size=40} Mabalacat City College\nInstitute of Computing Studies, 2026{/size}{/color}" at truecenter with dissolve
    pause 1.2
    hide text with dissolve
    pause 1.2

    play sound "audio/sfx/sfx_click.ogg"
    show text "{color=#1f6feb}{size=40}{cps=30}> A.I. na lang!  Defense Build  loading...{/cps}{/color}" at truecenter with dissolve
    pause 1.2
    hide text

    play sound "audio/sfx/sfx_click.ogg"
    show text "{color=#56d364}{size=40}{cps=40}> OK. All modules initialized.{/cps}{/color}" at truecenter with dissolve
    pause 1.2
    hide text
    return
label extras_setup:
    $ raw_name = renpy.input("I see, you've been here before na.\nAnong pangalan ang nais mong gagamitin?", default=player_name, length=20)
    $ player_name = raw_name.strip() if raw_name.strip() else player_name

    menu:
        "Male (Alex)":
            $ player_gender = "male"
        "Female (Alexa)":
            $ player_gender = "female"

    menu:
        "Carl ang bestfriend":
            $ player_bestfriend = "carl"
        "Carly ang bestfriend":
            $ player_bestfriend = "carly"

    narrator "Sa puntong ito ng kwento, kumusta ang naging takbo ng buhay-eskwela mo? (this may affect the ending of the story.)"

    menu:
        "Doing well!  (mataas ang grades, kaunti lang ang AI use)":
            $ critical_thinking = 85
            $ motivation = 85
            $ networking_grade = 88
            $ programming_grade = 88
            $ cyber_grade = 88
            $ ai_use_count = 0
            $ got_caught = False

        "Average  (basta, minsan may AI-assist)":
            $ critical_thinking = 55
            $ motivation = 55
            $ networking_grade = 68
            $ programming_grade = 68
            $ cyber_grade = 68
            $ ai_use_count = 2
            $ got_caught = False

        "Not too well  (hala ka, almost always uses AI)":
            $ critical_thinking = 25
            $ motivation = 30
            $ networking_grade = 55
            $ programming_grade = 55
            $ cyber_grade = 55
            $ ai_use_count = 7
            $ got_caught = False

    $ show_hud = True

    jump expression _extras_target


# PROLOGUE
## Restructured for the defense build: shorter cold open, HUD revealed only
## when it is explained, the bars really move during the flashback and are
## reset at the campus gate (so the Alpha/Beta balance is unchanged).
default mc = mc_m   # set for real after the gender choice; default keeps lint/loads happy
default pro_ct_base  = 50
default pro_mot_base = 50

label start:
label prologue:
    $ show_hud = False
    $ day_label = "2020, Online"
    scene black with fade
    pause 0.6

    narrator "(Sino ka sa kwentong ito?)"

    menu:
        "Alex. 'Basta mai-submit ko, okay na.'":
            $ player_gender = "male"
            $ player_name   = "Alex"
        "Alexa. 'Marami nang pinagdaanan. Pero nandito pa rin.'":
            $ player_gender = "female"
            $ player_name   = "Alexa"

    $ mc = mc_m if player_gender == "male" else mc_f

    $ raw_name = renpy.input(_("Ano'ng itatawag sa'yo ng ibang tao?"), default=player_name, length=20)
    $ player_name = raw_name.strip() if raw_name.strip() else player_name

    ## ---- COLD OPEN: 3 AM, 2020 ----
    $ safe_stop("music")
    $ safe_play("music", "audio/bgm/bgm_sad.ogg", loop=True)
    call screen chapter_title("", "Prologue : Copy-Paste", "Online Classes, 2020, 'Isang beses lang naman.'")

    scene bg_bedroom_night with dissolve
    pause 0.8
    mc "(Alas-tres na ng umaga. Parehong error, kanina pa naka-highlight. Ayaw talagang sumuko.)"
    play sound "audio/sfx/sfx_phone.ogg"
    mc "(May assignment tab akong nakabukas simula pa kanina. Ayokong buksan.)"
    mc "(Binuksan ko rin. Ayoko ma-late submission.)"

    scene bg_zoom with fade
    pause 0.4
    ai_voice "I can help with that."
    show cg_ai_chat with zoomin
    pause 0.8
    ai_voice "Complete solution generated. All answers provided."
    hide cg_ai_chat with dissolve
    ai_voice "Submit this solution."
    ai_voice "Walang makakaalam. Promise. (Maliban sa'yo na nagbabasa nito. Hi.)"
    mc "(...Sino ba 'yung kausap mo?)"

    ## HUD reveal + the first real drop of the Critical Thinking bar
    $ pro_ct_base  = critical_thinking
    $ pro_mot_base = motivation
    $ show_hud = True
    $ tutorial_highlight = "ct"
    $ ct_change(-15)
    $ renpy.notify("Critical Thinking -15 {color=#58a6ff}TUTORIAL{/color}")
    pause 0.4
    sys_voice "{color=#58a6ff}TUTORIAL{/color} Kung makikita mo sa taas. 'Yung Critical Thinking bar mo.\nYan ay bumababa tuwing binibigay mo sa AI ang pag-iisip. Tumataas kapag ikaw talaga ang gumawa."
    pause 1.2
    $ tutorial_highlight = None

    mc "(Sampung segundo. Kumpleto na.)"
    mc "(Tama lahat. Mas ayos pa sa kahit anong gagawin sa isang linggo.)"
    mc "(Kinopya ko. I-paste. Submit.)"
    narrator "{cps=15}Unang beses sa mahabang panahon, walang kasamang guilt yung antok.{/cps}"
    pause 1.0
    mc "(Isa lang naman ito. Hindi na mauulit.)"
    pause 1.2

    ## ---- THE NEW NORMAL ----
    scene black with dissolve
    pause 0.6
    scene bg_zoom with dissolve
    groupchat "CLASSMATE1: hehe same, di ko rin na-gets 'yung discussion kanina"
    groupchat "CLASSMATE2: cam off muna ko, ang lag dito eh"
    groupchat "CLASSMATE3: sino may notes? di ko na-catch buong lecture"
    pause 0.6

    menu:
        "(Typing) same guys, di rin gumagana mic ko HAHA":
            groupchat "[player_name]: same guys, di rin gumagana mic ko HAHA"
            groupchat "CLASSMATE1: HAHAHA solid. buti hindi ako nag-iisa"
        "(Typing) ...":
            groupchat "[player_name]: ... (nonchalant)"
            groupchat "CLASSMATE3: huy [player_name], buhay ka pa ba"

    pause 0.6
    hide bg_zoom with dissolve
    narrator "Dalawang linggo lang daw. Parang extended na break. Sarap."
    pause 0.5
    narrator "Anim na buwan. Isang taon. Dalawa."
    $ ct_change(-10)
    pause 0.6
    narrator "Paper? Nagawa na niya. Program? Tapos na. May module kang hindi maintindihan?\nPaulit-ulit niyang ipapaliwanag, walang pagod, walang reklamo."
    mc "(At ako? Tulog na.)"
    narrator "{cps=14}Inulit mo 'yun ilang beses hanggang sa naniwala ka na rin.{/cps}"
    pause 1.2

    $ safe_stop("music")
    pause 0.8
    narrator "Bumalik ang klase. Bumalik ang campus. Bumalik na daw ang 'normal.'"
    pause 0.8
    mc "(Pero may tanong na bumabalik tuwing tahimik ang paligid.)"
    mc "(Kung may magtatanong bukas ng kahit ano sa course or sa subjects ko...)"
    mc "Kaya ko ba 'to sagutin, gamit lang ang sarili ko?"
    pause 1.5
    narrator "Kung hindi ka IT, huwag kang mag-alala. Oo, may mga tanong dito tungkol sa network at code, pero setting lang 'yun, hindi ang punto."
    narrator "Ang totoong tanong: kapag may sagot nang nakahanda, titigil ka pa ba para mag-isip?"
    narrator "Estudyante ka man, empleyado, o magulang na nagche-check ng takdang-aralin ng anak mo, para sa'yo rin 'to."
    pause 1.0

    $ tutorial_highlight = "mot"
    $ mot_change(-10)
    $ renpy.notify("Motivation -10 {color=#58a6ff}TUTORIAL{/color}")
    sys_voice "{color=#58a6ff}TUTORIAL{/color} 'Yung puso sa kabila, Motivation mo. Bumababa 'yan sa panic o guilt. Tumataas kapag may confidence ka sa sarili mo."
    pause 1.2
    $ tutorial_highlight = None
    mc "(Hindi ko alam kung gaano karami sa 'natutunan' ko ang tunay na akin.)"
    pause 0.8
    narrator "Hindi ka naman talaga nag-iisa dito. Hindi niya man maintindihan lahat, pero nandiyan siya. Palagi."
    pause 1.0

    ## ---- DAY ONE: CAMPUS GATE ----
    scene bg_campus_gate with dissolve
    $ day_label = "Day 1, Umaga"
    $ safe_play("music", "audio/bgm/bgm_campus.ogg", loop=True)
    pause 0.8
    narrator "Fourth year ka na. Unang araw. Nakatayo ka sa labas ng gate."
    mc "(Alam ko naman on paper. Pumasok, umupo, matuto. Pero ngayong nasa harap na ako ng pinto, may parte ng utak ko na nagsasabi:)"
    mc "('Kung lalabas 'yung totoo, baka hindi mo kaya 'to.')"
    pause 0.8
    narrator "Tapos may tumapik sa balikat mo." with hpunch
    pause 1.0

    menu:
        "Carl. Kamay sa bulsa. Parang dalawang oras lang natulog.":
            $ player_bestfriend = "carl"
        "Carly. Nakangiti na bago ka pa lumingon.":
            $ player_bestfriend = "carly"
    if player_bestfriend == "carl":
        show carl happy at center, enter_right
        carl "Uy. Nandito ka rin pala."
        if player_gender == "male":
            mc "(Ganoon pa rin siya. Parang walang nagbago kahit lumipas yung dalawang taon.)"
        else:
            mc "(Napabuntong-hininga ako, nang hindi ko namamalayan.)"
        carl "Parang kasing-antok kita ah. Ano, nag-rank ka ba buong gabi? Mythic ka na ba?"
        if player_gender == "male":
            mc "Sana all. Wala akong energy pang mag-ML, boss."
        else:
            mc "Sana all. Puyat lang talaga, wala akong energy pang mag-ML."
        carl "G na. Ayoko nang mahuli sa first day na 'to."
        narrator "(Lumakad siya nang walang atubili. Sinundan mo, gaya ng dati.)"
        narrator "(Ngayon lang gusto mong ikaw mismo ang pumili kung saan ka patungo.)"
        hide carl with dissolve
    else:
        show carly happy at center, enter_right
        carly "Uy! Nandito ka na!"
        if player_gender == "male":
            mc "(Bigla na lang gumaan yung pakiramdam ko.)"
        else:
            mc "(Nakita ko lang siya, parang magkaklase ulit kami?)"
        show carly normal at center with quickfade
        carly "Parang hindi ka natulog ah. Okay ka lang?"
        if player_gender == "male":
            mc "Okay naman. Medyo."
        else:
            mc "Oo. I think so. Nandito naman ako."
        show carly happy at center, hop
        carly "Okay. Sapat na 'yon. Tara na."
        narrator "(Lumakad kayong magkasabay. Unang beses ngayong umaga na hindi ka nag-iisa.)"
        hide carly with dissolve

    ## ---- FRESH START: bars go back to where they were, then the full HUD tour ----
    pause 0.8
    $ critical_thinking = pro_ct_base
    $ motivation = pro_mot_base
    narrator "Bagong semester. Bumalik sa gitna ang mga bar. Ang nakasanayan, hindi."
    $ tutorial_highlight = "all"
    $ renpy.notify("Day 1 starting")
    sys_voice "{color=#58a6ff}TUTORIAL{/color} Sa taas, palaging makikita kung anong araw na, ang Critical Thinking bar, at ang Motivation bar mo. Pindutin ang 'Tingnan ang Grades' para makita ang grado mo sa tatlong subject."
    pause 0.4
    sys_voice "{color=#58a6ff}TUTORIAL{/color} Walang tama o maling sagot agad-agad dito. Pero may bigat ang bawat desisyon mong pinili, in due time."
    pause 1.2
    $ tutorial_highlight = None

    mc "(First day. Na naman.)"
    mc "(Pero ngayon, may isang bagay na gusto kong sagutan nang tama.)"
    mc "{cps=14}(Hindi para sa grado. Kundi para sa sarili ko.){/cps}"
    pause 1.6

    $ show_hud = False
    jump chapter1


label ai_used_result:
    ## AI is the core mechanic, so it gets its own moment (screens in ui_polish.rpy).
    ## This label is the ONE place that counts an AI answer.
    $ ai_use_count += 1
    play sound "audio/sfx/sfx_phone.ogg"
    with vpunch
    call screen ai_used_overlay
    return
