import sys
from pathlib import Path
from reports.handlers import HandlersReport
from pars.parse import parse_args
from open.readlogs import read_all_logs
from utils.parser import extract_requests

def main():
    args = parse_args()
    print("Выбранный отчёт:", args.report)
    print("Файлы логов:", args.log_files)

    for path_str in args.log_files:
        file_path = Path(path_str)
        if not file_path.is_file():
            print(f"Ошибка: файл '{path_str}' не найден.")
            sys.exit(1)

    print("✅ Все файлы найдены. Можно начинать анализ.")

    logs = read_all_logs(args.log_files)
    print(f"Всего считано строк: {len(logs)}")

    request = extract_requests(logs)
    print(f"Обнаружено строк django.request: {len(request)}")

    if args.report == "handlers":
        report = HandlersReport(request)
        report.build()
        report.display()


if __name__ == "__main__":
    main()
