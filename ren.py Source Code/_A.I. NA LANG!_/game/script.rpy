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
    show text "{color=#1f6feb}{size=40}{cps=30}> v1.3  loading...{/cps}{/color}" at truecenter with dissolve
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
        "Si Carl ang bestfriend":
            $ player_bestfriend = "carl"
        "Si Carly ang bestfriend":
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
label start:
label prologue:
    $ show_hud = True
    scene black with fade
    pause 0.6

    narrator "(Bago tayo magsimula...)"
    pause 0.4
    narrator "(Sino ka sa kwentong ito?)"

    menu:
        "Alex. 'Basta mai-submit ko, okay na.'":
            $ player_gender = "male"
            $ player_name   = "Alex"
        "Alexa. 'Marami nang pinagdaanan. Pero nandito pa rin.'":
            $ player_gender = "female"
            $ player_name   = "Alexa"

    narrator "(Ano'ng itatawag sa'yo ng ibang tao?)"

    menu:
        "Gusto ko ng ibang pangalan (Custom name, 20 characters max only)":
            $ raw_name = renpy.input("Pangalan:", default=player_name, length=20)
            $ player_name = raw_name.strip() if raw_name.strip() else player_name
        "[player_name] na lang":
            pass

    pause 0.6
    $ safe_stop("music")
    $ safe_play("music", "audio/bgm/bgm_sad.ogg", loop=True)

    pause 0.6
    narrator "Online Classes, 2020."
    pause 0.4

    scene bg_bedroom_night with dissolve
    pause 1.0

    if player_gender == "male":
        mc_m "(Alas-tres na ng umaga. Parehong error, kanina pa naka-highlight.)"
        mc_m "(Red squiggly lines. Ayaw talagang sumuko.)"
        mc_m "(Nakakainis.)"
    else:
        mc_f "(Alas-tres na ng umaga. Parehong error, kanina pa naka-highlight.)"
        mc_f "(Red squiggly lines. Ayaw talagang sumuko.)"
        mc_f "(Nakakainis.)"
    pause 1.0

    play sound "audio/sfx/sfx_phone.ogg"
    if player_gender == "male":
        mc_m "(May assignment tab akong nakabukas simula pa kanina. Ayokong buksan.)"
        mc_m "(Pero alas-tres na. May klase pa bukas.)"
        mc_m "(Binuksan ko rin. Ayoko ma late submission.)"
    else:
        mc_f "(May assignment tab akong nakabukas simula pa kanina. Ayokong buksan.)"
        mc_f "(Pero alas-tres na. May klase pa bukas.)"
        mc_f "(Binuksan ko rin. Ayoko ma late submission.)"
    pause 0.6

    scene bg_zoom with fade
    pause 0.5
    ai_voice "I can help with that."
    pause 1.0
    ai_voice "Complete solution generated. All answers provided."
    pause 1.2
    ai_voice "Submit this solution."
    hide bg_zoom with dissolve

    $ tutorial_highlight = "ct"
    $ renpy.notify("Critical Thinking -15 {color=#58a6ff}TUTORIAL{/color}")
    pause 0.4

    sys_voice "{color=#58a6ff}TUTORIAL{/color} Kung makikita mo sa taas. 'Yung Critical Thinking bar mo.\nYan ay bumababa tuwing binibigay mo sa AI ang pag-iisip. Tumataas kapag ikaw talaga ang gumawa."
    $ show_hud = True

    pause 2.0
    $ tutorial_highlight = None

    if player_gender == "male":
        mc_m "(Sampung segundo. Kumpleto na.)"
        mc_m "(Tama lahat. Mas ayos pa sa kahit anong gagawin sa isang linggo.)"
        mc_m "(Kinopya ko. I-paste. Submit.)"
        mc_m "(Tapos natulog na.)"
    else:
        mc_f "(Sampung segundo. Kumpleto na.)"
        mc_f "(Tama lahat. Mas ayos pa sa kahit anong gagawin sa isang linggo.)"
        mc_f "(Kinopya ko. I-paste. Submit.)"
        mc_f "(Tapos natulog na.)"
    pause 0.8
    narrator "{cps=15}Unang beses sa mahabang panahon, walang kasamang guilt yung antok.{/cps}"
    pause 1.5

    if player_gender == "male":
        mc_m "(Isa lang naman ito. Hindi na mauulit.)"
        mc_m "(May tanong akong hindi ko masagot. Simula pa noon.)"
    else:
        mc_f "(Isa lang naman ito. Hindi na mauulit.)"
        mc_f "(May tanong akong hindi ko masagot. Simula pa noon.)"
    pause 1.8

    scene black with dissolve
    pause 1.0

    scene bg_zoom with dissolve
    pause 1.0
    narrator "Parang chat na hindi mo na-scroll pero laging bukas."
    pause 0.8

    groupchat "CLASSMATE1: hehe same, di ko rin na-gets 'yung discussion kanina"
    pause 0.4
    groupchat "CLASSMATE2: cam off muna ko, ang log dito eh"
    pause 0.4
    groupchat "CLASSMATE3: sino may notes? di ko na-catch buong lecture"
    pause 0.8

    menu:
        "(Typing) same guys, di rin gumagana mic ko HAHA":
            groupchat "[player_name]: same guys, di rin gumagana mic ko HAHA"
        "(Typing) ...":
            groupchat "[player_name]: ... (nonchlant)"

    pause 0.8
    hide bg_zoom with dissolve

    narrator "Dalawang linggo lang daw. Parang extended na break. Sarap."
    pause 0.6
    narrator "Ikaapat na buwan, camera off na palagi."
    pause 0.6
    if player_gender == "male":
        mc_m "(Wala namang magtatanong. Ganito na lahat.)"
    else:
        mc_f "(Wala namang magtatanong. Ganito na lahat.)"
    pause 1.0

    narrator "Anim na buwan. Isang taon. Dalawa."
    pause 0.8
    narrator "Paper? Nagawa na niya. Program? Tapos na. May module kang hindi maintindihan?\nPaulit-ulit niyang ipapaliwanag, walang pagod, walang reklamo."
    pause 1.0
    if player_gender == "male":
        mc_m "(At ako? Tulog na.)"
        mc_m "('Pansamantala lang 'to. Survival mode lang naman eh.')"
    else:
        mc_f "(At ako? Tulog na.)"
        mc_f "('Pansamantala lang 'to. Survival mode lang naman eh.')"
    pause 1.2
    narrator "{cps=14}Inulit mo 'yun ilang beses hanggang sa naniwala ka na rin.{/cps}"
    pause 1.8

    $ safe_stop("music")
    pause 1.2

    narrator "Tapos, biglang natapos na rin."
    pause 0.8
    narrator "Bumalik ang klase. Bumalik ang campus. Bumalik na daw ang 'normal.'"
    pause 1.2

    if player_gender == "male":
        mc_m "(Pero may tanong na bumabalik tuwing tahimik ang paligid.)"
        mc_m "(Kung may magtatanong bukas ng kahit ano sa course or sa subjects ko...)"
        mc_m "Kaya ko ba 'to sagutin, gamit lang ang sarili ko lang?"
    else:
        mc_f "(Pero may tanong na bumabalik tuwing tahimik ang paligid.)"
        mc_f "(Kung may magtatanong bukas ng kahit ano sa course or sa subjects ko...)"
        mc_f "Kaya ko ba 'to sagutin, gamit lang ang sarili ko lang?"
    pause 2.2

    narrator "..."
    pause 2.0

    $ tutorial_highlight = "mot"
    $ renpy.notify("Motivation -10 {color=#58a6ff}TUTORIAL{/color}")
    sys_voice "{color=#58a6ff}TUTORIAL{/color} 'Yung puso sa kabila, Motivation mo. Bumababa 'yan sa panic o guilt. Tumataas kapag may confidence ka sa sarili mo."
    pause 2.0
    $ tutorial_highlight = None

    if player_gender == "male":
        mc_m "(Hindi ko alam kung gaano karami sa 'natutunan' ko ang tunay na akin.)"
    else:
        mc_f "(Hindi ko alam kung gaano karami sa 'natutunan' ko ang tunay na akin.)"
    pause 1.2
    narrator "Pero."
    pause 0.8
    narrator "Hindi ka naman talaga nag-iisa dito."
    pause 0.6
    narrator "May isang tao."
    pause 0.6
    narrator "Hindi niya man maintindihan lahat, pero nandiyan siya. Palagi."
    pause 1.5

    scene bg_campus_gate with dissolve
    $ safe_play("music", "audio/bgm/bgm_campus.ogg", loop=True)
    pause 1.2

    narrator "Fourth year kana. Unang araw. Nakatayo ka sa labas ng gate."
    pause 0.6
    if player_gender == "male":
        mc_m "(Alam ko naman on paper. Pumasok, umupo, matuto.)"
        mc_m "(Pero ngayon, na nasa harap na harap ako na nang pinto, may parte ng utak ko nagsasabi:)"
        mc_m "('Kung lalabas 'yung totoo, baka hindi mo kaya 'to.')"
    else:
        mc_f "(Alam ko naman on paper. Pumasok, umupo, matuto.)"
        mc_f "(Pero ngayon, na nasa harap na harap ako na nang pinto, may parte ng utak ko nagsasabi:)"
        mc_f "('Kung lalabas 'yung totoo, baka hindi mo kaya 'to.')"
    pause 1.2
    narrator "Tapos may tumapik sa balikat mo." with hpunch
    pause 1.5

    menu:
        "Carl. Kamay sa bulsa. Parang dalawang oras lang natulog.":
            $ player_bestfriend = "carl"
        "Carly. Nakangiti na bago ka pa lumingon.":
            $ player_bestfriend = "carly"
    if player_bestfriend == "carl":
        show carl happy at center with dissolve
        carl "Uy. Nandito ka rin pala."
        if player_gender == "male":
            mc_m "(Ganoon pa rin siya. Parang walang nagbago kahit lumipas yung dalawang taon.)"
        else:
            mc_f "(Napabuntong-hininga ako, nang hindi ko namamalayan.)"
        carl "Parang kasing-antok kita ah. Ano, nag-rank ka ba buong gabi? Mythic ka na ba?"
        if player_gender == "male":
            mc_m "Sana all. Wala akong energy pang mag-ML, boss."
        else:
            mc_f "Sana all. Puyat lang talaga, wala akong energy pang mag-ML."
        carl "G na. Ayoko nang mahuli sa first day na 'to."
        narrator "(Lumakad siya nang walang atubili. Sinundan mo, gaya ng dati.)"
        narrator "(Ngayon lang gusto mong ikaw mismo ang pumili kung saan ka patungo.)"
        hide carl with dissolve
    else:
        show carly happy at center with dissolve
        carly "Uy! Nandito ka na!"
        if player_gender == "male":
            mc_m "(Bigla na lang gumaan yung pakiramdam ko.)"
        else:
            mc_f "(Nakita ko lang siya, parang magkaklase ulit kami?)"
        carly "Parang hindi ka natulog ah. Okay ka lang?"
        if player_gender == "male":
            mc_m "Okay naman. Medyo."
        else:
            mc_f "Oo. I think so. Nandito naman ako."
        carly "Okay. Sapat na 'yon. Tara na."
        narrator "(Lumakad kayong magkasabay. Unang beses ngayong umaga na hindi ka nag-iisa.)"
        hide carly with dissolve

    pause 1.0
    $ tutorial_highlight = "all"
    $ renpy.notify("Day 1 starting")
    sys_voice "{color=#58a6ff}TUTORIAL{/color} Sa taas, palaging makikita kung anong araw na, ang grado mo sa tatlong subject, ang Critical Thinking bar, at ang Motivation bar mo."
    pause 0.4
    sys_voice "{color=#58a6ff}TUTORIAL{/color} Walang tama o maling sagot agad-agad dito. Pero may bigat ang bawat desisyon mong pinili, in due time."
    pause 1.5
    $ tutorial_highlight = None

    if player_gender == "male":
        mc_m "(First day. Na naman.)"
        mc_m "(Pero ngayon, may isang bagay na gusto kong sagutan nang tama.)"
        mc_m "{cps=14}(Hindi para sa grado. Kundi para sa sarili ko.){/cps}"
    else:
        mc_f "(First day. Na naman.)"
        mc_f "(Pero ngayon, may isang bagay na gusto kong sagutan nang tama.)"
        mc_f "{cps=14}(Hindi para sa grado. Kundi para sa sarili ko.){/cps}"
    pause 1.6

    $ show_hud = False
    jump chapter1

label ai_used_result:
    $ ai_use_count += 1
    narrator "Ginamit mo ang AI para sagutin ito."
    return