"""
Bug (Kairiki Bear feat. Hatsune Miku) - Code Animation
========================================================
Terinspirasi dari World.Execute(Me) oleh Kritzkingvoid
Dibuat oleh : Nuthfih
"""

import os
import sys
import time
import random

# ─────────────────────────────────────────────────────────────
#  ANSI COLOR CODES
# ─────────────────────────────────────────────────────────────
CYAN    = '\033[96m'
MAGENTA = '\033[95m'
RED     = '\033[91m'
YELLOW  = '\033[93m'
GREEN   = '\033[92m'
WHITE   = '\033[97m'
BLUE    = '\033[94m'
BOLD    = '\033[1m'
DIM     = '\033[2m'
BLINK   = '\033[5m'
RESET   = '\033[0m'

# Enable ANSI escape codes on Windows
if os.name == 'nt':
    os.system('')


# ─────────────────────────────────────────────────────────────
#  UTILITY FUNCTIONS
# ─────────────────────────────────────────────────────────────

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def color_print(text, color=WHITE, end='\n'):
    """Cetak teks dengan satu warna ANSI."""
    sys.stdout.write(color + text + RESET + end)
    sys.stdout.flush()


def type_text(text, speed=0.04, color=WHITE):
    """Efek ketikan typewriter dengan warna."""
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write(RESET)
    print()


def color_type(text, color=WHITE, speed=0.04, prefix='[Console] '):
    """
    Efek ketikan berwarna dengan label prefix di depan,
    seperti slowType() di referensi C#.
    """
    if prefix:
        sys.stdout.write(GREEN + prefix + color)
        sys.stdout.flush()
    else:
        sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write(RESET)
    print()


def glitch_text(text, color=YELLOW, loops=8, prefix=''):
    """
    Karakter acak berputar lalu reveal teks asli.
    Seperti animateText() di referensi C# — efek karakter shuffle.
    """
    glitch_chars = '!@#$%^&*<>?/\\|~`[]{}0123456789xXaBbCcDdEeFf'
    sys.stdout.write('\r')
    for i in range(loops):
        shuffled = ''.join(random.choice(glitch_chars) for _ in text)
        sys.stdout.write(color + prefix + shuffled + RESET + '\r')
        sys.stdout.flush()
        time.sleep(0.05)
    # Reveal teks asli
    sys.stdout.write(color + prefix + text + RESET)
    sys.stdout.flush()
    print()


def scroll_lines(lines, delay=0.4, color=GREEN):
    """
    Tampilkan setiap baris seolah data streaming mengalir.
    Seperti encryptWall() di referensi C#.
    """
    for line in lines:
        sys.stdout.write(color + line + RESET + '\r')
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')
    sys.stdout.flush()


def bug_scan(label, length=20, delay=0.05, color=RED):
    """
    Progress bar bertema BUG SCAN.
    Seperti simulateLoading() di referensi C#.
    """
    for i in range(length + 1):
        filled = '#' * i
        empty  = '-' * (length - i)
        percent = int(i * 100 / length)
        bar_line = f'\r{color}[BUG] [{filled}{empty}] {percent:3d}% | {label}{RESET}'
        sys.stdout.write(bar_line)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def corrupt_text(text, intensity=0.3):
    """Sisipkan karakter glitch acak di dalam teks untuk efek korupsi data."""
    glitch_chars = '!@#$%^0xXZz'
    result = ''
    for char in text:
        if char != ' ' and random.random() < intensity:
            result += random.choice(glitch_chars)
        else:
            result += char
    return result


def rain_effect(duration=2.0, color=GREEN):
    """
    Hujan karakter binary/hex — efek matrix-style.
    Digunakan di seksi GLITCH / VIRUS SEQUENCE.
    """
    chars = '01' * 6 + 'ABCDEF' + '!@#$%&xXzZ'
    end_time = time.time() + duration
    width = random.randint(40, 65)
    while time.time() < end_time:
        line = ''.join(random.choice(chars) for _ in range(width))
        sys.stdout.write(color + DIM + line + RESET + '\n')
        sys.stdout.flush()
        time.sleep(0.035)


