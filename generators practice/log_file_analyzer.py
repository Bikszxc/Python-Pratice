def log_reader(filename):
    try:
        with open(filename, "r") as file:
            for line in file:
                yield line.strip()
    except FileNotFoundError:
        print("File not found")

def filter_logs(logs, status_code):
    for log in logs:
        parts = log.split("] ") # ["[2025-03-25 10:00:12] ", "200 - OK"]
        if len(parts) > 1 and parts[1].startswith(f"{status_code}"):
            yield log

def main():
    filename = "server.log"
    status_code = input("Enter status code to filter: ")

    logs = log_reader(filename)
    fileread = filter_logs(logs, status_code)

    print(f"Logs with status code {status_code}:")
    found = False
    for log in fileread:
        print(log)
        found = True

    if not found:
        print(f"No logs found with status code {status_code}")

if __name__ == "__main__":
    main()