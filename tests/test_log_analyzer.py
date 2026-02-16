import os
import sys

print("CWD:", os.getcwd())
print("PATH:", sys.path)


from src.log_analyzer import analyze_log # pyright: ignore[reportMissingImports]

def test_analyze_log(tmp_path):
    # Create a temporary log file
    log_file = tmp_path / "test.log"
    log_file.write_text(
        "2024-06-01 12:00:00 INFO User logged in\n"
        "2024-06-01 12:05:00 ERROR Something broke\n"
    )

    result = analyze_log(str(log_file))

    assert len(result) == 2
    assert result[0]['level'] == "INFO"
    assert result[1]['level'] == "ERROR"

def test_analyze_log_with_malformed_lines(tmp_path):
    log_file = tmp_path / "test.log"
    log_file.write_text(
        "2024-06-01 12:00:00 INFO Start\n"
        "not a real log line\n"
    )

    result = analyze_log(str(log_file))

    assert result[1]['level'] == "UNKNOWN"
    assert result[1]['message'] == "not a real log line"