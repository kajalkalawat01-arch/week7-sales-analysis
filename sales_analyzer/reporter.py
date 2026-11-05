import json
from pathlib import Path


def generate_report(analysis, output_dir="data/reports"):
    if analysis is None:
        print("No analysis data available.")
        return

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    report = {}

    for key, value in analysis.items():
        if hasattr(value, "to_dict"):
            report[key] = value.to_dict()
        else:
            report[key] = value

    file_path = output_path / "sales_report.json"

    with open(file_path, "w") as file:
        json.dump(report, file, indent=4, default=str)

    print("Sales report generated successfully!")
