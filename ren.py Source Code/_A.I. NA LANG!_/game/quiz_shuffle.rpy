## game/quiz_shuffle.rpy
## Shuffles the answer order of every minigame question (Alpha feedback:
## the correct answer was always "A" in Chapter 2, mostly "B" in others).
##
## - The order is a pure function of the question text + a per-playthrough
##   salt, so it never changes on screen refresh, rollback, or save/load.
## - The letter badge (A-D) is drawn by the minigame screen from the
##   position, so the old "A. " prefixes inside the option text are stripped.

default mg_salt = renpy.random.randint(1, 999999)

init python:
    import re
    import zlib
    import random

    def mg_strip(opt):
        ## "A. switchport mode access" -> "switchport mode access"
        return re.sub(r'^[A-Da-d][\.\)]\s+', '', opt, count=1)

    def mg_order(question, n):
        ## Returns a list: position shown -> original index in `options`.
        seed = zlib.crc32(question.encode('utf-8')) ^ store.mg_salt
        order = list(range(n))
        random.Random(seed).shuffle(order)
        return order

    def mg_parse_title(title):
        ## "Midterm Exam, Subnetting (3/7), note"  ->  (category, topic, note, 3, 7)
        parts = [p.strip() for p in title.split(",")]
        cat = parts[0]
        qi = 0
        qn = 0
        clean = []
        for p in parts[1:]:
            m = re.search(r'\((\d+)/(\d+)\)', p)
            if m:
                qi = int(m.group(1))
                qn = int(m.group(2))
                p = re.sub(r'\s*\(\d+/\d+\)', '', p).strip()
            if p:
                clean.append(p)
        topic = clean[0] if clean else ""
        note = ", ".join(clean[1:]) if len(clean) > 1 else ""
        return cat, topic, note, qi, qn

    def quiz_accent(subject):
        ## accent colour per subject (respects colorblind mode)
        if subject == "networking":
            return cb("grade_net")
        if subject == "programming":
            return cb("grade_prog")
        if subject == "cyber":
            return cb("grade_cyber")
        return "#C41230"
