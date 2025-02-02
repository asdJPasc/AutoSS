import tkinter as tk
import subprocess
import threading

window = tk.Tk()
window.title("I51 autoSS ver. 3")
window.geometry("270x250")  # Set initial window size
window.iconbitmap(r"icoFile\icon.ico")

# Lock the window size (disable resizing)
window.resizable(False, False)

# Set the background color for the window (dark mode)
window.config(bg="#2e2e2e")  # Dark background color

process = None

def run_script():
    global process
    headless_mode = "True" if headless_var.get() else "False"
    
    # Disable the radio buttons once the script starts
    browser_on.config(state="disabled")
    browser_off.config(state="disabled")
    
    # Update the status label to indicate the script is running
    status_label.config(text="Script is running...", fg="green")
    
    # Run script in a new thread to avoid blocking the GUI
    process_thread = threading.Thread(target=start_process, args=(headless_mode,))
    process_thread.start()

    # Disable the "Run AutoSS" and "Check for Updates" buttons, enable the "Stop AutoSS" button
    button_run.config(state="disabled")
    button_check_updates.config(state="disabled")
    button_stop.config(state="normal")

def start_process(headless_mode):
    global process
    try:
        process = subprocess.Popen(["python", "auto.py", headless_mode])
        process.wait()  # Wait for the process to finish
        
        # Update the status when the script completes
        status_label.config(text="Script has stopped", fg="red")
    except Exception as e:
        # If there is an error running the script
        status_label.config(text=f"Error: {str(e)}", fg="red")
    finally:
        # Re-enable buttons after script completes or fails
        button_run.config(state="normal")
        button_check_updates.config(state="normal")
        button_stop.config(state="disabled")

        # Re-enable the radio buttons for browser mode after stopping the script
        browser_on.config(state="normal")
        browser_off.config(state="normal")

def stop_script():
    global process
    if process:
        process.terminate()
        process = None
        status_label.config(text="Script is stopped", fg="red")
        
        # Re-enable the buttons when AutoSS is stopped
        button_run.config(state="normal")
        button_check_updates.config(state="normal")
        button_stop.config(state="disabled")

        # Re-enable the radio buttons for browser mode after stopping the script
        browser_on.config(state="normal")
        browser_off.config(state="normal")
    else:
        status_label.config(text="No active process to stop", fg="black")

def check_for_updates():
    # Simulate checking for updates
    status_label.config(text="Checking for updates...", fg="blue")
    # Simulate a delay for checking
    window.after(2000, lambda: status_label.config(text="No updates available", fg="black"))

headless_var = tk.BooleanVar()
headless_var.set(False)

# Browser option - Radiobutton for "Browser On" and "Browser Off"
browser_frame = tk.Frame(window, bg="#2e2e2e")
browser_frame.pack(pady=10)

browser_on = tk.Radiobutton(browser_frame, text="Browser: On", variable=headless_var, value=True, bg="#2e2e2e", fg="white", selectcolor="#444444", indicatoron=0)
browser_on.pack(side="left", padx=5)

browser_off = tk.Radiobutton(browser_frame, text="Browser: Off", variable=headless_var, value=False, bg="#2e2e2e", fg="white", selectcolor="#444444", indicatoron=0)
browser_off.pack(side="left", padx=5)

# Run AutoSS button
button_run = tk.Button(window, text="Run AutoSS", command=run_script, bg="#444444", fg="white")
button_run.pack(pady=5)

# Stop AutoSS button (initially disabled)
button_stop = tk.Button(window, text="Stop AutoSS", command=stop_script, bg="#444444", fg="white", state="disabled")
button_stop.pack(pady=5)

# Check for updates button
button_check_updates = tk.Button(window, text="Check for Updates", command=check_for_updates, bg="#444444", fg="white")
button_check_updates.pack(pady=5)

# Status label
status_label = tk.Label(window, text="AutoSS is idle", fg="white", bg="#2e2e2e")
status_label.pack(pady=5)

window.mainloop()
