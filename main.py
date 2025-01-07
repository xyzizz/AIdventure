from tests.test_azure import test_azure 
from tests.test_crew import test_crew
from dotenv import load_dotenv

load_dotenv()

def run():
    test_crew()

if __name__ == "__main__":
    run()

