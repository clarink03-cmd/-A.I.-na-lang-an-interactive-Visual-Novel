# TODO: Translation updated at 2026-09-17 11:12

# game/chapter3.rpy:14
translate english chapter3_403cd512:

    # mr_kai "Good morning! Okay, for today's debugging activity. May code kayo sa harap ninyo. Broken. I-fix ninyo."
    mr_kai "Good morning! Okay, for today's debugging activity. You have code in front of you. It's broken. Fix it."

# game/chapter3.rpy:15
translate english chapter3_9eef8014:

    # mr_kai "Twenty minutes. Walang phone, walang AI, walang Google. Sariling utak lang. Go."
    mr_kai "Twenty minutes. No phones, no AI, no Google. Just your own brain. Go."

# game/chapter3.rpy:19
translate english chapter3_3ca47b9c:

    # mc_m "(Tiningnan ko ang pseudo-code sa screen. Maraming bugs na nakatago. May ilan akong nakikilala. Sana.)"
    mc_m "(I looked at the pseudo-code on screen. Lots of bugs hiding in there. I recognize a few. Hopefully.)"

# game/chapter3.rpy:21
translate english chapter3_84a54d5a:

    # mc_f "(Tiningnan ko ang pseudo-code sa screen. Maraming bugs na nakatago. May ilan akong nakikilala. Sana.)"
    mc_f "(I looked at the pseudo-code on screen. Lots of bugs hiding in there. I recognize a few. Hopefully.)"

# game/chapter3.rpy:22
translate english chapter3_3e1788ff:

    # narrator "(Inaasahan ni Mr. Kai na mahahanap mo silang lahat. Tignan natin kung kaya mong i-debug ang bawat isa.)"
    narrator "(Mr. Kai expects you to find all of them. Let's see if you can debug each one.)"

# game/chapter3.rpy:48
translate english chapter3_debug_q1_correct_4a177c1f:

    # narrator "(Tama! Bakit: hindi puwedeng pag-dugtungin ang string at int gamit ang '+' operator nang walang explicit conversion.)"
    narrator "(Correct! Why: you can't concatenate a string and an int using the '+' operator without an explicit conversion.)"

# game/chapter3.rpy:52
translate english chapter3_debug_q1_wrong_20a6f41b:

    # narrator "(Hindi 'yan. Mahigpit ang Python sa paghahalo ng data types gamit ang '+' operator. Hindi puwedeng sabayin ang string at integer.)"
    narrator "(Not that one. Python is strict about mixing data types with the '+' operator. You can't combine a string and an integer directly.)"

# game/chapter3.rpy:76
translate english chapter3_debug_q2_correct_86609c09:

    # narrator "(Tama! Bakit: kailangang naka-indent ang 'print' statement pagkatapos ng 'if'. \nGinagamit ng Python ang indentation para i-define ang code blocks.)"
    narrator "(Correct! Why: the 'print' statement after 'if' needs to be indented. \nPython uses indentation to define code blocks.)"

# game/chapter3.rpy:80
translate english chapter3_debug_q2_wrong_fdf6e6f3:

    # narrator "(Hindi 'yan. Tingnan ang linya pagkatapos ng 'if x > 0:', \ndapat naka-indent 'yon pero hindi. Mahalaga sa Python ang whitespace.)"
    narrator "(Not that one. Look at the line after 'if x > 0:', \nit should be indented but it isn't. Whitespace matters in Python.)"

# game/chapter3.rpy:104
translate english chapter3_debug_q3_correct_ea7a00ec:

    # narrator "(Tama! Bakit: hindi pa na-define ang 'a' at 'b' bago gamitin. Nag-raraise ang Python ng NameError.)"
    narrator "(Correct! Why: 'a' and 'b' weren't defined before being used. Python raises a NameError.)"

# game/chapter3.rpy:108
translate english chapter3_debug_q3_wrong_12c1bd9e:

    # narrator "(Hindi 'yan. Ginagamit ang 'a' at 'b' nang hindi pa naibibigay ang value nila. \nHindi alam ng Python kung ano ang tinutukoy nila.)"
    narrator "(Not that one. 'a' and 'b' are used before they're given a value. \nPython has no idea what they're supposed to refer to.)"

# game/chapter3.rpy:132
translate english chapter3_debug_q4_correct_3f5f27dc:

    # narrator "(Tama! Bakit: 0, 1, at 2 lang ang indices ng listahan. Wala sa index 3, kaya IndexError ang lalabas.)"
    narrator "(Correct! Why: 0, 1, and 2 are the only indices in the list. There's nothing at index 3, so it throws an IndexError.)"

