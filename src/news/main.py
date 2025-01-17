import sys
from .crew import NewsCrew


def run():
    """
    Run the crew.
    """
    date_str = sys.argv[1] if len(sys.argv) > 1 else None
    NewsCrew().crew().kickoff({"date": date_str})
