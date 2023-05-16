import time
import random
import tkinter as tk

SENTENCES = [
    "The quick brown fox jumps over the lazy dog." 
    " She sells seashells by the seashore.",
    "Peter Piper picked a peck of pickled peppers."
    "The quick brown fox jumps over the lazy dog",
    "The quick brown fox jumps over the lazy dog."
    "She sells seashells by the seashore."
    "Peter Piper picked a peck of pickled peppers.",
    "How much wood would a woodchuck chuck if a woodchuck could chuck wood?"
    "The rain in Spain stays mainly in the plain.",
     "How much wood would a woodchuck chuck if a woodchuck could chuck wood?"
]

TIME_LIMIT = 60


class TypingSpeedTest:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Typing Speed Test")
        self.root.geometry("1200x600")
        self.root.resizable(False, False)

        self.text_label = tk.Label(self.root, text="Type the following sentence:")
        self.text_label.pack(pady=10)

        self.sentence_label = tk.Label(self.root, font=("Arial", 16))
        self.sentence_label.pack(pady=10)

        self.entry = tk.Entry(self.root, font=("Arial", 16))
        self.entry.pack(pady=10)

        self.start_button = tk.Button(self.root, text="Start", command=self.start_test)
        self.start_button.pack(pady=10)

        self.words_typed_label = tk.Label(self.root, font=("Arial", 16))
        self.timer_label = tk.Label(self.root, font=("Arial", 16))
        self.wpm_label = tk.Label(self.root, font=("Arial", 16))

        self.root.mainloop()

    def start_test(self):
        self.entry.focus_set()
        self.start_time = time.time()
        self.remaining_time = TIME_LIMIT
        self.update_timer()
        self.sentence = random.choice(SENTENCES)
        self.sentence_label.configure(text=self.sentence)
        self.entry.delete(0, tk.END)
        self.entry.bind("<KeyRelease>", self.update_words_typed)
        self.start_button.configure(state=tk.DISABLED)

    def finish_test(self):
        self.entry.unbind("<KeyRelease>")
        end_time = time.time()
        user_input = self.entry.get()
        words_typed = len(user_input.split())
        time_taken = end_time - self.start_time
        typing_speed = int(words_typed / time_taken * 60)
        self.wpm_label.configure(text=f"Your typing speed is {typing_speed} WPM.")
        self.wpm_label.pack(pady=10)
        self.start_button.configure(text="Retry", command=self.start_test, state=tk.NORMAL)

    def update_words_typed(self, event):
        user_input = self.entry.get()
        num_words = len(user_input.split())
        if num_words > len(self.sentence.split()):
            self.finish_test()
        else:
            self.words_typed_label.configure(text=f"Words typed: {num_words}")

    def update_timer(self):
        self.remaining_time -= 1
        if self.remaining_time >= 0:
            self.timer_label.configure(text=f"Time remaining: {self.remaining_time}s")
            self.timer_label.pack(pady=10)
            self.timer_label.after(1000, self.update_timer)
        else:
            self.finish_test()


if __name__ == "__main__":
    TypingSpeedTest()
