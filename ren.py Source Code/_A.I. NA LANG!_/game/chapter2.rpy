## game/chapter2.rpy
## Chapter 2, "Laro Muna" (Week 2)

label chapter2:
    call screen chapter_title("", "2 : Laro Muna! Ano G?", "Week 2, 'A little procrastination is okay. Right?'")
    $ day_label = "Week 2, Gabi"
    $ current_week = 2

    ## ── SCENE 2-1: Group chat invite vs Packet Tracer assignment ─────────────
    scene bg_bedroom with dissolve
    $ safe_play("music", "audio/bgm/bgm_night.ogg", loop=True)

    if player_gender == "male":
        mc_m "(Hapon ng Martes. Dalawang tab bukas sa laptop, \nPacket Tracer at YouTube.)"
        mc_m "(May Networking activity si Mr. Earns: \ni-configure ang isang basic VLAN topology. Due bukas ng umaga.)"
        mc_m "(Overwhelming ang UI, pero kaya naman. Pwede namang i-search 'yung hindi ko alam.)"
    else:
        mc_f "(Hapon ng Martes. Dalawang tab bukas sa laptop, \nPacket Tracer at YouTube. Isa lang sa kanila ang gumagana.)"
        mc_f "(May Networking activity si Mr. Earns: \ni-configure ang isang basic VLAN topology. Due bukas ng umaga.)"
        mc_f "(Overwhelming ang UI, pero kaya naman. Pwede namang i-search 'yung hindi ko alam.)"

    play sound "audio/sfx/sfx_chat.ogg"
    groupchat "GABBY: uy laro na!! sabay tayo ranked tonight" with hpunch
    groupchat "GABBY: game na guys please puro darksystem sa random e 😭😭"

    if player_bestfriend == "carl":
        groupchat "CARL: ano g! uy [player_name] ikaw boii?"
    else:
        groupchat "CARLY: in! uy [player_name] ikaw? 👀"

    groupchat "KENT: nag-finish na ba lahat ng Packet Tracer activity? \nchecking the whole topology ata si Mr. Earns."
    groupchat "GABBY: KENT STOP BEING THE CONSCIENCE OF THE GROUP" with hpunch
    groupchat "REY: ... (online)"
    groupchat "(system) several people are typing..."

    if player_gender == "male":
        mc_m "(Patuloy pa rin ang notifications. Naka-hover ang cursor ko sa Packet Tracer.)"
    else:
        mc_f "(Patuloy pa rin ang notifications. Naka-hover ang cursor ko sa Packet Tracer.)"

    ## CHOICE NODE 2-A
    menu:
        "Tapusin muna ang Packet Tracer, tapos laro.":
            $ ct_change(3)
            $ mot_change(2)
            if player_gender == "male":
                mc_m "(I-type sa chat) Mamaya na. May activity pa ako. GL sa ranked."
                mc_m "(Isinara ko ang chat. Binuksan ang Packet Tracer manual.)" with moveinleft
            else:
                mc_f "(I-type sa chat) Mamaya muna. Activity muna, saka laro."
                mc_f "(Isinara ko ang chat. Binuksan ang Packet Tracer manual.)" with moveinleft
            jump chapter2_effort_route

        "Isang laro lang, pagkatapos Packet Tracer na.":
            $ ct_change(-2)
            $ mot_change(-2)
            if player_gender == "male":
                mc_m "(I-type sa chat) Okay, isa lang. Tapos serious mode na 'ko."
            else:
                mc_f "(I-type sa chat) Fine, isa lang. Promise."
            narrator "(Alas nwebe na ng gabi nang matapos ang 'isa lang.' Tatlong beses na pala 'yon.)"
            if player_gender == "male":
                mc_m "(Kinuskos ang mata. Binuksan ang Packet Tracer. Alas onse na.)"
            else:
                mc_f "(Kinuskos ang mata. Binuksan ang Packet Tracer. Alas onse na.)"
            jump chapter2_ai_route

        "Maglaro na lang. Bukas na ang Packet Tracer.":
            $ ct_change(-6)
            $ mot_change(-4)
            $ use_ai("networking", 8)
            if player_gender == "male":
                mc_m "(I-type sa chat) In. Ano pa pang Packet Tracer."
            else:
                mc_f "(I-type sa chat) In! Bukas na 'yan."
            narrator "(Nagising nang alas-singko ng umaga. Dalawang oras na lang bago mag-submit.)"
            if player_gender == "male":
                mc_m "(Alam ko na kung ano ang susunod kong gagawin.)"
            else:
                mc_f "(Alam ko na kung ano ang susunod kong gagawin.)"
            jump chapter2_ai_route

