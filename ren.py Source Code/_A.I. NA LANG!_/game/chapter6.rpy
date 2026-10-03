## game/chapter6.rpy
## Chapter 6, "Busted" (Week 6, Confrontation)

label chapter6:
    call screen chapter_title("", "6 : Busted", "Week 6, 'Ma'am, may explanation po ako...'")
    $ day_label = "Week 6, Umaga"
    $ current_week = 6
    scene bg_hallway with dissolve
    $ safe_play("music", "audio/bgm/bgm_tension.ogg", loop=True)

    narrator "(Bago magsimula ang klase. Tinatawag ka ni Ms. Iva.)"
    if player_gender == "male":
        mc_m "(Napansin ng lahat. Nagtataka. \nAko lang ang hindi nagtataka. Alam ko na kung bakit.)"
    else:
        mc_f "(Napansin ng lahat. Nagtataka. \nAko lang ang hindi nagtataka. Alam ko na kung bakit.)"

    show ms_iva thinking at center with dissolve
    ms_iva "Ang essay mo sa cybersecurity paper, may nahanap akong citation. \nRA 10173, Section 4, Subsection G, Paragraph 3."
    ms_iva "Binasa ko ang module. Walang ganoon na included." with vpunch
    narrator "(Bigla na lang tumahimik ang hallway.)"
    ms_iva "Hindi ito ang unang pagkakataon na nakakita ako ng ganito. \nAng AI ay madalas gumawa ng citations na mukhang totoo, exact section numbers, exact titles. Pero hindi totoo."
    show ms_iva disappointed at center with dissolve
    ms_iva "(mababa) Tanong ko lang sa'yo. \nIkaw mismo ba ang sumulat ng citation na 'yon, o kinopya mo ang output ng AI nang hindi nagve-verify?"

    ## CRITICAL CHOICE 6-A: Determines got_caught variable
    menu:
        "Totoo po, Ma'am. Hindi ko nabasa ang aktwal na batas. Kinopya ko ang AI output.":
            $ got_caught = False
            $ ct_change(15)
            $ mot_change(5)
            if player_gender == "male":
                mc_m "Totoo po, Ma'am. Hindi ko po bina-verify ang citation. Kinopya ko po ang sagot ng AI. Pasensya na po."
            else:
                mc_f "Hindi ko po bina-verify. Kinopya ko po ang output ng AI nang hindi nag-check. Mali ko po, Ma'am."
            show ms_iva thinking at center with dissolve
            ms_iva "..."
            ms_iva "Salamat sa katapatan. Hindi ko ito basta-basta babalewalain, may epekto ito sa grade mo. \nPero bibigyan kita ng pagkakataon na mag-resubmit ng tamang papel sa loob ng isang linggo."
            ms_iva "At ang conditions: sarili mong salita. Actual citations mula sa RA 10173 at RA 10175. \nAt isang talata tungkol sa kung ano ang natutunan mo mula sa pagkakamaling ito."
            if player_gender == "male":
                mc_m "Opo, Ma'am. Salamat po."
            else:
                mc_f "Opo. Salamat po, Ma'am. Gagawin ko po."
            narrator "(Lumakad siya. Nanatili kang nakatanga sa hallway, halos isang minuto.)"
            $ grade_change("cyber", -10)

        "N-Nabasa ko po, Ma'am. Baka nagkamali lang ng pag-cite.":
            $ got_caught = True
            $ ct_change(-20)
            $ mot_change(-15)
            if player_gender == "male":
                mc_m "N-Nabasa ko po 'yun, Ma'am. Baka nagkamali lang po ako ng pag-cite ng section number."
            else:
                mc_f "N-Nabasa ko po siya, Ma'am. Siguro nagkamali lang ako ng format ng citation."
            show ms_iva disappointed at center with dissolve
            ms_iva "..."
            ms_iva "Sineseryoso ko ang academic integrity sa klase ko. At sineseryoso ko rin ang bawat estudyante."
            ms_iva "Ibig sabihin, alam ko kung kailan nagsisinungaling ang isang estudyante sa harap ko."
            narrator "(Bumagsak ang mundo nang kaunti.)"
            ms_iva "Huwag kang pumasok sa klase ko bukas nang walang resubmission, at walang kumpletong paliwanag kung paano mo gagawin nang tama 'to."
            ms_iva "At gagawin nating opisyal ang pangyayaring 'to sa department."
            narrator "(Lumakad na siya. Naiwan ka sa hallway.)"
            if player_gender == "male":
                mc_m "(Wala akong nasabi. Wala na akong maisasagot.)"
            else:
                mc_f "(Wala akong nasabi. Wala na akong maisasagot.)"
            $ grade_change("cyber", -20)

    hide ms_iva with dissolve

    ## ── SCENE 6-2: After the confrontation ──────────────────────────────────
    scene bg_canteen with dissolve
    $ safe_play("music", "audio/bgm/bgm_sad.ogg", loop=True)
    $ day_label = "Week 6, Hapon"

    if player_bestfriend == "carl":
        show carl stressed at center with dissolve
        carl "Huy. Narinig ko. Okay ka lang ba?"
        if player_gender == "male":
            mc_m "Hindi ko in-expect na ganoon ka-strict si Ms. Iva."
        else:
            mc_f "Hindi ko in-expect na... ganoon pala talaga 'yun. Na mapapansin."
        carl "Lagi naman sinasabi ni Kent, 'verify your citations.' Ngayon alam mo na kung bakit."
        hide carl with dissolve
    else:
        show carly stressed at center with dissolve
        carly "Narinig ko kung ano'ng nangyari sa hallway. Okay ka ba?"
        if player_gender == "male":
            mc_m "Okay lang. Medyo napahiya ako, pero... kailangan ko na 'tong harapin."
        else:
            mc_f "Hindi okay, pero... kailangan ko nang gawin nang tama."
        carly "Tama 'yun. Nandito ako kung kailangan mo ng help sa resubmission."
        hide carly with dissolve

    ## ── SCENE 6-3: Cybersecurity redo activity ───────────────────────────────
    if not got_caught:
        scene bg_lab with dissolve
        $ safe_play("music", "audio/bgm/bgm_study.ogg", loop=True)
        $ day_label = "Week 6, Resubmission Prep"

        if player_gender == "male":
            mc_m "(Library. Nakabukas ang laptop ko sa dalawang tab: ang Official Gazette ng Pilipinas at ang blank na document.)"
            mc_m "(Binabasa ko nang maingat ang tunay na RA 10173. Section 3. Section 4. Section 16.)"
            mc_m "(Iba ang pakiramdam kapag sarili kong mata ang nagbabasa. Mabagal. Pero totoo.)"
        else:
            mc_f "(Library. Nakabukas ang laptop ko sa dalawang tab: ang Official Gazette ng Pilipinas at ang blank na document.)"
            mc_f "(Binabasa ko nang maingat ang tunay na RA 10173. Section 3. Section 4. Section 16.)"
            mc_f "(Iba ang pakiramdam kapag sarili kong mata ang nagbabasa. Mabagal. Pero totoo.)"
        jump chapter6_cyber_q1

    jump chapter7

