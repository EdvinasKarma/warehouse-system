import os

import dotenv
import uvicorn

from backend.app import app

dotenv.load_dotenv()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
