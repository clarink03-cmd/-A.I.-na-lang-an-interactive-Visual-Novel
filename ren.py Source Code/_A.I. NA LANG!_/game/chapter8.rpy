## game/chapter8.rpy
## Chapter 8, "Finals" (Week 8, Grand Finale)

label chapter8:
    call screen chapter_title("", "8 : Finals", "Week 8, 'The Deciding Factor'")
    $ day_label = "Week 8, Finals Day"
    $ current_week = 8

  
    ## ── SCENE 8-1: Morning of finals ─────────────────────────────────────────
    scene bg_campus with dissolve
    $ safe_play("music", "audio/bgm/bgm_finals.ogg", loop=True)

    narrator "(Alas siyete ng umaga. Maliwanag at maingay ang campus, lahat may dala-dalang reviewer, may mukhang halos hindi natulog, may kape.)"

    if player_bestfriend == "carl":
        show carl happy at center with moveinright
        carl "Uy! Heto ka na. Akala ko late ka na naman."
        if player_gender == "male":
            mc_m "Nagbago na 'ko. Maaga na 'ko ngayon."
        else:
            mc_f "Maaga na 'ko ngayon. Bago na akong tao."
        carl "Haha! Here, kape. Walang tulog kaya ito ang fuel."
        if player_gender == "male":
            mc_m "(Tinanggap ko ang kape. Mainit. Tama.)"
        else:
            mc_f "(Tinanggap ko ang kape. Sinimsim ko. Buo ang pakiramdam.)"
    else:
        show carly happy at center with moveinright
        carly "Nandito na! Alam ko na maaga ka na ngayon."
        if player_gender == "male":
            mc_m "Oo, nagbago na 'ko. Sineseryoso ko na ito."
        else:
            mc_f "Oo. Sineseryoso ko na. Huli na para mag-back down."
        carly "Heto, dalawa kang kape. Isa para ngayon, isa para in between exams."
        if player_gender == "male":
            mc_m "(Tumawa ako. Mainit ang kape, tama ang timing.)"
        else:
            mc_f "(Tumawa ako. Mainit ang kape at buo ang pakiramdam.)"

    show kent normal at left with dissolve
    kent "Nasa schedule: Networking una, Programming pagkatapos ng break, Cybersecurity last. I-pace ninyo ang sarili ninyo."
    show rey normal at right with dissolve
    rey "Kaya natin 'to."
    if player_gender == "male":
        mc_m "(Bihira kong marinig 'yan kay Rey.)"
    else:
        mc_f "(Bihira kong marinig 'yan kay Rey.)"
    rey "...Kaya natin."

    hide carl with dissolve
    hide carly with dissolve
    hide kent with dissolve
    hide rey with dissolve

    ## ── SCENE 8-2: Finals Exam 1, Networking (Mr. Earns) ────────────────────
    scene bg_classroom with dissolve
    $ safe_play("music", "audio/bgm/bgm_tension.ogg", loop=True)
    $ day_label = "Week 8, Networking Finals"

    show mr_earns normal at center with dissolve
    mr_earns "Magsimula na. Dalawang oras. Walang phone. Walang kahit ano."
    if player_gender == "male":
        mc_m "(Binaliktad ko ang papel. Unang tanong, routing protocols. Alam ko 'to.)"
        mc_m "(Hindi dahil kinopya ko mula sa AI. Kundi dahil ginawa ko sa sarili ko, paulit-ulit, hanggang sumama sa akin.)"
    else:
        mc_f "(Binaliktad ko ang papel. Unang tanong, routing protocols. Alam ko 'to.)"
        mc_f "(Hindi dahil kinopya ko mula sa AI. Kundi dahil ginawa ko sa sarili ko, paulit-ulit, hanggang sumama sa akin.)"
    hide mr_earns with dissolve
    jump chapter8_networking_final

label chapter8_networking_final:
    show screen minigame(
        "Networking Finals, Routing Protocol",
        "Alin sa mga sumusunod ang tamang katangian ng OSPF kumpara sa RIP?",
        [
            "A. Gumagamit ng hop count bilang metric; maximum 15 hops",
            "B. Link-state protocol; gumagamit ng Dijkstra's algorithm para sa routing",
            "C. Distance-vector protocol; nagse-send ng buong routing table tuwing 30 segundo",
            "D. Hindi sumusuporta sa VLSM at CIDR"
        ],
        1,
        "networking",
        15,
        18,
        correct_label="chapter8_networking_correct",
        wrong_label="chapter8_networking_wrong"
    )
    $ renpy.pause()

