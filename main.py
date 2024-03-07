import tkinter as tk
import time

class ClickSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Teste de Velocidade de Clique")
        self.root.geometry("800x600")

        self.clicks = 0
        self.start_time = 0
        self.is_running = False

        # Lista de cores para o botão
        self.colors = ["#0000aa", "#00aa00", "#aa0000", "#0000aa", "#00aa00", "#aa0000"]

        self.result_label = tk.Label(self.root, text=f"Você clicou {self.clicks} vezes.", font=("Arial", 20))
        self.click_button = tk.Button(self.root, text="Clique aqui!", command=self.start_test, bg="#0000aa",
                                      font=("Arial", 30), padx=100, pady=100)
        self.timer_label = tk.Label(self.root, text="Tempo restante: 5", font=("Arial", 20))

        # Centralizando os widgets
        self.result_label.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        self.click_button.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        self.timer_label.pack(side=tk.BOTTOM, expand=True, fill=tk.BOTH)

    def start_test(self):
        if not self.is_running:
            self.clicks = 0
            self.start_time = time.time()
            self.is_running = True
            self.click_button.config(state=tk.NORMAL)
            self.click_button.config(command=self.increment_clicks)
            self.update_timer()

    def increment_clicks(self):
        if self.is_running:
            self.clicks += 1
            # Mudar a cor do botão a cada clique
            self.click_button.config(bg=self.colors[self.clicks % len(self.colors)])
            self.result_label.config(text=f"Você clicou {self.clicks} vezes.")

    def update_timer(self):
        if self.is_running:
            elapsed_time = int(time.time() - self.start_time)
            remaining_time = 5 - elapsed_time
            if remaining_time <= 0:
                self.is_running = False

                self.timer_label.config(text="Tempo esgotado!")
                self.click_button.config(command=self.start_test, bg="white") # Altera a cor do botão para branco quando o tempo esgota
            else:
                self.timer_label.config(text=f"Tempo restante: {remaining_time}")
                self.root.after(1000, self.update_timer) # Atualiza o timer a cada segundo

if __name__ == "__main__":
    root = tk.Tk()
    ClickSpeedTest(root)
    root.mainloop()
