import requests
from bs4 import BeautifulSoup
import json
import customtkinter as ctk
from tkinter import messagebox


def load_config():
    try:
        with open("config.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        default_config = {
            "url": "https://example.com",
            "search_tag": "p",
            "search_class": "",
            "output_file": "output.txt"
        }
        with open("config.json", "w") as file:
            json.dump(default_config, file, indent=4)
        return default_config


def scrape_website():
    config = load_config()
    url = config["url"]
    tag = config["search_tag"]
    css_class = config["search_class"]
    output_file = config["output_file"]

    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        elements = soup.find_all(tag, class_=css_class if css_class else None)

        if not elements:
            messagebox.showinfo("Result", "No elements found with the given tag/class.")
            return

        with open(output_file, "w", encoding="utf-8") as file:
            for idx, elem in enumerate(elements, start=1):
                text = elem.get_text(strip=True)
                file.write(f"{idx}. {text}\n\n")

        messagebox.showinfo("Success", f"Scraping complete! Output saved to {output_file}")

    except requests.RequestException as e:
        messagebox.showerror("Error", f"Failed to fetch the website:\n{e}")


def save_config():
    new_config = {
        "url": url_entry.get(),
        "search_tag": tag_entry.get(),
        "search_class": class_entry.get(),
        "output_file": output_entry.get()
    }
    with open("config.json", "w") as file:
        json.dump(new_config, file, indent=4)
    messagebox.showinfo("Config Saved", "Configuration saved successfully!")


ctk.set_appearance_mode("System")  # Light/Dark/Auto
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Jcreepers Web Scraper")
app.geometry("500x400")

title = ctk.CTkLabel(app, text="🌐 JCS Web Scraper", font=ctk.CTkFont(size=24, weight="bold"))
title.pack(pady=20)

config = load_config()

url_entry = ctk.CTkEntry(app, width=400, placeholder_text="Website URL")
url_entry.insert(0, config["url"])
url_entry.pack(pady=10)

tag_entry = ctk.CTkEntry(app, width=400, placeholder_text="HTML Tag (e.g., div, p)")
tag_entry.insert(0, config["search_tag"])
tag_entry.pack(pady=10)

class_entry = ctk.CTkEntry(app, width=400, placeholder_text="CSS Class (optional)")
class_entry.insert(0, config["search_class"])
class_entry.pack(pady=10)

output_entry = ctk.CTkEntry(app, width=400, placeholder_text="Output File")
output_entry.insert(0, config["output_file"])
output_entry.pack(pady=10)

scrape_button = ctk.CTkButton(app, text="Scrape Website", command=scrape_website)
scrape_button.pack(pady=15)

save_button = ctk.CTkButton(app, text="Save Configuration", command=save_config)
save_button.pack(pady=5)

app.mainloop()