def bsod_flash(times=3):
    """Kilatan layar invert seperti crash / system error."""
    for _ in range(times):
        sys.stdout.write('\033[7m')   # invert colors
        sys.stdout.flush()
        time.sleep(0.09)
        sys.stdout.write('\033[0m')   # reset
        sys.stdout.flush()
        time.sleep(0.07)


def flash_screen(times=2, delay=0.07):
    """Efek layar berkedip biasa."""
    for _ in range(times):
        sys.stdout.write('\033[7m')
        sys.stdout.flush()
        time.sleep(delay)
        sys.stdout.write('\033[0m')
        sys.stdout.flush()
        time.sleep(delay)


def autocorrect_text(original, corrected, speed=0.03, backspace_speed=0.035):
    """
    Ketik teks asli, flash (seperti autocorrect gagal),
    hapus pakai backspace, lalu ketik teks yang benar.
    """
    sys.stdout.write(WHITE)
    for char in original:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write(RESET)
    time.sleep(0.3)

    flash_screen(times=3, delay=0.06)
    time.sleep(0.1)

    for _ in range(len(original)):
        sys.stdout.write('\b \b')
        sys.stdout.flush()
        time.sleep(backspace_speed)
    time.sleep(0.15)

    sys.stdout.write(CYAN)
    for char in corrected:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write(RESET)
    print()


def print_colored_art(art_text, char_map=None):
    """
    Cetak ASCII art dengan warna berbeda per karakter.
    Seperti readFileColor() di referensi C#.
    char_map = dict mapping char -> color_code
    """
    if char_map is None:
        char_map = {
            '*': CYAN, '#': YELLOW, '@': MAGENTA,
            '!': RED,  'X': RED,    '<': GREEN, '>': GREEN,
            '[': YELLOW, ']': YELLOW,
        }
    for char in art_text:
        c = char_map.get(char)
        if c:
            sys.stdout.write(c + char + RESET)
        else:
            sys.stdout.write(WHITE + char + RESET)
    sys.stdout.flush()
    if not art_text.endswith('\n'):
        print()


def password_prompt():
    """
    Command prompt interaktif di awal sebelum animasi dimulai.
    Seperti password check di Program.cs referensi.
    """
    clear_screen()
    color_print(BOLD + "  +------------------------------------------------------+" + RESET, WHITE)
    color_print(BOLD + "  |     BUG-MIKU  ANIMATION  TERMINAL   v 1.0.0          |" + RESET, WHITE)
    color_print(BOLD + "  |       [ Kairiki Bear  feat.  Hatsune Miku ]           |" + RESET, WHITE)
    color_print(BOLD + "  +------------------------------------------------------+" + RESET, WHITE)
    print()
    color_print("  System  : MikuOS  v2.0.6  (BugKernel)", GREEN)
    color_print("  Status  : INFECTED — 3 critical bugs detected", RED)
    color_print("  Audio   : bugmiku.mp3  [loaded]", CYAN)
    color_print("  Artist  : Kairiki Bear  feat.  Hatsune Miku", MAGENTA)
    print()
    color_print("  Type  'bug.execute()'  to begin.", YELLOW)
    print()

    while True:
        sys.stdout.write(CYAN + '> ' + RESET)
        sys.stdout.flush()
        cmd = input().strip().lower()
        if cmd in ['bug.execute()', 'bug.execute', 'run', '']:
            break
        else:
            color_print(f"  ERROR: command '{cmd}' not recognized.", RED)
            color_print("  Hint: try  bug.execute()", YELLOW)

    print()
    glitch_text("Initializing Bug.Execute()...", color=CYAN, loops=6)
    bug_scan("Loading audio stream    ", length=18, delay=0.04, color=CYAN)
    bug_scan("Compiling lirik data    ", length=18, delay=0.03, color=MAGENTA)
    bug_scan("Injecting  B U G        ", length=18, delay=0.05, color=RED)
    time.sleep(0.5)
    clear_screen()


# ─────────────────────────────────────────────────────────────
#  AUDIO
# ─────────────────────────────────────────────────────────────

