## game/chapter7.rpy
## Chapter 7, "Last Chance Na" (Week 7, Finals Prep)

label chapter7:
    call screen chapter_title("", "7 : Last Chance Na", "Week 7, 'Finals Prep'")
    $ day_label = "Week 7, Sabado"
    $ current_week = 7
    scene bg_campus with dissolve
    $ safe_play("music", "audio/bgm/bgm_study.ogg", loop=True)

    narrator "(Sabado ng umaga. Tahimik ang campus maliban sa ilang grupong nag-aaral sa labas ng mga silid-aralan.)"
    if player_gender == "male":
        mc_m "(May naghihintay sa akin sa harap ng IT building.)"
    else:
        mc_f "(May naghihintay sa akin sa harap ng IT building.)"

    show kent happy at left with moveinleft
    show rey normal at center with dissolve

    kent "Nandito na lahat. Mababa halos lahat."
    narrator "(May dalang malaking notebook at tatlong kulay ng highlighter si Kent.\n May dalang dalawang cups ng instant coffee si Rey.)"

    if player_bestfriend == "carl":
        show carl happy at right with moveinright
        carl "Uy! Nag-aalala na ako. Tara na, malamig sa labas."
    else:
        show carly happy at right with moveinright
        carly "Nandito ka! Tara na, naghintay na kaming matagal."

    narrator "(Pumasok kayo. Malinis ang study room, tahimik, walang distraksiyon, walang game console, walang ranked queue.)"

    ## Study montage
    scene bg_classroom with dissolve
    $ safe_play("music", "audio/bgm/bgm_study.ogg", loop=True)

    narrator "(Nagsimula si Kent sa Networking. VLAN, subnetting, routing protocols.)"
    narrator "(Hindi siya nagtuturo nang parang guro, nagtatanong siya. Binibigyan kayo ng pagkakataon na sumagot.)"

    show kent normal at center with dissolve
    kent "Okay. Simpleng tanong. Ano ang pagkakaiba ng VLAN at physical LAN segment?"
    if player_gender == "male":
        mc_m "(Nag-isip ako. Totoong nag-isip. Hindi nag-phone, hindi nag-AI.)"
    else:
        mc_f "(Nag-isip ako. Totoong nag-isip. Hindi nag-phone, hindi nag-AI.)"

    if player_gender == "male":
        mc_m "Sa physical LAN, ang segmentasyon ay base sa hardware. \nSa VLAN, logical, kahit nasa parehong switch, maaaring magkaibang broadcast domain."
    else:
        mc_f "Sa physical LAN, segmented by hardware. \nSa VLAN, software-defined ang segmentation, kahit physically connected, \nlogically separated ang broadcast domain."

    show kent happy at center with dissolve
    kent "Tama. Exactly. Yan ang klase ng sagot na gusto ko."

    show rey normal at left with dissolve
    rey "..."
    narrator "(Tiningnan ka ni Rey. May bahagyang ngiti, bihira para sa kanya.)"
    rey "Hindi ka ganito dati. Sa lab activities noon."
    if player_gender == "male":
        mc_m "Tinatamad lang ako dati."
    else:
        mc_f "...Oo. Tinatamad lang talaga."
    rey "Hindi tinatamad. Takot. May pagkakaiba."
    if player_gender == "male":
        mc_m "(Tumingin ako sa kanya. Wala akong nasabi. Wala akong itinanggi.)"
    else:
        mc_f "(Tumingin ako sa kanya. Wala akong nasabi. Wala akong itinanggi.)"

    hide kent with dissolve
    hide rey with dissolve
    if player_bestfriend == "carl":
        hide carl with dissolve
    else:
        hide carly with dissolve

    ## Gabby arrives late
    show gabby normal at right with hpunch
    gabby "Uy! Nandito na! Sorry late, nalaro ko ng konti,"
    show kent normal at center with dissolve
    kent "(bumabalik) Gabby. Sit down. Cybersecurity na tayo."
    gabby "(tahimik na umupo) Sige na, sige na."

    ## ── SCENE 7-2: Evening, Programming review ──────────────────────────────
    scene bg_canteen with dissolve
    $ day_label = "Week 7, Gabi"
    $ safe_play("music", "audio/bgm/bgm_canteen.ogg", loop=True)

    narrator "(Pagkatapos ng anim na oras. Gutom na kayong lahat. Kumain sa canteen bago umuwi.)"

    show gabby normal at right with dissolve
    if player_bestfriend == "carl":
        show carl normal at left with dissolve
        carl "Hoy, nagpapasalamat ako kay Kent. Pero ang utak ko ay kapasidad na."
    else:
        show carly normal at left with dissolve
        carly "Nag-aral tayo nang matagal ngayon. Feels different 'no? 'Yung naiintindihan mo talaga."

    show kent normal at center with dissolve

    kent "Bukas, Programming review. May coding output required ang finals ni Mr. Kai. Walang AI."
    gabby "Alam ko na 'yun, Kent."
    kent "Sinasabi ko para sa lahat."
    rey "...Kasama ka ba bukas?"

    ## CHOICE 7-A: Finals eve decision
    menu:
        "Oo, nandito ako bukas. Finals na 'to, sineseryoso ko.":
            $ ct_change(10)
            $ mot_change(10)
            if player_gender == "male":
                mc_m "Nandito. Promise. Sineseryoso ko na 'to."
            else:
                mc_f "Nandito. Wala na akong excuse. Sineseryoso ko ito."
            narrator "(Ngumiti si Kent nang bihira. Tumango si Rey.)"
            $ grade_change("programming", 8)
            $ grade_change("networking", 5)

        "Baka maaga kayo, matutulog pa ako.":
            $ ct_change(-3)
            if player_gender == "male":
                mc_m "Depende kung anong oras kayo magsisimula."
            else:
                mc_f "Anong oras? Baka medyo late ako."
            if player_bestfriend == "carl":
                carl "Alas nwebe. Wag kang magpapa-late."
            else:
                carly "Alas nwebe. Hintayin kita."
            if player_gender == "male":
                mc_m "(Pumangako ako. Sana masunod ko.)"
            else:
                mc_f "(Pumangako ako. Sana masunod ko.)"

    hide gabby with dissolve
    hide kent with dissolve
    hide rey with dissolve
    if player_bestfriend == "carl":
        hide carl with dissolve
    else:
        hide carly with dissolve

    ## ── SCENE 7-3: Night before finals, phone face-down ────────────────────
    scene bg_zoom with dissolve
    $ safe_play("music", "audio/bgm/bgm_study.ogg", loop=True)
    $ day_label = "Week 7, Gabi (Finals Eve)"

    narrator "(Gabi na. Nakababa ang phone sa mesa.)"
    if player_gender == "male":
        mc_m "(Ang notes ko, sariling sulat, hindi AI-generated, nakaladlad sa harapan ko.)"
        mc_m "(Alam ko na slow ako. Pero nandito na din ako.)"
        mc_m "(Binabasa ko ang sarili kong sulat. May mga mali. May mga hindi kumpleto. Pero ako ang nagsulat nito.)"
    else:
        mc_f "(Ang notes ko, sariling sulat, hindi AI-generated, nakaladlad sa harapan ko.)"
        mc_f "(Alam ko na slow ako. Pero nandito na din ako.)"
        mc_f "(Binabasa ko ang sarili kong sulat. May mga mali. May mga hindi kumpleto. Pero ako ang nagsulat nito.)"

    if player_gender == "male":
        mc_m "(Ganito pala 'yung pakiramdam ng sariling aral. Hindi 'yung magbasa ng AI output. Magbasa ng sariling notes.)"
    else:
        mc_f "(Ganito pala 'to. Hindi ru-rush. Hindi nagsho-shortcut. Sariling mga salita, sariling mga tanong.)"

    narrator "(Isinara ko ang laptop. Natulog nang may maliwanag na konsensya, \nhindi perpekto, pero mas maliwanag kaysa noong mga nakaraang linggo.)"
    if player_gender == "male":
        mc_m "(Bukas na ang finals.)"
    else:
        mc_f "(Bukas na ang finals.)"
    jump chapter8