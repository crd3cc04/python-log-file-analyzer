import re
from collections import Counter

def parse_log_line(line):
    parts = line.split(" ", 3)

    if len(parts) == 4: 
        timestamp_part1 = parts[0]
        timestamp_part2 = parts[1]
        level = parts[2]
        message = parts[3]

        # Validate timestamp format (basic check)
        if timestamp_part1.count("-") == 2 and timestamp_part2.count(":") == 2:
            # Validate level
            if level in ["INFO", "WARNING", "ERROR"]:
                return {
                    "timestamp": f"{timestamp_part1} {timestamp_part2}",
                    "level": level,
                    "message": message
                }
    # if we reach here, it means the line is malformed
    return {
        "timestamp": None,
        "level": "UNKNOWN",
        "message": line
    }    

def analyze_log(file_path):
    results = [] # <-- store parsed log entries here
    with open(file_path, "r") as file:
        for line in file:
            parsed = parse_log_line(line.strip())
            results.append(parsed)

    # (your summary printing code stays the same)
             

    error_count = 0
    warning_count = 0
    info_count = 0
    error_messages = []

    for line in results:
        if line['level'] == "ERROR":
            error_count += 1
            error_messages.append(line['message'])
        elif line['level'] == "WARNING":
            warning_count += 1
        elif line['level'] == "INFO":
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

    return results    

if __name__ == "__main__":
    analyze_log("../sample_logs/system.log")
