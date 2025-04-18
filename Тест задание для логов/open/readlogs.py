def read_all_logs(log_paths: list[str]) -> list[str]:
    all_lines: list[str] = []
    for path in log_paths:
        with open(path, encoding="utf-8") as f:
            all_lines.extend(f.readlines())
    return all_lines