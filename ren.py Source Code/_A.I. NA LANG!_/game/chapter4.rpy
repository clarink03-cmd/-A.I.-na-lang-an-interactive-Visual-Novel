## game/chapter4.rpy
## Chapter 4, "May Test Bukas" (Week 4, Midterms Approaching)

label chapter4:
    call screen chapter_title("", "4 : May Test Bukas", "Week 4, 'Kailangan ko pa ba mag-review?'")
    $ day_label = "Week 4, Gabi"
    $ current_week = 4

    ## ── SCENE 4-1: Night before the exam ─────────────────────────────────────
    scene bg_bedroom with dissolve
    $ safe_play("music", "audio/bgm/bgm_night.ogg", loop=True)

    if player_gender == "male":
        mc_m "(Gabi bago ang Networking midterm. \nBukas ang notes ko sa laptop. Patay ang phone, naka-charge lang.)"
        mc_m "(Alas nwebe pa lang. Maaga ako. Sa akin, kahit paano.)"
    else:
        mc_f "(Gabi bago ang Networking midterm. \nBukas ang notes ko sa laptop. Patay ang phone, naka-charge lang.)"
        mc_f "(Alas nwebe pa lang. Maaga ako. Sa akin, kahit paano.)"

    play sound "audio/sfx/sfx_chat.ogg"
    groupchat "GABBY: huy last game na please!! ranked!! isa lang HAHA" with hpunch
    groupchat "GABBY: wag ka magtampo pag hindi ka sumama"

    if player_bestfriend == "carl":
        groupchat "CARL: huy matulog na kayo. test bukas."
        groupchat "GABBY: luhh yoko nga 😤" with hpunch
    else:
        groupchat "CARLY: seryoso 'to, matulog na kayo. review muna kayo."
        groupchat "GABBY: ayy pabibo" with hpunch

    groupchat "KENT: The recommended pre-exam sleep duration is 7-9 hours. REM sleep is critical for memory consolidation of newly acquired,"
    groupchat "GABBY: KENT HINDI KO NEED ANG SCIENCE" with hpunch
    groupchat "REY: zzz"

    if player_gender == "male":
        mc_m "(Naka-mute ang phone ko. Bukas ang notes. Pero kating-kati na ang kamay ko na maglaro.)"
    else:
        mc_f "(Naka-mute ang phone ko. Bukas ang notes. Pero kating-kati na ang kamay ko na maglaro.)"

    ## CHOICE NODE 4-A
    menu:
        "Matulog na. Review na lang sana sa umaga.":
            $ ct_change(3)
            $ mot_change(2)
            if player_gender == "male":
                mc_m "(I-type sa chat) Matulog na 'ko. GL sa ranked mga baliw."
            else:
                mc_f "(I-type sa chat) Matutulog na 'ko. GL sa ranked mga baliw."
            narrator "(Nagising nang may oras pa. Nag-review ng isang oras. Kumain ng almusal. Nakarating sa klase nang maaga.)"
            $ grade_change("networking", 2)

        "Isa lang na laro, tapos matutulog na talaga.":
            $ ct_change(-2)
            $ mot_change(-2)
            if player_gender == "male":
                mc_m "(I-type sa chat) Fine. Isa lang. ISA."
            else:
                mc_f "(I-type sa chat) Okay FINE. Isa lang ha."
            narrator "(Tatlong laro pagkatapos, alas dose na ng hatinggabi. Natulog nang walang review.)"
            if player_gender == "male":
                mc_m "PATAY." with vpunch
                mc_m "(Alarm. Hindi ko narinig. Ilang oras na akong tulog?)"
            else:
                mc_f "PATAY." with vpunch
                mc_f "(Alarm. Hindi ko narinig. Ilang oras na akong tulog?)"
            $ mot_change(-2)
            jump chapter4_late_scene

        "Mag-aral pa ng konti, kahit pagod na.":
            $ ct_change(2)
            if player_gender == "male":
                mc_m "(I-type sa chat) Mag-aral muna 'ko mga boss. Kayo na muna."
            else:
                mc_f "(I-type sa chat) Nah, mag-aral muna 'ko mga boss. Kayo na lang."
            narrator "(Pinagpatuloy ang review. Dalawang oras. Pagod pero may natandaan.)"
            narrator "(Natulog nang alas onse. Nagising nang may oras pa. Nakarating pa sa klase nang maaga.)"
            $ grade_change("networking", 1)

    ## ── SCENE 4-2: Running late ───────────────────────────────────────────────
    scene bg_hallway with dissolve
    $ safe_play("music", "audio/bgm/bgm_tension.ogg", loop=True)
    $ day_label = "Week 4, Exam Day"
    if player_gender == "male":
        mc_m "(Nakarating ako sa klase. Nakarating, 'yun ang mahalaga.)"
    else:
        mc_f "(Nakarating ako sa klase. Nakarating, 'yun ang mahalaga.)"
    jump chapter4_exam

