
from pathlib import Path
import sys
import uvicorn
from server import App

# add py path tp system path
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

if __name__ == '__main__':
    init_app = App()
    uvicorn.run("server:App", host="localhost", port=8080, reload=True)

