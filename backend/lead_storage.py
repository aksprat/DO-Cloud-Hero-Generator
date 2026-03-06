import csv
import os
from datetime import datetime

CSV_FILE = "/tmp/leads.csv"

def save_lead(name, email, company, designation):

    file_exists = os.path.isfile(CSV_FILE)

    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow([
                "Name",
                "Email",
                "Company",
                "Designation",
                "Timestamp"
            ])

        writer.writerow([
            name,
            email,
            company,
            designation,
            datetime.utcnow().isoformat()
        ])