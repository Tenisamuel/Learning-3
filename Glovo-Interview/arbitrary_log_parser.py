import re

def parse_logs(file_path):
    results = []

    with open(file_path, "r") as file:
        for line in file:
            timestamp = re.search(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", line)
            exe = re.search(r"exe=([\w\.]+)", line)
            domain = re.search(r"domain=([\w\.-]+)", line)

            entry = {
                "timestamp": timestamp.group() if timestamp else None,
                "executable": exe.group(1) if exe else None,
                "domain": domain.group(1) if domain else None
            }

            results.append(entry)

    return results


if __name__ == "__main__":
    logs = parse_logs("sample.log")

    for log in logs:
        print(log)