# game/chapter3.rpy:136
translate english chapter3_debug_q4_wrong_c6710cdd:

    # narrator "(Isipin muli. Zero-indexed ang mga listahan sa Python. \nAng listahan na may tatlong elemento ay may indices 0, 1, at 2 lang. Ano ang mangyayari sa index 3?)"
    narrator "(Think again. Lists in Python are zero-indexed. \nA list with three elements only has indices 0, 1, and 2. What happens at index 3?)"

# game/chapter3.rpy:160
translate english chapter3_debug_q5_correct_88152f87:

    # narrator "(Tama! Bakit: bawat compound statement gaya ng 'if', 'for', \n'while' ay kailangan ng colon sa dulo ng condition line.)"
    narrator "(Correct! Why: every compound statement like 'if', 'for', \n'while' needs a colon at the end of the condition line.)"

# game/chapter3.rpy:164
translate english chapter3_debug_q5_wrong_7ad42def:

    # narrator "(Hindi 'yan. Tingnan ang linya ng 'if', may kulang sa dulo. \nInaasahan ng Python ang colon pagkatapos ng condition sa mga compound statement.)"
    narrator "(Not that one. Look at the 'if' line, something's missing at the end. \nPython expects a colon after the condition in compound statements.)"

# game/chapter3.rpy:189
translate english chapter3_debug_q6_correct_ff079a86:

    # narrator "(Tama! Bakit: walang quotes ang 'Hello, World!' kaya tinuturing itong \ninvalid na expression ng Python, hindi text. SyntaxError agad, hindi pa nga nag-run.)"
    narrator "(Correct! Why: 'Hello, World!' has no quotes, so Python treats it as \nan invalid expression, not text. It's a SyntaxError right away, before it even runs.)"

# game/chapter3.rpy:193
translate english chapter3_debug_q6_wrong_10cbf1b1:

    # narrator "(Hindi 'yan. Walang quotation marks ang 'Hello, World!' dito, kaya hindi ito valid na string. \nHindi nga makaka-run ang code para magkaroon pa ng runtime error.)"
    narrator "(Not that one. There are no quotation marks around 'Hello, World!' here, so it isn't a valid string. \nThe code won't even run far enough to hit a runtime error.)"

# game/chapter3.rpy:218
translate english chapter3_debug_q7_correct_be9e8ba8:

    # narrator "(Tama! Bakit: immutable ang tuples sa Python. \nHindi mo mababago ang laman nito pagkatapos itong magawa, kahit ano pang laman ang element.)"
    narrator "(Correct! Why: tuples are immutable in Python. \nYou can't change their contents once they're created, no matter what the elements are.)"

# game/chapter3.rpy:219
translate english chapter3_debug_q7_correct_71b82828:

    # narrator "(Kumpleto na ang pitong bugs. Malamang, proud si Mr. Kai sa debugging skills mo ngayon.)"
    narrator "(All seven bugs are cleared. Mr. Kai's probably proud of your debugging skills right now.)"

# game/chapter3.rpy:223
translate english chapter3_debug_q7_wrong_b2b1fbb1:

    # narrator "(Hindi 'yan. Immutable ang tuples, kahit anong laman meron ito. \nHindi ito depende sa bilang ng elemento o kung strings ba ang laman.)"
    narrator "(Not that one. Tuples are immutable no matter what they contain. \nIt doesn't depend on the number of elements or whether they're strings.)"

# game/chapter3.rpy:232
translate english chapter3_post_minigame_c4df3983:

    # mr_kai "Okay, time. Let's check the scoreboard."
    mr_kai "Okay, time. Let's check the scoreboard."

# game/chapter3.rpy:233
translate english chapter3_post_minigame_d204b768:

    # narrator "(Lumitaw ang mga pangalan sa screen. Nasa gitna ang sa'yo. \nHindi pinaka-mataas. Hindi rin pinaka-mababa.)"
    narrator "(Names popped up on screen. Yours is right in the middle. \nNot the highest. Not the lowest either.)"

# game/chapter3.rpy:234
translate english chapter3_post_minigame_471be2ce:

    # mr_kai "Good progress, everyone. Pero gusto ko pa ring makita 'yung individual approach niyo. \nHindi lahat ng sagot ay oo o hindi, minsan mas mahalaga 'yung proseso."
    mr_kai "Good progress, everyone. But I still want to see your individual approach. \nNot every answer is a yes or no, sometimes the process matters more."

# game/chapter3.rpy:242
translate english chapter3_post_minigame_497269b5:

    # narrator "(Hapon. Nasa canteen ang grupo. Si Rey, na hindi karaniwang nagsasalita, ay may sasabihin ngayon.)"
    narrator "(Afternoon. The group's at the canteen. Rey, who doesn't usually talk much, has something to say today.)"