## ── Cybersecurity Resubmission Check (7 questions) ──────────────────────────
## Q1 Source: RA 10173 (Data Privacy Act of 2012)
## Q2-7 Source: Cyber Threat Management (CyberTM) Final Exam bank

label chapter6_cyber_q1:
    show screen minigame(
        "Cybersecurity, RA 10173 Data Privacy Act (1/7)",
        "Alin sa mga sumusunod ang isang karapatan ng data subject sa ilalim ng RA 10173 (Data Privacy Act of 2012)?",
        [
            "A. Karapatang mag-access ng personal data na hawak ng isang organization",
            "B. Karapatang tanggapin ang suweldo ng data controller",
            "C. Karapatang mag-imbak ng datos sa ibang tao nang walang pahintulot",
            "D. Karapatang baguhin ang privacy policy ng isang kumpanya"
        ],
        0,
        "cyber",
        12,
        10,
        correct_label="chapter6_cyber_q1_correct",
        wrong_label="chapter6_cyber_q1_wrong"
    )
    $ renpy.pause()

label chapter6_cyber_q1_correct:
    narrator "(Tama! Bakit: ang right to access ay isa sa mga karapatan ng data subject sa RA 10173, \nang karapatang malaman at makuha ang kopya ng sariling personal data na hawak ng isang organisasyon.)"
    jump chapter6_cyber_q2

