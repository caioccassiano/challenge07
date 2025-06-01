from dotenv import load_dotenv
from src.main.server.server import app

load_dotenv()



if __name__=="__main__":
  app.run(host="0.0.0.0", port=7500, debug=True)