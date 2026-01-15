# 📂 Office Automation Suite

A collection of Python scripts designed to automate repetitive administrative tasks, reduce manual data entry errors, and improve office workflow efficiency.

## 🚀 Overview
As a Computer Science student, I noticed that many office roles involve repetitive digital chores. I built this suite to automate those processes, allowing users to focus on higher-value work.

**Key Features:**
* **Instant Organization:** Sorts messy folders by file type automatically.
* **Data Consolidation:** Merges multiple Excel reports into a single master file.
* **Market Research:** scrapes competitor pricing data from the web for analysis.

## 🛠️ Tools Included

### 1. File Sorter (`organize_files.py`)
Scans a target directory (like "Downloads") and organizes files into subfolders (`/Documents`, `/Images`, `/Videos`) based on their extensions.
* **Tech:** `os`, `shutil`

### 2. Excel Merger (`merge_excel.py`)
Reads all Excel files in a specific folder and combines them into one master spreadsheet, preserving headers and data structure.
* **Tech:** `pandas`, `openpyxl`

### 3. Price Monitor (`price_monitor.py`)
A web scraper that tracks product prices on competitor websites and exports the data to a clean CSV file.
* **Tech:** `requests`, `BeautifulSoup`, `csv`

### 4. Email Reporter (`send_report.py`)
(Optional) Automatically sends the generated reports or CSVs via email using secure SMTP protocols.
* **Tech:** `smtplib`, `ssl`, `dotenv`
