import tkinter as tk
import random

# Basic Hiragana
hiragana_dict = {
    'あ': 'a', 'い': 'i', 'う': 'u', 'え': 'e', 'お': 'o',
    'か': 'ka', 'き': 'ki', 'く': 'ku', 'け': 'ke', 'こ': 'ko',
    'さ': 'sa', 'し': 'shi', 'す': 'su', 'せ': 'se', 'そ': 'so',
    'た': 'ta', 'ち': 'chi', 'つ': 'tsu', 'て': 'te', 'と': 'to',
    'な': 'na', 'に': 'ni', 'ぬ': 'nu', 'ね': 'ne', 'の': 'no',
    'は': 'ha', 'ひ': 'hi', 'ふ': 'fu', 'へ': 'he', 'ほ': 'ho',
    'ま': 'ma', 'み': 'mi', 'む': 'mu', 'め': 'me', 'も': 'mo',
    'や': 'ya', 'ゆ': 'yu', 'よ': 'yo',
    'ら': 'ra', 'り': 'ri', 'る': 'ru', 'れ': 're', 'ろ': 'ro',
    'わ': 'wa', 'を': 'wo', 'ん': 'n'
}

# Hiragana + (Dakuten, Han-Dakuten, and Combination Kana)
hiragana_plus_dict = {
    **hiragana_dict,
    # Dakuten
    'が': 'ga', 'ぎ': 'gi', 'ぐ': 'gu', 'げ': 'ge', 'ご': 'go',
    'ざ': 'za', 'じ': 'ji', 'ず': 'zu', 'ぜ': 'ze', 'ぞ': 'zo',
    'だ': 'da', 'ぢ': 'ji', 'づ': 'zu', 'で': 'de', 'ど': 'do',
    'ば': 'ba', 'び': 'bi', 'ぶ': 'bu', 'べ': 'be', 'ぼ': 'bo',
    # Han-Dakuten
    'ぱ': 'pa', 'ぴ': 'pi', 'ぷ': 'pu', 'ぺ': 'pe', 'ぽ': 'po',
    # Combination Kana (Yoon)
    'きゃ': 'kya', 'きゅ': 'kyu', 'きょ': 'kyo',
    'しゃ': 'sha', 'しゅ': 'shu', 'しょ': 'sho',
    'ちゃ': 'cha', 'ちゅ': 'chu', 'ちょ': 'cho',
    'にゃ': 'nya', 'にゅ': 'nyu', 'にょ': 'nyo',
    'ひゃ': 'hya', 'ひゅ': 'hyu', 'ひょ': 'hyo',
    'みゃ': 'mya', 'みゅ': 'myu', 'みょ': 'myo',
    'りゃ': 'rya', 'りゅ': 'ryu', 'りょ': 'ryo',
    'ぎゃ': 'gya', 'ぎゅ': 'gyu', 'ぎょ': 'gyo',
    'じゃ': 'ja',  'じゅ': 'ju',  'じょ': 'jo',
    'びゃ': 'bya', 'びゅ': 'byu', 'びょ': 'byo',
    'ぴゃ': 'pya', 'ぴゅ': 'pyu', 'ぴょ': 'pyo'
}

# Basic Katakana
katakana_dict = {
    'ア': 'a', 'イ': 'i', 'ウ': 'u', 'エ': 'e', 'オ': 'o',
    'カ': 'ka', 'キ': 'ki', 'ク': 'ku', 'ケ': 'ke', 'コ': 'ko',
    'サ': 'sa', 'シ': 'shi', 'ス': 'su', 'セ': 'se', 'ソ': 'so',
    'タ': 'ta', 'チ': 'chi', 'ツ': 'tsu', 'テ': 'te', 'ト': 'to',
    'ナ': 'na', 'ニ': 'ni', 'ヌ': 'nu', 'ネ': 'ne', 'ノ': 'no',
    'ハ': 'ha', 'ヒ': 'hi', 'フ': 'fu', 'ヘ': 'he', 'ホ': 'ho',
    'マ': 'ma', 'ミ': 'mi', 'ム': 'mu', 'メ': 'me', 'モ': 'mo',
    'ヤ': 'ya', 'ユ': 'yu', 'ヨ': 'yo', 'ラ': 'ra', 'リ': 'ri',
    'ル': 'ru', 'レ': 're', 'ロ': 'ro', 'ワ': 'wa', 'ヲ': 'wo', 'ン': 'n'
}

