             import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    # Insert interface components inside the string below
    return """
    """
<div id="view-login" class="zinc-card rounded-xl p-6 text-center shadow-2xl">
    <div class="w-12 h-12 bg-zinc-900 border border-zinc-800 text-orange-500 rounded-full flex items-center justify-center mx-auto mb-4 text-xl font-black">G</div>
    <h2 class="text-lg font-bold mb-1">Sign in to LightView</h2>
    <p class="text-xs text-zinc-400 mb-5">Connect with your official Google account to browse real estate inventory.</p>
    <input type="email" id="login-email" placeholder="username@gmail.com" class="w-full bg-zinc-950 border border-zinc-800 rounded-lg px-3 py-2.5 text-sm text-center focus:outline-none focus:border-orange-500 mb-4 text-white">
    <button onclick="handleGmailLogin()" class="w-full bg-orange-600 text-white text-xs font-bold py-3 rounded-lg tracking-wider">
        LOG IN WITH GMAIL
    </button>
</div>
<div id="view-role" class="hidden zinc-card rounded-xl p-6 text-center shadow-2xl">
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

<div id="view-seller-phone" class="hidden zinc-card rounded-xl p-6 shadow-2xl">
    <h3 class="text-base font-bold mb-1">Seller Verification</h3>
    <p class="text-xs text-zinc-400 mb-4">Sellers must provide a valid phone number before posting listings.</p>
    <input type="tel" id="seller-phone" placeholder="e.g. +234 801 234 5678" class="w-full bg-zinc-950 border border-zinc-800 rounded-lg px-3 py-2.5 text-sm font-mono text-center focus:outline-none focus:border-orange-500 mb-4 text-white">
    <button onclick="saveSellerPhone()" class="w-full bg-orange-600 text-white text-xs font-bold py-3 rounded-lg tracking-wider">
        VERIFY & PROCEED
    </button>
</div>

<div id="view-buyer-location" class="hidden zinc-card rounded-xl p-6 shadow-2xl space-y-4">
    <div>
        <h3 class="text-base font-bold mb-1">Your Location</h3>
        <p class="text-xs text-zinc-400">Specify your region to sync local asset currencies.</p>
    </div>
    <input type="text" id="buyer-country" placeholder="Country (e.g. Nigeria)" class="w-full bg-zinc-950 border border-zinc-800 rounded-lg px-3 py-2.5 text-sm focus:outline-none focus:border-orange-500 text-white">
    <input type="text" id="buyer-state" placeholder="State / Province" class="w-full bg-zinc-950 border border-zinc-800 rounded-lg px-3 py-2.5 text-sm focus:outline-none focus:border-orange-500 text-white">
    <button onclick="saveBuyerLocation()" class="w-full bg-white text-black text-xs font-bold py-3 rounded-lg tracking-wider">
        ENTER MARKETPLACE BASE
   </button>
</div>
<div id="view-marketplace" class="hidden space-y-4 w-full">
    <div class="zinc-card rounded-xl p-3 flex gap-2 items-center">
        <input type="text" id="search-input" onkeyup="triggerSearch()" placeholder="Type to search locations instantly..." class="flex-1 bg-zinc-950 border border-zinc-800 rounded-lg px-3 py-2 text-xs text-white focus:outline-none focus:border-orange-500">
    </div>

    <div class="flex justify-between items-center border-b border-zinc-900 pb-1">
        <h3 class="text-xs font-bold uppercase tracking-wider text-zinc-400">Products Grid</h3>
        <span id="currency-tag" class="text-[10px] text-orange-400 font-mono"></span>
    </div>

    <div id="housing-feed" class="grid grid-cols-2 gap-3 w-full"></div>
