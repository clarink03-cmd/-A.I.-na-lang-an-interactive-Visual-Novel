################################################################################
## POST-FINAL-DEFENSE BUILD - HUD logic
##   * build_label: shown on the main menu next to the version
##   * stat_cue():  pop-up whenever Critical Thinking / Motivation changes
##   * toggle_stat_info(): tap a HUD stat to see what it means
################################################################################

define build_label = "Post-Final Defense Build · Major Revisions"

init 11 python:

    def stat_cue(stat, amount):
        """Show the change pop-up. Skipped while skipping, with the HUD hidden, and during
        the tutorial (the tutorial has its own notification)."""
        if not amount:
            return
        if not store.show_hud or store.tutorial_highlight:
            return
        if renpy.is_skipping():
            return
        renpy.show_screen("stat_cue", stat=stat, amount=amount, _tag="stat_cue_" + stat)

    def toggle_stat_info(stat):
        if renpy.get_screen("hud_info"):
            renpy.hide_screen("hud_info")
        else:
            renpy.show_screen("hud_info", stat=stat)

    ## wrap the original stat functions from definitions.rpy so every change shows a cue
    _ct_change_orig = ct_change
    _mot_change_orig = mot_change

    def ct_change(delta):
        old = store.critical_thinking
        _ct_change_orig(delta)
        stat_cue("ct", store.critical_thinking - old)

    def mot_change(delta):
        old = store.motivation
        _mot_change_orig(delta)
        stat_cue("mot", store.motivation - old)
