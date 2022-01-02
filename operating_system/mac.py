from talon import Context, actions, app, ui
from talon.mac import applescript
import os

ctx = Context()
ctx.matches = r"""
os: mac
"""

ctx.lists["self.launch_command"] = {}


def update_preferences_list():
    preferences = {}
    if app.platform == "mac":
        preferences_path = "/System/Library/PreferencePanes"
        if os.path.isdir(preferences_path):
            for name in os.listdir(preferences_path):
                path = os.path.join(preferences_path, name)

                preferences[
                    os.path.splitext(name)[0]
                ] = f"open -b com.apple.systempreferences {path}"

    ctx.lists["self.launch_command"] = actions.user.create_spoken_forms_from_map(
        preferences, generate_subsequences=False
    )


@ctx.action_class("user")
class UserActionsMac:
    # def exec(command: str):
    #     actions.key("cmd-space")
    #     actions.sleep("150ms")
    #     actions.insert(command)
    #     actions.sleep("150ms")
    #     actions.key("enter")

    def system_shutdown():
        applescript.run(
            r"""
        tell application "Finder"
            shut down
        end tell"""
        )

    def system_restart():
        applescript.run(
            r"""
        tell application "Finder"
            restart
        end tell"""
        )

    def system_hibernate():
        applescript.run(
            r"""
        tell application "Finder"
            sleep
        end tell"""
        )

    def system_lock():
        actions.key("ctrl-cmd-q")

    def system_show_desktop():
        actions.key("shift-f13")

    def system_task_manager():
        ui.launch(path="/System/Applications/Utilities/Activity Monitor.app")

    def system_task_view():
        actions.key("shift-f11")

    def system_switcher():
        actions.key("shift-f11")

    def system_search():
        actions.key("cmd-space")


def on_ready():
    update_preferences_list()


if app.platform == "mac":
    app.register("ready", on_ready)
