import tkinter as tk
import subprocess

window = tk.Tk()
window.title("I51 autoSS ver. 3")
window.geometry("270x180")
window.iconbitmap(r"icoFile\icon.ico")

process = None

def run_script():
    global process
    headless_mode = "True" if headless_var.get() else "False"
    process = subprocess.Popen(["python", "auto.py", headless_mode])
    status_label.config(text="AutoSS is running", fg="green")

def stop_script():
    global process
    if process:
        process.terminate()
        process = None
        status_label.config(text="AutoSS is stopped", fg="red")
    else:
        status_label.config(text="No active process to stop", fg="black")

headless_var = tk.BooleanVar()
headless_var.set(False)
headless_checkbox = tk.Checkbutton(window, text="Browser: On", variable=headless_var)
headless_checkbox.pack(pady=10)

button_run = tk.Button(window, text="Run AutoSS", command=run_script)
button_run.pack(pady=5)

button_stop = tk.Button(window, text="Stop AutoSS", command=stop_script)
button_stop.pack(pady=5)

status_label = tk.Label(window, text="AutoSS is idle", fg="black")
status_label.pack(pady=5)

window.mainloop()
