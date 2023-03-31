import random
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt

class BrownianMotion:
    def __init__(self, width=600, height=400, ball_radius=10, speed=1, velocity_x=10, velocity_y=10, num_steps=10000):
        self.width = width
        self.height = height
        self.ball_radius = ball_radius
        self.speed = speed
        self.window = tk.Tk()
        self.window.title("Brownian Motion")
        self.canvas = tk.Canvas(self.window, width=self.width, height=self.height, bg="white")
        self.canvas.pack()
        self.ball_x = 0
        self.ball_y = 0
        self.ball = self.canvas.create_oval(self.ball_x - self.ball_radius, self.ball_y - self.ball_radius,
                                             self.ball_x + self.ball_radius, self.ball_y + self.ball_radius,
                                             fill="blue")
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.num_steps = num_steps
        self.x = np.zeros(num_steps + 1)
        self.y = np.zeros(num_steps + 1)

    def update(self):
        self.velocity_x += random.uniform(-self.speed, self.speed)
        self.velocity_y += random.uniform(-self.speed, self.speed)
        self.ball_x += self.velocity_x
        self.ball_y += self.velocity_y
        if self.ball_x - self.ball_radius < 0:
            self.ball_x = self.ball_radius
            self.velocity_x = -self.velocity_x
        elif self.ball_x + self.ball_radius > self.width:
            self.ball_x = self.width - self.ball_radius
            self.velocity_x = -self.velocity_x
        if self.ball_y - self.ball_radius < 0:
            self.ball_y = self.ball_radius
            self.velocity_y = -self.velocity_y
        elif self.ball_y + self.ball_radius > self.height:
            self.ball_y = self.height - self.ball_radius
            self.velocity_y = -self.velocity_y

        self.x = np.append(self.x, self.ball_x)
        self.y = np.append(self.y, self.ball_y)
        self.canvas.coords(self.ball, self.ball_x - self.ball_radius, self.ball_y - self.ball_radius,
                            self.ball_x + self.ball_radius, self.ball_y + self.ball_radius)
        self.window.after(10, self.update)

    def start(self):
        self.update()
        self.window.after(self.num_steps, self.window.destroy)
        self.window.mainloop()
        self.plot()

    def plot(self):
        fig = plt.figure(figsize=(6, 6))
        ax = fig.add_subplot(111)
        ax.plot(self.x, self.y, linewidth=1, color="blue")
        ax.set_xlim(0, self.width)
        ax.set_ylim(0, self.height)
        ax.set_aspect("equal", adjustable="box")
        plt.show()

if __name__ == "__main__":
    b = BrownianMotion()
    b.start()
