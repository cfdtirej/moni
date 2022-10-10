import uvicorn
from main import api

uvicorn.run(api, host='0.0.0.0', port=8000)
