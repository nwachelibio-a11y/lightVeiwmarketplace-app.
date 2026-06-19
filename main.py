fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def render_complete_marketplace():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>LightView Real Estate Marketplace</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <style>
            body { background-color: #000000; color: #ffffff; font-family: sans-serif; }
            .zinc-card { background-color: #0b0b0c; border: 1px solid #1f1f22; }
            .jumia-badge { background-color: #f68b1e; color: white; } /* Jumia accent orange */
        </style>
    </head>
    <body class="min-h-screen flex flex-col p-3 max-w-md mx-auto border-x border-zinc-900 select-none">

        <div id="ad-player" class="hidden fixed inset-0 bg-black z-50 flex flex-col items-center justify-center p-6 text-center">
            <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-orange-500 mb-4"></div>
            <p class="text-xs uppercase tracking-widest text-zinc-500 font-mono mb-1">Sponsored Advertisement</p>
            <h3 class="text-xl font-black text-white mb-6">SPONSORED ADVERTISEMENT IS PLAYING</h3>
            <div class="bg-zinc-900 text-orange-500 px-6 py-2 rounded-full font-mono text-lg border border-zinc-800">
                Time Remaining: <span id="ad-timer">10</span>s
            </div>
        </div>

        <header class="border-b border-zinc-900 pb-3 mb-4 flex justify-between items-center">
            <div class="flex items-center gap-2">
                <span class="text-orange-500 font-black text-xl tracking-tighter">LIGHTVIEW</span>
                <span class="text-zinc-500 text-xs font-bold font-mono">HOUSES</span>
            </div>
            <div class="flex items-center gap-2 font-mono text-[10px]">
                <div class="bg-zinc-900 border border-zinc-800 px-2 py-1 rounded text-orange-400">
                    📺 Ads Watched: <span id="ad-counter">0</span>
                </div>
            </div>
        </header>

        <main class="flex-1 flex flex-col justify-start">

            <div id="view-login" class="zinc-card rounded-xl p-5 text-center my-auto shadow-2xl">
                <div class="w-12 h-12 bg-zinc-900 border border-zinc-800 text-orange-500 rounded-full flex items-center justify-center mx-auto mb-4 text-xl font-black">G</div>
                <h2 class="text-lg font-bold mb-1">Sign in to LightView</h2>
                <p class="text-xs text-zinc-400 mb-5">Connect with your official Google account to browse real estate inventory.</p>
                <input type="email" id="login-email" placeholder="example@gmail.com" class="w-full bg-zinc-950 border border-zinc-800 rounded-lg px-3 py-2.5 text-sm text-center focus:outline-none focus:border-orange-500 mb-3">
                <button onclick="handleGmailLogin()" class="w-full bg-orange-600 hover:bg-orange-700 text-white text-xs font-bold py-3 rounded-lg transition-all">
                    LOG IN WITH GMAIL
                </button>
            </div>

            <div id="view-role" class="hidden zinc-card rounded-xl p-5 text-center my-auto">
                <h3 class="text-base font-bold mb-1">Select Account Type</h3>
                <p class="text-xs text-zinc-400 mb-6">Are you searching for housing or listing a property?</p>
                <div class="grid grid-cols-2 gap-3">
                    <button onclick="selectRole('buyer')" class="p-4 bg-zinc-900 border border-zinc-800 rounded-xl hover:border-orange-500 group transition-all">
                        <span class="block text-xl mb-1">🛒</span>
                        <span class="text-xs font-bold text-white group-hover:text-orange-500">I am a Buyer</span>
                    </button>
                    <button onclick="selectRole('seller')" class="p-4 bg-zinc-900 border border-zinc-800 rounded-xl hover:border-orange-500 group transition-all">
                        <span class="block text-xl mb-1">🏢</span>
                        <span class="text-xs font-bold text-white group-hover:text-orange-500">I am a Seller</span>
                    </button>
                </div>
            </div>

            <div id="view-seller-phone" class="hidden zinc-card rounded-xl p-5 my-auto">
                <h3 class="text-base font-bold mb-1">Seller Verification</h3>
                <p class="text-xs text-zinc-400 mb-4">Sellers must provide a valid phone number before posting listings.</p>
                <input type="tel" id="seller-phone" placeholder="e.g. +234 801 234 5678" class="w-full bg-zinc-950 border border-zinc-800 rounded-lg px-3 py-2.5 text-sm font-mono text-center focus:outline-none focus:border-orange-500 mb-3">
                <button onclick="saveSellerPhone()" class="w-full bg-orange-600 text-white text-xs font-bold py-3 rounded-lg">
                    VERIFY & PROCEED
                </button>
            </div>

            <div id="view-buyer-location" class="hidden zinc-card rounded-xl p-5 my-auto space-y-3">
                <div>
                    <h3 class="text-base font-bold">Your Location</h3>
                    <p class="text-xs text-zinc-400">Specify your region to sync currency rates correctly.</p>
                </div>
                <input type="text" id="buyer-country" placeholder="Country (e.g. Nigeria, Ghana)" class="w-full bg-zinc-950 border border-zinc-800 rounded-lg px-3 py-2.5 text-sm focus:outline-none focus:border-orange-500">
                <input type="text" id="buyer-state" placeholder="State / Province" class="w-full bg-zinc-950 border border-zinc-800 rounded-lg px-3 py-2.5 text-sm focus:outline-none focus:border-orange-500">
                <button onclick="saveBuyerLocation()" class="w-full bg-white text-black text-xs font-bold py-3 rounded-lg">
                    ENTER MARKETPLACE
                </button>
            </div>

            <div id="view-marketplace" class="hidden space-y-4">
                
                <div class="zinc-card rounded-xl p-3 flex gap-2 items-center">
                    <input type="text" id="search-input" placeholder="Search houses by city, state or local area..." class="flex-1 bg-zinc-950 border border-zinc-800 rounded-lg px-3 py-2 text-xs text-white focus:outline-none focus:border-orange-500">
                    <button onclick="triggerSearch()" class="bg-orange-600 text-white text-xs font-bold px-4 py-2 rounded-lg">
                        Search
                    </button>
                </div>

                <div class="flex justify-between items-center border-b border-zinc-900 pb-1">
                    <h3 class="text-xs font-bold uppercase tracking-wider text-zinc-400">Available Properties</h3>
                    <span class="text-[10px] text-zinc-500" id="currency-notice">Local Currency Active</span>
                </div>

                <div id="housing-feed" class="grid grid-cols-2 gap-3">
                    </div>
            </div>

            <div id="view-detail" class="hidden space-y-4">
                <button onclick="backToFeed()" class="text-xs text-zinc-400 underline mb-2 block">← Back to Feed</button>
                <div class="zinc-card rounded-xl overflow-hidden shadow-2xl">
                    <div id="detail-media" class="w-full h-44 bg-zinc-900 flex items-center justify-center relative">
                        </div>
                    <div class="p-4 space-y-3">
                        <div class="flex justify-between items-start">
                        
