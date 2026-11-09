import json, keyboard, pyperclip, time, os, platform, sys


# Data Functions
def get_resource_path(relative_path: str) -> str:
    """
    Finds the file path whether running as a normal script,
    with an external folder, or bundled inside a PyInstaller executable.
    """
    # 1. Check if an external file exists next to the executable/script first
    if getattr(sys, "frozen", False):
        app_dir = os.path.dirname(sys.executable)
    else:
        app_dir = os.path.dirname(os.path.abspath(__file__))

    external_path = os.path.join(app_dir, relative_path)
    if os.path.exists(external_path):
        return external_path

    # 2. Fall back to the bundled PyInstaller temporary directory
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)

    return relative_path


def load_config(filepath: str) -> dict:
    """
    :param filepath:
    :return:  dict
    """
    try:
        with open(filepath, mode="r", encoding="utf-8") as json_file:
            config = json.load(json_file)
            return config
    except FileNotFoundError:
        print("File Wasn't Found")
        return {}


def load_dictionary(filepath: str) -> dict:
    """
    :param filepath:
    :return: dictionary
    """
    try:
        with open(filepath, mode="r", encoding="utf-8") as json_file:

            layouts_dict = json.load(json_file)
            return layouts_dict.get("dictionary", {})

    except FileNotFoundError:
        print("File Wasn't Found")
        return {}


def create_reverse_dictionary(layouts_dict: dict) -> dict:
    reverse_dict = dict()
    for a, b in layouts_dict.items():
        reverse_dict[b] = a
    return reverse_dict


def translate(gib_text: str, layouts_dict: dict, reverse_layout_dict: dict) -> str:
    """
    :param gib_text:
    :return: new_str
    """
    new_str = ""

    active_dict = layouts_dict

    for char in gib_text:
        char_id = ord(char)

        if char_id > 1000:
            active_dict = reverse_layout_dict
            break
        elif (65 <= char_id <= 90) or (97 <= char_id <= 122):
            active_dict = layouts_dict
            break

    for char in gib_text:
        if char in active_dict: new_str += active_dict[char]
        else: new_str += char

    return new_str

def main():
    config_path = get_resource_path(os.path.join("dictionaries", "config.json"))
    layouts_path = get_resource_path(os.path.join("dictionaries", "layouts.json"))

    config = load_config(config_path)
    layouts_dict = load_dictionary(layouts_path)

    if not layouts_dict:
        print("Error: Layout dictionary is empty or missing. Exiting.")
        return

    reverse_layout_dict = create_reverse_dictionary(layouts_dict)
    trigger_hotkey = config.get("trigger_hotkey", "ctrl+shift+l")

    # Detect OS for proper copy/paste shortcuts
    is_mac = platform.system() == "Darwin"
    copy_shortcut = "command+c" if is_mac else "ctrl+c"
    paste_shortcut = "command+v" if is_mac else "ctrl+v"

    print(f"Wrong Language Fixer is running ({platform.system()}). Press '{trigger_hotkey}' to fix highlighted text.")

    while True:
        keyboard.wait(trigger_hotkey)
        time.sleep(0.5)

        pyperclip.copy("")
        keyboard.send(copy_shortcut)
        time.sleep(0.1)

        text_to_fix = pyperclip.paste()
        if text_to_fix:
            fixed_text = translate(text_to_fix, layouts_dict, reverse_layout_dict)
            pyperclip.copy(fixed_text)
            time.sleep(0.1)
            keyboard.send(paste_shortcut)


if __name__ == "__main__":
    main()