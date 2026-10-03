## game/chapter3.rpy
## Chapter 3, "Submit Mo Na Lang" (Week 3)

label chapter3:
    call screen chapter_title("", "3 : Submit Mo Na Lang", "Week 3, 'Basta may nasubmit...'")
    $ day_label = "Week 3, Umaga"
    $ current_week = 3

    ## ── SCENE 3-1: Mr. Kai's Python debug activity ───────────────────────────
    scene bg_lab with dissolve
    $ safe_play("music", "audio/bgm/bgm_classroom.ogg", loop=True)

    show mr_kai normal at left with dissolve
    mr_kai "Good morning! Okay, for today's debugging activity. May code kayo sa harap ninyo. Broken. I-fix ninyo."
    mr_kai "Twenty minutes. Walang phone, walang AI, walang Google. Sariling utak lang. Go."
    hide mr_kai with dissolve

    if player_gender == "male":
        mc_m "(Tiningnan ko ang pseudo-code sa screen. Maraming bugs na nakatago. May ilan akong nakikilala. Sana.)"
    else:
        mc_f "(Tiningnan ko ang pseudo-code sa screen. Maraming bugs na nakatago. May ilan akong nakikilala. Sana.)"
    narrator "(Inaasahan ni Mr. Kai na mahahanap mo silang lahat. Tignan natin kung kaya mong i-debug ang bawat isa.)"
    jump chapter3_debug_q1

## ── ROUTE A: Programming Debug Minigame (7 questions) ───────────────────────
## Source: Python Essentials exam bank

label chapter3_debug_q1:
    show screen minigame(
        "Programming, Python Debug Challenge (1/7)",
        "What error will this code produce?\n\ndef greet(name):\n    print('Hello, ' + name)\n\ngreet(123)",
        [
            "A. The function name 'greet' is invalid",
            "B. TypeError: cannot concatenate str and int",
            "C. No error, it will run fine",
            "D. IndentationError inside the function"
        ],
        1,
        "programming",
        8,
        5,
        correct_label="chapter3_debug_q1_correct",
        wrong_label="chapter3_debug_q1_wrong"
    )
    $ renpy.pause()

label chapter3_debug_q1_correct:
    narrator "(Tama! Bakit: hindi puwedeng pag-dugtungin ang string at int gamit ang '+' operator nang walang explicit conversion.)"
    jump chapter3_debug_q2

label chapter3_debug_q1_wrong:
    narrator "(Hindi 'yan. Mahigpit ang Python sa paghahalo ng data types gamit ang '+' operator. Hindi puwedeng sabayin ang string at integer.)"
    jump chapter3_debug_q1

## ── Question 2: IndentationError ─────────────────────────────────────────────
label chapter3_debug_q2:
    show screen minigame(
        "Programming, Python Debug Challenge (2/7)",
        "What error will this code produce?\n\ndef check_number(x):\n    if x > 0:\n    print('Positive')\n    else:\n        print('Not positive')",
        [
            "A. SyntaxError: invalid syntax",
            "B. IndentationError: expected an indented block",
            "C. NameError: x is not defined",
            "D. ZeroDivisionError: division by zero"
        ],
        1,
        "programming",
        8,
        5,
        correct_label="chapter3_debug_q2_correct",
        wrong_label="chapter3_debug_q2_wrong"
    )
    $ renpy.pause()

label chapter3_debug_q2_correct:
    narrator "(Tama! Bakit: kailangang naka-indent ang 'print' statement pagkatapos ng 'if'. \nGinagamit ng Python ang indentation para i-define ang code blocks.)"
    jump chapter3_debug_q3

label chapter3_debug_q2_wrong:
    narrator "(Hindi 'yan. Tingnan ang linya pagkatapos ng 'if x > 0:', \ndapat naka-indent 'yon pero hindi. Mahalaga sa Python ang whitespace.)"
    jump chapter3_debug_q2

