 import os
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
            <span class="text-[10px] bg-emerald-950 text-emerald-400 px-2 py-0.5 rounded border border-emerald-900 font-mono">🟢 Live</span>
        </header>

        <main class="flex-1 flex flex-col justify-center my-6">
            
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

        </main>

        <footer class="text-center text-[10px] text-zinc-600 font-mono pt-3 border-t border-zinc-900">
            LightView Housing Hub © 2026
        </footer>

        <script>
            let session = { email: "", role: "", phone: "", country: "", state: "" };
            let currentSelectedPropertyIndex = null;

            // REAL-ESTATE PLATFORM INVENTORY ASSET DATA STORE
            let propertiesData = [
                { title: "Luxury 3 Bedroom Duplex", area: "Gra Phase 2", city: "Asaba", state: "Delta", country: "Nigeria", price: 45000000, currency: "₦", isVideo: false, icon: "🏠", rawStars: 450 },
                { title: "Modern Condo Complex", area: "Lekki Phase 1", city: "Lagos", state: "Lagos", country: "Nigeria", price: 85000000, currency: "₦", isVideo: true, icon: "📹", rawStars: 920 },
                { title: "Urban Executive Studio", area: "Bodija", city: "Ibadan", state: "Oyo", country: "Nigeria", price: 15000000, currency: "₦", isVideo: false, icon: "🏢", rawStars: 120 }
            ];

            function handleGmailLogin() {
                const emailInput = document.getElementById('login-email').value;
                if(!emailInput || !emailInput.includes('@gmail.com')) { alert("Provide a valid Gmail address."); return; }
                session.email = emailInput;
                document.getElementById('view-login').classList.add('hidden');
                document.getElementById('view-role').classList.remove('hidden');
            }

            function selectRole(selectedRole) {
                session.role = selectedRole;
                document.getElementById('view-role').classList.add('hidden');
                if(selectedRole === 'seller') {
                    document.getElementById('view-seller-phone').classList.remove('hidden');
                } else {
                    document.getElementById('view-buyer-location').classList.remove('hidden');
                }
            }

            function saveSellerPhone() {
                const phoneInput = document.getElementById('seller-phone').value;
                if(!phoneInput) { alert("Phone identification configuration required."); return; }
                session.phone = phoneInput;
                session.country = "Nigeria";
                session.state = "All-Active";
                openMarketplaceFeed();
            }

            function saveBuyerLocation() {
                const countryInput = document.getElementById('buyer-country').value;
                const stateInput = document.getElementById('buyer-state').value;
                if(!countryInput || !stateInput) { alert("All local geography items required."); return; }
                session.country = countryInput;
                session.state = stateInput;
                openMarketplaceFeed();
            }

            function openMarketplaceFeed() {
                document.getElementById('view-seller-phone').classList.add('hidden');
                document.getElementById('view-buyer-location').classList.add('hidden');
                document.getElementById('view-marketplace').classList.remove('hidden');
                document.getElementById('currency-tag').innerText = `${session.country.toUpperCase()} (${session.state})`;
                renderJumiaFeed(propertiesData);
            }

            function renderJumiaFeed(items) {
                const feedContainer = document.getElementById('housing-feed');
                feedContainer.innerHTML = "";
                
                // RANK CRITERIA: Auto-sort items based on raw Star metrics (Highest rating shows first)
                let sorted = [...items].sort((a,b) => b.rawStars - a.rawStars);

                sorted.forEach(item => {
                    let calculatedStars = (item.rawStars * 0.01).toFixed(2);
                    let card = document.createElement('div');
                    card.className = "zinc-card rounded-xl overflow-hidden flex flex-col justify-between p-2 space-y-2 border border-zinc-900 cursor-pointer hover:border-zinc-700 transition-all";
                    card.setAttribute('onclick', `inspectHouseDetails(${propertiesData.indexOf(item)})`);
                    card.innerHTML = `
                        <div class="w-full h-24 bg-zinc-950 flex items-center justify-center text-3xl relative rounded-lg">
                            ${item.icon}
                            <span class="absolute top-1 left-1 text-[8px] px-1 py-0.5 rounded font-bold ${item.isVideo ? 'bg-red-900 text-red-100' : 'bg-zinc-800 text-zinc-300'}">
                                ${item.isVideo ? '📹 VIDEO' : '🖼️ PICTURE'}
                            </span>
                        </div>
                        <div>
                            <h4 class="text-[11px] font-bold text-zinc-200 truncate">${item.title}</h4>
                            <p class="text-[9px] text-zinc-500 truncate">📍 ${item.area}</p>
                        </div>
                        <div class="pt-1 border-t border-zinc-900 flex justify-between items-center text-[10px] font-mono">
                            <span class="font-black text-orange-500">${item.currency}${item.price.toLocaleString()}</span>
                            <span class="text-zinc-400">⭐${calculatedStars}</span>
                        </div>
                    `;
                    feedContainer.appendChild(card);
                });
            }

            function inspectHouseDetails(index) {
                currentSelectedPropertyIndex = index;
                const item = propertiesData[index];
                
                document.getElementById('view-marketplace').classList.add('hidden');
                document.getElementById('view-detail').classList.remove('hidden');
                
                document.getElementById('detail-media').innerText = item.icon;
                document.getElementById('detail-title').innerText = item.title;
                document.getElementById('detail-price').innerText = `${item.currency}${item.price.toLocaleString()}`;
                document.getElementById('detail-area').innerText = item.area;
                document.getElementById('detail-city').innerText = item.city;
                document.getElementById('detail-state').innerText = item.state;
                document.getElementById('detail-country').innerText = item.country;
                
                document.getElementById('detail-stars').innerText = (item.rawStars * 0.01).toFixed(2);
                
                document.getElementById('add-star-btn').onclick = function() {
                    item.rawStars += 1;
                    document.getElementById('detail-stars').innerText = (item.rawStars * 0.01).toFixed(2);
                };
            }

            function backToFeed() {
                document.getElementById('view-detail').classList.add('hidden');
                document.getElementById('view-marketplace').classList.remove('hidden');
                renderJumiaFeed(propertiesData);
            }

            function triggerSearch() {
                let query = document.getElementById('search-input').value.toLowerCase();
                if(!query) { renderJumiaFeed(propertiesData); return; }
                let results = propertiesData.filter(item => 
                    item.area.toLowerCase().includes(query) || 
                    item.city.toLowerCase().includes(query) ||
                    item.state.toLowerCase().includes(query)
                );
                renderJumiaFeed(results);
            }

            function openChatRoom() {
                document.getElementById('view-detail').classList.add('hidden');
                document.getElementById('view-chat').classList.remove('hidden');
                
                const asset = propertiesData[currentSelectedPropertyIndex];
                document.getElementById('chat-agent-title').innerText = `Property Negotiator Agent ID-0${asset.id || currentSelectedPropertyIndex + 1}`;
                document.getElementById('chat-box').innerHTML = '<p class="text-zinc-600 text-center text-[9px]">— Instantiated Direct Deal Line —</p>';
            }

            function closeChat() {
                document.getElementById('view-chat').classList.add('hidden');
                document.getElementById('view-detail').classList.remove('hidden');
            }

            function sendMessage() {
                const txt = document.getElementById('chat-input').value;
                if(!txt) return;
                
                const box = document.getElementById('chat-box');
                let userNode = document.createElement('p');
                userNode.innerHTML = `<span class="text-orange-500 font-bold">[BUYER]:</span> ${txt}`;
                box.appendChild(userNode);
                document.getElementById('chat-input').value = "";
                
                // Instant responses with zero ad loops
                setTimeout(() => {
                    let sellerNode = document.createElement('p');
                    sellerNode.innerHTML = `<span class="text-zinc-400 font-bold">[OWNER]:</span> Message parameter received. Let's arrange immediate inspections for this asset item.`;
                    box.appendChild(sellerNode);
                    box.scrollTop = box.scrollHeight;
                }, 400);
            }
        </script>
    </body>
    </html>
    """
                   
