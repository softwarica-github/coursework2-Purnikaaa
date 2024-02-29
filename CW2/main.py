import tkinter as tk
from tkinter import scrolledtext
import threading
import requests
from core import requester, extractor, crawler
from urllib.parse import unquote

# Functionality adapted from sqlifinder.py
def scan_for_vulnerabilities(domain, output_text, update_status):
    update_status("Scanning...")
    vulnerabilities_found = False  # Track if any vulnerabilities are found
    
    url = f"http://web.archive.org/cdx/search/cdx?url={domain}/*&output=txt&fl=original&collapse=urlkey&page=/"
    
    response = requester.connector(url)
    crawled_urls = crawler.spider(f"http://{domain}", 10)
    response = "\n".join(crawled_urls) + "\n" + response if response else ""
    response = unquote(response)

    exclude = ['woff', 'js', 'ttf', 'otf', 'eot', 'svg', 'png', 'jpg']
    final_uris = extractor.param_extract(response, "high", exclude, "")

    with open('./payloads.txt', 'r') as file:
        payloads = file.read().splitlines()

    output_text.config(state=tk.NORMAL)  # Set state to NORMAL before inserting text

    for uri in final_uris:
        for payload in payloads:
            final_url = f"{uri}{payload}"
            try:
                req = requests.get(final_url)
                if 'SQL' in req.text or 'sql' in req.text or 'Sql' in req.text:
                    output_text.insert(tk.END, f"[sql-injection] {final_url}\n")
                    vulnerabilities_found = True
            except Exception as e:
                continue

    output_text.config(state=tk.DISABLED)  # Set state back to DISABLED after inserting text

    if not vulnerabilities_found:
        output_text.insert(tk.END, "No SQL injection found in the website.\n")
    
    update_status("Scan completed.")

# Tkinter GUI setup
def setup_gui():
    window = tk.Tk()
    window.title("SQLiFinder GUI")
    window.geometry("800x600")
    window.configure(bg="#003366")  # Dark blue background
    
    def update_status(message):
        status_label.config(text=message)
        window.update_idletasks()

    def start_scan():
        domain = domain_entry.get()
        output_text.delete(1.0, tk.END)
        threading.Thread(target=scan_for_vulnerabilities, args=(domain, output_text, update_status)).start()

    def clear_url():
        domain_entry.delete(0, tk.END)
        clear_output()

    def clear_output():
        output_text.config(state=tk.NORMAL)  # Set state to NORMAL before clearing text
        output_text.delete(1.0, tk.END)
        output_text.config(state=tk.DISABLED)  # Set state back to DISABLED after clearing text

    def exit_app():
        window.destroy()

    domain_label = tk.Label(window, text="Domain:", bg="#003366", fg="white")
    domain_label.pack(pady=(10, 0))

    domain_entry = tk.Entry(window, width=50)
    domain_entry.pack(pady=(0, 20))

    button_frame = tk.Frame(window, bg="#003366")
    button_frame.pack()

    start_button = tk.Button(button_frame, text="Start Scan", command=start_scan)
    start_button.pack(side=tk.LEFT, padx=5)

    clear_button = tk.Button(button_frame, text="Clear", command=clear_url)
    clear_button.pack(side=tk.LEFT, padx=5)

    exit_button = tk.Button(button_frame, text="Exit", command=exit_app)
    exit_button.pack(side=tk.LEFT, padx=5)

    output_text = scrolledtext.ScrolledText(window, width=70, height=20)
    output_text.pack(pady=(10, 10))
    output_text.configure(state=tk.DISABLED)  # Set initial state to DISABLED

    # Status label to show scanning status
    status_label = tk.Label(window, text="Ready", bg="#003366", fg="white")
    status_label.pack(pady=(10, 0))

    window.mainloop()

if __name__ == "__main__":
    setup_gui()