## ── Question 3: NameError (undefined variable) ───────────────────────────────
label chapter3_debug_q3:
    show screen minigame(
        "Programming, Python Debug Challenge (3/7)",
        "What error will this code produce?\n\ndef calculate():\n    result = a + b\n    return result\n\nprint(calculate())",
        [
            "A. SyntaxError: invalid syntax",
            "B. NameError: name 'a' is not defined",
            "C. TypeError: unsupported operand type",
            "D. ValueError: not enough values to unpack"
        ],
        1,
        "programming",
        8,
        5,
        correct_label="chapter3_debug_q3_correct",
        wrong_label="chapter3_debug_q3_wrong"
    )
    $ renpy.pause()

label chapter3_debug_q3_correct:
    narrator "(Tama! Bakit: hindi pa na-define ang 'a' at 'b' bago gamitin. Nag-raraise ang Python ng NameError.)"
    jump chapter3_debug_q4

label chapter3_debug_q3_wrong:
    narrator "(Hindi 'yan. Ginagamit ang 'a' at 'b' nang hindi pa naibibigay ang value nila. \nHindi alam ng Python kung ano ang tinutukoy nila.)"
    jump chapter3_debug_q3

## ── Question 4: IndexError (list out of range) ───────────────────────────────
label chapter3_debug_q4:
    show screen minigame(
        "Programming, Python Debug Challenge (4/7)",
        "What error will this code produce?\n\nnumbers = [[10, 20, 30]]\nprint(numbers[[3]])",
        [
            "A. IndexError: list index out of range",
            "B. KeyError: key not found",
            "C. TypeError: list indices must be integers",
            "D. ZeroDivisionError: division by zero"
        ],
        0,
        "programming",
        8,
        5,
        correct_label="chapter3_debug_q4_correct",
        wrong_label="chapter3_debug_q4_wrong"
    )
    $ renpy.pause()

label chapter3_debug_q4_correct:
    narrator "(Tama! Bakit: 0, 1, at 2 lang ang indices ng listahan. Wala sa index 3, kaya IndexError ang lalabas.)"
    jump chapter3_debug_q5

label chapter3_debug_q4_wrong:
    narrator "(Isipin muli. Zero-indexed ang mga listahan sa Python. \nAng listahan na may tatlong elemento ay may indices 0, 1, at 2 lang. Ano ang mangyayari sa index 3?)"
    jump chapter3_debug_q4

## ── Question 5: SyntaxError (missing colon) ──────────────────────────────────
label chapter3_debug_q5:
    show screen minigame(
        "Programming, Python Debug Challenge (5/7)",
        "What error will this code produce?\n\nscore = 85\nif score >= 75\n    print('Passing')",
        [
            "A. SyntaxError: expected ':' after 'if' condition",
            "B. NameError: score is not defined",
            "C. IndentationError: unexpected indent",
            "D. TypeError: '>=' not supported"
        ],
        0,
        "programming",
        8,
        5,
        correct_label="chapter3_debug_q5_correct",
        wrong_label="chapter3_debug_q5_wrong"
    )
    $ renpy.pause()

label chapter3_debug_q5_correct:
    narrator "(Tama! Bakit: bawat compound statement gaya ng 'if', 'for', \n'while' ay kailangan ng colon sa dulo ng condition line.)"
    jump chapter3_debug_q6

label chapter3_debug_q5_wrong:
    narrator "(Hindi 'yan. Tingnan ang linya ng 'if', may kulang sa dulo. \nInaasahan ng Python ang colon pagkatapos ng condition sa mga compound statement.)"
    jump chapter3_debug_q5

## ── Question 6: print() with undefined names ──────────────────────────────
## Source: Python Essentials bank, Q35
label chapter3_debug_q6:
    show screen minigame(
        "Programming, Python Debug Challenge (6/7)",
        "What will happen when you attempt to run this code?\n\nprint(Hello, World!)",
        [
            "A. It will print Hello, World! to the console",
            "B. SyntaxError",
            "C. TypeError",
            "D. AttributeError"
        ],
        1,
        "programming",
        8,
        5,
        correct_label="chapter3_debug_q6_correct",
        wrong_label="chapter3_debug_q6_wrong"
    )
    $ renpy.pause()