## ── ROUTE A: Effort Route (Networking minigame) ──────────────────────────────
label chapter2_effort_route:
    scene bg_bedroom with dissolve
    if player_gender == "male":
        mc_m "(Three hours in. Naintindihan ko na ang basic VLAN concept. Dalawang switch na ang na-configure.)"
        mc_m "(Marami pa ring kailangang i-configure. Oras na para subukan ang natutunan.)"
    else:
        mc_f "(Three hours in. Naintindihan ko na ang basic VLAN concept. Dalawang switch na ang na-configure.)"
        mc_f "(Marami pa ring kailangang i-configure. Oras na para subukan ang natutunan.)"

    if player_bestfriend == "carl":
        show carl normal at right with moveinright
        carl "(text) hey done yet? txt me if u need help"
        hide carl with dissolve
    else:
        show carly normal at right with moveinright
        carly "(text) how's the activity going? msg me if you're stuck"
        hide carly with dissolve

    if player_gender == "male":
        mc_m "(Sumagot ako nang maikli. Ngayon, kailangan kong patunayan na alam ko talaga ang ginagawa ko.)"
        mc_m "(Pitong tanong na lang. Kaya ko 'to.)"
    else:
        mc_f "(Sumagot ako nang maikli. Ngayon, kailangan kong patunayan na alam ko talaga ang ginagawa ko.)"
        mc_f "(Pitong tanong na lang. Kaya ko 'to.)"
    jump chapter2_effort_q1

## ROUTE A, Question 1: Access Port VLAN Assignment
## Source: CCNA 200-301, Configuring VLAN Access Ports
label chapter2_effort_q1:
    show screen minigame(
        "Networking, VLAN Configuration (1/7)",
        "Which two IOS commands must be executed in interface configuration mode\nto assign an access port to VLAN 10 on a Cisco switch?",
        [
            "A. switchport mode access\n    switchport access vlan 10",
            "B. switchport access vlan 10\n    switchport trunk encap dot1q",
            "C. set port vlan 10\n    set port mode access",
            "D. vlan 10\n    switchport mode access"
        ],
        0,
        "networking",
        8,
        5,
        correct_label="chapter2_effort_q1_correct",
        wrong_label="chapter2_effort_q1_wrong"
    )
    $ renpy.pause()

label chapter2_effort_q1_correct:
    sys_voice "(Tama! Bakit: 'switchport mode access' ang nagtatakda ng port bilang access port\n bago i-assign sa isang VLAN gamit ang 'switchport access vlan 10'.)"
    jump chapter2_effort_q2

label chapter2_effort_q1_wrong:
    sys_voice "(Mali ang syntax. Sa interface config mode ng Cisco switch, \nkailangan mo munang i-set ang port sa access mode, bago i-assign sa specific VLAN.)"
    jump chapter2_effort_q1

## ── ROUTE A, Question 2: Trunk Port Configuration ──────────────────────────
## Source: CCNA 200-301, Configuring VLAN Trunks
label chapter2_effort_q2:
    show screen minigame(
        "Networking, VLAN Configuration (2/7)",
        "A network administrator needs to configure a GigabitEthernet port as a trunk\nand allow VLANs 10, 20, and 30. Which command set accomplishes this?",
        [
            "A. switchport mode trunk\n    switchport trunk allowed vlan 10,20,30",
            "B. switchport mode trunk\n    switchport trunk vlan add 10,20,30",
            "C. interface trunk\n    allow vlan 10,20,30",
            "D. set trunk enable\n    trunk vlan 10,20,30"
        ],
        0,
        "networking",
        8,
        5,
        correct_label="chapter2_effort_q2_correct",
        wrong_label="chapter2_effort_q2_wrong"
    )
    $ renpy.pause()

