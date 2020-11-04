from tkinter import *


def direct_entry_pane(self):
    """
    Directly enter fwpw.
    """
    self.logger.info("%s: activated" % inspect.stack()[0][3])

    self.current_key = tkSimpleDialog.askstring(
        "FW Password", "Enter firmware password:", show="*", parent=self.root
    )

    if self.current_key:
        self.keys_loaded = True
        self.calculate_hash()
        self.status_string.set("Keys loaded successfully.")
        self.keys_label["image"] = self.key_icon_photoimage
        self.keys_loaded_string.set("Keys in memory.")
        self.change_state_btn.configure(state="normal")

    else:
        self.flush_keys()
        self.status_string.set("Blank password entered.")
        self.logger.error("Direct enter blank password.")
        self.change_state_btn.configure(state="disabled")