def play_audio(file_path):
    """Putar musik menggunakan pygame (non-blocking)."""
    try:
        import pygame
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
    except ImportError:
        color_print("Library 'pygame' tidak ditemukan. Audio tidak akan diputar.", RED)
        color_print("Install dengan: pip install pygame", YELLOW)
        time.sleep(3)
    except Exception as e:
        color_print(f"Gagal memutar audio: {e}", RED)
        time.sleep(3)


# ─────────────────────────────────────────────────────────────
#  ART LOADER
# ─────────────────────────────────────────────────────────────

def load_art(directory):
    """Muat semua file .txt dari folder art ke dalam dictionary."""
    frames = {}
    if os.path.exists(directory):
        for filename in sorted(os.listdir(directory)):
            if filename.endswith('.txt'):
                filepath = os.path.join(directory, filename)
                with open(filepath, 'r', encoding='utf-8') as f:
                    frames[filename] = f.read()
    return frames


# ─────────────────────────────────────────────────────────────
#  MAIN
# ─────────────────────────────────────────────────────────────

def main():
    base_dir  = os.path.dirname(os.path.abspath(__file__))
    art_dir   = os.path.join(base_dir, 'art')
    music_file = os.path.join(base_dir, 'music', 'bugmiku.mp3')

    frames = load_art(art_dir)

    # ── Prompt interaktif di awal ──────────────────────────────
    password_prompt()

    # ─────────────────────────────────────────────────────────
    #  TIMELINE
    # ─────────────────────────────────────────────────────────
    #
    # action types:
    #   'clear'       -> hapus layar
    #   'art'         -> tampilkan ASCII art (target = nama file)
    #   'art_colored' -> tampilkan ASCII art dengan warna per karakter
    #   'print'       -> cetak teks biasa langsung
    #   'cprint'      -> cetak teks berwarna (color_print)
    #   'type'        -> efek ketikan typewriter biasa
    #   'ctype'       -> efek ketikan berwarna + prefix [Console]
    #   'glitch'      -> karakter acak berputar lalu reveal
    #   'autocorrect' -> ketik, flash, hapus, ketik ulang
    #   'scroll'      -> baris bergilir streaming data
    #   'bugscan'     -> progress bar [BUG SCAN]
    #   'rain'        -> hujan karakter binary/hex
    #   'bsod'        -> kilatan layar crash
    #
    # CATATAN: Semua 'time' dalam detik dari awal musik.
    # Sesuaikan angka jika sinkronisasi terasa kurang pas.
    # ─────────────────────────────────────────────────────────

    timeline = [

        # ── INTRO (0s – 13s) ─────────────────────────────────────
        {"time": 0.0,  "action": "clear"},
        {"time": 0.1,  "action": "art", "target": "1_title.txt"},
        {"time": 2.0,  "action": "ctype",  "text": "Song     : Bug",              "color": CYAN,    "prefix": "[Console] "},
        {"time": 3.5,  "action": "ctype",  "text": "Producer : Kairiki Bear",     "color": CYAN,    "prefix": "[Console] "},
        {"time": 5.0,  "action": "ctype",  "text": "Vocal    : Hatsune Miku",     "color": MAGENTA, "prefix": "[Console] "},
        {"time": 9.0,  "action": "glitch", "text": "[ bug.initialize() ]",        "color": YELLOW,  "loops": 7},
        {"time": 11.0, "action": "bugscan","label": "Scanning system for bugs...", "length": 10, "delay": 0.12, "color": RED},
        {"time": 13.0, "action": "clear"},

        # ── [Verse 1] ~13.7s ─────────────────────────────────────
        #    Maigo maigo mattadanaka saa
        {"time": 13.5, "action": "art",    "target": "6_miku.txt"},
        {"time": 14.0, "action": "ctype",  "text": "Maigo maigo mattadanaka saa",  "color": CYAN,    "prefix": ""},
        {"time": 16.0, "action": "cprint", "text": "Pa",                            "color": MAGENTA},
        {"time": 16.4, "action": "cprint", "text": "pa",                            "color": MAGENTA},
        {"time": 16.8, "action": "cprint", "text": "para",                          "color": MAGENTA},
        {"time": 17.4, "action": "cprint", "text": "paranoia",                      "color": RED},
        {"time": 17.5, "action": "autocorrect",
            "original":  "Giko giko mai kokoro sentei",
            "corrected": "Giko giko my heart sentei"},
        {"time": 21.0, "action": "cprint", "text": "Pa",                            "color": MAGENTA},
        {"time": 21.4, "action": "cprint", "text": "pa",                            "color": MAGENTA},
        {"time": 21.8, "action": "cprint", "text": "para",                          "color": MAGENTA},
        {"time": 22.5, "action": "cprint", "text": "paranoia",                      "color": RED},

        # ── [Verse 2] ~23.8s ─────────────────────────────────────
        #    Tairo tairo tatta karamatta
        {"time": 23.5, "action": "clear"},
        {"time": 23.7, "action": "ctype",  "text": "Tairo tairo tatta karamatta",  "color": CYAN, "prefix": ""},
        {"time": 26.5, "action": "scroll", "lines": [
            '  >> MEMORY LEAK DETECTED at 0xDEADC0DE',
            '  >> STACK: heart.dll -> emotion.cpp -> line 404',
            '  >> ERROR: Pa-pa-para paaranooi-"a"',
        ], "delay": 0.5, "color": YELLOW},
        {"time": 29.5, "action": "ctype",  "text": "Sad, sad, tsuppushite kara",   "color": CYAN, "prefix": ""},
        {"time": 32.0, "action": "cprint", "text": 'Pa-pa-pa-la paaranooi-"do"',   "color": RED},

        # ── [Pre-Chorus] ~34s ────────────────────────────────────
        #    Saa ba-ba-bagu sa bagubagu
        {"time": 33.8, "action": "clear"},
        {"time": 34.0, "action": "art",    "target": "3_error.txt"},
        {"time": 34.5, "action": "glitch", "text": "Saa ba-ba-bagu sa bagubagu",     "color": RED,     "loops": 5},
        {"time": 37.0, "action": "glitch", "text": "Ta-ta-tagu sainou no tagu",      "color": YELLOW,  "loops": 5},
        {"time": 39.5, "action": "glitch", "text": "Mou ha-ha-hagu kanjou wa hagu",  "color": RED,     "loops": 5},
        {"time": 42.0, "action": "ctype",  "text": 'Hasshou "kurushii" wa iyaiya, iya', "color": MAGENTA, "prefix": ""},
        {"time": 44.5, "action": "cprint", "text": "Iyaiya, iya",                    "color": MAGENTA},

        # ── [Chorus 1] ~46s ──────────────────────────────────────
        #    Maa! zekkyouna kanjou rakka
        {"time": 45.8, "action": "clear"},
        {"time": 46.0, "action": "art",    "target": "2_spider.txt"},
        {"time": 46.3, "action": "glitch", "text": 'Maa! zekkyouna kanjou rakka papparanoi-"a"', "color": CYAN, "loops": 7},
        {"time": 49.0, "action": "ctype",  "text": "Oboregoe agete wa guruguru",                 "color": MAGENTA, "prefix": ""},
        {"time": 51.5, "action": "cprint", "text": "Maa! zettai zetsumei rakka yatta ra metta ra","color": RED},
        {"time": 54.0, "action": "ctype",  "text": "Shizume yumeyume iyaiya, iya",               "color": CYAN, "prefix": ""},

        # ── [Post-Chorus 1] ~56s ─────────────────────────────────
        {"time": 55.8, "action": "clear"},
        {"time": 56.0, "action": "art",    "target": "7_virus.txt"},
        {"time": 56.3, "action": "cprint", "text": "Saa ba-ba-bagu sa bagubagu",     "color": RED},
        {"time": 58.5, "action": "scroll", "lines": [
            '  [BUG/Paranoia.A] mato hazurezure jiai iyaiya',
            '  [BUG/Paranoia.A] 0x4E554C4C -> NullReferenceException',
            '  [BUG/Paranoia.A] Threat level: CRITICAL — cannot remove',
        ], "delay": 0.45, "color": YELLOW},
        {"time": 61.8, "action": "cprint", "text": "Saa ba-ba-bagu sa bagubagu",     "color": RED},
        {"time": 64.2, "action": "cprint", "text": "Kotae taedae iyaiya, iya",       "color": MAGENTA},
        {"time": 66.2, "action": "cprint", "text": "Iyaiya, iya",                    "color": MAGENTA},

        # ── [GLITCH / VIRUS SEQUENCE] ~68s ───────────────────────
        {"time": 67.8, "action": "clear"},
        {"time": 68.0, "action": "bsod"},
        {"time": 68.2, "action": "ctype",  "text": "CRITICAL ERROR: SYSTEM INFECTED BY BUG/Paranoia.A",
                                            "color": RED, "prefix": "", "speed": 0.02},
        {"time": 69.2, "action": "scroll", "lines": [
            '  0x0000DEAD : NullPointerException  in module [HEART]',
            '  0xDEADC0DE : Segmentation fault    — emotion.dll crashed',
            '  0xBAADF00D : Stack overflow         in recursion of "iyaiya"',
            '  0xCAFEBABE : Unhandled exception    at bug.core -> line ???',
            '  0xDEADBEEF : Access violation       soul.exe terminated',
        ], "delay": 0.28, "color": RED},
        {"time": 70.7, "action": "rain",   "duration": 1.6, "color": GREEN},
        {"time": 72.5, "action": "ctype",  "text": "01000010 01010101 01000111  <-- [B][U][G]",
                                            "color": GREEN, "prefix": "[Memory] ", "speed": 0.02},
        {"time": 73.2, "action": "bsod"},
        {"time": 73.4, "action": "art",    "target": "9_crash.txt"},
        {"time": 74.2, "action": "glitch", "text": "FATAL: ERR_CONNECTION_RESET_HEART",  "color": RED,    "loops": 9},
        {"time": 75.2, "action": "ctype",  "text": "ATTEMPTING SYSTEM REBOOT...",         "color": YELLOW, "prefix": "[SYS]   ", "speed": 0.05},
        {"time": 76.5, "action": "bugscan","label": "REBOOTING KERNEL     ", "length": 12, "delay": 0.12, "color": RED},
        {"time": 78.0, "action": "clear"},
        {"time": 78.2, "action": "ctype",  "text": "System Reboot OK. Resuming operation...", "color": GREEN, "prefix": "[SYS]   "},

        # ── [Verse 3] ~79s ───────────────────────────────────────
        #    Kurukuru pakkaan keihou
        {"time": 78.8, "action": "clear"},
        {"time": 79.0, "action": "art",    "target": "4_kuru.txt"},
        {"time": 79.3, "action": "ctype",  "text": "Pakkaan keihou matte muri guruguru-",
                                            "color": CYAN,    "prefix": "",  "speed": 0.03},
        {"time": 82.0, "action": "ctype",  "text": "Seenode maware",
                                            "color": MAGENTA, "prefix": ""},
        {"time": 84.0, "action": "glitch", "text": "Kurukuru, kurukuru", 
                                            "color":MAGENTA, "loops": 5},
        {"time": 84.8, "action": "glitch", "text": "Aaaa pakkaan keihou yappa muri guruguru-",
                                            "color": CYAN,    "loops": 5},
        {"time": 87.8, "action": "ctype",  "text": "An yo ni kusari",
                                            "color": MAGENTA, "prefix": ""},
        {"time": 88.8, "action": "glitch", "text": "Kurukuru, kurukuru", 
                                            "color":MAGENTA, "loops": 5},
        {"time": 90.0, "action": "cprint", "text": "Endoresu yami? ahaa!",          "color": RED},

        # ── [Verse 4] ~92.8s ─────────────────────────────────────
        #    Dakko dakko iranai ko da
        {"time": 92.5, "action": "clear"},
        {"time": 92.8, "action": "ctype",  "text": "Dakko dakko iranai ko da",      "color": CYAN, "prefix": ""},
        {"time": 95.2, "action": "scroll", "lines": [
            '  >> Pa-pa-para paaranooi-"a"',
            '  >> ERROR: child.isWanted()      returned  false',
            '  >> ERROR: self.isNeeded()        returned  false',
            '  >> WARN:  world.continue()       returned  null',
        ], "delay": 0.5, "color": YELLOW},
        {"time": 98.0, "action": "ctype",  "text": 'Iiko iiko "Ganbare" no hanran', "color": CYAN, "prefix": ""},
        {"time": 100.2,"action": "cprint", "text": "Adominisutoreita, aa!",          "color": RED},

        # ── [Bridge] ~104.8s ─────────────────────────────────────
        {"time": 104.5, "action": "clear"},
        {"time": 104.8, "action": "art",    "target": "5_lyrics.txt"},
        {"time": 105.2, "action": "glitch", "text": "Ba-ba-bagu sa bagubagu",       "color": RED,     "loops": 4},
        {"time": 107.2, "action": "glitch", "text": "Ra-ra-ragu rantaimu ragu",     "color": YELLOW,  "loops": 4},
        {"time": 109.2, "action": "glitch", "text": "Ro-ro-rogu hankou no rogu",    "color": MAGENTA, "loops": 4},
        {"time": 111.2, "action": "glitch", "text": "Ba-ba-bagu pa-pa-pa-la-pa",   "color": RED,     "loops": 4},
        {"time": 113.0, "action": "cprint", "text": 'Pa, paaranooi-"a"',             "color": CYAN},
        {"time": 114.5, "action": "cprint", "text": 'Pa, paaranooi-"a"',             "color": CYAN},
        {"time": 116.3, "action": "cprint", "text": 'Pa, paaranooi-"a" iyaiya',     "color": MAGENTA},

        # ── [Chorus 2] ~119.8s ───────────────────────────────────
        {"time": 119.5, "action": "clear"},
        {"time": 119.8, "action": "art",    "target": "2_spider.txt"},
        {"time": 120.0, "action": "glitch", "text": 'Saa, zekkyouna kanjou rakka papparanoi-"a"',
                                             "color": CYAN,    "loops": 8},
        {"time": 123.0, "action": "ctype",  "text": "Hidari migi yukue mo guruguru hisan",
                                             "color": MAGENTA, "prefix": ""},
        {"time": 126.0, "action": "cprint", "text": "Genkai nou kurucchatte yatta ra metta ra", "color": RED},
        {"time": 129.0, "action": "ctype",  "text": "Yami mayoe yoe inai inai baa",  "color": CYAN,    "prefix": ""},
        {"time": 131.0, "action": "ctype",  "text": "Inai inai batten",               "color": MAGENTA, "prefix": ""},
        {"time": 133.0, "action": "glitch", "text": 'Zekkyouna kanjou rakka papparanoi-"a"',
                                             "color": CYAN,    "loops": 7},
        {"time": 136.0, "action": "cprint", "text": "Obore goe agete wa guruguru",    "color": MAGENTA},
        {"time": 139.0, "action": "cprint", "text": "Maa! zettai zetsumei rakka yatta ra metta ra", "color": RED},
        {"time": 142.0, "action": "ctype",  "text": "Kogoe kare hate iyaiya iya",     "color": CYAN, "prefix": ""},

        # ── [Post-Chorus 2] ~144.8s ──────────────────────────────
        {"time": 144.5, "action": "clear"},
        {"time": 144.8, "action": "art",    "target": "8_heart.txt"},
        {"time": 145.0, "action": "cprint", "text": "Saa ba-ba-bagu sa bagubagu",     "color": RED},
        {"time": 147.0, "action": "cprint", "text": "Tadare are are hiai iyaiya",     "color": MAGENTA},
        {"time": 149.0, "action": "glitch", "text": "Saa ba-ba-bagu sa bagubagu",     "color": RED,     "loops": 5},
        {"time": 151.0, "action": "cprint", "text": "Kuro mamire risei iyaiya iya",  "color": MAGENTA},
        {"time": 153.0, "action": "ctype",  "text": "Ima, ima, ima",                   "color": CYAN, "prefix": ""},
        {"time": 155.0, "action": "scroll", "lines": [
            '  iyaiya...',
            '  iyaiya, iyaiya...',
            '  iyaiya, iyaiya, iyaiya...',
            '  iyaiya, iyaiya, iyaiya, iyaiya, iya',
        ], "delay": 0.55, "color": MAGENTA},

        # ── [OUTRO] ~160s ────────────────────────────────────────
        {"time": 159.5, "action": "clear"},
        {"time": 159.8, "action": "rain",   "duration": 2.5, "color": CYAN},
        {"time": 162.5, "action": "clear"},
        {"time": 162.8, "action": "art",    "target": "10_end.txt"},
        {"time": 164.0, "action": "ctype",  "text": "bug.terminate()",              "color": YELLOW,  "prefix": "[System] ", "speed": 0.08},
        {"time": 166.0, "action": "bugscan","label": "Cleaning up memory...", "length": 12, "delay": 0.14, "color": GREEN},
        {"time": 169.5, "action": "clear"},
        {"time": 169.8, "action": "art",    "target": "1_title.txt"},
        {"time": 170.2, "action": "ctype",  "text": "--- E  N  D ---",              "color": CYAN, "prefix": ""},
        {"time": 172.0, "action": "cprint", "text": "Animated by Nuthfih  |  Bug (c) Kairiki Bear  |  feat. Hatsune Miku",
                                             "color": DIM},
    ]

    # ── Mulai musik ───────────────────────────────────────────
    play_audio(music_file)

    start_time = time.time()

    # ── Jalankan timeline ─────────────────────────────────────
    for event in timeline:
        target_time  = start_time + event["time"]
        current_time = time.time()
        if target_time > current_time:
            time.sleep(target_time - current_time)

        action = event["action"]

        if action == "clear":
            clear_screen()

        elif action == "art":
            key = event["target"]
            if key in frames:
                print(frames[key])
            else:
                color_print(f"[Art '{key}' tidak ditemukan]", RED)

        elif action == "art_colored":
            key = event["target"]
            if key in frames:
                print_colored_art(frames[key], event.get("char_map"))
            else:
                color_print(f"[Art '{key}' tidak ditemukan]", RED)

        elif action == "print":
            print(event.get("text", ""))

        elif action == "cprint":
            color_print(event.get("text", ""), event.get("color", WHITE))

        elif action == "type":
            type_text(event.get("text", ""), speed=event.get("speed", 0.04))

        elif action == "ctype":
            color_type(
                event.get("text", ""),
                color=event.get("color", WHITE),
                speed=event.get("speed", 0.04),
                prefix=event.get("prefix", "[Console] "),
            )

        elif action == "glitch":
            glitch_text(
                event.get("text", ""),
                color=event.get("color", YELLOW),
                loops=event.get("loops", 6),
                prefix=event.get("prefix", ""),
            )

        elif action == "autocorrect":
            autocorrect_text(event["original"], event["corrected"])

        elif action == "scroll":
            scroll_lines(
                event.get("lines", []),
                delay=event.get("delay", 0.4),
                color=event.get("color", GREEN),
            )

        elif action == "bugscan":
            bug_scan(
                event.get("label", "Scanning"),
                length=event.get("length", 20),
                delay=event.get("delay", 0.05),
                color=event.get("color", RED),
            )

        elif action == "rain":
            rain_effect(duration=event.get("duration", 1.5), color=event.get("color", GREEN))

        elif action == "bsod":
            bsod_flash(times=event.get("times", 3))

    # ── Tunggu musik selesai ──────────────────────────────────
    print()
    color_print("Sekuens animasi selesai.", GREEN)
    try:
        import pygame
        color_print("Menunggu musik selesai...", DIM)
        while pygame.mixer.music.get_busy():
            time.sleep(1)
    except ImportError:
        pass


# ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear_screen()
        color_print("\nAnimasi dihentikan.", YELLOW)
