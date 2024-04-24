import tkinter as tk
import random


class SnakeGame:
    """Конструктор """
    def __init__(self, master):
        self.master = master
        self.master.title("Snake Game")
        self.canvas = tk.Canvas(master, width=400, height=400, bg="black")
        self.canvas.pack()
        self.master.bind("<KeyPress>", self.change_direction)
        self.snake = [(20, 20)]
        self.food = self.generate_food()
        self.direction = "Right"
        self.score = 0
        self.game_speed = 100
        self.running = True

        self.update()

    def generate_food(self):
        """Создает еду на поле"""
        while True:
            x = random.randint(0, 19) * 20
            y = random.randint(0, 19) * 20
            if (x, y) not in self.snake:
                return x, y

    def change_direction(self, event):
        """Меняет направление змеи"""
        key = event.keysym
        if key == "Up" and self.direction != "Down":
            self.direction = "Up"
        elif key == "Down" and self.direction != "Up":
            self.direction = "Down"
        elif key == "Left" and self.direction != "Right":
            self.direction = "Left"
        elif key == "Right" and self.direction != "Left":
            self.direction = "Right"

    def update(self):
        """Обновляет игровой цикл"""
        if self.running:
            x, y = self.snake[0]
            if self.direction == "Up":
                y -= 20
            elif self.direction == "Down":
                y += 20
            elif self.direction == "Left":
                x -= 20
            elif self.direction == "Right":
                x += 20

            if x < 0 or x >= 400 or y < 0 or y >= 400 or (x, y) in self.snake:
                self.running = False

            self.snake.insert(0, (x, y))
            if (x, y) == self.food:
                self.score += 10
                self.food = self.generate_food()
            else:
                self.snake.pop()

            self.canvas.delete("all")
            self.canvas.create_rectangle(*self.food, self.food[0] + 20, self.food[1] + 20, fill="red")
            for segment in self.snake:
                self.canvas.create_rectangle(segment[0], segment[1], segment[0] + 20, segment[1] + 20, fill="green")

            self.canvas.create_text(200, 10, text=f"Score: {self.score}", fill="white")
            self.master.after(self.game_speed, self.update)

# Создание экземпляра игры
root = tk.Tk()
game = SnakeGame(root)
root.mainloop()