label chapter4_late_scene:
    scene bg_hallway with dissolve
    $ safe_play("music", "audio/bgm/bgm_tension.ogg", loop=True)
    $ day_label = "Week 4, Exam Day (Late)"

    show mr_earns disappointed at center with dissolve
    mr_earns "Twelve minutes late."
    if player_gender == "male":
        mc_m "(Wala na siyang sinabi pa. Pinanood lang niya akong umupo, walang galit, walang awa.)"
    else:
        mc_f "(Wala na siyang sinabi pa. Pinanood lang niya akong umupo, walang galit, walang awa.)"
    mr_earns "Exam na. Walang phone."
    hide mr_earns with dissolve
    $ grade_change("networking", -3)
    if player_gender == "male":
        mc_m "(Sa mga tanong sa exam, may nakita akong ilan sa notes ko. Kahapon. Bago ako natulog nang maaga sana.)"
    else:
        mc_f "(Sa mga tanong sa exam, may nakita akong ilan sa notes ko. Kahapon. Bago ako natulog nang maaga sana.)"

## ── SCENE 4-3: Networking Long Test ──────────────────────────────────────────
label chapter4_exam:
    scene bg_classroom with dissolve
    $ safe_play("music", "audio/bgm/bgm_tension.ogg", loop=True)

    show mr_earns thinking at center with dissolve
    mr_earns "Phones in your bags. Begin."
    hide mr_earns with dissolve

    if player_gender == "male":
        mc_m "(Unang tanong, subnetting. Alam ko ang formula. O sa tingin ko.)"
        mc_m "(Pitong tanong lahat-lahat. Naka-lock ang phone ko sa bag. Walang shortcuts ngayon. Ako na lang.)"
    else:
        mc_f "(Unang tanong, subnetting. Alam ko ang formula. O sa tingin ko.)"
        mc_f "(Pitong tanong lahat-lahat. Naka-lock ang phone ko sa bag. Walang shortcuts ngayon. Ako na lang.)"
    jump chapter4_subnet_q1

## ── Chapter 4: Midterm Exam (7 questions) ────────────────────────────────────
## Q1-5 Source: Cisco CCNA 200-301, Subnetting fundamentals
## Q6-7 Source: CCNA2 SRWE, Modules 1-4 Checkpoint Exam

label chapter4_subnet_q1:
    show screen minigame(
        "Midterm Exam, Subnetting (1/7), You can somehow glimpse at your phone",
        "Given the network address 192.168.10.0/26,\nwhat is the maximum number of usable hosts per subnet?",
        [
            "A. 30",
            "B. 62",
            "C. 126",
            "D. 14"
        ],
        1,
        "networking",
        12,
        5,
        correct_label="chapter4_subnet_q1_correct",
        wrong_label="chapter4_subnet_q1_wrong"
    )
    $ renpy.pause()

label chapter4_subnet_q1_correct:
    sys_voice "(Tama! Bakit: 6 host bits ang /26. 2^6 = 64, tanggalin ang network at broadcast = 62 usable.)"
    jump chapter4_subnet_q2

label chapter4_subnet_q1_wrong:
    sys_voice "(Hindi 'yan. Ang /26 prefix ay nag-iiwan ng 6 host bits. \nI-compute mo ang 2^6, tapos bawasan ng 2 para sa network at broadcast address.)"
    jump chapter4_subnet_q1

## ── Question 2: Subnet Mask ──────────────────────────────────────────────────
label chapter4_subnet_q2:
    show screen minigame(
        "Midterm Exam, Subnetting (2/7), You can somehow glimpse at your phone",
        "What is the subnet mask equivalent of the /28 prefix length?",
        [
            "A. 255.255.255.192",
            "B. 255.255.255.224",
            "C. 255.255.255.240",
            "D. 255.255.255.248"
        ],
        2,
        "networking",
        12,
        5,
        correct_label="chapter4_subnet_q2_correct",
        wrong_label="chapter4_subnet_q2_wrong"
    )
    $ renpy.pause()

