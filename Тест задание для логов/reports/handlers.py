from collections import defaultdict
from typing import List, Tuple

LOG_LEVELS = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

class HandlersReport:
    def __init__(self, data: List[Tuple[str, str]]):
        self.data = data
        self.report = defaultdict(lambda: {level: 0 for level in LOG_LEVELS})

    def build(self):
        for url, level in self.data:
            if level in LOG_LEVELS:
                self.report[url][level] += 1

    def display(self):
        print("\nHANDLER".ljust(30), end="")
        for level in LOG_LEVELS:
            print(level.rjust(10), end="")
        print()

        total_by_level = {level: 0 for level in LOG_LEVELS}
        total_requests = 0

        for handler in sorted(self.report.keys()):
            print(handler.ljust(30), end="")
            for level in LOG_LEVELS:
                count = self.report[handler][level]
                print(str(count).rjust(10), end="")
                total_by_level[level] += count
                total_requests += count
            print()

        print("".ljust(30), end="")
        for level in LOG_LEVELS:
            print(str(total_by_level[level]).rjust(10), end="")
        print(f"\n\nTotal requests: {total_requests}")