label chapter3_debug_q6_correct:
    narrator "(Tama! Bakit: walang quotes ang 'Hello, World!' kaya tinuturing itong \ninvalid na expression ng Python, hindi text. SyntaxError agad, hindi pa nga nag-run.)"
    jump chapter3_debug_q7

label chapter3_debug_q6_wrong:
    narrator "(Hindi 'yan. Walang quotation marks ang 'Hello, World!' dito, kaya hindi ito valid na string. \nHindi nga makaka-run ang code para magkaroon pa ng runtime error.)"
    jump chapter3_debug_q6

## ── Question 7: Tuple Immutability ──────────────────────────────────────────
## Source: Python Essentials bank, Q19
label chapter3_debug_q7:
    show screen minigame(
        "Programming, Python Debug Challenge (7/7)",
        "Assuming my_tuple is a correctly created tuple, what happens\nwhen this line runs?\n\nmy_tuple[1] = my_tuple[1] + my_tuple[0]",
        [
            "A. It runs fine if the tuple has at least two elements",
            "B. It is illegal",
            "C. It is fully correct",
            "D. It may be illegal only if the tuple contains strings"
        ],
        1,
        "programming",
        8,
        5,
        correct_label="chapter3_debug_q7_correct",
        wrong_label="chapter3_debug_q7_wrong"
    )
    $ renpy.pause()

label chapter3_debug_q7_correct:
    narrator "(Tama! Bakit: immutable ang tuples sa Python. \nHindi mo mababago ang laman nito pagkatapos itong magawa, kahit ano pang laman ang element.)"
    narrator "(Kumpleto na ang pitong bugs. Malamang, proud si Mr. Kai sa debugging skills mo ngayon.)"
    jump chapter3_post_minigame

label chapter3_debug_q7_wrong:
    narrator "(Hindi 'yan. Immutable ang tuples, kahit anong laman meron ito. \nHindi ito depende sa bilang ng elemento o kung strings ba ang laman.)"
    jump chapter3_debug_q7

