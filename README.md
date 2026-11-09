# Wrong Language Fixer

A lightweight desktop utility to instantly fix text typed in the wrong keyboard layout. Highlight the gibberish, press a hotkey, and the text translates back. Supports English and Ukrainian out of the box.

## 🚀 Installation (For Regular Users)

You do not need to install Python to use this tool.

1. Go to the **Releases** page on the right side of this repository.
2. Download the version for your operating system (Windows `.exe`, macOS binary, or Linux binary).
3. Double-click to run the application. It will run silently in the background.

## ⌨️ How to Use

1. Start typing in the wrong layout by mistake (e.g., typing `ghbdtn` instead of `привіт`).
2. Highlight the incorrect text.
3. Press **`Ctrl + Shift + L`** (Windows/Linux) or **`Cmd + Shift + L`** (macOS).
4. The script will instantly swap the characters and replace the text.

## ⚙️ Configuration

By default, the application runs using the bundled `Ctrl+Shift+L` hotkey and English/Ukrainian dictionary.

To customize the app, create a folder named `dictionaries` in the exact same directory as your downloaded executable. Place these two files inside:

**1. `config.json`** (To change the hotkey)

```json
{
  "trigger_hotkey": "alt+t"
}
```

**2. `layouts.json`** (To modify character mappings)

```json
{
  "dictionary": {
    "q": "й",
    "w": "ц"
  }
}
```

> **Note:** If the `dictionaries` folder is present next to the executable, the app will prioritize it over the built-in defaults.

## 💻 OS-Specific Notes

* **Windows:** Works immediately out of the box.
* **macOS:** Apple's security model requires you to grant the app **Accessibility permissions** before it can read hotkeys. Go to *System Settings > Privacy & Security > Accessibility* and toggle the app on.
* **Linux:** The underlying `keyboard` library reads raw hardware device inputs. You must run the application with administrator privileges (e.g., `sudo ./wrong_lang_fixer`). This tool currently only supports X11 display servers (not Wayland).

## 🛠️ Building from Source (For Developers)

1. Clone the repository and navigate to the folder:

```bash
git clone [https://github.com/nazzony/Wrong-Language-Fixer.git](https://github.com/nazzony/Wrong-Language-Fixer.git)
cd Wrong-Language-Fixer
```

2. Install the required Python libraries:

```bash
pip install -r desktop/requirements.txt
```

3. Run the script in the background:

```bash
python desktop/wrong_lang_fixer.py
```

4. Compile the standalone executable using PyInstaller:

```bash
pyinstaller --onefile --noconsole desktop/wrong_lang_fixer.py
```