label chapter2_effort_q2_correct:
    sys_voice "(Tama! Bakit: 'switchport mode trunk' ang nagbubukas ng trunk mode, \ntapos 'switchport trunk allowed vlan' ang nagsasabi kung aling VLANs ang pwedeng dumaan.)"
    jump chapter2_effort_q3

label chapter2_effort_q2_wrong:
    sys_voice "(Hindi tama. Sa Cisco switch, ang pag-set ng port sa trunk mode ay ginagawa gamit ang 'switchport mode trunk', \ntapos ise-specify kung aling mga VLAN ang pwedeng dumaan dito.)"
    jump chapter2_effort_q2

## ── ROUTE A, Question 3: Creating a VLAN ────────────────────────────────────
## Source: CCNA 200-301, Creating and Naming VLANs
label chapter2_effort_q3:
    show screen minigame(
        "Networking, VLAN Configuration (3/7)",
        "Which sequence of IOS commands correctly creates VLAN 10\nand assigns it the name Engineering?",
        [
            "A. configure terminal\n    vlan 10\n    name Engineering",
            "B. create vlan 10\n    set name Engineering",
            "C. vlan database\n    vlan 10 name Engineering",
            "D. configure terminal\n    interface vlan 10\n    description Engineering"
        ],
        0,
        "networking",
        8,
        5,
        correct_label="chapter2_effort_q3_correct",
        wrong_label="chapter2_effort_q3_wrong"
    )
    $ renpy.pause()

label chapter2_effort_q3_correct:
    sys_voice "(Tama! Bakit: VLANs are created in global config mode, 'vlan <id>' first, then 'name' to label it, hindi sa interface o vlan database mode.)"
    jump chapter2_effort_q4

label chapter2_effort_q3_wrong:
    sys_voice "(Hindi tama. Sa Cisco switch, ginagawa ang mga VLAN sa global configuration mode. \nUna, 'configure terminal', tapos ang command na 'vlan' na sinusundan ng VLAN number, tapos 'name' para i-label.)"
    jump chapter2_effort_q3

## ── ROUTE A, Question 4: Verifying VLAN Configuration ──────────────────────
## Source: CCNA 200-301, Verifying VLAN Configuration
label chapter2_effort_q4:
    show screen minigame(
        "Networking, VLAN Configuration (4/7)",
        "Which Cisco IOS command displays a summary of all VLANs\nand shows which switch ports belong to each VLAN?",
        [
            "A. show vlan brief",
            "B. show running-config",
            "C. display vlan all",
            "D. show interfaces vlan"
        ],
        0,
        "networking",
        8,
        5,
        correct_label="chapter2_effort_q4_correct",
        wrong_label="chapter2_effort_q4_wrong"
    )
    $ renpy.pause()

label chapter2_effort_q4_correct:
    sys_voice "(Tama! Bakit: 'show vlan brief' ang standard verification command, nagbibigay ito ng maikling summary ng VLANs at port assignments.)"
    jump chapter2_effort_q5

label chapter2_effort_q4_wrong:
    sys_voice "(May specific na 'show' command na nagbibigay ng maikling summary ng mga VLAN at ang port assignments nila. \nHint: isa 'yan sa pinaka-common na CCNA verification commands.)"
    jump chapter2_effort_q4

## ── ROUTE A, Question 5: Native VLAN ────────────────────────────────────────
## Source: CCNA 200-301, Native VLAN Security Best Practice
label chapter2_effort_q5:
    show screen minigame(
        "Networking, VLAN Configuration (5/7)",
        "What is the default Native VLAN on a Cisco switch,\nand what is the security best practice concerning it?",
        [
            "A. VLAN 1, it should be changed to an unused VLAN for security",
            "B. VLAN 100, it is automatically assigned to voice VLAN",
            "C. VLAN 0, it is used for management traffic only",
            "D. VLAN 999, it is the default for all trunk ports"
        ],
        0,
        "networking",
        8,
        5,
        correct_label="chapter2_effort_q5_correct",
        wrong_label="chapter2_effort_q5_wrong"
    )
    $ renpy.pause()

