## game/options.rpy
## Core game configuration for A.I. na lang!

define config.name = _("A.I. na lang!")

define config.version = "v1.3"

define config.window_title = "A.I. na lang!, A Visual Novel"

default _game_menu_screen = "preferences"

define config.fast_skipping = True

define config.thumbnail_width = 320
define config.thumbnail_height = 180

init -1 python:
    config.physical_width = 1920
    config.physical_height = 1080
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