label chapter8_networking_correct:
    scene bg_hallway with dissolve
    sys_voice "(Tama! Bakit: OSPF ay link-state protocol na gumagamit ng Dijkstra's algorithm para makabuo ng pinaka-maiksing landas, iba sa RIP na distance-vector at hop-count based lang.)"
    if player_gender == "male":
        mc_m "(Natapos ang Networking exam. Lumabas ako nang tahimik. Sa loob ko lang: kaya ko 'yun.)"
    else:
        mc_f "(Natapos ang Networking exam. Lumabas ako nang tahimik. Sa loob ko lang: kaya ko 'yun.)"
    jump chapter8_programming_start

label chapter8_networking_wrong:
    sys_voice "(Hindi 'yan. Isipin ang pagkakaiba ng link-state at distance-vector protocols. Ano ang algorithm na ginagamit ng OSPF para kumalkula ng landas?)"
    jump chapter8_networking_final

## ── SCENE 8-3: Finals Exam 2, Programming (Mr. Kai) ──────────────────────────
label chapter8_programming_start:
    scene bg_lab with dissolve
    $ safe_play("music", "audio/bgm/bgm_tension.ogg", loop=True)
    $ day_label = "Week 8, Programming Finals"

    show mr_kai normal at center with dissolve
    mr_kai "Okay! Finals na. May coding output kayo, i-type ninyo ang inyong solusyon sa editor. Walang AI tools open. Siniseryoso ko ito."
    mr_kai "At para sa lahat, mapapansin ko ang code na masyadong perpekto para sa lalim ng topic."
    mr_kai "Good luck. Kaya ninyo."
    hide mr_kai with dissolve
    jump chapter8_programming_final

label chapter8_programming_final:
    show screen minigame(
        "Programming Finals, Python Functions",
        "Ano ang output ng sumusunod na Python code?\n\ndef square(n):\n    return n * n\n\nresult = square(4) + square(3)\nprint(result)",
        [
            "A. 49",
            "B. 25",
            "C. 7",
            "D. 12"
        ],
        1,
        "programming",
        15,
        18,
        correct_label="chapter8_programming_correct",
        wrong_label="chapter8_programming_wrong"
    )
    $ renpy.pause()

label chapter8_programming_correct:
    scene bg_hallway with dissolve
    sys_voice "(Tama! Bakit: square(4) = 16, square(3) = 9. 16 + 9 = 25.)"
    if player_gender == "male":
        mc_m "(Tapos na ang Programming exam. Hindi perpekto ang code ko. May isang function na medyo awkward.)"
        mc_m "(Pero ako ang nag-isip nito. Bawat linya, ako.)"
    else:
        mc_f "(Tapos na ang Programming exam. Hindi perpekto ang code ko. May isang function na medyo awkward.)"
        mc_f "(Pero ako ang nag-isip nito. Bawat linya, ako.)"
    jump chapter8_cyber_start

label chapter8_programming_wrong:
    sys_voice "(Hindi 'yan. I-trace ang function: square(4) ibig sabihin 4 * 4, square(3) ibig sabihin 3 * 3. I-add ang dalawang resulta.)"
    jump chapter8_programming_final

## ── SCENE 8-4: Finals Exam 3, Cybersecurity (Ms. Iva) ────────────────────────
label chapter8_cyber_start:
    scene bg_classroom with dissolve
    $ safe_play("music", "audio/bgm/bgm_tension.ogg", loop=True)
    $ day_label = "Week 8, Cybersecurity Finals"

    show ms_iva normal at center with dissolve
    ms_iva "Ang huling exam. May MCQ portion at may essay."
    ms_iva "Ang essay prompt, tandaan ninyo: ipaliwanag ang cognitive debt sa konteksto ng AI use sa edukasyon. At isang hakbang para gamitin ang AI nang etikal."
    ms_iva "Actual citations kung may ci-cite, verified mula sa tunay na batas. Wala akong tinatanggap na AI-generated references."
    hide ms_iva with dissolve
    jump chapter8_cyber_final

label chapter8_cyber_final:
    show screen minigame(
        "Cybersecurity Finals, RA 10175",
        "Sa ilalim ng RA 10175 (Cybercrime Prevention Act of 2012), alin ang nakalista bilang cybercrime offense?",
        [
            "A. Paggamit ng social media para mag-post ng personal na larawan",
            "B. Illegal access sa isang computer system nang walang pahintulot",
            "C. Pag-download ng libre at legal na open-source software",
            "D. Pagtanggap ng email mula sa hindi kilalang sender"
        ],
        1,
        "cyber",
        15,
        18,
        correct_label="chapter8_cyber_correct",
        wrong_label="chapter8_cyber_wrong"
    )
    $ renpy.pause()

label chapter8_cyber_correct:
    sys_voice "(Tama! Bakit: ang illegal access, ang pagpasok sa isang computer system nang walang pahintulot, ay malinaw na nakalista bilang cybercrime offense sa RA 10175.)"
    jump chapter8_essay