# game/chapter3.rpy:248
translate english chapter3_post_minigame_26f63687:

    # rey "...Nakita ko yung submission ni Gabby."
    rey "...I saw Gabby's submission."

# game/chapter3.rpy:249
translate english chapter3_post_minigame_4df9dabd:

    # narrator "(Tahimik. Lahat tumingin kay Rey.)" with vpunch
    narrator "(Silence. Everyone looks at Rey.)" with vpunch

# game/chapter3.rpy:250
translate english chapter3_post_minigame_9c377fd4:

    # rey "Pareho ng sagot namin sa debugging activity. Word for word. Pero hindi tayo nag-usap."
    rey "Our answers to the debugging activity were identical. Word for word. But we never talked."

# game/chapter3.rpy:251
translate english chapter3_post_minigame_4f36009f:

    # gabby "Coincidence lang 'yan. Pareho naman ang bugs, pareho ang solusyon."
    gabby "That's just a coincidence. Same bugs, same fix."

# game/chapter3.rpy:252
translate english chapter3_post_minigame_fd2cd97e:

    # rey "Hindi ko sinasabi na kinopya mo. \nSinasabi ko lang, parehong solusyon. Ganoon talaga kapag AI ang nagbigay ng sagot."
    rey "I'm not saying you copied. \nI'm just saying, identical answers. That's what happens when AI gives you the solution."

# game/chapter3.rpy:253
translate english chapter3_post_minigame_d069d3da:

    # kent "Urm, technically, valid observation 'yan tungkol sa AI output homogeneity,"
    kent "Um, technically, that's a valid observation about AI output homogeneity,"

# game/chapter3.rpy:254
translate english chapter3_post_minigame_1fc431aa:

    # gabby "Okay, sige, patunayan mo."
    gabby "Okay, fine, prove it."

# game/chapter3.rpy:263
translate english chapter3_post_minigame_9c761d47:

    # mc_m "(Napansin kong tinitigan ako ni [player_bestfriend].)"
    mc_m "(I noticed [player_bestfriend] staring at me.)"

# game/chapter3.rpy:265
translate english chapter3_post_minigame_a4ccc945:

    # mc_f "(Napansin kong tinitigan ako ni [player_bestfriend].)"
    mc_f "(I noticed [player_bestfriend] staring at me.)"

# game/chapter3.rpy:268
translate english chapter3_post_minigame_121f1e70:

    # carl "(mababa) Ikaw... sarili mo ba ang ginawa mo?"
    carl "(quietly) You... did you do yours yourself?"

# game/chapter3.rpy:270
translate english chapter3_post_minigame_2d462f1c:

    # carly "(mababa) Ano sa tingin mo, tama ba si Rey?"
    carly "(quietly) What do you think, is Rey right?"

# game/chapter3.rpy:277
translate english chapter3_post_minigame_f6481add:

    # mc_m "Sarili ko. Bagal ko nga ng kalahati ng klase, pero sarili ko."
    mc_m "On my own. Sure, I was half the class slower, but it's on my own."

# game/chapter3.rpy:279
translate english chapter3_post_minigame_94a35cd2:

    # mc_f "Sarili ko. May mga parts na kinailangan ko ng tulong mula sa notes, pero sarili ko."
    mc_f "On my own. There were parts where I needed help from my notes, but it's on my own."

# game/chapter3.rpy:281
translate english chapter3_post_minigame_33b7da25:

    # carl "(huminga sya ng malalim) Okay. Good."
    carl "(takes a deep breath) Okay. Good."

# game/chapter3.rpy:283
translate english chapter3_post_minigame_636b8570:

    # carly "(ngumiti) Sige. Ganoon talaga dapat."
    carly "(smiles) Alright. That's how it should be."

# game/chapter3.rpy:285
translate english chapter3_post_minigame_3fea581c:

    # mc_m "(Nag-move on ang grupo. Pero sa isip ko, sigurado ba talaga ako?)"
    mc_m "(The group moved on. But in my head — am I really sure?)"

# game/chapter3.rpy:287
translate english chapter3_post_minigame_73e12101:

    # mc_f "(Nag-move on ang grupo. Pero sa isip ko, sigurado ba talaga ako?)"
    mc_f "(The group moved on. But in my head — am I really sure?)"

# game/chapter3.rpy:292
translate english chapter3_post_minigame_d26db091:

    # mc_m "Mostly sarili ko. May isang part na kinonsulta ko sa AI."
    mc_m "Mostly my own. There was one part I checked with AI."

# game/chapter3.rpy:294
translate english chapter3_post_minigame_d28db0bb:

    # mc_f "Mostly. May napagod ako at pinag-AI ang isang section."
    mc_f "Mostly. I got tired at one point and had AI handle one section."

