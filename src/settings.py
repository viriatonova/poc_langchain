import json
import os

from dotenv import load_dotenv

# CONSTANTS
BASE_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..")
OPENAI_MODELS = json.load(
    open(os.path.join(BASE_DIR, "src", "utils", "openia_models.json"))
)

# Define the path to the .env file
env_path = os.path.join(BASE_DIR, ".env")

# Load the .env file
load_dotenv(dotenv_path=env_path)

# VARIABLES
TEST = os.getenv("TEST")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


if __name__ == "__main__":
    print(OPENAI_MODELS)