# Katakana + (Dakuten, Han-Dakuten, and Combination Katakana)
katakana_plus_dict = {
    **katakana_dict,
    # Dakuten
    'ガ': 'ga', 'ギ': 'gi', 'グ': 'gu', 'ゲ': 'ge', 'ゴ': 'go',
    'ザ': 'za', 'ジ': 'ji', 'ズ': 'zu', 'ゼ': 'ze', 'ゾ': 'zo',
    'ダ': 'da', 'ヂ': 'ji', 'ヅ': 'zu', 'デ': 'de', 'ド': 'do',
    'バ': 'ba', 'ビ': 'bi', 'ブ': 'bu', 'ベ': 'be', 'ボ': 'bo',
    # Han-Dakuten
    'パ': 'pa', 'ピ': 'pi', 'プ': 'pu', 'ペ': 'pe', 'ポ': 'po',
    # Combination Katakana (Yoon)
    'キャ': 'kya', 'キュ': 'kyu', 'キョ': 'kyo',
    'シャ': 'sha', 'シュ': 'shu', 'ショ': 'sho',
    'チャ': 'cha', 'チュ': 'chu', 'チョ': 'cho',
    'ニャ': 'nya', 'ニュ': 'nyu', 'ニョ': 'nyo',
    'ヒャ': 'hya', 'ヒュ': 'hyu', 'ヒョ': 'hyo',
    'ミャ': 'mya', 'ミュ': 'myu', 'ミョ': 'myo',
    'リャ': 'rya', 'リュ': 'ryu', 'リョ': 'ryo',
    'ギャ': 'gya', 'ギュ': 'gyu', 'ギョ': 'gyo',
    'ジャ': 'ja',  'ジュ': 'ju',  'ジョ': 'jo',
    'ビャ': 'bya', 'ビュ': 'byu', 'ビョ': 'byo',
    'ピャ': 'pya', 'ピュ': 'pyu', 'ピョ': 'pyo'
}

class QuickKanaApp:
    def __init__(self, master):
        self.master = master
        self.master.title("QuickKana")
        self.master.attributes("-fullscreen", True)
        self.master.bind("<Escape>", self.exit_fullscreen)
        self.master.configure(bg="#2E2E2E")
        
        self.selected_mode = tk.StringVar(value="Hiragana")
        
        # Create a frame for the control buttons
        self.control_frame = tk.Frame(self.master, bg="#2E2E2E")
        self.control_frame.pack(side=tk.TOP, fill=tk.X)

        # Add control buttons
        self.add_control_buttons()

        # Show the start screen initially
        self.start_screen()

    def add_control_buttons(self):
        """Creates exit, minimize, and fullscreen toggle buttons."""
        # Minimize button
        minimize_button = tk.Button(self.control_frame, text="_", font=("Helvetica", 18), bg="#4A4A4A", fg="#F0F0F0",
                                     activebackground="#5B5B5B", relief="flat", cursor="hand2", command=self.minimize)
        minimize_button.pack(side=tk.RIGHT, padx=5)

        # Fullscreen toggle button
        fullscreen_button = tk.Button(self.control_frame, text="[]", font=("Helvetica", 18), bg="#4A4A4A", fg="#F0F0F0",
                                       activebackground="#5B5B5B", relief="flat", cursor="hand2", command=self.toggle_fullscreen)
        fullscreen_button.pack(side=tk.RIGHT, padx=5)

        # Exit button
        exit_button = tk.Button(self.control_frame, text="X", font=("Helvetica", 18, "bold"), bg="#FF4C4C", fg="white",
                                relief="flat", activebackground="#FF2A2A", cursor="hand2", command=self.exit_program)
        exit_button.pack(side=tk.RIGHT, padx=5)

    def start_screen(self):
        """Creates the starting screen with title, mode options, and start button.""" 
        self.clear_screen()
        
        # Title label
        title_label = tk.Label(self.master, text="QuickKana", font=("Helvetica", 72, "bold"), bg="#2E2E2E", fg="#F0F0F0")
        title_label.pack(pady=50)
        
        # Mode selection frame
        mode_frame = tk.Frame(self.master, bg="#2E2E2E")
        mode_frame.pack(pady=30)
        
        modes = ["Hiragana", "Katakana", "Hiragana +", "Katakana +"]
        for mode in modes:
            tk.Radiobutton(mode_frame, text=mode, variable=self.selected_mode, value=mode,
                           font=("Helvetica", 24), bg="#2E2E2E", fg="#F0F0F0", selectcolor="#3A3A3A",
                           activebackground="#2E2E2E", cursor="hand2").pack(side=tk.LEFT, padx=20)
        
        # Start button
        start_button = tk.Button(self.master, text="Start", font=("Helvetica", 36), bg="#4A4A4A", fg="#F0F0F0",
                                 activebackground="#5B5B5B", relief="flat", cursor="hand2", command=self.start_quiz)
        start_button.pack(pady=50)

    def start_quiz(self):
        """Starts the flashcard quiz with the selected mode."""        
        mode = self.selected_mode.get()
        if mode == "Hiragana":
            self.character_set = hiragana_dict
        elif mode == "Katakana":
            self.character_set = katakana_dict
        elif mode == "Hiragana +":
            self.character_set = hiragana_plus_dict
        elif mode == "Katakana +":
            self.character_set = katakana_plus_dict
        
        # Start the flashcard section
        self.flashcard_screen()

    def flashcard_screen(self):
        """Creates the flashcard quiz interface."""
        self.clear_screen()
        HiraganaFlashcards(self.master, self.character_set, self)

    def clear_screen(self):
        """Removes all existing widgets from the screen except the control frame."""
        for widget in self.master.winfo_children():
            if widget != self.control_frame:
                widget.destroy()

    def exit_fullscreen(self, event=None):
        self.master.attributes("-fullscreen", False)

    def minimize(self):
        self.master.iconify()

    def toggle_fullscreen(self):
        is_fullscreen = self.master.attributes("-fullscreen")
        self.master.attributes("-fullscreen", not is_fullscreen)

    def exit_program(self):
        self.master.quit()