</div>
<div id="view-detail" class="hidden space-y-4 w-full">
    <button onclick="backToFeed()" class="text-xs text-zinc-500 underline mb-1 block">← Back to Feed</button>
    <div class="zinc-card rounded-xl overflow-hidden shadow-xl">
        <div id="detail-media" class="w-full h-40 bg-zinc-950 flex items-center justify-center text-5xl border-b border-zinc-900"></div>
        <div class="p-4 space-y-3">
            <div class="flex justify-between items-start">
                <h2 id="detail-title" class="text-sm font-bold text-zinc-100"></h2>
                <p id="detail-price" class="text-sm font-black text-orange-500"></p>
            </div>
            <div class="grid grid-cols-2 gap-2 text-[10px] text-zinc-400 border-y border-zinc-900 py-2 font-mono">
                <p>📍 Local Area: <span id="detail-area" class="text-white"></span></p>
                <p>🏙️ City: <span id="detail-city" class="text-white"></span></p>
                <p>🗺️ State: <span id="detail-state" class="text-white"></span></p>
                <p>🌍 Country: <span id="detail-country" class="text-white"></span></p>
            </div>
            <div class="flex justify-between items-center text-xs">
                <div class="flex items-center gap-1 font-mono text-zinc-300">
                    🌟 <span id="detail-stars"></span> Stars
                </div>
                <button id="add-star-btn" class="bg-zinc-900 border border-zinc-800 text-[10px] px-2 py-1 rounded text-zinc-300 hover:text-white">
                    Give +1 Star (+0.01)
                </button>
            </div>
            <button onclick="openChatRoom()" class="w-full bg-orange-600 text-white text-xs font-bold py-3 rounded-lg mt-2 uppercase tracking-wide">
                Open Chat Platform to End Deal
            </button>
        </div>
    </div>
</div>
<div id="view-chat" class="hidden flex flex-col h-[55vh] zinc-card rounded-xl overflow-hidden">
    <div class="bg-zinc-900 p-3 border-b border-zinc-800 flex justify-between items-center">
        <div>
            <h4 id="chat-agent-title" class="text-xs font-bold text-white">Direct Chat Deal Room</h4>
            <p class="text-[9px] text-emerald-400 font-mono">Instant Consumer-to-Owner Link</p>
        </div>
        <button onclick="closeChat()" class="text-xs text-zinc-500 underline">Close</button>
    </div>
    <div id="chat-box" class="flex-1 p-3 font-mono text-xs overflow-y-auto space-y-2 bg-zinc-950"></div>
    <div class="p-2 bg-zinc-900 border-t border-zinc-800 flex gap-1">
        <input type="text" id="chat-input" placeholder="Type deal proposal parameters..." class="flex-1 bg-zinc-950 border border-zinc-800 rounded px-2 text-xs text-white focus:outline-none">
        <button onclick="sendMessage()" class="bg-orange-600 text-white text-xs font-bold px-4 py-1.5 rounded">Send</button>
    </div>
</div>
<div id="ad-player" class="hidden fixed inset-0 bg-black z-50 flex flex-col items-center justify-center p-6 text-center">
    <div class="animate-spin rounded-full h-10 w-10 border-b-2 border-orange-500 mb-4"></div>
    <p class="text-[10px] uppercase tracking-widest text-zinc-500 font-mono mb-1">Google Admob Stream Loaded</p>
    <h3 class="text-lg font-black text-white mb-6 uppercase" id="ad-title-display">ADVERTISEMENT PLAYING</h3>
    <div class="bg-zinc-900 text-orange-500 px-6 py-2 rounded-full font-mono text-sm border border-zinc-800">
        Time Remaining: <span id="ad-timer">10</span>s
    </div>
</div>

<div id="pic-ad-banner" class="hidden bg-zinc-900 border border-orange-900/50 rounded-xl p-3 flex items-center justify-between text-left mb-2">
    <div class="flex items-center gap-3">
        <div class="text-xl">🎁</div>
        <div>
            <h5 class="text-[11px] font-bold text-white">Continuous Session Reward Ad</h5>
            <p class="text-[9px] text-zinc-400">You spent 10mins in app! (Pic ad running)</p>
        </div>
    </div>
    <button onclick="dismissPicAd()" class="text-[9px] font-mono bg-zinc-950 border border-zinc-800 px-2 py-1 rounded text-zinc-400">Close (2s)</button>
</div>



