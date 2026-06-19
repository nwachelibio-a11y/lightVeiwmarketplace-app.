from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>LightView Marketplace</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-black text-white min-h-screen flex flex-col justify-center items-center p-6 text-center">
        <h1 class="text-orange-500 font-black text-3xl tracking-tighter mb-2">LIGHTVIEW</h1>
        <p class="text-sm text-zinc-400 mb-6">Real Estate Marketplace Server is Running Successfully!</p>
        <div class="bg-zinc-900 border border-zinc-800 p-4 rounded-xl max-w-xs font-mono text-xs text-left">
            <p class="text-emerald-400">🟢 Status: Online</p>
            <p class="text-zinc-500 mt-1">Ready for app interface integrations.</p>
        </div>
    </body>
    </html>
    """
