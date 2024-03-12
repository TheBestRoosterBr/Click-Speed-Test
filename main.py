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

        self.colors = ["#0000aa", "#00aa00", "#aa0000", "#0000aa", "#00aa00", "#aa0000"]

        self.result_label = tk.Label(self.root, text=f"Você clicou {self.clicks} vezes.", font=("Arial", 20))
        self.click_button = tk.Button(self.root, text="Clique aqui!", command=self.start_test, bg="#0000aa",
                                      font=("Arial", 30), padx=100, pady=100)
        self.timer_label = tk.Label(self.root, text="Tempo restante: 5", font=("Arial", 20))
        self.restart_button = tk.Button(self.root, text="Reiniciar", command=self.reiniciar, state=tk.NORMAL)

        self.result_label.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        self.click_button.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        self.timer_label.pack(side=tk.BOTTOM, expand=True, fill=tk.BOTH)
        self.restart_button.pack(side=tk.BOTTOM, expand=True, fill=tk.BOTH)

    def start_test(self):
        if not self.is_running:
            self.clicks = 1
            self.start_time = time.time()
            self.is_running = True
            self.click_button.config(state=tk.NORMAL)
            self.click_button.config(command=self.increment_clicks)
            self.restart_button.config(state=tk.NORMAL)
            self.update_timer()
            self.result_label.config(text=f"Você clicou {self.clicks} vezes.")
            self.click_button.config(text="Clique aqui!", image="")  # Limpa a imagem do botão

    def reiniciar(self):
        self.root.destroy()
        main()

    def increment_clicks(self):
        if self.is_running:
            self.clicks += 1
            self.click_button.config(bg=self.colors[self.clicks % len(self.colors)])
            self.result_label.config(text=f"Você clicou {self.clicks} vezes.")
        else:
            self.is_running = True
            self.clicks += 1
            self.start_time = time.time()
            self.start_test()

    def update_timer(self):
        if self.is_running:
            elapsed_time = time.time() - self.start_time
            remaining_time = 5 - elapsed_time
            remaining_seconds = int(remaining_time)
            remaining_milliseconds = int((remaining_time - remaining_seconds) * 1000)
            if remaining_time <= 0:
                self.is_running = False
                self.timer_label.config(text="Tempo esgotado!")
                self.click_button.config(state=tk.DISABLED, bg="white")
                self.restart_button.config(state=tk.NORMAL)
                self.determine_animal()
            else:
                self.timer_label.config(text=f"Tempo restante: {remaining_seconds}:{remaining_milliseconds:03d}")
                self.root.after(1, self.update_timer)

    def determine_animal(self):
        animal_image = None
        if self.clicks < 20:
            animal = "Patético. Você é um Saguin"
            animal_image = tk.PhotoImage(file="Assets/saguin.png")
        elif self.clicks < 30:
            animal = "Horrível. Você é uma Coruja"
            animal_image = tk.PhotoImage(file="Assets/coruja.png")
        elif self.clicks < 50:
            animal = "Parabéns! Você é um Calango"
            animal_image = tk.PhotoImage(file="Assets/calango.png")
        elif self.clicks < 70:
            animal = "Nossa! Você é um Carcará"
            animal_image = tk.PhotoImage(file="Assets/carcara.png")
        else:
            animal = "Caramba! Você precisa de uma namorada"
            animal_image = tk.PhotoImage(file="Assets/namorada.png")

        self.result_label.config(text=f"{self.clicks} cliques. {animal}.")
        self.click_button.config(text="", image=animal_image)
        self.click_button.image = animal_image  # Garante que a imagem não seja coletada pelo garbage collector


def main():
    root = tk.Tk()
    ClickSpeedTest(root)
    root.mainloop()


if __name__ == "__main__":
    main()
