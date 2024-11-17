import tkinter as tk
import math


class MouseTrackerApp:
    def __init__(self, display):
        self.root = tk.Tk()
        self.root.title("Mouse Tracker")
        self.display = display
        self.recording = False
        self.mouse_positions = []

    def start_recording(self, pos_x ,pos_y):
        self.recording = True
        self.mouse_positions = [(pos_x, pos_y)]

    def track_mouse(self, pos_x ,pos_y):
        if self.recording:
            self.mouse_positions.append((pos_x,pos_y))

    def stop_recording(self):
        if self.recording:
            self.recording = False
            return self.determine_direction()
        
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

        if longest_segment_index + 1 < len(self.mouse_positions):
            x1, y1 = self.mouse_positions[longest_segment_index]
            x2, y2 = self.mouse_positions[longest_segment_index + 1]
            dx = x2 - x1
            dy = y2 - y1

            angle = math.degrees(math.atan2(dy, dx))
            if angle < 0:
                angle += 360

            if 22.5 <= angle < 67.5:
                return "RIGHT_DOWN"
            elif 67.5 <= angle < 112.5:
                return "DOWN"
            elif 112.5 <= angle < 157.5:
                return "LEFT_DOWN"
            elif 157.5 <= angle < 202.5:
                return "LEFT"
            elif 202.5 <= angle < 247.5:
                return "LEFT_UP"
            elif 247.5 <= angle < 292.5:
                return "UP"
            elif 292.5 <= angle < 337.5:
                return "RIGHT_UP"
            else:
                return "RIGHT"
            
        else: return "BLOCK"
        
