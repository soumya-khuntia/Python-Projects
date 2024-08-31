import tkinter as tk
from threading import Thread
import pyautogui
import cv2
import numpy as np

class ScreenRecorder:
    def __init__(self, root):
        self.root = root
        self.root.title("Screen Recorder")

        self.recording = False
        self.output_file_path = "screen_record.avi"
        self.frame_rate = 30
        self.screen_width, self.screen_height = pyautogui.size()

        self.start_button = tk.Button(root, text="Start Recording", command=self.start_recording)
        self.stop_button = tk.Button(root, text="Stop Recording", state=tk.DISABLED, command=self.stop_recording)

        self.start_button.pack(pady=10)
        self.stop_button.pack(pady=10)

    def start_recording(self):
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

        self.recording = True
        self.out = cv2.VideoWriter(self.output_file_path, cv2.VideoWriter_fourcc(*'XVID'), self.frame_rate, (self.screen_width, self.screen_height))

        self.recording_thread = Thread(target=self.record_screen)
        self.recording_thread.start()

    def stop_recording(self):
        self.recording = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def record_screen(self):
        while self.recording:
            screen = pyautogui.screenshot()
            frame = np.array(screen)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.out.write(frame)

        self.out.release()

if __name__ == "__main__":
    root = tk.Tk()
    app = ScreenRecorder(root)
    root.mainloop()