label chapter2_effort_q5_correct:
    sys_voice "(Tama! Bakit: VLAN 1 ang default native VLAN sa lahat ng Cisco switch. \nKilalang security risk ang pag-iwan nito as-is, kaya dapat baguhin sa unused VLAN.)"
    jump chapter2_effort_q6

label chapter2_effort_q5_wrong:
    sys_voice "(Isipin ang default VLAN na existing sa bawat Cisco switch. \nAng hindi pagbabago nito sa trunk ports ay kilalang security risk sa CCNA.)"
    jump chapter2_effort_q5

## ── ROUTE A, Question 6: Removing a Single VLAN ─────────────────────────────
## Source: CCNA2 SRWE, Modules 1-4 Checkpoint Exam, Q26
label chapter2_effort_q6:
    show screen minigame(
        "Networking, VLAN Configuration (6/7)",
        "On a switch that is configured with multiple VLANs,\nwhich command will remove only VLAN 100 from the switch?",
        [
            "A. Switch(config)# no vlan 100",
            "B. Switch# delete flash:vlan.dat",
            "C. Switch(config-if)# no switchport access vlan 100",
            "D. Switch(config-if)# no switchport trunk allowed vlan 100"
        ],
        0,
        "networking",
        8,
        5,
        correct_label="chapter2_effort_q6_correct",
        wrong_label="chapter2_effort_q6_wrong"
    )
    $ renpy.pause()

label chapter2_effort_q6_correct:
    sys_voice "(Tama! Bakit: 'no vlan 100' sa global config mode ang tanging command \nna talagang bubura ng VLAN 100 mismo, hindi lang tatanggalin sa isang port o trunk.)"
    jump chapter2_effort_q7

label chapter2_effort_q6_wrong:
    sys_voice "('delete flash:vlan.dat' ay bubura ng LAHAT ng VLAN, hindi lang isa. \n'no switchport access/trunk allowed vlan' ay tatanggal lang ng VLAN sa isang interface o trunk, hindi buburahin ang VLAN mismo. Ang 'no vlan <id>' sa global config mode ang siyang bubura ng VLAN talaga.)"
    jump chapter2_effort_q6

## ── ROUTE A, Question 7: Store-and-Forward vs Cut-Through ───────────────────
## Source: CCNA2 SRWE, Modules 1-4 Checkpoint Exam, Q22
label chapter2_effort_q7:
    show screen minigame(
        "Networking, VLAN Configuration (7/7)",
        "Which switching method ensures that the incoming frame\nis error-free before forwarding it?",
        [
            "A. store-and-forward",
            "B. cut-through",
            "C. fragment free",
            "D. FCS"
        ],
        0,
        "networking",
        8,
        5,
        correct_label="chapter2_effort_q7_correct",
        wrong_label="chapter2_effort_q7_wrong"
    )
    $ renpy.pause()

label chapter2_effort_q7_correct:
    sys_voice "(Tama! Bakit: store-and-forward switching checks the frame's \nFCS value for errors BEFORE forwarding it. Cut-through skips this check para bumilis.)"
    if player_gender == "male":
        mc_m "(Isinara ang terminal. Naka-save na ang topology. Bago matulog, sinilip ko ulit ang oras. Bago pa mag-hatinggabi.)"
        mc_m "(May katuwaan dito na hindi ko inaasahan. 'Yung galing sa sarili kong pag-unawa.)"
        mc_m "(Hindi ako umasa sa AI para dito. Ako mismo ang gumawa.)"
    else:
        mc_f "(Isinara ang terminal. Naka-save na ang topology. Bago matulog, sinilip ko ulit ang oras. Bago pa mag-hatinggabi.)"
        mc_f "(May katuwaan dito na hindi ko inaasahan. 'Yung galing sa sarili kong pag-unawa.)"
        mc_f "(Hindi ako umasa sa AI para dito. Ako mismo ang gumawa.)"
    jump chapter2_scene3

