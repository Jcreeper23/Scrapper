🌐 Web Scraper – Configurable Python GUI Scraper
A modern, easy-to-use Python web scraper with a GUI for scraping content from websites. Built with BeautifulSoup and CustomTkinter, this tool lets you fetch website data, customize settings, and save output with just a few clicks.

✨ Features
✅ Beautiful GUI – Built with CustomTkinter for a clean and modern interface.
✅ Configurable Settings – Supports saving and loading settings from a config.json file.
✅ Formatted Output – Saves scraped data into a text file or easily extendable to HTML.
✅ Fast & Lightweight – Simple, beginner-friendly, and easy to extend.
✅ Error Handling – Alerts for connection issues or empty results.

💻 Screenshots
![Web Scrapper](Scrapper.png)

📥 Installation
```bash
git clone https://github.com/Jcreeper23/Scrapper.git
cd Scrapper
```
Install the dependencies:
```bash
pip install requests beautifulsoup4 customtkinter
```
Run the app:
```bash
python Scrapper.py
```

🖥️ How to Use
1. Launch the app by running `python Scrapper.py`.  
2. In the app:
   - Enter the **website URL** to scrape.  
   - Specify the **HTML tag** (e.g., `div`, `p`) you want to extract.  
   - (Optional) Add a **CSS class** for more targeted scraping.  
   - Set the **output file name** (e.g., `output.txt`).  
3. Click **"Scrape Website"** to start scraping.  
4. Results will be saved in the specified file.  
5. (Optional) Click **"Save Configuration"** to store your settings in `config.json` for later use.  

🛠 Example
Setting	Example
URL	https://example.com
HTML Tag	p
CSS Class (optional)	article-content
Output File	results.txt

📄 Config File (config.json)
You can edit your scraper settings directly in config.json:

```json
{
  "url": "https://example.com",
  "search_tag": "p",
  "search_class": "article",
  "output_file": "output.txt"
}
```

