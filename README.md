# 🛡️ Breach Exposure Analyzer  

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Status](https://img.shields.io/badge/Status-Completed-green.svg)
![Security](https://img.shields.io/badge/Security-Risk%20Analysis-red.svg)

---

## 📌 Project Overview

The **Breach Exposure Analyzer** is an automated security analysis tool that simulates real-world incident response workflows. It scrapes exposed employee data from a public source, evaluates Social Security Number (SSN) exposure risk using an external API, and generates structured outputs for reporting and mitigation.

The system produces:
- A structured CSV risk report
- Automated alert emails for high-risk individuals
- Summary statistics for incident analysis

---

## ⚙️ How It Works

```text
🌐 Scrape exposed employee data from target website
        ↓
🧾 Parse and structure employee records
        ↓
🔐 Send each SSN to risk evaluation API
        ↓
📊 Receive risk classification (LOW / MEDIUM / HIGH)
        ↓
📁 Write results to employee_risk.csv
        ↓
📧 Generate alert files for HIGH-risk employees
        ↓
📈 Output risk summary to console


### 📁 Project Structure
final_project/
│
├── index.py                      # Main program entry point
│
├── data/                         # (Optional) raw or backup datasets
│
├── output-data/
│   ├── employee_risk.csv        # Generated risk report
│   └── email/                   # High-risk alert messages
│       ├── john_doe.txt
│       ├── jane_smith.txt
│       └── ...
│
├── README.md
└── LICENSE