label chapter2_effort_q7_wrong:
    sys_voice "(Hindi 'yan ang isa na nagche-check ng error bago mag-forward. \n'Cut-through' ay bumibilis nga, pero hindi nag-che-check ng frame check sequence bago i-forward. Alin ang siyang gumagawa ng full error check?)"
    jump chapter2_effort_q7

## ── ROUTE B: AI Route ────────────────────────────────────────────────────────
label chapter2_ai_route:
    scene bg_bedroom with pixellate
    ai_voice "Here is the complete configuration for your VLAN topology."
    if player_gender == "male":
        mc_m "(Tumingin ako. Kumpleto. Perpekto. Mas maganda pa sa gagawin ko sa sarili kong salita ang thesis, kung gagawin ko man 'yon.)"
    else:
        mc_f "(Tumingin ako. Kumpleto. Perpekto. Mas maganda pa sa gagawin ko sa sarili kong salita ang thesis, kung gagawin ko man 'yon.)"
    if player_gender == "male":
        mc_m "(Isang problema lang: wala akong maintindihan kahit isang hakbang nito.)"
    else:
        mc_f "(Isang problema lang: wala akong maintindihan kahit isang hakbang nito.)"
    narrator "(Tatlong minuto lang ang ginugol dito. Tatlo.)"
    if player_gender == "male":
        mc_m "(Isasara ko na sana ang app. Pero bago pa 'yon...)"
    else:
        mc_f "(Isasara ko na sana ang app. Pero bago pa 'yon...)"
    ai_voice "Would you like me to explain how this configuration works step by step?"
    if player_gender == "male":
        mc_m "(Sa isip) Gusto ko ba? Oo. Pero kung ie-explain pa nito, baka isang oras 'to."
    else:
        mc_f "(Sa isip) Gusto ko. Pero alam ko na naman kung ano ang pipindutin ko. 'No.' Magpapanggap na naintindihan ko na lang."
    if player_gender == "male":
        mc_m "(Kumpleto ang copy-paste. Isinara ang laptop. Nahiga. Hindi ako makatulog. Hindi dahil sa caffeine.)"
    else:
        mc_f "(Kumpleto ang copy-paste. Isinara ang laptop. Nahiga. Hindi ako makatulog. Hindi dahil sa caffeine.)"
    call ai_used_result from _c2_ai_result

    ## ── SCENE 2-3: Submission Day, Mr. Earns ────────────────────────────────