label chapter4_subnet_q2_correct:
    sys_voice "(Tama! Bakit: 24 bits = 255.255.255, dagdag pa ng 4 bits = 240. Kaya ang /28 ay 255.255.255.240, may natitirang 4 host bits.)"
    jump chapter4_subnet_q3

label chapter4_subnet_q2_wrong:
    sys_voice "(Isipin sa binary. Ang /28 ay nangangahulugang unang 28 bits ay network bits. 24 bits = 255.255.255, tapos 4 pang bits = 240.)"
    jump chapter4_subnet_q2

## ── Question 3: Number of Subnets ────────────────────────────────────────────
label chapter4_subnet_q3:
    show screen minigame(
        "Midterm Exam, Subnetting (3/7), You can somehow glimpse at your phone",
        "You are given 192.168.1.0/24. You need 4 subnets with equal hosts.\nWhat subnet mask should you use and how many hosts per subnet?",
        [
            "A. /25, 126 hosts per subnet",
            "B. /26, 62 hosts per subnet",
            "C. /27, 30 hosts per subnet",
            "D. /28, 14 hosts per subnet"
        ],
        1,
        "networking",
        12,
        5,
        correct_label="chapter4_subnet_q3_correct",
        wrong_label="chapter4_subnet_q3_wrong"
    )
    $ renpy.pause()

label chapter4_subnet_q3_correct:
    sys_voice "(Tama! Bakit: ang pag-hiram ng 2 bits mula /24 ay nagbibigay ng /26, gumagawa ng 4 subnets (2^2), 62 usable hosts bawat isa.)"
    jump chapter4_subnet_q4

label chapter4_subnet_q3_wrong:
    sys_voice "(Para gumawa ng 4 subnets, kailangan mo ng sapat na bits. \n2 bits = 4 subnets. Mula /24, ang paghiram ng 2 ay nagbibigay ng /26.)"
    jump chapter4_subnet_q3

## ── Question 4: Broadcast Address ────────────────────────────────────────────
label chapter4_subnet_q4:
    show screen minigame(
        "Midterm Exam, Subnetting (4/7), You can somehow glimpse at your phone",
        "The network 172.16.0.0 is subnetted with a /20 mask.\nWhat is the broadcast address of the third subnet (subnet 3)?",
        [
            "A. 172.16.31.255",
            "B. 172.16.47.255",
            "C. 172.16.63.255",
            "D. 172.16.15.255"
        ],
        1,
        "networking",
        12,
        5,
        correct_label="chapter4_subnet_q4_correct",
        wrong_label="chapter4_subnet_q4_wrong"
    )
    $ renpy.pause()

label chapter4_subnet_q4_correct:
    sys_voice "(Tama! Bakit: /20 = 255.255.240.0, block size na 16 bawat subnet. \nNagsisimula sa 172.16.32.0 ang subnet 3, kaya 172.16.47.255 ang broadcast.)"
    jump chapter4_subnet_q5

label chapter4_subnet_q4_wrong:
    sys_voice "(Sa /20 mask, 16 ang block size sa third octet. \nSubnet 0 = 172.16.0.0, Subnet 1 = .16.0, Subnet 2 = .32.0. Ang broadcast ay 'yung susunod na subnet, minus 1.)"
    jump chapter4_subnet_q4

## ── Question 5: Wildcard Mask ────────────────────────────────────────────────
label chapter4_subnet_q5:
    show screen minigame(
        "Midterm Exam, Subnetting (5/7), You can somehow glimpse at your phone",
        "What wildcard mask matches all hosts in the 192.168.1.0/27 network?",
        [
            "A. 0.0.0.31",
            "B. 0.0.0.63",
            "C. 0.0.0.15",
            "D. 0.0.0.7"
        ],
        0,
        "networking",
        12,
        5,
        correct_label="chapter4_subnet_q5_correct",
        wrong_label="chapter4_subnet_q5_wrong"
    )
    $ renpy.pause()

label chapter4_subnet_q5_correct:
    sys_voice "(Tama! Bakit: /27 = 255.255.255.224. Ang wildcard ay inverse ng mask = 0.0.0.31.)"
    jump chapter4_subnet_q6

label chapter4_subnet_q5_wrong:
    sys_voice "(Ang wildcard mask ay inverse ng subnet mask. \nPara sa /27 = 255.255.255.224. Bawasan ang 255 sa bawat octet.)"
    jump chapter4_subnet_q5

