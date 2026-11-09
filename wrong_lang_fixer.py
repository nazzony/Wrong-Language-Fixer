import json, keyboard, pyperclip, time


# Data Functions
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
            return layouts_dict["dictionary"]

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


config = load_config("dictionaries/config.json")
layouts_dict = load_dictionary("dictionaries/layouts.json")
reverse_layout_dict = create_reverse_dictionary(layouts_dict)

while True:
    keyboard.wait(config["trigger_hotkey"])
    time.sleep(0.5)
    keyboard.send("ctrl + c")
    time.sleep(0.1)
    text_to_fix = pyperclip.paste()
    fixed_text = translate(text_to_fix, layouts_dict, reverse_layout_dict)
    pyperclip.copy(fixed_text)
    time.sleep(0.1)
    keyboard.send("ctrl + v")

