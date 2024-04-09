import tkinter as tk
import math

class MouseTrackerApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Mouse Tracker")

        self.canvas = tk.Canvas(self.root, width=400, height=300, bg='white')
        self.canvas.pack()

        self.canvas.bind('<Button-1>', self.start_recording)
        self.canvas.bind('<B1-Motion>', self.track_mouse)
        self.canvas.bind('<ButtonRelease-1>', self.stop_recording)

        self.recording = False
        self.mouse_positions = []

    def start_recording(self, event):
        self.recording = True
        self.mouse_positions = [(event.x, event.y)]

    def track_mouse(self, event):
        if self.recording:
            self.mouse_positions.append((event.x, event.y))
            self.draw_line()

    def stop_recording(self, event):
        if self.recording:
            self.recording = False
            self.draw_line()
            self.determine_direction()

    def draw_line(self):
        self.canvas.delete("line")
        for i in range(len(self.mouse_positions) - 1):
            x1, y1 = self.mouse_positions[i]
            x2, y2 = self.mouse_positions[i + 1]
            self.canvas.create_line(x1, y1, x2, y2, fill='black', width=2, tags="line")

    def determine_direction(self):
        longest_length = 0
        longest_segment_index = 0

        for i in range(len(self.mouse_positions) - 1):
            x1, y1 = self.mouse_positions[i]
            x2, y2 = self.mouse_positions[i + 1]
            length = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            if length > longest_length:
                longest_length = length
                longest_segment_index = i

        x1, y1 = self.mouse_positions[longest_segment_index]
        x2, y2 = self.mouse_positions[longest_segment_index + 1]
        dx = x2 - x1
        dy = y2 - y1

        angle = math.degrees(math.atan2(dy, dx))
        if angle < 0:
            angle += 360

        if 22.5 <= angle < 67.5:
            print("Huong phai-duoi")
        elif 67.5 <= angle < 112.5:
            print("Huong duoi")
        elif 112.5 <= angle < 157.5:
            print("Huong duoi-trai")
        elif 157.5 <= angle < 202.5:
            print("Huong trai")
        elif 202.5 <= angle < 247.5:
            print("Huong trai-tren")
        elif 247.5 <= angle < 292.5:
            print("Huong tren")
        elif 292.5 <= angle < 337.5:
            print("Huong tren-phai")
        else:
            print("Huong phai")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = MouseTrackerApp()
    app.run()
