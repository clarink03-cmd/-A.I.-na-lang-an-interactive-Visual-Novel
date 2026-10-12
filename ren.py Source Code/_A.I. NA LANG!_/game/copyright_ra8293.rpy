## game/copyright_ra8293.rpy
## RA 8293 (Intellectual Property Code of the Philippines) scene + 5-question quiz.
## Called from chapter7 (Finals Prep study group):  call copyright_review
## The quiz uses the same screen/labels as every other quiz. It changes Critical
## Thinking only (no subject grade), so grade balance is unchanged.

label copyright_review:
    $ mc = mc_m if player_gender == "male" else mc_f
    show kent normal at center with dissolve
    show gabby happy at right with dissolve
    gabby "Kent! Pa-send naman ng notes mo, 'yung hand-annotated. Ipo-post ko sa page ng batch natin, para sa lahat!"
    show kent stressed at center with quickfade
    kent "Urm, Gabby. Gawa ko 'yan. Hindi mo pwedeng i-post nang walang paalam ko."
    gabby "Grabe ka! 'Yung ibang notes nga sa internet, libre lahat!"
    show kent normal at center with quickfade
    kent "Libre makita, hindi ibig sabihing libre gamitin. Diyan pumapasok ang RA 8293, ang Intellectual Property Code of the Philippines."
    kent "Sa ilalim ng Section 172, protektado na ang isang orihinal na gawa sa mismong sandali na nilikha ito. Essay, larawan, kanta, code. Hindi na kailangang i-register."
    gabby "Eh 'yung code na nakuha ko sa GitHub kagabi?"
    kent "Karamihan may license na may kondisyon. Kapag walang license, hindi ibig sabihing libre. Nasa gumawa pa rin ang karapatan."
    show gabby stressed at right with quickfade
    gabby "Eh kung AI naman ang gumawa ng code?"
    kent "Debatable pa kung sino ang may-ari ng gawa ng AI. Pero kung kinopya ng AI ang gawa ng iba at ginamit mo nang walang credit, ikaw ang haharap sa guro. At posibleng sa batas din."
    mc "(Hindi lang pala ito para sa mga IT. Kahit sinong gumagamit ng AI, puwedeng makakopya ng gawa ng iba nang hindi namamalayan.)"
    kent "May exception: fair use, Section 185. Puwedeng gumamit ng bahagi ng gawa para sa pag-aaral, pananaliksik, o puna, basta patas ang gamit."
    kent "At ayon sa Section 193, may karapatan ang gumawa na mabanggit siya bilang may-akda. Kaya cite, cite, cite."
    kent "Hindi ako abogado, ha. Basahin pa rin ang mismong teksto ng batas."
    show gabby happy at right with quickfade
    gabby "Okay, okay! Hindi ko na ipo-post. Pero bakit parang lahat ng sinasabi mo, may section number?"
    kent "Kasi may quiz ako. Limang tanong."
    gabby "Bakit ba lagi akong may kaibigang may quiz?"
    jump copyright_q1

label copyright_q1:
    show screen minigame(
        _("Batas at Etika, RA 8293 Copyright (1/5)"),
        _("Alin ang batas na pangunahing nagpoprotekta sa copyright ng mga orihinal na gawa sa Pilipinas?"),
        [
            _("A. RA 8293, Intellectual Property Code of the Philippines"),
            _("B. RA 10173, Data Privacy Act"),
            _("C. RA 10175, Cybercrime Prevention Act"),
            _("D. Wala. Hindi protektado ang mga gawa sa Pilipinas")
        ],
        0,
        None,
        2,
        0,
        correct_label="copyright_q1_correct",
        wrong_label="copyright_q1_wrong"
    )
    $ renpy.pause()

label copyright_q1_correct:
    narrator "(Tama! Ang RA 8293 ang Intellectual Property Code ng Pilipinas, kasama diyan ang copyright.)"
    $ quiz_fb = None
    jump copyright_q2

label copyright_q1_wrong:
    narrator "(Hindi 'yan. Isipin kung aling batas ang tungkol sa intellectual property, hindi sa data privacy o cybercrime.)"
    $ quiz_fb = None
    jump copyright_q1

label copyright_q2:
    show screen minigame(
        _("Batas at Etika, RA 8293 Copyright (2/5)"),
        _("Kailan nagsisimula ang copyright protection ng isang orihinal na essay, larawan, o code?"),
        [
            _("A. Kapag na-register na sa gobyerno"),
            _("B. Sa mismong paglikha ng gawa"),
            _("C. Kapag may nagbayad na para dito"),
            _("D. Kapag na-post na sa social media")
        ],
        1,
        None,
        2,
        0,
        correct_label="copyright_q2_correct",
        wrong_label="copyright_q2_wrong"
    )
    $ renpy.pause()

