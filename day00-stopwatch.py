import tkinter as tk
import time
import requests

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.start_time = None
        self.elapsed_time = 0
        self.running = False

        self.root.configure(bg='black')
        self.root.minsize(600, 300)  # Set minimum window size


        self.label = tk.Label(root, text="00:00:00", font=("Helvetica", 48), bg='black', fg='white', pady=10)
        self.label.pack()

        self.buttons_frame = tk.Frame(root, bg='black')
        self.buttons_frame.pack(pady=10)

        button_font = ("Helvetica", 16)  # Font size for buttons
        button_width = 10  # Width of buttons
        button_height = 2  # Height of buttons
        button_color = "#4f4f4f"  # Button background color

        self.start_button = tk.Button(self.buttons_frame, text="Start", command=self.start, bg=button_color, fg='white', font=button_font, width=button_width, height=button_height)
        self.start_button.pack(side=tk.LEFT, padx=5)

        self.stop_button = tk.Button(self.buttons_frame, text="Stop", command=self.stop, bg=button_color, fg='white', font=button_font, width=button_width, height=button_height)
        self.stop_button.pack(side=tk.LEFT, padx=5)

        self.reset_button = tk.Button(self.buttons_frame, text="Reset", command=self.reset, bg=button_color, fg='white', font=button_font, width=button_width, height=button_height)
        self.reset_button.pack(side=tk.LEFT, padx=5)

        self.fact_label = tk.Label(root, text="", font=("Helvetica", 14), bg='black', fg='white', wraplength=300, pady=10)
        self.fact_label.pack()

        self.update_clock()

    def start(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True

    def stop(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.running = False
            self.show_fact()

    def reset(self):
        self.start_time = None
        self.elapsed_time = 0
        self.running = False
        self.label.config(text="00:00:00:00")
        self.fact_label.config(text="")

    def get_time(self):
        if self.running:
            current_time = time.time() - self.start_time
        else:
            current_time = self.elapsed_time
        return current_time

    def update_clock(self):
        current_time = self.get_time()
        minutes, seconds = divmod(current_time, 60)
        hours, minutes = divmod(minutes, 60)
        seconds, milliseconds = divmod(seconds, 1)
        time_string = f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}.{int(milliseconds * 1000):03}"
        self.label.config(text=time_string)
        self.root.after(10, self.update_clock)

    def show_fact(self):
        elapsed_seconds = int(self.get_time())
        fact = self.fetch_fact(elapsed_seconds)
        self.fact_label.config(text=f"{fact}")

    def fetch_fact(self, seconds):
        try:
            response = requests.get(f"http://numbersapi.com/{seconds}/trivia")
            if response.status_code == 200:
                return response.text
            else:
                return "Couldn't fetch a fun fact."
        except Exception as e:
            return f"Error: {e}"

def main():
    root = tk.Tk()
    root.title("Stopwatch with Fun Trivia")
    stopwatch = Stopwatch(root)
    root.mainloop()

if __name__ == "__main__":
    main()
