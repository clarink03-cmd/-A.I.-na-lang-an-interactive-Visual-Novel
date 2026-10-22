################################################################################
## PLAYBACK SPEEDS - Auto-Forward and Skip, as labelled steps (0.5x, 1x, 2x ...)
##
## How Ren'Py works (checked against its source):
##   Auto-Forward waits  ((25 + characters) / 250) * afm_time  seconds per line,
##   so a BIGGER afm_time = SLOWER. (The stock bar also treats its far-right end as
##   "off", which is why the old Auto bar looked backwards.)
##   Skip waits config.skip_delay milliseconds per line, so a SMALLER delay = FASTER.
## Each step below maps a label to the real value. 1x keeps the game's old defaults
## (afm_time 15, skip_delay 167).
################################################################################

default persistent.auto_speed = 1       # index into AUTO_STEPS  (1 = "1x")
default persistent.skip_speed = 0       # index into SKIP_STEPS  (0 = "1x")

init 10 python:

    ## (label, afm_time in seconds per 250 characters)
    AUTO_STEPS = [("0.5x", 30.0), ("1x", 15.0), ("1.5x", 10.0), ("2x", 7.5), ("3x", 5.0)]

    ## (label, config.skip_delay in milliseconds)
    SKIP_STEPS = [("1x", 167), ("2x", 83), ("4x", 42), ("8x", 21), ("Max", 5)]

    AUTO_LABELS = [s[0] for s in AUTO_STEPS]
    SKIP_LABELS = [s[0] for s in SKIP_STEPS]

    def _idx(v, steps, default):
        ## persistent values can still be None while init runs; fall back to the default step
        if v is None:
            return default
        try:
            v = int(v)
        except Exception:
            return default
        return max(0, min(len(steps) - 1, v))

    def apply_speeds():
        a = _idx(persistent.auto_speed, AUTO_STEPS, 1)
        k = _idx(persistent.skip_speed, SKIP_STEPS, 0)
        _preferences.afm_time = AUTO_STEPS[a][1]
        config.skip_delay = SKIP_STEPS[k][1]

    def set_auto_speed(i):
        persistent.auto_speed = i
        apply_speeds()

    def set_skip_speed(i):
        persistent.skip_speed = i
        apply_speeds()

    def cycle_auto_speed():
        set_auto_speed((_idx(persistent.auto_speed, AUTO_STEPS, 1) + 1) % len(AUTO_STEPS))

    def cycle_skip_speed():
        set_skip_speed((_idx(persistent.skip_speed, SKIP_STEPS, 0) + 1) % len(SKIP_STEPS))

    ## runs after options.rpy (which forces afm_time = 15.0 on every launch)
    apply_speeds()