label chapter6_cyber_q1_wrong:
    narrator "(Hindi 'yan. Isipin kung ano ang natural na karapatan ng may-ari ng datos, hindi ng kumpanyang humahawak nito.)"
    jump chapter6_cyber_q1

## Source: CyberTM Final Exam, Q2
label chapter6_cyber_q2:
    show screen minigame(
        "Cybersecurity, Policy Fundamentals (2/7)",
        "Which security policy would address the rules that determine access to\nand use of network resources, and define the consequences of policy violations?",
        [
            "A. Data policy",
            "B. Remote access policy",
            "C. Acceptable use policy",
            "D. Password policy"
        ],
        2,
        "cyber",
        12,
        10,
        correct_label="chapter6_cyber_q2_correct",
        wrong_label="chapter6_cyber_q2_wrong"
    )
    $ renpy.pause()

label chapter6_cyber_q2_correct:
    narrator "(Tama! Bakit: ang acceptable use policy ang nagtatakda ng access \nat usage rules ng network resources, kasama ang consequences ng violations.)"
    jump chapter6_cyber_q3

label chapter6_cyber_q2_wrong:
    narrator "(Hindi 'yan. Ang password policy ay para sa password requirements, \nremote access policy naman ay para sa pag-konekta mula sa labas. May specific policy para sa general usage rules at consequences.)"
    jump chapter6_cyber_q2

## Source: CyberTM Final Exam, Q3
label chapter6_cyber_q3:
    show screen minigame(
        "Cybersecurity, Policy Fundamentals (3/7)",
        "Which framework should be recommended for establishing a comprehensive\ninformation security management system in an organization?",
        [
            "A. ISO OSI model",
            "B. CIA Triad",
            "C. NIST/NICE framework",
            "D. ISO/IEC 27000"
        ],
        3,
        "cyber",
        12,
        10,
        correct_label="chapter6_cyber_q3_correct",
        wrong_label="chapter6_cyber_q3_wrong"
    )
    $ renpy.pause()

label chapter6_cyber_q3_correct:
    narrator "(Tama! Bakit: ang ISO/IEC 27000 ang standard family na nagtatakda ng comprehensive\n information security management system, hindi lang isang model o triad.)"
    jump chapter6_cyber_q4

label chapter6_cyber_q3_wrong:
    narrator "(Hindi 'yan. Ang CIA Triad ay isang konsepto lang (confidentiality, integrity, availability), \nhindi isang buong management framework. May specific na ISO family para dito.)"
    jump chapter6_cyber_q3

## Source: CyberTM Final Exam, Q4
label chapter6_cyber_q4:
    show screen minigame(
        "Cybersecurity, Law & Compliance (4/7)",
        "If a person knowingly accesses a government computer without permission,\nwhat federal act would the person be subject to?",
        [
            "A. SOX",
            "B. ECPA",
            "C. GLBA",
            "D. CFAA"
        ],
        3,
        "cyber",
        12,
        10,
        correct_label="chapter6_cyber_q4_correct",
        wrong_label="chapter6_cyber_q4_wrong"
    )
    $ renpy.pause()

label chapter6_cyber_q4_correct:
    narrator "(Tama! Bakit: ang Computer Fraud and Abuse Act (CFAA) ang nagbibigay ng foundation \npara sa mga batas laban sa unauthorized access ng computer systems.)"
    jump chapter6_cyber_q5

label chapter6_cyber_q4_wrong:
    narrator "(Hindi 'yan. Ang SOX ay para sa financial reporting, GLBA para sa financial institutions, \nECPA para sa electronic communications. May specific act para sa unauthorized computer access.)"
    jump chapter6_cyber_q4

