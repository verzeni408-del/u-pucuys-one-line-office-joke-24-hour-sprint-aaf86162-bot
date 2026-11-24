from pathlib import Path


def get_entry():
    return "The office plant has never taken a sick day in six years, and HR still says it lacks leadership potential."


def main():
    Path("/output").mkdir(parents=True, exist_ok=True)
    Path("/output/entry.txt").write_text(get_entry(), encoding="utf-8")


if __name__ == "__main__":
    main()
