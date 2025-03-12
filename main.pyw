import tkinter as tk
import random
import platform

class FBISeizureScreen:
    def __init__(self, root):
        self.root = root
        self.setup_window()
        self.create_elements()
        self.start_warnings()

    def setup_window(self):
        self.root.title("FBI SEIZURE NOTICE")
        self.root.configure(bg="navy")
        self.root.attributes("-fullscreen", True)
        
        # Get screen width and height
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

    def create_elements(self):
        # Main frame
        self.main_frame = tk.Frame(self.root, bg="navy")
        self.main_frame.pack(expand=True, fill="both", padx=40, pady=40)
        
        # Top warning label
        self.warning_label = tk.Label(
            self.main_frame, 
            text="*** FEDERAL BUREAU OF INVESTIGATION ***",
            font=("Courier New", 24, "bold"), 
            fg="red", 
            bg="navy"
        )
        self.warning_label.pack(pady=20)
        
        # FBI text logo instead of image
        self.text_logo = tk.Label(
            self.main_frame,
            text="FBI",
            font=("Impact", 72, "bold"),
            fg="gold",
            bg="navy"
        )
        self.text_logo.pack(pady=10)
        
        # Second line of FBI text
        self.text_logo_line2 = tk.Label(
            self.main_frame,
            text="FEDERAL BUREAU OF INVESTIGATION",
            font=("Arial", 16, "bold"),
            fg="gold",
            bg="navy"
        )
        self.text_logo_line2.pack(pady=5)
        
        # Main message text
        self.message_frame = tk.Frame(self.main_frame, bg="navy", bd=2, relief=tk.RIDGE)
        self.message_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        message_text = (
            "THIS DEVICE AND OTHER DEVICES CONNECTED TO YOUR INTERNET HAS BEEN SEIZED BY FBI\n\n"
            "YOUR COMPUTER HAS BEEN LOCKED DUE TO VIOLATION OF FEDERAL LAWS\n"
            "SECTION 1030 - FRAUD AND RELATED ACTIVITY IN CONNECTION WITH COMPUTERS\n\n"
            "THIS IS AN OFFICIAL FBI INVESTIGATION\n"
            "CASE ID: #FWN-778391-04\n\n"
            "THE FOLLOWING VIOLATIONS HAVE BEEN DETECTED:\n"
            "- UNAUTHORIZED ACCESS TO PROTECTED NETWORKS\n"
            "- DISTRIBUTION OF PROHIBITED CONTENT\n"
            "- MULTIPLE CYBERLAW VIOLATIONS\n"
            "- HOLDING FILES MAY CAUSE MULTIPLE CYBERLAW VIOLATIONS AND CONTAINS ILLEGAL GOVERNMENT INFO\n\n"
            "ALL FILES HAVE BEEN ENCRYPTED AND YOUR SYSTEM ACTIVITY IS BEING MONITORED\n\n"
        )
        
        self.message_text = tk.Label(
            self.message_frame, 
            text=message_text,
            font=("Courier New", 14), 
            fg="white", 
            bg="black",
            justify=tk.LEFT,
            padx=10,
            pady=10
        )
        self.message_text.pack(fill="both", expand=True)
        
        # Bottom warning and instructions
        self.footer_frame = tk.Frame(self.main_frame, bg="navy")
        self.footer_frame.pack(fill="x", pady=20)
        
        self.timer_label = tk.Label(
            self.footer_frame,
            text="TIME REMAINING: 23:59:59.000",
            font=("Courier New", 30, "bold"),  # Font büyüklüğünü 16'dan 24'e çıkardım
            fg="red",
            bg="navy"
        )
        self.timer_label.pack(pady=10)
        
        # System info
        system_info = f"SYSTEM: {platform.system()} {platform.version()}\nUSER: {platform.node()}\nPROCESSOR: {platform.processor()}"
        self.system_info = tk.Label(
            self.footer_frame,
            text=system_info,
            font=("Courier New", 10),
            fg="white",
            bg="navy",
            justify=tk.LEFT
        )
        self.system_info.pack(pady=10)
        
        # Fake console output
        self.console_frame = tk.Frame(self.main_frame, bg="black", bd=1, relief=tk.SUNKEN)
        self.console_frame.pack(fill="x", padx=20, pady=10)
        
        self.console = tk.Text(
            self.console_frame,
            font=("Courier New", 10),
            bg="black",
            fg="#00ff00",
            height=7,
            width=80
        )
        self.console.pack(fill="both", expand=True)
        self.console.insert(tk.END, "FBI@SEIZURE-SYSTEM:~$ Initializing seizure protocol...\n")
        self.console.configure(state="disabled")
        
        # Exit button with warning (for the simulation)
        self.exit_note = tk.Label(
            self.main_frame,
            text="This is only a simulation. Press ESC to exit.",
            font=("Arial", 8),
            fg="white",
            bg="navy"
        )
        self.exit_note.pack(side="bottom", pady=5)
        
        # Bind ESC key to exit
        self.root.bind("<Escape>", self.exit_simulation)

    def exit_simulation(self, event=None):
        self.root.destroy()

    def start_warnings(self):
        self.update_timer()
        self.update_console()
        self.flash_elements()

    def update_timer(self):
        # Fake countdown timer
        current_time = self.timer_label.cget("text")
        time_parts = current_time.split(": ")[1].split(":")
        hours = int(time_parts[0])
        minutes = int(time_parts[1])
        seconds, milliseconds = map(int, time_parts[2].split("."))

        # Decrease milliseconds first
        milliseconds -= 1
        if milliseconds < 0:
            milliseconds = 999
            seconds -= 1

        # If seconds run out, reset to 59 and decrease minutes
        if seconds < 0:
            seconds = 59
            minutes -= 1

        # If minutes run out, reset to 59 and decrease hours
        if minutes < 0:
            minutes = 59
            hours -= 1

        # If hours run out, reset to 23
        if hours < 0:
            hours = 23

        new_time = f"TIME REMAINING: {hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:03d}"
        self.timer_label.config(text=new_time)

        # Update every 1 ms
        self.root.after(1, self.update_timer)

    def flash_elements(self):
        # Flash the warning label
        current_color = self.warning_label.cget("fg")
        new_color = "white" if current_color == "red" else "red"
        self.warning_label.config(fg=new_color)
        
        # Flash the FBI text logo occasionally
        if random.random() < 0.3:  # 30% chance of flashing
            current_logo_color = self.text_logo.cget("fg")
            new_logo_color = "red" if current_logo_color == "gold" else "gold"
            self.text_logo.config(fg=new_logo_color)
        
        self.root.after(500, self.flash_elements)

    def update_console(self):
        # Fake console output
        console_messages = [
            "Scanning system files...",
            "Encrypted 32% of user data...",
            "Backing up critical evidence...",
            "Monitoring network connections...",
            "Capturing system information...",
            "Blocking access to system resources...",
            "Transmitting data to FBI central server...",
            "Installing monitoring software...",
            "Checking for tampering attempts...",
            "Recording biometric data...",
            "Scanning for external drives...",
            "Monitoring for countermeasures...",
            f"Detected {random.randint(2, 8)} active network connections",
            f"Found {random.randint(10, 50)} pieces of evidence",
            f"Disabling system recovery: {random.choice(['SUCCESS', 'IN PROGRESS'])}",
            f"Camera surveillance activated: {random.choice(['ACTIVE', 'PENDING'])}",
            f"Geolocation tracking: {random.choice(['ACTIVE', 'TRIANGULATING', 'CONFIRMED'])}",
            "Bypassing user security measures..."
        ]
        
        self.console.configure(state="normal")
        random_message = random.choice(console_messages)
        self.console.insert(tk.END, f"FBI@SEIZURE-SYSTEM:~$ {random_message}\n")
        
        # Scroll to the end
        self.console.see(tk.END)
        
        # Limit console text length
        all_text = self.console.get("1.0", tk.END)
        lines = all_text.split("\n")
        if len(lines) > 8:
            self.console.delete("1.0", "2.0")
            
        self.console.configure(state="disabled")
        
        # Update console at random intervals
        self.root.after(random.randint(1500, 4000), self.update_console)

# Main function to start the application
def main():
    root = tk.Tk()
    app = FBISeizureScreen(root)
    root.mainloop()

if __name__ == "__main__":
    main()
