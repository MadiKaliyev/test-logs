import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description="Анализатор логов формирует отчёт по API-ручкам."
    )
    parser.add_argument(
        "log_files",
        nargs="+",
        help="Пути к лог-файлам"
    )
    parser.add_argument(
        "--report",
        choices=["handlers"],
        required=True,
        help="Тип отчёта: handlers"
    )
    return parser.parse_args()