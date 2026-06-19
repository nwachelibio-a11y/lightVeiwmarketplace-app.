import os
import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>LightView Hub</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-black text-white min-h-screen flex flex-col items-center justify-center font-sans">
        <h1 class="text-orange-500 font-black text-2xl tracking-wider mb-2">LIGHTVIEW ONLINE</h1>
        <p class="text-xs text-zinc-400 font-mono">Web Engine Active & Stable</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
    
                    