label chapter2_scene3:
    scene bg_classroom with dissolve
    $ safe_play("music", "audio/bgm/bgm_tension.ogg", loop=True)
    $ day_label = "Week 2, Submission"

    show mr_earns normal at center with dissolve
    mr_earns "VLAN activity. Checked."
    if player_gender == "male":
        mc_m "(Tumayo siya sa harap ng klase, hawak ang isang printout. Parang may dalang death note.)"
    else:
        mc_f "(Tumayo siya sa harap ng klase, hawak ang isang printout. Parang may dalang death note.)"
    mr_earns "May dalawang topology na may parehong interface numbering error. Pareho. Hindi nagkataon."
    if player_gender == "male":
        mc_m "(Ramdam ko ang biglaang init sa leeg ko.)" with vpunch
        mc_m "(Hindi ako tumingin sa kahit kanino.)"
    else:
        mc_f "(Ramdam ko ang biglaang init sa leeg ko.)" with vpunch
        mc_f "(Hindi ako tumingin sa kahit kanino.)"
    mr_earns "Alam ko kung sino kayo. At alam ko kung bakit. Huwag na lang ninyong ulitin."
    if player_gender == "male":
        mc_m "(Hindi siya tumingin sa akin. Pero naramdaman ko. Lahat naramdaman.)"
        mc_m "(May bumubulong sa likod. Hindi ko sigurado kung si Gabby o si Kent o ang sarili kong konsensya.)"
    else:
        mc_f "(Hindi siya tumingin sa akin. Pero naramdaman ko. Lahat naramdaman.)"
        mc_f "(May bumubulong sa likod. Hindi ko sigurado kung si Gabby o si Kent o ang sarili kong konsensya.)"
    mr_earns "Next topic. Subnetting."
    if player_gender == "male":
        mc_m "(Huminto siya. Tumingin sa buong klase — hindi biro 'yung tingin niya.)"
    else:
        mc_f "(Huminto siya. Tumingin sa buong klase — hindi biro 'yung tingin niya.)"
    hide mr_earns with dissolve
    show mr_earns thinking at center with dissolve
    mr_earns "Walang shortcuts doon."
    mr_earns "(mahinang segundo, halos hindi napansin) ...Nakita ko rin naman 'yung mga gumawa ng tama. Alam ko rin 'yon."
    hide mr_earns with dissolve

    if player_gender == "male":
        mc_m "(Natapos ang klase. Lumapit sa akin si [player_bestfriend] sa hallway. Mukhang concerned. O baka curious lang.)"
    else:
        mc_f "(Natapos ang klase. Lumapit sa akin si [player_bestfriend] sa hallway. Mukhang concerned. O baka curious lang.)"

    if player_bestfriend == "carl":
        show carl stressed at right with moveinright
        carl "(bulong, papalapit) Uy. Okay ka lang? Mukha kang character sa horror game na hindi nakaligtas sa unang chapter."
        if player_gender == "male":
            mc_m "(tawa, pilit) Grabe naman. Okay lang. Natapos ko naman ang activity."
        else:
            mc_f "(pilit na ngiti) Grabe ka naman. Okay lang. Natapos ko."
        carl "(hindi kumbinsido) Oo... 'Yung topology mo, pumasok naman?"
        if player_gender == "male":
            mc_m "Oo naman. Bakit hindi?"
        else:
            mc_f "Oo. Bakit?"
        carl "(kibit balikat) Kasi pareho kayo ng error ng isa pa. \nSabi ni Kent, hindi raw kayo magkaklase noong isang section. Interesting daw."
        if player_gender == "male":
            mc_m "(Nawala ang ngiti ko.) Ano? Sinabi ni Kent 'yun?"
        else:
            mc_f "(Napahinto.) Sinabi ni Kent 'yun?"
        carl "Hindi sa akin. Kay Gabby. Pero narinig ko."
        if player_gender == "male":
            mc_m "...Sige na. Subnetting pa."
        else:
            mc_f "...Next topic na lang. Subnetting."
        carl "(tapik sa balikat) Oo. Sige. Text mo ako kung gusto mo ng tulong. Totoong tulong."
        hide carl with dissolve
    else:
        show carly stressed at right with moveinright
        carly "(bulong, papalapit) Huy. Okay ka? Namumutla ka. As in. Napansin pa ni Gabby."
        if player_gender == "male":
            mc_m "Okay lang 'to. Kulang lang sa tulog."
        else:
            mc_f "Okay lang. Baka kulang lang sa tulog."
        carly "Uh-huh. At yung topology mo?"
        if player_gender == "male":
            mc_m "Ano roon?"
        else:
            mc_f "Ano roon?"
        carly "Wala. Sinabi lang ni Kent na pareho raw ng interface numbering error 'yung sa'yo \nat sa isa pang submission mula sa kabilang section. \nSabi niya, statistically improbable daw."
        if player_gender == "male":
            mc_m "...Gusto mo bang sabihin kay Kent na mag-focus na lang sa sarili niyang grades?"
        else:
            mc_f "...Pwedeng sabihin kay Kent na mag-aral na lang siya ng sarili niya?"
        carly "(tawa) Oo nga 'no. Sige, subnetting na tayo. Pero totoo, kung kailangan mo ng tulong, nandito lang ako. 'Yung totoong tulong ha."
        hide carly with dissolve

    if player_gender == "male":
        mc_m "(Tumalikod ako. Onwards sa next class session. \nBitbit ang pakiramdam na hindi ko maintindihan: nakapasa ako. Pero bakit ang bigat pa rin?)"
    else:
        mc_f "(Tumalikod ako. Onwards sa next class session. \nBitbit ang pakiramdam na hindi ko maintindihan: nakapasa ako. Pero bakit ang bigat pa rin?)"
    jump chapter3