## ── Question 6: BOOT Environment Variable ────────────────────────────────────
## Source: CCNA2 SRWE, Modules 1-4 Checkpoint Exam, Q7
label chapter4_subnet_q6:
    show screen minigame(
        "Midterm Exam, IOS Fundamentals (6/7), You can somehow glimpse at your phone",
        "Which command is used to set the BOOT environment variable\nthat defines where to find the IOS image file on a switch?",
        [
            "A. config-register",
            "B. boot system",
            "C. boot loader",
            "D. confreg"
        ],
        1,
        "networking",
        12,
        5,
        correct_label="chapter4_subnet_q6_correct",
        wrong_label="chapter4_subnet_q6_wrong"
    )
    $ renpy.pause()

label chapter4_subnet_q6_correct:
    sys_voice "(Tama! Bakit: 'boot system' ang command na nagse-set ng BOOT environment variable.\n Ang config-register/confreg ay para sa configuration register, hindi para dito.)"
    jump chapter4_subnet_q7

label chapter4_subnet_q6_wrong:
    sys_voice "(Hindi 'yan. Ang 'boot system' ang command na nagta-take charge ng BOOT environment variable.\n 'config-register' at 'confreg' ay para sa ibang bagay, ang configuration register.)"
    jump chapter4_subnet_q6

## ── Question 7: Remote Access Security Protocol ──────────────────────────────
## Source: CCNA2 SRWE, Modules 1-4 Checkpoint Exam, Q9
label chapter4_subnet_q7:
    show screen minigame(
        "Midterm Exam, IOS Fundamentals (7/7), You can somehow glimpse at your phone",
        "Which protocol adds security to remote connections\nto a network device?",
        [
            "A. FTP",
            "B. HTTP",
            "C. SSH",
            "D. POP"
        ],
        2,
        "networking",
        12,
        5,
        correct_label="chapter4_subnet_q7_correct",
        wrong_label="chapter4_subnet_q7_wrong"
    )
    $ renpy.pause()

label chapter4_subnet_q7_correct:
    sys_voice "(Tama! Bakit: SSH ang nagbibigay ng secure na connection papuntang remote device.\n Ang HTTP ay para sa web pages, FTP ay para sa file transfer, POP naman ay para mag-download ng email.)"
    if player_gender == "male":
        mc_m "(Pumapayat na ang oras. Binaliktad ko ang papel. Deep breath. Isa pa.)"
        mc_m "(Hindi ako sigurado sa lahat ng sagot ko. Pero sinubukan ko. Walang AI. Walang phone. Ako lang at ang natutunan ko.)"
    else:
        mc_f "(Pumapayat na ang oras. Binaliktad ko ang papel. Deep breath. Isa pa.)"
        mc_f "(Hindi ako sigurado sa lahat ng sagot ko. \nPero sinubukan ko. Walang AI. Walang phone. Ako lang at ang natutunan ko.)"
    jump chapter4_exam_done

label chapter4_subnet_q7_wrong:
    sys_voice "(Hindi 'yan. Ang SSH lang ang nagbibigay ng encrypted, \nsecure na koneksyon papunta sa isang remote device. Ang iba dito ay plaintext o para sa ibang gamit.)"
    jump chapter4_subnet_q7

## ── Exam completion ──────────────────────────────────────────────────────────
label chapter4_exam_done:
    scene bg_classroom with dissolve
    if player_gender == "male":
        mc_m "(Natapos ang exam.)"
    else:
        mc_f "(Natapos ang exam.)"

    show mr_earns normal at center with dissolve
    mr_earns "Pens down. Pass your papers forward."
    mr_earns "...Mas mabilis kayong tumapos ngayong term kumpara sa nakaraan. Palagay ko, may nag-aaral."
    hide mr_earns with dissolve

    if player_bestfriend == "carl":
        show carl normal at right with moveinright
        carl "Kumusta? Mahirap ba?"
        if player_gender == "male":
            mc_m "Okay lang. 'Yung subnetting... hindi ko sure."
        else:
            mc_f "Ewan. Sagot ko sa subnetting, 62. Tama ba?"
        carl "Ako rin. Tama 'yun. Sixty-two."
        hide carl with dissolve
    else:
        show carly normal at right with moveinright
        carly "Kumusta ang exam? Kaya pa ba?"
        if player_gender == "male":
            mc_m "Siguro. Yung isa o dalawa hindi ko sure."
        else:
            mc_f "Ewan, pero yung subnetting sagot ko ay sixty-two. Tama?"
        carly "Sixty-two rin sagot ko! Sana tama."
        hide carly with dissolve

    jump chapter5