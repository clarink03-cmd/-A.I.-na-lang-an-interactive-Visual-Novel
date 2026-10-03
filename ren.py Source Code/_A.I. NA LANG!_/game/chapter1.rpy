## game/chapter1.rpy
## Chapter 1, "Day One Vibes" (Week 1)

label chapter1:
    call screen chapter_title("", "1 : Day One na?", "Week 1, 'Sana ol, may motivation.'")
    if _preferences.skip_unseen:
        $ renpy.get_screen("skip_indicator") or None
    $ day_label = "Week 1, Umaga"
    $ current_week = 1

## ── SCENE 1-1: First Day, Classroom ──────────────────────────────────────
    scene bg_classroom with dissolve
    $ safe_play("music", "audio/bgm/bgm_campus.ogg", loop=True)
    $ show_hud = True

    if player_gender == "male":
        mc_m "(First day ng semester. Alam ko na ang drill: pumasok, humanap ng upuan na hindi sa harap, pero hindi rin masyadong sa likod.)"
        mc_m "(Walang gustong maging taga-sagot ng katok sa pinto.)"
        mc_m "(Umupo ako sa gitna. 'Yung pwede na zone. Hindi ka masyadong nakikita, pero hindi ka rin nawawala.)"
        mc_m "(Amoy cables. At 'yung specific na brand ng panic na alam kong tatagal ng isang buong semester.)"
    else:
        mc_f "(First day ng semester. Alam ko na ang drill: pumasok, humanap ng upuan na hindi sa harap, pero hindi rin masyadong sa likod.)"
        mc_f "(Walang gustong maging taga-sagot ng katok sa pinto.)"
        mc_f "(Umupo ako sa gitna. 'Yung pwede na zone. Hindi ka masyadong nakikita, pero hindi ka rin nawawala.)"
        mc_f "(Amoy cables. At 'yung specific na brand ng panic na alam kong tatagal ng isang buong semester.)"

    show gabby normal at center with dissolve
    gabby "UY! Guys! Tayo na naman magkakaklase!"
    gabby "Sabog na naman tayo this sem!"

    show kent happy at left with dissolve
    kent "Technically, hindi tayo group. Cluster tayo ng mga individual na \nnagkataong parehas ang enrollment block. Pero yes, emotionally speaking, group tayo."
    gabby "Kent."
    gabby "Minsan gusto kita sapakin."
    kent "That would be an inefficient use of your kinetic energy.\n Pero appreciated ang sentiment, po."

    if player_bestfriend == "carl":
        show carl normal at right with dissolve
        carl "(sabay upo sa tabi mo) Huy. Na-review mo na ba syllabus?"
        if player_gender == "male":
            mc_m "Meron na palang syllabus?"
        else:
            mc_f "Meron na palang syllabus?"
        carl "(tawa) Classic. Ayos lang 'yan. Basta magkaklase tayo, keri na."
        carl "Saka sabi ni Gabby, madami raw breaks this sem. \nParang nag-design si Ms. Iva ng calendar para sa mga gustong matulog."
        kent "Actually, na-compute ko na 'yung break distribution.\nMay total na 14 non-instructional days sa buong semester, hindi pa kasama ang holidays. Above national average 'yan para sa IT programs."
        gabby "See! Sabi ko sa inyo! Break tayo nang break!"
        carl "(sa iyo, mababa) Ginawang research paper ni Kent 'yung enrollment natin."
        hide carl with dissolve
    else:
        show carly normal at right with dissolve
        carly "(sabay upo sa tabi mo) Huy! Same block tayo! Sabi ko na eh. Magkaklase ulit tayo."
        if player_gender == "male":
            mc_m "Buti na lang. Kung hindi, wala akong kausap."
        else:
            mc_f "Buti na lang. Kung hindi, wala akong karamay."
        carly "Totoo!"
        carly "Sabi ni Gabby, maraming breaks daw this sem. Baka ma-enjoy ko pa 'tong IT."
        kent "Actually, na-compute ko na 'yung break distribution.\nMay total na 14 non-instructional days sa buong semester, hindi pa kasama ang holidays. Above national average 'yan para sa IT programs."
        gabby "See! Panalo tayo!"
        carly "(sa iyo, mababa) Ginawa ni Kent na Excel sheet 'yung buong semester natin."
        hide carly with dissolve

    show kent normal at left with dissolve
    kent "Anyway. May nilista akong tips para sa first day. Isang page lang naman. 8-point font."
    gabby "Isang PAGE? Kent, first day pa lang. Chill."
    kent "May pie chart din. Para sa motivation."
    gabby "...Sige, i-send mo sa GC."
    kent "Na-send ko na noong 6:47 AM."
    if player_gender == "male":
        mc_m "(Tiningnan ang phone. May notification nga mula sa group chat: \nisang PDF, title na 'SEMESTER OPTIMIZATION GUIDE v1.3.')"
        mc_m "(v1.3. Ibig sabihin, dalawang beses niya na 'to na-update bago pa man magsimula ang klase.)"
    else:
        mc_f "(Tiningnan ang phone. May notification nga mula sa group chat: \nisang PDF, title na 'SEMESTER OPTIMIZATION GUIDE v1.3.')"
        mc_f "(v1.3. Ibig sabihin, dalawang beses niya na 'to na-update bago pa man magsimula ang klase.)"

    show rey normal at right with dissolve
    if player_gender == "male":
        mc_m "(Pumasok si Rey. Walang ingay na pagbati,\n dumeretso lang sa tabi ng bintana, kinuha ang notebook, nagbasa.)"
    else:
        mc_f "(Pumasok si Rey. Walang ingay na pagbati\n dumeretso lang sa tabi ng bintana, kinuha ang notebook, nagbasa.)"
    narrator "(Ilan sa inyo, kasama si Kent, ay napatingin sa kanya nang matagal.)"
    gabby "(bulong) Si Rey, seryoso agad. First day pa lang, ang tense na."
    kent "(bulong) Actually, hinahangaan ko 'yung preparedness. Yan, that's what I call a pro-gamer move."
    rey "Guys... naririnig ko kayo."
    gabby "Sorry sorry."
    kent "No regrets. Angas mo, men. *thumbs up*"
    rey "(tumingin sandali sa pinto, tapos bumalik sa notebook) ...Wala. Continue lang kayo."
    if player_gender == "male":
        mc_m "(Isang segundo lang, pero napansin ko. Parang may hinihintay siyang hindi darating.)"
    else:
        mc_f "(Isang segundo lang, pero napansin ko. Parang may hinihintay siyang hindi darating.)"

    if player_gender == "male":
        mc_m "(Tumawa ako nang tahimik. Ganito pala ulit: yung energy na sabay kang napapagod at napapasaya.)"
    else:
        mc_f "(Tumawa ako nang tahimik. Ganito pala ulit: yung energy na sabay kang napapagod at napapasaya.)"

    hide gabby with dissolve
    hide kent with dissolve
    hide rey with dissolve

    ## Ms. Iva enters
    $ safe_stop("music")
    $ safe_play("music", "audio/bgm/bgm_tension.ogg", loop=True)
    show ms_iva thinking at center with dissolve

    ms_iva "Good morning, everyone. \nAko si Ms. Iva, ang instructor niyo this semester. Sana kasing-excited niyo ako para dito."
    ms_iva "Hindi na tayo mag-aaksaya ng oras sa introductions. Alam ko na magkakakilala na kayo."
    ms_iva "At sawang-sawa na kayo sa isa't isa, malamang. Kaya diretso na tayo."
    ms_iva "Gusto kong pag-usapan ngayon 'yung isang bagay na \nginagamit niyo na lahat, simula pa noong high school niyo."
    narrator "(Nagsulat siya sa board: ARTIFICIAL INTELLIGENCE.)"
    ms_iva "Ang AI ay isang tool. Sigurado ako alam na ninyong lahat kung ano 'to."
    ms_iva "Ang tanong ko sa inyo, at gusto kong seryosohin niyo 'to:"
    ms_iva "Kailan nagiging crutch ang isang tool?"

    if player_gender == "male":
        mc_m "(Tahimik ang buong room. May kumalabog sa loob ko na hindi ko alam kung paano tatawagin.)"
    else:
        mc_f "(Tahimik ang buong room. May kumalabog sa loob ko na hindi ko alam kung paano tatawagin.)"

    show gabby normal at right with dissolve
    if player_bestfriend == "carl":
        show carl normal at left with dissolve
        gabby "(bumubulong) Grabe, yan na agad. Lecture agad, first day pa lang."
        carl "(bumubulong) Shh."
    else:
        show carly normal at left with dissolve
        gabby "(bumubulong) Grabe, yan na agad. Lecture agad, first day pa lang."
        carly "(bumubulong) Shh."

    ms_iva "Sa katapusan ng semester na 'to, \numaasa akong masasagot niyo 'yung tanong na 'yon. Hindi para sa akin. Para sa inyo."
    hide ms_iva with dissolve
    if player_bestfriend == "carl":
        hide carl with dissolve
    else:
        hide carly with dissolve
    hide gabby with dissolve

    if player_gender == "male":
        mc_m "(Nagpatuloy ang klase, pero hindi ko na masyadong naririnig. \nPaulit-ulit lang sa isip ko 'yung tanong niya. Kailan ba talaga nagiging crutch ang isang tool?)"
    else:
        mc_f "(Nagpatuloy ang klase, pero hindi ko na masyadong naririnig. \nPaulit-ulit lang sa isip ko 'yung tanong niya. Kailan ba talaga nagiging crutch ang isang tool?)"

    ## ── SCENE 1-2: Canteen after class ───────────────────────────────────────
    scene bg_canteen with dissolve
    $ safe_play("music", "audio/bgm/bgm_canteen.ogg", loop=True)
    $ day_label = "Day 1, Hapon"

    narrator "Nahanap ng grupo ang mesa. Tray ng kanin, ulam, malamig na inumin. Ang universal na college meal."
    show gabby normal at left with dissolve
    if player_bestfriend == "carl":
        show carl normal at right with dissolve
    else:
        show carly normal at right with dissolve
    show kent normal at center with dissolve

    gabby "Hoy, 'yung sinabi ni Ms. Iva kanina, grabe ang O.A. Obvious naman kung sino tinutukoy nun."
    kent "Actually, tinutukoy niya 'yung isang documented na phenomenon sa cognitive science. \nSkill atrophy. Paulit-ulit mong i-externalize ang isang cognitive task sa isang tool, 'yung neural pathway na dapat mag-ha-handle nun ay,"
    gabby "Kent. Kumain ka muna."
    kent "...Valid pa rin ang concern ko."

    if player_bestfriend == "carl":
        carl "Bakit ka tahimik? Masyado kang quiet kanina."
        if player_gender == "male":
            mc_m "Naiisip ko lang 'yung sinabi ni Ms. Iva. Alam mo naman 'yung nangyari noong online classes."
        else:
            mc_f "Naiisip ko lang 'yung sinabi ni Ms. Iva. Alam mo naman 'yung nangyari noong online classes."
        carl "(mas seryoso) Oo. Lahat naman tayo gumawa ng shortcuts noon. Wala tayong choice eh."
    else:
        carly "Huy, ano meron sa'yo? Masyado kang tahimik kanina."
        if player_gender == "male":
            mc_m "Naiisip ko lang 'yung sinabi ni Ms. Iva. Alam mo naman 'yung nangyari noong online classes."
        else:
            mc_f "Naiisip ko lang 'yung sinabi ni Ms. Iva. Alam mo naman 'yung nangyari noong online classes."
        carly "(mas seryoso) Oo. Lahat naman tayo gumawa niyon. Pero iba na ngayon, 'di ba? Face-to-face na tayo."

    if player_gender == "male":
        mc_m "Pero may choice naman tayo. Hindi lang natin pinili 'yun noon."
    else:
        mc_f "Pero may choice naman tayo noon. Hindi lang natin pinili 'yun."

    narrator "(Tumahimik ang mesa ng isang segundo. Tapos binasag ni Gabby ang katahimikan, kagaya ng dati.)"
    gabby "Uy, ang seryoso naman ng aura niyo! Kain na, mag-usap tayo ng masaya! May bagong season nga pala! G na!"
    if player_gender == "male":
        mc_m "(Nagbago ang mood. Tawanan. Lumipas ang sandali. Pero may nanatili sa akin.)"
    else:
        mc_f "(Nagbago ang mood. Tawanan. Lumipas ang sandali. Pero may nanatili sa akin.)"
    hide gabby with dissolve
    if player_bestfriend == "carl":
        hide carl with dissolve
    else:
        hide carly with dissolve
    hide kent with dissolve

    ## ── SCENE 1-3: First assignment dropped ─────────────────────────────────
    scene bg_hallway with dissolve
    $ safe_play("music", "audio/bgm/bgm_classroom.ogg", loop=True)
    $ day_label = "Day 2, Hapon"

    show mr_kai normal at left with dissolve
    mr_kai "Class, naka-post na 'yung unang programming activity niyo. \nBasic Python, input-output, conditionals, loops. Due in three days. Independently po, please."
    mr_kai "Gusto kong makita 'yung sarili niyong logic, hindi 'yung generated na sagot. Magiging malinaw kung alin ang alin."
    mr_kai "(mas mahinang tono) At kung sakaling ma-stuck kayo . may consultation hours ako. Gamitin niyo. 'Yun ang tamang shortcut."
    hide mr_kai with dissolve

    show gabby normal at right with dissolve
    gabby "(agad tiningnan ang phone) Three days? Kukunin ko na lang 'to mamaya. Sampung minuto, tapos na."
    show kent normal at center with dissolve
    kent "Gabby. Specifically sinabi ni Mr. Kai na independently,"
    gabby "Lahat naman ata gumagawa niyon, Kent."

    if player_bestfriend == "carl":
        show carl normal at left with dissolve
        carl "Ikaw? Gagawin mo talaga?"
    else:
        show carly normal at left with dissolve
        carly "Ikaw? Paano mo gagawin?"

    ## CHOICE NODE 1-A: How to handle first programming assignment
    $ show_hud = True
    menu:
        "Gagawin ko. Matututo naman tayo dito.":
            $ ct_change(3)
            $ mot_change(2)
            if player_gender == "male":
                mc_m "Gagawin ko. Para naman matuto."
            else:
                mc_f "Gagawin ko. Para matuto naman."
            if player_bestfriend == "carl":
                carl "Seryoso ka? Sige, game."
            else:
                carly "Oo naman! Sama-sama tayo, susubukan ko rin."
            narrator "(Pumunta ka sa library pagkatapos ng klase. Binuksan ang IDE. Nagsimulang mag-code.\n May mga parteng na-stuck, pero nag-research, nag-Google, nag-YouTube. Natapos rin sa huli.)"
            if player_gender == "male":
                mc_m "(Medyo matagal. Pero natapos ko. Sarili kong sagot.)"
            else:
                mc_f "(Medyo matagal. Pero natapos ko. Sarili kong sagot.)"
            $ grade_change("programming", 3)

        "Depende. Subukan ko muna bago mag-AI.":
            $ ct_change(1)
            if player_gender == "male":
                mc_m "Tignan ko muna kung kaya ko."
            else:
                mc_f "Subukan ko muna. Kung talagang hindi ko kaya, saka na lang."
            if player_bestfriend == "carl":
                carl "Fair enough. Text mo ako kung may tanong."
            else:
                carly "Sige, text mo ako kung may part na hindi mo gets."
            narrator "(Sinubukan mo. May mga parteng napagdaanan nang maayos. \nMay ilang linya na Google AI ang ginamit. Pero ikaw pa rin ang nag-type ng logic.)"

        "I-AI ko na lang. Tatlong araw lang naman.":
            $ ct_change(-4)
            $ mot_change(-2)
            $ use_ai("programming", 8)
            if player_gender == "male":
                mc_m "(I-AI na lang siguro. Mabilis lang naman 'to.)"
            else:
                mc_f "(I-AI na lang siguro. Para mabilis.)"
            narrator "(Pinindot ang app. Nag-generate. Kinopya ang sagot. Tapos na sa loob ng sampung segundo.)"
            if player_gender == "male":
                mc_m "(Hmm. Hindi ko maintindihan kahit isang linya nito. Pero ang importante...)"
            else:
                mc_f "(Hmm. Hindi ko maintindihan kahit isang linya nito. Pero ang importante...)"
            narrator "(Matapos na agad.)"
            call ai_used_result from _c1_ai_result

    hide gabby with dissolve
    hide kent with dissolve
    if player_bestfriend == "carl":
        hide carl with dissolve
    else:
        hide carly with dissolve
    jump chapter2