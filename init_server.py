
from pathlib import Path
import sys
import uvicorn

# add py path tp system path
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

if __name__ == '__main__':
    uvicorn.run("api.server:App", host="localhost", port=8080, reload=True)

