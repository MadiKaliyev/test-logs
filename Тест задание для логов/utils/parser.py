import re

def extract_requests(log_lines: list[str]) -> list[tuple[str, str]]:
    request_data: list[tuple[str, str]] = []

    for line in log_lines:
        if "django.request" not in line:
            continue

        match = re.search(r"(DEBUG|INFO|WARNING|ERROR|CRITICAL)\s+django\.request.*?: (GET|POST|PUT|DELETE|PATCH) (\/[^\s]+)", line)
        if match:
            level = match.group(1)
            url = match.group(3)
            request_data.append((url, level))

    return request_data