## ── Return point after all 7 questions ───────────────────────────────────────
label chapter3_post_minigame:
    scene bg_lab with dissolve
    $ safe_play("music", "audio/bgm/bgm_classroom.ogg", loop=True)

    show mr_kai normal at left with dissolve
    mr_kai "Okay, time. Let's check the scoreboard."
    narrator "(Lumitaw ang mga pangalan sa screen. Nasa gitna ang sa'yo. \nHindi pinaka-mataas. Hindi rin pinaka-mababa.)"
    mr_kai "Good progress, everyone. Pero gusto ko pa ring makita 'yung individual approach niyo. \nHindi lahat ng sagot ay oo o hindi, minsan mas mahalaga 'yung proseso."
    hide mr_kai with dissolve

    ## ── SCENE 3-2: Canteen halftime check-in ────────────────────────────────
    scene bg_canteen with dissolve
    $ safe_play("music", "audio/bgm/bgm_canteen.ogg", loop=True)
    $ day_label = "Week 3, Tanghali"

    narrator "(Hapon. Nasa canteen ang grupo. Si Rey, na hindi karaniwang nagsasalita, ay may sasabihin ngayon.)"

    show rey normal at left with moveinleft
    show kent normal at center with dissolve
    show gabby normal at right with moveinright

    rey "...Nakita ko yung submission ni Gabby."
    narrator "(Tahimik. Lahat tumingin kay Rey.)" with vpunch
    rey "Pareho ng sagot namin sa debugging activity. Word for word. Pero hindi tayo nag-usap."
    gabby "Coincidence lang 'yan. Pareho naman ang bugs, pareho ang solusyon."
    rey "Hindi ko sinasabi na kinopya mo. \nSinasabi ko lang, parehong solusyon. Ganoon talaga kapag AI ang nagbigay ng sagot."
    kent "Urm, technically, valid observation 'yan tungkol sa AI output homogeneity,"
    gabby "Okay, sige, patunayan mo."
    hide gabby with dissolve

    if player_bestfriend == "carl":
        show carl normal at right with moveinright
    else:
        show carly normal at right with moveinright

    if player_gender == "male":
        mc_m "(Napansin kong tinitigan ako ni [player_bestfriend].)"
    else:
        mc_f "(Napansin kong tinitigan ako ni [player_bestfriend].)"

    if player_bestfriend == "carl":
        carl "(mababa) Ikaw... sarili mo ba ang ginawa mo?"
    else:
        carly "(mababa) Ano sa tingin mo, tama ba si Rey?"

    ## CHOICE NODE 3-A
    menu:
        "Oo, sarili ko. Kahit na medyo mahirap.":
            $ ct_change(2)
            if player_gender == "male":
                mc_m "Sarili ko. Bagal ko nga ng kalahati ng klase, pero sarili ko."
            else:
                mc_f "Sarili ko. May mga parts na kinailangan ko ng tulong mula sa notes, pero sarili ko."
            if player_bestfriend == "carl":
                carl "(huminga sya ng malalim) Okay. Good."
            else:
                carly "(ngumiti) Sige. Ganoon talaga dapat."
            if player_gender == "male":
                mc_m "(Nag-move on ang grupo. Pero sa isip ko, sigurado ba talaga ako?)"
            else:
                mc_f "(Nag-move on ang grupo. Pero sa isip ko, sigurado ba talaga ako?)"

        "...Mostly. May AI-assisted na parts.":
            $ ct_change(-1)
            if player_gender == "male":
                mc_m "Mostly sarili ko. May isang part na kinonsulta ko sa AI."
            else:
                mc_f "Mostly. May napagod ako at pinag-AI ang isang section."
            if player_bestfriend == "carl":
                carl "Basta wag maging habit, okay? Mapapansin ni Sir 'yan."
            else:
                carly "Ingat ka lang. Matalino si Mr. Kai. Mapapansin niya."
            if player_gender == "male":
                mc_m "(Tama sila. At alam kong tama sila.)"
            else:
                mc_f "(Tama sila. At alam kong tama sila.)"

        "Huwag mo nang alamin.":
            $ ct_change(-4)
            $ mot_change(-2)
            if player_gender == "male":
                mc_m "Huwag mo nalang alamin."
            else:
                mc_f "Huwag mo nalang alamin."
            if player_bestfriend == "carl":
                carl "...Sige."
            else:
                carly "...Okay."
            if player_gender == "male":
                mc_m "(Binalewala ko siya. Pero hindi siya tumitigil sa pagmasid sa akin.)"
            else:
                mc_f "(Binalewala ko siya. Pero hindi siya tumitigil sa pagmasid sa akin.)"

    hide rey with dissolve
    hide kent with dissolve
    if player_bestfriend == "carl":
        hide carl with dissolve
    else:
        hide carly with dissolve

    ## ── SCENE 3-3: Rey's warning ─────────────────────────────────────────────
    scene bg_hallway with dissolve
    $ day_label = "Week 3, Hapon"

    show rey normal at center with dissolve
    if player_gender == "male":
        mc_m "(Naabutan ako ni Rey sa hallway pagkatapos ng klase.)"
    else:
        mc_f "(Naabutan ako ni Rey sa hallway pagkatapos ng klase.)"
    rey "Hindi kita kinokontra. Alam ko kung bakit ginagawa 'yun ng mga tao."
    rey "Pero may napansin ako. Kapag puro AI na ang sumasagot, \nhindi ka na nagtatanong ng sarili mong mga tanong."
    rey "At 'yung mga sariling tanong, 'yun 'yung hindi kayang sagutin ng AI."

    if player_gender == "male":
        mc_m "(Lumakad na siya bago pa ako makasagot. \nHindi ko alam kung ano'ng sasabihin ko kung nagawa ko man.)"
    else:
        mc_f "(Lumakad na siya bago pa ako makasagot. \nHindi ko alam kung ano'ng sasabihin ko kung nagawa ko man.)"
    hide rey with dissolve
    jump chapter4