## game/options.rpy
## Core game configuration for A.I. na lang!

define config.name = _("A.I. na lang!")

init -2 python:
    def is_phone():
        # One yes/no for "small touch screen", cached on the function so it is never written into save files.
        # renpy.variant("small") alone is unreliable in a browser (no real DPI),
        # so on web we also ask the browser for the screen size in CSS pixels.
        if hasattr(is_phone, "v"):
            return is_phone.v
        v = bool(renpy.variant(["touch", "small", "mobile"]))
        if not v and renpy.variant("web"):
            try:
                import emscripten
                v = bool(emscripten.run_script_int(
                    "(Math.min(screen.width, screen.height) <= 820 && navigator.maxTouchPoints > 0) ? 1 : 0"))
            except Exception:
                v = False
        is_phone.v = v
        return v

define config.version = "FINAL"

define config.window_title = "A.I. na lang!, A Visual Novel"

default _game_menu_screen = "preferences"

define config.fast_skipping = True

define config.thumbnail_width = 320
define config.thumbnail_height = 180
define config.image_cache_size_mb = 128
define config.predict_statements = 12
define config.rollback_length = 32
init -1 python:
    config.screen_width = 1920
    config.screen_height = 1080

define config.has_music = True

define config.has_sound = True

define config.has_voice = False

define config.main_menu_music = "audio/bgm/bgm_menu.ogg"

define config.save_directory = "ai_na_lang"

define config.history_length = 250

define config.language = None

define config.developer = False

define config.enter_transition = dissolve

define config.exit_transition  = dissolve

define config.window = "auto"

define config.check_conflicting_properties = True

define config.skip_delay = 167

default persistent.text_scale = 1.0

init python:
    def stop_skipping():
        renpy.config.skipping = False
init python:
    def tsz(n):
        return int(n * persistent.text_scale)

init python:
    _preferences.afm_time = 15.0

init python:
    _preferences.skip_unseen = True

init python:
    def safe_play(channel, filename, loop=True):
        if not renpy.loadable(filename):
            return
        try:
            if loop:
                renpy.music.play(filename, channel=channel, loop=True)
            else:
                renpy.music.play(filename, channel=channel, loop=False)
        except Exception:
            pass

    def safe_stop(channel="music"):
        try:
            renpy.music.stop(channel=channel, fadeout=1.0)
        except Exception:
            pass