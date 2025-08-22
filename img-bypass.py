# Python3+
# GITHUB: https://github.com/denoyey/Img-Bypass
# LICENSE: MIT License

import os
import sys
import importlib.util
import platform
import subprocess
import random

OUTPUT_DIR = "output_img_bypass"

colors = {
    "RED": "\033[91m",
    "GREEN": "\033[92m",
    "YELLOW": "\033[93m",
    "BLUE": "\033[94m",
    "MAGENTA": "\033[95m",
    "CYAN": "\033[96m",
    "WHITE": "\033[97m",
    "RESET": "\033[0m",
}


def clear_screen():
    try:
        subprocess.run("cls" if platform.system() == "Windows" else "clear", shell=True)
    except Exception as e:
        print(f"[!] Error clearing screen: {e}")
        sys.exit(1)


def create_output_dir():
    try:
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)
    except OSError as e:
        print(f"[!] Error creating output directory: {e}")
        sys.exit(1)


def check_pip():
    try:
        subprocess.check_output([sys.executable, "-m", "pip", "--version"])
    except subprocess.CalledProcessError:
        print("\n[!] pip is not installed or not working.")
        sys.exit(1)


def check_installed(dependencies):
    try:
        for module_name, package_name in dependencies.items():
            if importlib.util.find_spec(module_name) is None:
                print(f"\n[*] Installing missing package: {package_name}")
                try:
                    subprocess.check_call(
                        [
                            sys.executable,
                            "-m",
                            "pip",
                            "install",
                            package_name,
                            "--break-system-packages",
                        ]
                    )
                except subprocess.CalledProcessError as e:
                    print(f"[!] Failed to install {package_name}: {e}")
                    sys.exit(1)
    except Exception as e:
        print(f"[!] Error checking installed packages: {e}")
        sys.exit(1)


def auto_import(module_name, alias=None):
    try:
        module = importlib.import_module(module_name)
        if alias:
            globals()[alias] = module
        else:
            globals()[module_name] = module
    except ImportError:
        print(f"[!] Failed to import module: {module_name}")
        sys.exit(1)


check_pip()
required_deps = {
    "PIL": "Pillow",
    "piexif": "piexif",
}
check_installed(required_deps)
import piexif
from PIL import Image


def logo():
    available_colors = [c for name, c in colors.items() if name != "RESET"]
    my_logo = rf"""
.___   _____    ________         __________                                    
|   | /     \  /  _____/         \______   \___.__.___________    ______ ______
|   |/  \ /  \/   \  ___   ______ |    |  _<   |  |\____ \__  \  /  ___//  ___/
|   /    Y    \    \_\  \ /_____/ |    |   \\___  ||  |_> > __ \_\___ \ \___ \ 
|___\____|__  /\______  /         |______  // ____||   __(____  /____  >____  >
            \/        \/                 \/ \/     |__|       \/     \/     \/ 
            GITHUB: https://github.com/denoyey/Img-Bypass
    """
    lines = my_logo.strip("\n").split("\n")
    rainbow_logo = ""
    color_index = 0
    for i, line in enumerate(lines):
        if i % 1 == 0:
            color = random.choice(available_colors)
        rainbow_logo += f"{color}{line}{colors['RESET']}\n"
    print(rainbow_logo)


def embed_php(jpg_path, php_path):
    try:
        if not os.path.isfile(jpg_path):
            print(f"[!] Image file not found: {jpg_path}")
            return
        if not os.path.isfile(php_path):
            print(f"[!] PHP file not found: {php_path}")
            return
        if not jpg_path.lower().endswith((".jpg", ".jpeg")):
            print("[!] Only JPG/JPEG images are supported.")
            return
        with open(php_path, "r", encoding="utf-8", errors="ignore") as php_file:
            php_code = php_file.read()
        try:
            exif_dict = piexif.load(jpg_path)
        except piexif.InvalidImageDataError:
            exif_dict = {
                "0th": {},
                "Exif": {},
                "GPS": {},
                "Interop": {},
                "1st": {},
                "thumbnail": None,
            }
        exif_dict["Exif"][piexif.ExifIFD.UserComment] = php_code.encode("utf-8")
        exif_bytes = piexif.dump(exif_dict)
        image = Image.open(jpg_path)
        image_name = os.path.basename(jpg_path)
        output_path = os.path.join(OUTPUT_DIR, f"embedded_{image_name}")
        image.save(output_path, "jpeg", exif=exif_bytes)
        print(f"\n[✔] PHP code embedded successfully! Saved to: {output_path}")
    except Exception as e:
        print(f"\n[!] Error embedding PHP: {e}")
        sys.exit(1)


def extract_php(jpg_path):
    try:
        exif_dict = piexif.load(jpg_path)
        php_code = (
            exif_dict["Exif"]
            .get(piexif.ExifIFD.UserComment, b"")
            .decode("utf-8", errors="ignore")
        )
        if php_code.strip():
            image_name = os.path.splitext(os.path.basename(jpg_path))[0]
            output_php_path = os.path.join(OUTPUT_DIR, f"extracted_{image_name}.php")
            with open(output_php_path, "w", encoding="utf-8") as php_file:
                php_file.write(php_code)
            print(f"\n[*] PHP code extracted to {output_php_path}")
        else:
            print("\n[!] No PHP code found in the image.")
    except Exception as e:
        print(f"\n[!] Error extracting PHP: {e}")
        sys.exit(1)


def main():
    try:
        create_output_dir()
        while True:
            clear_screen()
            logo()
            print(
                f"""
[ ------ MENU ------ ]
[1] Embed PHP
[2] Extract PHP
[0] Exit
                """
            )
            choice = input("[~] Number (1/2/0) >> ").strip()

            if choice == "1":
                clear_screen()
                logo()
                print("\n[~] Embedding PHP code into JPG image...")
                jpg_path = input("\n[~] Enter the path to the JPG image\n>> ").strip()
                php_path = input("\n[~] Enter the path to the PHP file\n>> ").strip()
                embed_php(jpg_path, php_path)
            elif choice == "2":
                clear_screen()
                logo()
                print("\n[~] Extracting PHP code from JPG image...")
                jpg_path = input("\n[~] Enter the path to the JPG image\n>> ").strip()
                extract_php(jpg_path)
            elif choice == "0":
                clear_screen()
                logo()
                print("\n[!] Thankyou for using Img-Bypass!")
                exit(0)
            else:
                print("\n[!] Invalid choice. Please select 1, 2, or 0.")
                input("\n[~] Press Enter to continue...")
    except KeyboardInterrupt:
        print("\n\n[!] Exiting...")
        exit(0)
    except Exception as e:
        print(f"[!] An error occurred: {e}")
        exit(1)


if __name__ == "__main__":
    main()