class HiraganaFlashcards:
    def __init__(self, master, character_set, app):
        self.master = master
        self.character_set = character_set
        self.app = app  # Reference to the main app (for navigation)

        self.streak_count = 0

        # Streak counter
        self.streak_label = tk.Label(master, text="Streak: 0", font=("Helvetica", 24, "bold"), bg="#2E2E2E", fg="#F0F0F0")
        self.streak_label.place(relx=0.5, rely=0.05, anchor='n')

        # Back button
        self.back_button = tk.Button(master, text="Back", command=self.go_back, font=("Helvetica", 18, "bold"),
                                     bg="#4A4A4A", fg="#F0F0F0", relief="flat", activebackground="#5B5B5B", cursor="hand2")
        self.back_button.place(relx=0.02, rely=0.05, anchor='nw')

        # Centering frames
        self.center_frame = tk.Frame(master, bg="#2E2E2E")
        self.center_frame.pack(expand=True)

        self.question_label = tk.Label(self.center_frame, text="", font=("Helvetica", 72, "bold"), bg="#2E2E2E", fg="#F0F0F0")
        self.question_label.pack(pady=40)

        self.buttons_frame = tk.Frame(self.center_frame, bg="#2E2E2E")
        self.buttons_frame.pack(pady=20)

        self.buttons = [tk.Button(self.buttons_frame, text="", font=("Helvetica", 36), width=5, height=2,
                                  command=lambda b=i: self.check_answer(b), relief="flat", bg="#4A4A4A", fg="#F0F0F0",
                                  activebackground="#5B5B5B", cursor="hand2") for i in range(4)]
        for button in self.buttons:
            button.pack(side=tk.LEFT, padx=20)

        self.result_label = tk.Label(self.center_frame, text="", font=("Helvetica", 24, "italic"), bg="#2E2E2E", fg="#F0F0F0")
        self.result_label.pack(pady=30)

        self.next_question()

    def next_question(self):
        self.result_label.config(text="")
        self.kana, self.correct_answer, self.options = self.get_flashcard()
        self.question_label.config(text=self.kana)
        
        for i, option in enumerate(self.options):
            self.buttons[i].config(text=option, state=tk.NORMAL)

    def get_flashcard(self):
        kana = random.choice(list(self.character_set.keys()))
        correct_answer = self.character_set[kana]
        options = [correct_answer]

        while len(options) < 4:
            wrong_answer = random.choice(list(self.character_set.values()))
            if wrong_answer not in options:
                options.append(wrong_answer)

        random.shuffle(options)
        return kana, correct_answer, options

    def check_answer(self, button_index):
        selected_answer = self.options[button_index]
        if selected_answer == self.correct_answer:
            self.streak_count += 1
            self.result_label.config(text="Correct!", fg="green")
        else:
            self.streak_count = 0
            self.result_label.config(text=f"Wrong! The correct answer was '{self.correct_answer}'.", fg="red")
        
        self.streak_label.config(text=f"Streak: {self.streak_count}")
        
        for button in self.buttons:
            button.config(state=tk.DISABLED)

        self.master.after(2000, self.next_question)

    def go_back(self):
        """Navigates back to the start screen."""
        self.app.start_screen()

    def exit_program(self):
        self.master.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = QuickKanaApp(root)
    root.mainloop()