# pwned-ssn-analyzer
Automated breach analysis tool that scrapes exposed employee data from a public source, evaluates SSN exposure risk via API, and generates structured CSV reports. Includes automated alert files for high-risk individuals and summary metrics to support incident response and risk assessment.


# 🛡️ Breach Exposure Analyzer (CIT 30900 Final Project)

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Security](https://img.shields.io/badge/Security-Risk%20Analysis-red)

---

## 🚨 Overview

Automated breach analysis tool that scrapes exposed employee data from a public source, evaluates Social Security Number (SSN) exposure risk via an external API, and generates structured risk reports.

It also produces automated alert files for high-risk individuals and summarizes exposure metrics to support incident response and security assessment workflows.

---

## ⚙️ System Workflow

```text
🌐 Scrape exposed employee data
        ↓
🧾 Parse and normalize records
        ↓
🔐 Send SSNs to risk evaluation API
        ↓
📊 Classify risk (LOW / MEDIUM / HIGH)
        ↓
📁 Generate CSV report
        ↓
📧 Create alert emails for HIGH-risk employees
        ↓
📈 Print summary statistics
