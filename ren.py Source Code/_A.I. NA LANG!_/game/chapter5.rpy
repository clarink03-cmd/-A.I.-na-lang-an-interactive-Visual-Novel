## game/chapter5.rpy
## Chapter 5, "Incomplete?" (Week 5, Midterm Results)

label chapter5:
    call screen chapter_title("", "5 : Incomplete?", "Week 5, 'Kahit ano nalang grade, basta di incomplete.'")
    $ day_label = "Week 5, Hapon"
    $ current_week = 5

    ## ── SCENE 5-1: Midterm results posted ───────────────────────────────────
    scene bg_hallway with dissolve
    $ safe_play("music", "audio/bgm/bgm_sad.ogg", loop=True)

    if player_gender == "male":
        mc_m "(Naka-post na ang midterm grades sa portal.)"
        mc_m "(Ayaw kong agad mag-check. May kutob na ako.)"
    else:
        mc_f "(Naka-post na ang midterm grades sa portal.)"
        mc_f "(Ayaw kong agad mag-check. May kutob na ako.)"

    ## Grade reveal based on current stats
    python:
        ng_letter = letter_grade(networking_grade)
        pg_letter = letter_grade(programming_grade)
        cg_letter = letter_grade(cyber_grade)
        any_inc   = any_incomplete()

    if any_inc:
        if player_gender == "male":
            mc_m "(Nakita ko ang pangalan ko sa listahan. Networking: [ng_letter]. Programming: [pg_letter]. Cybersecurity: [cg_letter].)"
            mc_m "(May isa, naka-red. INC sa midterm component. Tumitig ako sa screen. Nawala ang ingay ng hallway.)"
            mc_m "(Alam ko naman. Lagi kong alam. Pero iba pala kapag nakikita mo na nakasulat mismo.)"
        else:
            mc_f "(Nakita ko ang pangalan ko sa listahan. Networking: [ng_letter]. Programming: [pg_letter]. Cybersecurity: [cg_letter].)"
            mc_f "(May isa, naka-red. INC sa midterm component. Tumitig ako sa screen. Nawala ang ingay ng hallway.)"
            mc_f "(Alam ko naman. Lagi kong alam. Pero iba pala kapag nakikita mo na nakasulat mismo.)"
        $ mot_change(-15)
    else:
        if player_gender == "male":
            mc_m "(Nakita ko ang pangalan ko sa listahan. Networking: [ng_letter]. Programming: [pg_letter]. Cybersecurity: [cg_letter].)"
            mc_m "(Nakaraos ako. Hindi maganda, pero nakaraos. Isang malalim na buntong-hininga ang lumabas, hindi ko namalayang kinikimkim ko pala.)"
        else:
            mc_f "(Nakita ko ang pangalan ko sa listahan. Networking: [ng_letter]. Programming: [pg_letter]. Cybersecurity: [cg_letter].)"
            mc_f "(Nakaraos ako. Hindi maganda, pero nakaraos. Isang malalim na buntong-hininga ang lumabas, hindi ko namalayang kinikimkim ko pala.)"
        $ mot_change(5)

    show gabby normal at right with dissolve
    if player_bestfriend == "carl":
        show carl normal at left with dissolve
    else:
        show carly normal at left with dissolve

    if any_inc:
        gabby "Huy, okay ka lang ba? Medyo tahimik ka ah..."
        if player_gender == "male":
            mc_m "(Tahimik lang...)"
        else:
            mc_f "(Habang tinitingnan ko ang papel, lumuluha ako nang hindi ko namamalayan.)"
        if player_bestfriend == "carl":
            carl "(mababa) Uy. Kaya pa ba."
        else:
            carly "(mababa) Hey. Huwag muna mag-isip ng masama."
        if player_gender == "male":
            mc_m "(Tumango ako, kahit hindi ko sinadya. Alam kong hindi ako okay. \nPero kung sasabihin ko nang malakas, magiging totoo talaga.)"
        else:
            mc_f "(Tumango ako, kahit hindi ko sinadya. Alam kong hindi ako okay. \nPero kung sasabihin ko nang malakas, magiging totoo talaga.)"
    else:
        gabby "Ay, okay naman! Ako rin, okay rin!"
        if player_bestfriend == "carl":
            carl "Oo naman. Kaya pa natin."
        else:
            carly "Maganda ang midterm scores! Next step, finals."
        if player_gender == "male":
            mc_m "(May relief. Pero may maliit na tinig din sa isip ko na nagtatanong \nkung natuto ba talaga ako ng kahit ano. \nMaganda ang grades, pero paano ang aking natutunan?)"
        else:
            mc_f "(May relief. Pero may maliit na tinig din sa isip ko na nagtatanong \nkung natuto ba talaga ako ng kahit ano. \nMaganda ang grades, pero paano ang aking natutunan?)"

    show kent normal at center with dissolve
    kent "Before anyone celebrates or drowns in silence, gusto ko lang sabihin, designed to filter ang midterm. \nDesigned to challenge what you actually learned and retained ang finals."
    kent "Kung nakalusot kayo dahil sa pag-copy ng configuration o pag-debug \nnang hindi naiintindihan, hindi na kayo forgiving-in ng finals."
    if player_gender == "male":
        mc_m "(Nananatili sa hangin ang mga salita niya. \nWala siyang tinitingnan nang direkta. Pero pakiramdam ko, ako ang tinutukoy.)"
    else:
        mc_f "(Nananatili sa hangin ang mga salita niya. \nWala siyang tinitingnan nang direkta. Pero pakiramdam ko, ako ang tinutukoy.)"

    hide gabby with dissolve
    hide kent with dissolve
    if player_bestfriend == "carl":
        hide carl with dissolve
    else:
        hide carly with dissolve

    ## ── SCENE 5-2: Kent speaks up in canteen ────────────────────────────────
    scene bg_canteen with dissolve
    $ safe_play("music", "audio/bgm/bgm_canteen.ogg", loop=True)
    $ day_label = "Week 5, Hapon"

    narrator "(Kakaibang katahimikan sa canteen para sa isang Biyernes ng hapon. \nNasa usual na mesa ang grupo, pero walang gumagalaw sa pagkain.)"

    show rey normal at left with dissolve
    show kent normal at center with dissolve

    if player_bestfriend == "carl":
        show carl normal at right with dissolve
    else:
        show carly normal at right with dissolve

    rey "So. Nakita naman nating lahat ang listahan."
    kent "Oo. At may sasabihin ako. Something that might make some of you uncomfortable."
    rey "Sige, Kent."
    kent "Tiningnan ko ang department-wide grade distribution. \nThree patterns stood out. Una, lahat ng top ten scores ay galing sa mga estudyanteng bihira gumamit ng AI tools sa submissions nila. Pangalawa, ang middle cluster, karamihan sa atin 'yun, mixed results. Pangatlo, ang bottom fifteen, lahat sila may very low critical thinking metrics sa assessments nila."
    kent "Wala akong balak mag-expose ng kahit sino. Nandito ako dahil may finals pa tayo. \nAt completion exams para sa mga kakailanganin nito."

    if player_bestfriend == "carl":
        carl "Kent, personal 'yung grades,"
    else:
        carly "Kent, personal 'yung grades,"

    kent "Alam ko. Hindi ko hinihingi na i-share ninyo ang scores niyo. \nTinatanong ko lang kung pwede tayong mag-aral together. \nMay compiled notes na ako sa tatlong subjects. Pwede tayong mag-review. Mag-testahan. No AI, discussion lang."
    if player_gender == "male":
        mc_m "(Tahimik. Naririnig ko pa ang kalansing ng yelo sa baso ng isang tao, tatlong mesa ang layo.)"
    else:
        mc_f "(Tahimik. Naririnig ko pa ang kalansing ng yelo sa baso ng isang tao, tatlong mesa ang layo.)"
    rey "May point si Kent. Study session? Weekend na 'to. Library. Walang laro. Walang phone."
    kent "Dadalhin ko ang Cisco Packet Tracer lab notes ko, 'yung hand-annotated. \nAt ang Python debugging cheat sheet ko. At ang RA 10173 summary na ginawa ko."
    if player_gender == "male":
        mc_m "(Handa siya. Palagi siyang handa. Ang tanong, handa na rin ba ako?)"
    else:
        mc_f "(Handa siya. Palagi siyang handa. Ang tanong, handa na rin ba ako?)"

    ## CRITICAL CHOICE 5-A: Sets the direction toward ending
    menu:
        "Oo, gusto ko ng tulong. Sineseryoso ko ang finals.":
            $ ct_change(12)
            $ mot_change(15)
            if player_gender == "male":
                mc_m "Oo. Kailangan ko ng tulong. Sineseryoso ko 'to."
            else:
                mc_f "Sige. Oo. Kailangan ko ng help, at aaminin ko 'yun."
            kent "(ngumiti nang bihira) Good. Saturday, 9 AM. Library. I'll save you a seat."
            if player_gender == "male":
                mc_m "(May bumago sa mesa. Maliit lang. Pero naramdaman ko.)"
                mc_m "(Ang aminin na kailangan ko ng tulong, hindi 'yun kahinaan. \n'Yun ang unang totoong hakbang na nagawa ko buong semester.)"
            else:
                mc_f "(May bumago sa mesa. Maliit lang. Pero naramdaman ko.)"
                mc_f "(Ang aminin na kailangan ko ng tulong, hindi 'yun kahinaan. \n'Yun ang unang totoong hakbang na nagawa ko buong semester.)"
            $ grade_change("networking", 5)
            $ grade_change("programming", 5)
            $ grade_change("cyber", 5)

        "Mag-AI study session na lang, mas mabilis.":
            $ ct_change(-10)
            $ mot_change(-5)
            if player_gender == "male":
                mc_m "Sige... oo. Pero may paraan naman ako. AI-generated reviewers, mas efficient."
            else:
                mc_f "...May paraan naman ako. Mag-o-organize ng AI reviewer."
            kent "(naging seryoso) Hindi problema ang AI reviewer. \nAng problema, kung hindi mo mabasa ang mga sagot niya nang may pag-unawa. May nakita akong AI-generated notes na parang tama, pero may buong concepts na nawawala."
            $ use_ai(None, 0)
            if player_gender == "male":
                mc_m "(Alam kong tama siya. Pero nariyan na 'yung habit, \nkomportable, madali. At mahirap sirain ang mga habit.)"
            else:
                mc_f "(Alam kong tama siya. Pero nariyan na 'yung habit, \nkomportable, madali. At mahirap sirain ang mga habit.)"

        "Kaya ko pa 'to mag-isa. Hindi ko kailangan ng group study.":
            $ ct_change(-5)
            $ mot_change(-10)
            if player_gender == "male":
                mc_m "Kaya ko 'to. Mag-isa lang ako nag-aral noon, kaya pa 'yun."
            else:
                mc_f "Okay na ako. Kaya ko 'to."
            kent "(bumubulong) Hindi 'yan katamaran. Takot 'yan." with vpunch
            if player_gender == "male":
                mc_m "(Narinig ko siya. Kahit bulong lang. \nPumatong sa dibdib ko ang mga salita niya, parang bato.)"
                mc_m "(Hindi ako sumagot. Kasi ano naman ang masasabi ko? Tama siya.)"
                mc_m "(Tumuloy ang usapan nang wala ako. At hinayaan ko na lang.)"
            else:
                mc_f "(Narinig ko siya. Kahit bulong lang. Pumatong sa dibdib ko ang mga salita niya, parang bato.)"
                mc_f "(Hindi ako sumagot. Kasi ano naman ang masasabi ko? Tama siya.)"
                mc_f "(Tumuloy ang usapan nang wala ako. At hinayaan ko na lang.)"

    show gabby normal at right with dissolve
    gabby "Okay, kahit ano man ang mapagdesisyunan natin, \ndalawang linggo na lang ang finals. Wag na tayong magpanggap na forever pa tayo."
    rey "Tama si Gabby. Hindi naghihintay ang deadline para sa kahit sino."
    hide gabby with dissolve
    hide rey with dissolve
    hide kent with dissolve
    if player_bestfriend == "carl":
        hide carl with dissolve
    else:
        hide carly with dissolve

    if player_gender == "male":
        mc_m "(Lumabas ako sa canteen na mas maraming tanong kaysa sagot. \nPero isang bagay ang malinaw: may kailangang magbago.)"
    else:
        mc_f "(Lumabas ako sa canteen na mas maraming tanong kaysa sagot. \nPero isang bagay ang malinaw: may kailangang magbago.)"

    ## ── SCENE 5-3: Ms. Iva's reminder ───────────────────────────────────────
    scene bg_classroom with dissolve
    $ safe_play("music", "audio/bgm/bgm_tension.ogg", loop=True)
    $ day_label = "Week 5, Huling Klase"

    narrator "(Huling klase ng linggo. \nNakatayo si Ms. Iva sa podium, hawak ang tumpok ng papel. \nHindi siya mukhang masaya.)"

    show ms_iva thinking at center with dissolve
    ms_iva "Bago kayo umalis, isa pang bagay. Ang final paper na ibibigay ko, may essay component."
    ms_iva "Ang prompt: i-explain ang cognitive debt sa konteksto ng paggamit ng AI sa edukasyon. \nTapos magbigay ng isang concrete step na magagawa ng isang IT student para gamitin nang etikal ang AI."
    ms_iva "Pwede ninyong i-cite ang RA 10173 o RA 10175. Pero i-cite nang tama. \nAng mga citation na hindi ma-verify sa aktwal na teksto ng batas ay ma-flag. \nTatlong estudyante na ang nahuli ko sa midterm essay na gumawa niyan."
    show ms_iva disappointed at center with dissolve
    narrator "(Hinayaan niyang lumubog 'yon. May ilang estudyanteng kumilos sa upuan. Kumuha siya ng isang papel mula sa tumpok.)"
    ms_iva "Maging malinaw tayo. Kayang-kaya kong makilala kung sino ang nagbasa mismo ng aktwal na teksto ng batas. \nIba ang pagkakasulat. Iba ang daloy ng lohika. \nAng AI-generated citations, malinis ang tunog, pero kulang sa texture ng tunay na pag-unawa ng tao."
    ms_iva "Ni-cite ng estudyanteng 'to ang RA 10173 Section 4 at nag-quote ng definition na hindi umiiral sa aktwal na batas. \nGinawa-gawa 'yun ng AI. At isinumite ng estudyante nang hindi na-check."
    ms_iva "Matulog nang mahusay. Mag-aral nang mahusay. \nGisingin ang sarili ninyong utak bago ninyo hilingin sa isang makina, na mag-isip para sa inyo."
    ms_iva "(mas mahinahon) ...Hindi ko 'to ginagawa para hulihin kayo. \nGinagawa ko 'to dahil balang araw, wala nang ibang titingin sa gawa ninyo bago ninyo ito ipasa. Only you guys will know it before the submission. Gusto ko lang kayong maging handa."
    if player_gender == "male":
        mc_m "(Tahimik ang silid habang lumalabas siya. \nNaiwan ako sa notes ko, sa konsensya ko, at dalawang linggo na lang bago ang finals.)"
    else:
        mc_f "(Tahimik ang silid habang lumalabas siya. \nNaiwan ako sa notes ko, sa konsensya ko, at dalawang linggo na lang bago ang finals.)"
    hide ms_iva with dissolve
    jump chapter6