## Source: CyberTM Final Exam, Q6
label chapter6_cyber_q5:
    show screen minigame(
        "Cybersecurity, Security Testing (5/7)",
        "What type of security test uses simulated attacks to determine\nthe possible consequences of a real threat?",
        [
            "A. Vulnerability scanning",
            "B. Integrity checking",
            "C. Penetration testing",
            "D. Network scanning"
        ],
        2,
        "cyber",
        12,
        10,
        correct_label="chapter6_cyber_q5_correct",
        wrong_label="chapter6_cyber_q5_wrong"
    )
    $ renpy.pause()

label chapter6_cyber_q5_correct:
    narrator "(Tama! Bakit: ang penetration testing ay gumagamit ng simulated attacks \npara malaman ang posibleng consequences ng isang tunay na threat. Iba 'yan sa vulnerability scanning, na naghahanap lang ng weaknesses.)"
    jump chapter6_cyber_q6

label chapter6_cyber_q5_wrong:
    narrator "(Hindi 'yan. Ang vulnerability scanning ay naghahanap lang ng weaknesses, \nhindi sumusubok ng simulated attack. May specific test na gumagaya ng aktwal na atake.)"
    jump chapter6_cyber_q5

## Source: CyberTM Final Exam, Q14
label chapter6_cyber_q6:
    show screen minigame(
        "Cybersecurity, Security Organizations (6/7)",
        "Which security organization maintains a list of common vulnerabilities\nand exposures (CVE) used by prominent security organizations?",
        [
            "A. CIS",
            "B. SecurityNewsWire",
            "C. SANS",
            "D. MITRE"
        ],
        3,
        "cyber",
        12,
        10,
        correct_label="chapter6_cyber_q6_correct",
        wrong_label="chapter6_cyber_q6_wrong"
    )
    $ renpy.pause()

label chapter6_cyber_q6_correct:
    narrator "(Tama! Bakit: ang MITRE Corporation ang nag-maintain ng \nCVE list na ginagamit ng mga prominent security organizations sa buong mundo.)"
    jump chapter6_cyber_q7

label chapter6_cyber_q6_wrong:
    narrator "(Hindi 'yan. Ang SANS ay kilala sa NewsBites digest, hindi CVE list. \nMay specific na organization na siyang nag-maintain ng CVE database.)"
    jump chapter6_cyber_q6

## Source: CyberTM Final Exam, Q31
label chapter6_cyber_q7:
    show screen minigame(
        "Cybersecurity, Security Controls (7/7)",
        "The manager of a data center requisitions magnetic door locks that\nrequire employees to swipe an ID card to open. Which type of\nsecurity control is being implemented?",
        [
            "A. Corrective",
            "B. Compensative",
            "C. Recovery",
            "D. Preventive"
        ],
        3,
        "cyber",
        12,
        10,
        correct_label="chapter6_cyber_q7_correct",
        wrong_label="chapter6_cyber_q7_wrong"
    )
    $ renpy.pause()

label chapter6_cyber_q7_correct:
    narrator "(Tama! Bakit: preventive controls ang nag-aapply ng restrictions para pigilan \nang unauthorized activities bago pa man ito mangyari, tulad ng ID card locks.)"
    scene bg_lab with dissolve
    if player_gender == "male":
        mc_m "(Natapos ko ang resubmission paper. Bawat citation, may totoong section number.)"
        mc_m "(Matagal. Pero tunay na akin.)"
    else:
        mc_f "(Natapos ko ang resubmission paper. Bawat citation, may totoong section number.)"
        mc_f "(Matagal. Pero tunay na akin.)"
    $ grade_change("cyber", 10)
    jump chapter7

label chapter6_cyber_q7_wrong:
    narrator "(Hindi 'yan. Ang preventive controls ang nagpipigil sa unauthorized activities bago pa mangyari, \ngaya ng physical locks. Corrective at recovery ay pagkatapos na ng insidente, compensative ay panandaliang alternative lang.)"
    jump chapter6_cyber_q7