label chapter8_cyber_wrong:
    sys_voice "(Hindi 'yan. Ang ibang mga choices ay legal o neutral na aksyon. Alin dito ang talagang paglabag sa pahintulot at seguridad ng isang system?)"
    jump chapter8_cyber_final

## ── SCENE 8-5: The essay ──────────────────────────────────────────────────
label chapter8_essay:
    scene bg_classroom with dissolve

    show cg_ai_chat with zoomin
    hide cg_ai_chat with dissolve
    narrator "'Ipaliwanag ang cognitive debt sa konteksto ng AI use sa edukasyon, \nat isang hakbang na magagawa ng isang IT student para gamitin ang AI nang etikal.'"
    if player_gender == "male":
        mc_m "(Ang essay prompt, nakaharap sa akin. Puti ang papel. Blangko pa.)"
        mc_m "(Naisip ko ang lahat ng nangyari nitong walong linggo. Ang mga aral, ang mga pagkakamali, ang mga pagpipilian.)"
        mc_m "(Hindi ito ang papel na gusto kong isulat. Pero ito ang pinakatotoo.)"
        mc_m "(Nagsimula akong magsulat. Hindi mabilis. Hindi perfect. Pero bawat salita, sarili ko.)"
        mc_m "(RA 10173, Section 3. Ang kahulugan ng personal information. Tama ang section number, kasi bina-verify ko.)"
        mc_m "(Natapos ako. Hindi ko alam kung mataas ang grado ko dito. Pero alam kong totoo ang isinulat ko.)"
    else:
        mc_f "(Ang essay prompt, nakaharap sa akin. Puti ang papel. Blangko pa.)"
        mc_f "(Naisip ko ang lahat ng nangyari nitong walong linggo. Ang mga aral, ang mga pagkakamali, ang mga pagpipilian.)"
        mc_f "(Hindi ko ito maisusulat para sa grado. Isusulat ko ito dahil totoo ito.)"
        mc_f "(Nagsimula akong magsulat. Hindi mabilis. Hindi perfect. Pero bawat salita, sarili ko.)"
        mc_f "(RA 10173, Section 3. Ang kahulugan ng personal information. Tama ang section number, kasi bina-verify ko.)"
        mc_f "(Natapos ako. Hindi ko alam kung mataas ang grado ko dito. Pero alam kong totoo ang isinulat ko.)"
    $ grade_change("cyber", 12)

    ## ── SCENE 8-6: After the last exam ───────────────────────────────────────
    scene bg_campus with dissolve
    $ safe_play("music", "audio/bgm/bgm_campus.ogg", loop=True)
    $ day_label = "Week 8, Pagkatapos ng Finals"

    narrator "(Hapon na. Maliwanag at maingay pa rin ang campus, pero iba na ang ingay. Mas magaan.)"
    if player_gender == "male":
        mc_m "(Nakarating ako sa canteen entrance. Nandoon na ang buong grupo.)"
    else:
        mc_f "(Nakarating ako sa canteen entrance. Nandoon na ang buong grupo.)"

    show gabby happy at right with dissolve
    show kent happy at left with dissolve
    show rey normal at center with dissolve

    gabby "TAPOS NA! LAHAT TAPOS NA!" with hpunch
    kent "Technically-"
    gabby "KENT."
    kent "Hahahaah Tara mag-meryenda tayo. Libre mo ko Gabs"
    rey "Mauuna na muna ko. May kailangan lang akong ayusin sa dorm. Good job guys ingat ha."
    hide rey with dissolve

    if player_bestfriend == "carl":
        show carl happy at center with dissolve
        carl "Uy! Kumusta ang exam ni Ms. Iva?"
        if player_gender == "male":
            mc_m "Sariling salita ko yung sinulat ko. Hindi AI."
        else:
            mc_f "Sarili ko. Verified citations at lahat."
        carl "Seryoso? Ikaw talaga."
        hide carl with dissolve
    else:
        show carly happy at center with dissolve
        carly "Kumusta ang exam ni Ms. Iva? Tinupad mo ba ang promise mo?"
        if player_gender == "male":
            mc_m "Oo. Sarili ko. Bini-verify ko pa ang bawat citation."
        else:
            mc_f "Oo. Sarili kong salita. Lahat bina-verify ko."
        carly "(ngumiti) Proud ako. Seryoso."
        hide carly with dissolve

    hide gabby with dissolve
    hide kent with dissolve
    hide rey with dissolve

    scene black with dissolve
    narrator "(Ilang linggo pagkatapos, lalabas ang mga grades.)"
    narrator "(Ngayon, kumain muna. Grupo. Maingay. Buhay.)"
    if player_gender == "male":
        mc_m "(At ako, nandito. Presente. Tunay.)"
    else:
        mc_f "(At ako, nandito. Presente. Tunay.)"

    jump ending_sequence