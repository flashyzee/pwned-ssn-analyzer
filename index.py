# pip install requests beautifulsoup4

from bs4 import BeautifulSoup
import requests
import csv
import os
from typing import List, Dict

BASE_URL = "https://focusonfiles.com/strawbridge/"
API_URL = "https://focusonfiles.com/strawbridge/api/"


def silent_crawler() -> None:
    # 1. UI / intro stuff FIRST
    """
    This is a basic user interface that initializes before all other components and launches Silent Crawler.
    """
    print("=" * 40)
    print("   Welcome to SilentCrawler")
    print("=" * 40)

    print(r"""
      ________  _ _            _   
     / _____/ (_) |          | |  
    ( (____   _| | ___ _ __  | |_ 
     \____ \ | | |/ _ \ '_ \ | __|
     _____) )| | |  __/ | | || |_ 
    (______/ |_|_|\___|_| |_| \__|
    """)

    print("\n[SilentCrawler] Starting...\n")


def fetch_employee_data() -> List[Dict[str, str]]:
    """
    Scrapes employee data from Strawbridge Industries website.
    Returns list of employees with first name, last name, email, ssn.
    """

    page = requests.get(BASE_URL)
    soup = BeautifulSoup(page.content, "html.parser")

    employees = []

    first_names = soup.find_all("span", class_="emp_first_name")
    last_names = soup.find_all("span", class_="emp_last_name")
    emails = soup.find_all("span", class_="emp_email")
    ssns = soup.find_all("span", class_="secret")

    for i in range(min(len(first_names), len(last_names), len(emails), len(ssns))):
        employees.append({
            "first_name": first_names[i].get_text(strip=True),
            "last_name": last_names[i].get_text(strip=True),
            "email": emails[i].get_text(strip=True),
            "ssn": ssns[i].get_text(strip=True)
        })

    return employees


def get_risk_level(username: str, ssn: str) -> str:
    """
    Calls external API to get SSN exposure risk level.
    Returns LOW, MEDIUM, or HIGH.
    """

    try:
        url = f"{API_URL}?username={username}&ssn={ssn}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()
        return data["data"]["risk"].upper()

    except Exception:
        return "LOW"


def write_csv(employees: List[Dict[str, str]]) -> None:
    """
    Writes employee risk data to employee_risk.csv
    """

    with open("employee_risk.csv", "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["first_name", "last_name", "email", "ssn", "risk_level"]
        )

        writer.writeheader()
        writer.writerows(employees)


def create_email(emp: Dict[str, str]) -> None:
    """
    Creates email text file for high risk employees.
    """

    os.makedirs("email", exist_ok=True)

    safe_name = f"{emp['first_name']}_{emp['last_name']}".replace(" ", "_").lower()
    filename = f"email/{safe_name}.txt"

    content = f"""To: {emp['first_name']} {emp['last_name']} <{emp['email']}>
From: IT Security Admin <itsecadmin@yourcompany.com>

Dear {emp['first_name']} {emp['last_name']},

Your personal data was accidentally exposed on the Strawbridge Industries website and is at risk of being compromised. The company regrets this error and would like to offer a credit monitoring service at no cost to you. Please contact HR to establish this service.

Thank you,
Dick Strawbridge, CEO
"""

    with open(filename, "w") as file:
        file.write(content)


def print_summary(employees: List[Dict[str, str]]) -> None:
    """
    Prints LOW, MEDIUM, HIGH exposure counts.
    """

    low = 0
    medium = 0
    high = 0

    for emp in employees:
        risk = emp.get("risk_level", "LOW")

        if risk == "LOW":
            low += 1
        elif risk == "MEDIUM":
            medium += 1
        elif risk == "HIGH":
            high += 1

    print()
    print(f"{low} low risk exposures detected ")
    print(f"{medium} medium risk exposures detected")
    print(f"{high} high risk exposures detected")


def main() -> None:
    """
    Full workflow:
    1. Scrape employee data
    2. Call API once per SSN
    3. Assign risk levels
    4. Write CSV file
    5. Create email files for HIGH risk
    6. Print summary
    """

    silent_crawler()  

    username = "zadedipe"

    print("Scraping data...")
    employees = fetch_employee_data()

    if not employees:
        print("No employee data found.")
        return

    print("Analyzing SSNs...")

    #API CALL ONCE PER SSN 
    for emp in employees:
        risk = get_risk_level(username, emp["ssn"])
        emp["risk_level"] = risk

        if risk == "HIGH":
            create_email(emp)

    print("Writing results...")

    # OUTPUT FILES
    write_csv(employees)

    print_summary(employees)

    print("\nDone.")


if __name__ == "__main__":
    main()