import os
import time
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_text(text, speed=0.05):
    """Mengetik teks satu per satu karakter seperti efek mesin tik"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def play_audio(file_path):
    try:
        import pygame
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
    except ImportError:
        print("Library 'pygame' tidak ditemukan. Audio tidak akan diputar.")
        print("Silahkan install dengan menjalankan: pip install pygame")
        time.sleep(3)
    except Exception as e:
        print(f"Gagal memutar audio: {e}")
        time.sleep(3)

def load_art(directory):
    frames = {}
    if os.path.exists(directory):
        for filename in sorted(os.listdir(directory)):
            if filename.endswith(".txt"):
                filepath = os.path.join(directory, filename)
                with open(filepath, 'r', encoding='utf-8') as f:
                    frames[filename] = f.read()
    return frames

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    art_dir = os.path.join(base_dir, 'art')
    music_file = os.path.join(base_dir, 'music', 'bugmiku.mp3')
    
    frames = load_art(art_dir)
    
    # action: 
    # 'clear' -> hapus layar console
    # 'art'   -> tampilkan ASCII art (target = nama file)
    # 'print' -> tampilkan teks/lirik sekaligus
    # 'type'  -> tampilkan teks/lirik dengan efek mengetik (typewriter)
    
    # PERHATIAN: Waktu (time) di bawah ini adalah perkiraan (dalam detik).
    # Anda perlu menyesuaikan angka 'time' ini agar pas dan sinkron 
    # dengan ketukan asli lagu mp3 Anda.
    timeline = [
        {"time": 0.0, "action": "clear"},
        {"time": 0.1, "action": "art", "target": "1_title.txt"},
        {"time": 13.5, "action": "clear"},
        
        # [Verse 1] - Starts at 14s
        {"time": 14.0, "action": "type", "text": "Maigo maigo mattadanaka saa"},
        {"time": 16.2, "action": "print", "text": "Pa-pa-para paaranooi-\"a\""},
        {"time": 19.0, "action": "type", "text": "Giko giko mai kokoro sentei"},
        {"time": 22.0, "action": "print", "text": "Pa-pa-para paaranooi-\"a\""},
        
        # [Verse 2]
        {"time": 23.8, "action": "clear"},
        {"time": 24.0, "action": "type", "text": "Tairo tairo tatta karamatta"},
        {"time": 27.0, "action": "print", "text": "Pa-pa-para paaranooi-\"a\""},
        {"time": 29.5, "action": "type", "text": "Sad, sad, tsuppushite kara"},
        {"time": 32.0, "action": "print", "text": "Pa-pa-pa-la paaranooi-\"do\""},
        
        # [Pre-Chorus]
        {"time": 34.0, "action": "clear"},
        {"time": 34.1, "action": "art", "target": "3_error.txt"},
        {"time": 34.2, "action": "type", "text": "Saa ba-ba-bagu sa bagubagu"},
        {"time": 37.2, "action": "type", "text": "Ta-ta-tagu sainou no tagu"},
        {"time": 40.2, "action": "type", "text": "Mou ha-ha-hagu kanjou wa hagu"},
        {"time": 42.5, "action": "type", "text": "Hasshou \"kurushii\" wa iyaiya, iya"},
        {"time": 45.0, "action": "print", "text": "Iyaiya, iya"},
        
        # [Chorus]
        {"time": 46.0, "action": "clear"},
        {"time": 46.1, "action": "art", "target": "2_spider.txt"},
        {"time": 46.2, "action": "print", "text": "Maa! zekkyouna kanjou rakka papparanoi-\"a\""},
        {"time": 49.0, "action": "print", "text": "Oboregoe agete wa guruguru"},
        {"time": 51.5, "action": "print", "text": "Maa! zettai zetsumei rakka yatta ra metta ra"},
        {"time": 54.0, "action": "type", "text": "Shizume yumeyume iyaiya, iya"},
        
        # [Post-Chorus]
        {"time": 56.0, "action": "clear"},
        {"time": 56.1, "action": "art", "target": "3_error.txt"},
        {"time": 56.2, "action": "print", "text": "Saa ba-ba-bagu sa bagubagu"},
        {"time": 59.2, "action": "print", "text": "Mato hazurezure jiai iyaiya"},
        {"time": 61.8, "action": "print", "text": "Saa ba-ba-bagu sa bagubagu"},
        {"time": 64.2, "action": "print", "text": "Kotae taedae iyaiya, iya"},
        {"time": 66.2, "action": "print", "text": "Iyaiya, iya"},
        # Berhenti di kisaran waktu 1:08 (68.0 detik)

        # [Verse 3] - Starts at 1:19 (79s)
        {"time": 78.8, "action": "clear"},
        {"time": 78.9, "action": "art", "target": "4_kuru.txt"},
        {"time": 79.0, "action": "type", "text": "Kurukuru pakkaan keihou matte muri guruguru-"},
        {"time": 82.0, "action": "type", "text": "Seenode maware (Kurukuru, kurukuru)"},
        {"time": 84.8, "action": "type", "text": "Aaaa pakkaan keihou yappa muri guruguru-"},
        {"time": 87.8, "action": "type", "text": "An yo ni kusari (Kurukuru, kurukuru)"},
        {"time": 90.0, "action": "print", "text": "Endoresu yami? ahaa!"},

        # [Verse 4]
        {"time": 92.8, "action": "clear"},
        {"time": 93.1, "action": "type", "text": "Dakko dakko iranai ko da"},
        {"time": 95.2, "action": "print", "text": "Pa-pa-para paaranooi-\"a\""},
        {"time": 98.0, "action": "type", "text": "Iiko iiko \"Ganbare\" no hanran"},
        {"time": 100.2, "action": "print", "text": "Adominisutoreita, aa!"},

        # [Bridge]
        {"time": 104.8, "action": "clear"},
        {"time": 104.9, "action": "art", "target": "5_lyrics.txt"},
        {"time": 105.2, "action": "print", "text": "Ba-ba-bagu sa bagubagu"},
        {"time": 107.2, "action": "print", "text": "Ra-ra-ragu rantaimu ragu"},
        {"time": 109.2, "action": "print", "text": "Ro-ro-rogu hankou no rogu"},
        {"time": 111.2, "action": "print", "text": "Ba-ba-bagu pa-pa-pa-la-pa"},
        {"time": 113.2, "action": "print", "text": "Pa, paaranooi-\"a\""},
        {"time": 114.7, "action": "print", "text": "Pa, paaranooi-\"a\""},
        {"time": 116.5, "action": "print", "text": "Pa, paaranooi-\"a\" iyaiya"},

        # [Chorus 2]
        {"time": 119.8, "action": "clear"},
        {"time": 119.9, "action": "art", "target": "2_spider.txt"},
        {"time": 120.0, "action": "print", "text": "Saa, zenkkyouna kanjou rakka papparanoi-\"a\""},
        {"time": 123.0, "action": "print", "text": "Hidari migi yukue mo guruguru hisan"},
        {"time": 126.0, "action": "print", "text": "Genkai nou kurucchatte yatta ra metta ra"},
        {"time": 129.0, "action": "type", "text": "Yami mayoe yoe inai inai baa"},
        {"time": 131.0, "action": "type", "text": "Inai inai batten"},
        {"time": 133.0, "action": "print", "text": "Zekkyouna kanjou rakka papparanoi-\"a\""},
        {"time": 136.0, "action": "print", "text": "Obore goe agete wa guruguru"},
        {"time": 139.0, "action": "print", "text": "Maa! zettai zetsumei rakka yatta ra metta ra"},
        {"time": 142.0, "action": "type", "text": "Kogoe kare hate iyaiya iya"},

        # [Post-Chorus 2]
        {"time": 144.8, "action": "clear"},
        {"time": 144.9, "action": "art", "target": "3_error.txt"},
        {"time": 145.0, "action": "print", "text": "Saa ba-ba-bagu sa bagubagu"},
        {"time": 147.0, "action": "print", "text": "Tadare are are hiai iyaiya"},
        {"time": 149.0, "action": "print", "text": "Saa ba-ba-bagu sa bagubagu"},
        {"time": 151.0, "action": "print", "text": "Kuro mamire risei iyaiya iya"},
        {"time": 153.0, "action": "type", "text": "Ima, ima, ima"},
        {"time": 156.0, "action": "type", "text": "Iyaiya, iyaiya, iyaiya, iyaiya, iya"},
        
        # End at 2:50 (170.0s)
        {"time": 169.8, "action": "clear"},
        {"time": 169.9, "action": "art", "target": "1_title.txt"},
        {"time": 170.0, "action": "type", "text": "--- E N D ---"}
    ]
    
    play_audio(music_file)
    
    print("Memulai animasi...")
    time.sleep(1)
    
    start_time = time.time()
    
    for event in timeline:
        target_time = start_time + event["time"]
        current_time = time.time()
        
        if target_time > current_time:
            time.sleep(target_time - current_time)
            
        action = event["action"]
        
        if action == "clear":
            clear_screen()
        elif action == "art":
            if event["target"] in frames:
                print(frames[event["target"]])
            else:
                print(f"[Art {event['target']} tidak ditemukan]")
        elif action == "print":
            print(event["text"])
        elif action == "type":
            type_text(event["text"], speed=0.03)
            
    print("\nSekuens animasi selesai.")
    
    try:
        import pygame
        print("Menunggu musik selesai...")
        while pygame.mixer.music.get_busy():
            time.sleep(1)
    except ImportError:
        pass

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear_screen()
        print("Animasi dihentikan.")
