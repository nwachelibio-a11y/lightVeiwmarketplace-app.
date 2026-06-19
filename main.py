import os
import uvicorn
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
        <title>LightView Real Estate Hub</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <style>
            body { background-color: #000000; color: #ffffff; font-family: sans-serif; }
            .zinc-card { background-color: #0b0b0c; border: 1px solid #1f1f22; }
        </style>
    </head>
    <body class="min-h-screen flex flex-col p-4 max-w-md mx-auto select-none justify-between">

        <header class="border-b border-zinc-900 pb-3 flex justify-between items-center">
            <div class="flex items-center gap-2">
                <span class="text-orange-500 font-black text-xl tracking-tighter">LIGHTVIEW</span>
                <span class="text-zinc-500 text-[10px] font-mono">MARKETPLACE</span>
            </div>
            <span class="text-[10px] bg-emerald-950 text-emerald-400 px-2 py-0.5 rounded border border-emerald-900 font-mono">LIVE</span>
        </header>

        <main class="flex-1 flex flex-col justify-center my-6">
            
            <div id="view-login" class="zinc-card rounded-xl p-6 text-center shadow-2xl">
                <div class="w-12 h-12 bg-zinc-900 border border-zinc-800 text-orange-500 rounded-full flex items-center justify-center mx-auto mb-4 text-xl font-black">G</div>
                <h2 class="text-lg font-bold mb-1">Sign in to LightView</h2>
                <p class="text-xs text-zinc-400 mb-5">Connect with your official Google account to browse real estate inventory.</p>
                <input type="email" id="login-email" placeholder="username@gmail.com" class="w-full bg-zinc-950 border border-zinc-800 rounded-lg px-3 py-2.5 text-sm text-center focus:outline-none focus:border-orange-500 mb-4 text-white">
                <button onclick="handleGmailLogin()" class="w-full bg-orange-600 text-white text-xs font-bold py-3 rounded-lg tracking-wider">LOG IN WITH GMAIL</button>
            </div>

            <div id="view-role" class="hidden zinc-card rounded-xl p-6 text-center shadow-2xl">
                <h3 class="text-base font-bold mb-1">Select Account Type</h3>
                <p class="text-xs text-zinc-400 mb-6">Are you searching for housing or listing a property?</p>
                <div class="grid grid-cols-2 gap-3">
                    <button onclick="alert('System Active')" class="p-4 bg-zinc-900 border border-zinc-800 rounded-xl">
                        <span class="block text-xl mb-1">BUYER</span>
                        <span class="text-xs font-bold text-white">I am a Buyer</span>
                    </button>
                    <button onclick="alert('System Active')" class="p-4 bg-zinc-900 border border-zinc-800 rounded-xl">
                        <span class="block text-xl mb-1">SELLER</span>
                        <span class="text-xs font-bold text-white">I am a Seller</span>
                    </button>
                </div>
            </div>

        </main>

        <footer class="text-center text-[10px] text-zinc-600 font-mono pt-3 border-t border-zinc-900">
            LightView Housing Hub © 2026
        </footer>

        <script>
            function handleGmailLogin() {
                const emailInput = document.getElementById('login-email').value;
                if(!emailInput || !emailInput.includes('@gmail.com')) { 
                    alert("Provide a valid Gmail address."); 
                    return; 
                }
                document.getElementById('view-login').classList.add('hidden');
                document.getElementById('view-role').classList.remove('hidden');
            }
        </script>
    </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
    
