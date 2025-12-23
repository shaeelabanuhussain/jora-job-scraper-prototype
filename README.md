# Jora Job Scraper - NZ Healthcare Jobs

A Python web scraper for collecting publicly available GP job listings from Jora NZ using Selenium.

## ⚠️ Disclaimer

**For educational and personal research only.** Users must comply with Jora's Terms of Service and robots.txt. The author assumes no liability for misuse. Web scraping may violate terms of service—always check before use.

## Features

- Scrapes GP job listings from Jora NZ
- Extracts: title, company, location, posted date, job link
- Auto-pagination with duplicate detection
- Exports to CSV

## Installation

```bash
git clone https://github.com/yourusername/jora-job-scraper.git
cd jora-job-scraper
pip install -r requirements.txt
```

**requirements.txt:**
```
selenium==4.15.2
webdriver-manager==4.0.1
pandas==2.1.3
```

## Usage

Run the scraper:
```bash
python jora_scraper.py
```

Output: `jora_jobs.csv` with job details.

**Customize:**
- Change `max_pages` variable to scrape fewer/more pages
- Modify `url` variable for different search terms or locations
- Uncomment `options.add_argument('--headless')` to run without GUI

## Ethical Usage

- Check `https://nz.jora.com/robots.txt` before scraping
- Limit frequency (max once per day recommended)
- Don't reduce built-in delays (5 seconds)
- Personal use only—no commercial use without permission
- Don't share personal information from job postings

## Troubleshooting

- **No data collected**: Increase `time.sleep()` values or check if website structure changed
- **Timeout errors**: Increase WebDriverWait timeout to 20
- **ChromeDriver issues**: Script auto-downloads it, ensure internet connection

## License

MIT License - see LICENSE file

---

**Not affiliated with Jora.** This tool may break if Jora updates their website. Always respect rate limits and Terms of Service.
