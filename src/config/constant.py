import os 
from dotenv import load_dotenv
load_dotenv()
WORK_DIR = "temp"
TIMEOUT = 120
MAX_TURNS = 10
TERMINATION = "DONE"
OPENAI_MODEL = "gpt-4o"
GROQ_MODEL = "openai/gpt-oss-20b"

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
JSEARCH_API = os.getenv('JSEARCH_API_KEY')
print(OPENAI_API_KEY)
print(GROQ_API_KEY)