label copyright_q2_correct:
    narrator "(Tama! Protektado ang gawa sa mismong paglikha. Hindi kailangang i-register o i-post muna.)"
    $ quiz_fb = None
    jump copyright_q3

label copyright_q2_wrong:
    narrator "(Hindi 'yan. Kailangan bang may pumayag o may form muna para maging iyo ang sarili mong essay?)"
    $ quiz_fb = None
    jump copyright_q2

label copyright_q3:
    show screen minigame(
        _("Batas at Etika, RA 8293 Copyright (3/5)"),
        _("Gusto mong gumamit ng larawang nakita mo sa Google para sa school presentation. Alin ang pinakamainam gawin?"),
        [
            _("A. I-download at ilagay agad, libre naman sa internet"),
            _("B. Gumamit ng larawang may bukas na lisensya, o i-credit ang gumawa at ang source"),
            _("C. Burahin ang watermark para hindi mahalata"),
            _("D. Sabihing ikaw ang kumuha ng larawan")
        ],
        1,
        None,
        2,
        0,
        correct_label="copyright_q3_correct",
        wrong_label="copyright_q3_wrong"
    )
    $ renpy.pause()

label copyright_q3_correct:
    narrator "(Tama! I-credit ang gumawa o gumamit ng larawang may bukas na lisensya. Libre makita, hindi laging libre gamitin.)"
    $ quiz_fb = None
    jump copyright_q4

label copyright_q3_wrong:
    narrator "(Hindi 'yan. Hindi lahat ng nasa Google ay libreng gamitin, at lalong hindi puwedeng angkinin.)"
    $ quiz_fb = None
    jump copyright_q3

label copyright_q4:
    show screen minigame(
        _("Batas at Etika, RA 8293 Copyright (4/5)"),
        _("Alin sa mga ito ang pinakamalamang na maituturing na fair use (Section 185)?"),
        [
            _("A. Pag-quote ng maikling bahagi ng artikulo sa essay, may tamang citation, para sa pag-aaral"),
            _("B. Pag-upload ng buong libro sa website para ma-download ng kahit sino"),
            _("C. Pagbebenta ng kopya ng isang pelikula"),
            _("D. Pagkopya ng buong essay ng kaklase at pag-submit bilang sarili")
        ],
        0,
        None,
        2,
        0,
        correct_label="copyright_q4_correct",
        wrong_label="copyright_q4_wrong"
    )
    $ renpy.pause()

label copyright_q4_correct:
    narrator "(Tama! Maikling bahagi, may citation, para sa pag-aaral: halimbawa ng fair use sa Section 185.)"
    $ quiz_fb = None
    jump copyright_q5

label copyright_q4_wrong:
    narrator "(Hindi 'yan. Isipin kung gaano karami ang kinuha, para saan, at kung may credit.)"
    $ quiz_fb = None
    jump copyright_q4

label copyright_q5:
    show screen minigame(
        _("Batas at Etika, RA 8293 Copyright (5/5)"),
        _("Nag-generate ang AI ng sagot na halos kapareho ng isang published na artikulo, at isinumite mo ito nang walang banggit sa source. Ano ang totoo?"),
        [
            _("A. Okay lang, AI naman ang gumawa"),
            _("B. Ikaw pa rin ang may pananagutan: plagiarism sa school, at posibleng paglabag sa copyright"),
            _("C. Walang problema basta may binago kang ilang salita"),
            _("D. Ang AI company lang ang mananagot")
        ],
        1,
        None,
        2,
        0,
        correct_label="copyright_q5_correct",
        wrong_label="copyright_q5_wrong"
    )
    $ renpy.pause()

label copyright_q5_correct:
    narrator "(Tama! Ikaw pa rin ang mananagot, kahit AI ang nag-generate. Magbanggit ng source at suriin ang output.)"
    $ quiz_fb = None
    jump copyright_outro

label copyright_q5_wrong:
    narrator "(Hindi 'yan. Hindi ka nakakalusot dahil AI ang gumawa. Isipin kung sino ang nag-submit.)"
    $ quiz_fb = None
    jump copyright_q5

label copyright_outro:
    show kent happy at center with quickfade
    kent "Good. Hindi lang sa exam ang batas. Nasa bawat copy-paste mo."
    show gabby normal at right with quickfade
    gabby "Sige na, uuwi na ako. Baka may copyright pa 'yung upuang kinauupuan natin."
    return