# game/chapter3.rpy:296
translate english chapter3_post_minigame_009ffadc:

    # carl "Basta wag maging habit, okay? Mapapansin ni Sir 'yan."
    carl "Just don't let it become a habit, okay? Sir will notice."

# game/chapter3.rpy:298
translate english chapter3_post_minigame_ca3c77f9:

    # carly "Ingat ka lang. Matalino si Mr. Kai. Mapapansin niya."
    carly "Just be careful. Mr. Kai's sharp. He'll notice."

# game/chapter3.rpy:300
translate english chapter3_post_minigame_89db39ce:

    # mc_m "(Tama sila. At alam kong tama sila.)"
    mc_m "(They're right. And I know they're right.)"

# game/chapter3.rpy:302
translate english chapter3_post_minigame_e7d56d2f:

    # mc_f "(Tama sila. At alam kong tama sila.)"
    mc_f "(They're right. And I know they're right.)"

# game/chapter3.rpy:308
translate english chapter3_post_minigame_926ec155:

    # mc_m "Huwag mo nalang alamin."
    mc_m "Better if you don't know."

# game/chapter3.rpy:310
translate english chapter3_post_minigame_de53fb45:

    # mc_f "Huwag mo nalang alamin."
    mc_f "Better if you don't know."

# game/chapter3.rpy:312
translate english chapter3_post_minigame_a44a7bc3:

    # carl "...Sige."
    carl "...Alright."

# game/chapter3.rpy:314
translate english chapter3_post_minigame_2e0cb36b:

    # carly "...Okay."
    carly "...Okay."

# game/chapter3.rpy:316
translate english chapter3_post_minigame_3d0814f3:

    # mc_m "(Binalewala ko siya. Pero hindi siya tumitigil sa pagmasid sa akin.)"
    mc_m "(I brushed it off. But he didn't stop watching me.)"

# game/chapter3.rpy:318
translate english chapter3_post_minigame_2ebbba95:

    # mc_f "(Binalewala ko siya. Pero hindi siya tumitigil sa pagmasid sa akin.)"
    mc_f "(I brushed it off. But he didn't stop watching me.)"

# game/chapter3.rpy:333
translate english chapter3_post_minigame_b406b676:

    # mc_m "(Naabutan ako ni Rey sa hallway pagkatapos ng klase.)"
    mc_m "(Rey caught up with me in the hallway after class.)"

# game/chapter3.rpy:335
translate english chapter3_post_minigame_d9847328:

    # mc_f "(Naabutan ako ni Rey sa hallway pagkatapos ng klase.)"
    mc_f "(Rey caught up with me in the hallway after class.)"

# game/chapter3.rpy:336
translate english chapter3_post_minigame_ab517084:

    # rey "Hindi kita kinokontra. Alam ko kung bakit ginagawa 'yun ng mga tao."
    rey "I'm not against you. I know why people do it."

# game/chapter3.rpy:337
translate english chapter3_post_minigame_3801dd59:

    # rey "Pero may napansin ako. Kapag puro AI na ang sumasagot, \nhindi ka na nagtatanong ng sarili mong mga tanong."
    rey "But I noticed something. When AI answers everything for you, \nyou stop asking your own questions."

# game/chapter3.rpy:338
translate english chapter3_post_minigame_633a198e:

    # rey "At 'yung mga sariling tanong, 'yun 'yung hindi kayang sagutin ng AI."
    rey "And those questions of your own, those are the ones AI can't answer for you."

# game/chapter3.rpy:341
translate english chapter3_post_minigame_a7922fad:

    # mc_m "(Lumakad na siya bago pa ako makasagot. \nHindi ko alam kung ano'ng sasabihin ko kung nagawa ko man.)"
    mc_m "(He walked off before I could respond. \nI didn't know what I would have said, even if I'd had the chance.)"

# game/chapter3.rpy:343
translate english chapter3_post_minigame_1578b63b:

    # mc_f "(Lumakad na siya bago pa ako makasagot. \nHindi ko alam kung ano'ng sasabihin ko kung nagawa ko man.)"
    mc_f "(He walked off before I could respond. \nI didn't know what I would have said, even if I'd had the chance.)"

translate english strings:

    # game/chapter3.rpy:274
    old "Oo, sarili ko. Kahit na medyo mahirap."
    new "Yes, my own. Even if it was a bit hard."

    # game/chapter3.rpy:289
    old "...Mostly. May AI-assisted na parts."
    new "...Mostly. Some parts were AI-assisted."

    # game/chapter3.rpy:304
    old "Huwag mo nang alamin."
    new "Better if you don't know."

