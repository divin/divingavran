import datetime

def convert_to_datetime(date: str) -> datetime.date:
    """"Converts a date in format YYYY-MM-DD to datetime."""
    return datetime.datetime.strptime(date, "%Y-%m-%d")


def sort_projects(projects: list[dict]) -> list[dict]:
    """Sorts projects by date."""
    return sorted(projects, key=lambda project: convert_to_datetime(project["updated"]), reverse=True)