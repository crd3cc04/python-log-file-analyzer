import re
from collections import Counter

def analyze_log(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    error_count = 0
    warning_count = 0
    info_count = 0
    error_messages = []

    for line in lines:
        if "ERROR" in line:
            error_count += 1
            msg = line.split("ERROR")[1].strip()
            error_messages.append(msg)
        elif "WARNING" in line:
            warning_count += 1
        elif "INFO" in line:
            info_count += 1

    most_common_error = None
    if error_messages:
        most_common_error = Counter(error_messages).most_common(1)[0]

    print("\n===== Log File Summary =====")
    print(f"Total INFO messages: {info_count}")
    print(f"Total WARNING messages: {warning_count}")
    print(f"Total ERROR messages: {error_count}")

    if most_common_error:
        print(f"\nMost common error: '{most_common_error[0]}' occurred {most_common_error[1]} times")
    else:
        print("\nNo errors found.")

if __name__ == "__main__":
    analyze_log("../sample_logs/system.log")
