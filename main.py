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
                     onclick="systemRole('buyer')" class="p-4 bg-zinc-900 border border-zinc-800 rounded-xl">
                        <span class="block text-xl mb-1">BUYER</span>
                        <span class="text-xs font-bold text-white">I am a Buyer</span>
                    </button>
                     onclick="sysyeRole('Seller')" class="p-4 bg-zinc-900 border border-zinc-800 rounded-xl">
                        <span class="block text-xl mb-1">SELLER</span>
                        <span class="text-xs font-bold text-white">I am a Seller</span>
                    </button>
                </div>
            </div>
            <div id="view-buyer-location" class="hidden zinc-card rounded-xl p-6 shadow-2xl space-y-4">
                <div>
                    <h3 class="text-base font-bold mb-1">Your Location</h3>
                    <p class="text-xs text-zinc-400">Specify your region to sync local asset currencies.</p>
                </div>
                <input type="text" id="buyer-country" placeholder="Country (e.g. Nigeria)" class="w-full bg-zinc-950 border border-zinc-800 rounded-lg px-3 py-2.5 text-sm focus:outline-none focus:border-orange-500 text-white">
                <input type="text" id="buyer-state" placeholder="State / Province" class="w-full bg-zinc-950 border border-zinc-800 rounded-lg px-3 py-2.5 text-sm focus:outline-none focus:border-orange-500 text-white">
                <button onclick="processBuyerRegistration()" class="w-full bg-white text-black text-xs font-bold py-3 rounded-lg tracking-wider">ENTER MARKETPLACE BASE</button>
            </div>

            <div id="view-seller-phone" class="hidden zinc-card rounded-xl p-6 shadow-2xl space-y-4">
                <div>
                    <h3 class="text-base font-bold mb-1">Seller Verification</h3>
                    <p class="text-xs text-zinc-400">Sellers must authenticate their locale parameters before listing items.</p>
                </div>
                <input type="tel" id="seller-phone" placeholder="Phone Number (e.g. +234...)" class="w-full bg-zinc-950 border border-zinc-800 rounded-lg px-3 py-2.5 text-sm focus:outline-none focus:border-orange-500 text-white">
                <input type="text" id="seller-country" placeholder="Country" class="w-full bg-zinc-950 border border-zinc-800 rounded-lg px-3 py-2.5 text-sm focus:outline-none focus:border-orange-500 text-white">
                <input type="text" id="seller-state" placeholder="State / Province" class="w-full bg-zinc-950 border border-zinc-800 rounded-lg px-3 py-2.5 text-sm focus:outline-none focus:border-orange-500 text-white">
                <button onclick="processSellerRegistration()" class="w-full bg-orange-600 text-white text-xs font-bold py-3 rounded-lg tracking-wider">VERIFY SELLER IDENTIFICATION</button>
            </div>
                        <div id="view-marketplace" class="hidden space-y-6">
                <div class="zinc-card rounded-xl p-4 shadow-xl space-y-3">
                    <input type="text" id="market-search" oninput="executeInstantSearch()" placeholder="Search properties, areas, or cities..." class="w-full bg-zinc-950 border border-zinc-800 rounded-lg px-3 py-2.5 text-sm focus:outline-none focus:border-orange-500 text-white">
                    <div class="flex items-center justify-between text-xs text-zinc-400 px-1">
                        <span id="display-user-id" class="font-mono text-orange-400">ID: --</span>
                        <span id="display-user-locale" class="tracking-wide">Locale: --</span>
                    </div>
                   <div id="inventory-grid" class="grid grid-cols-1 gap-4">
                    </div>
              </div>

        </main>

        <footer class="text-center text-[10px] text-zinc-600 font-mono pt-3 border-t border-zinc-900">
            LightView Housing Hub © 2026
        </footer>

        <script>
            // LAYER 1: GLOBAL DATA REGISTRY (EMOJI-FREE STRUCTURAL MATRIX)
    let session = { 
        email: "", 
        role: "", 
        phone: "", 
        country: "", 
        state: "",
        registrationNumber: "" 
    };
    
    let currentSelectedPropertyIndex = null;
    let watchedAdsCount = 0;

    // GLOBAL EXCHANGE RATES MATRIX (BASE UNIT AGAINST US DOLLAR VALUE EQUIVALENCE)
    const currencyRates = {
        "nigeria": { symbol: "NGN ", rate: 1500 },
        "ghana": { symbol: "GHS ", rate: 15 },
        "united states": { symbol: "USD $", rate: 1 },
        "united kingdom": { symbol: "GBP £", rate: 0.78 }
    };

    // SYSTEM REGISTRATION SEED COUNTERS
    let nextBuyerSequence = 0; 
    let nextSellerSequence = 1;

    // GLOBAL PROPERTY INVENTORY DATABASE (STORED IN STANDARD LOCAL BASE VALUE)
    let propertiesData = [
        { id: 101, title: "Luxury 3 Bedroom Duplex", area: "Gra Phase 2", city: "Asaba", state: "Delta", country: "Nigeria", basePriceUSD: 30000, isVideo: false, rawStars: 450 },
        { id: 102, title: "Modern Condo Complex", area: "Lekki Phase 1", city: "Lagos", state: "Lagos", country: "Nigeria", basePriceUSD: 56600, isVideo: true, rawStars: 920 },
        { id: 103, title: "Urban Executive Studio", area: "Bodija", city: "Ibadan", state: "Oyo", country: "Nigeria", basePriceUSD: 10000, isVideo: false, rawStars: 120 },
        { id: 104, title: "Suburban Family Villa", area: "East Legon", city: "Accra", state: "Greater Accra", country: "Ghana", basePriceUSD: 45000, isVideo: true, rawStars: 310 }
    ];

            function handleGmailLogin() { 
                const emailInput = document.getElementById('login-email').value;
                if(!emailInput || !emailInput.includes('@gmail.com')) { 
                    alert("Provide a valid Gmail address."); 
                    return; 
                }
                document.getElementById('view-login').classList.add('hidden');
                document.getElementById('view-role').classList.remove('hidden');
            }
                // LAYER 3: INTERACTION LOGIC ENGINE
    function selectRole(chosenRole) {
        session.role = chosenRole;
        document.getElementById('view-role').classList.add('hidden');
        
        if (chosenRole === 'buyer') {
            document.getElementById('view-buyer-location').classList.remove('hidden');
        } else {
            document.getElementById('view-seller-phone').classList.remove('hidden');
        }
    }

    function processBuyerRegistration() {
        const country = document.getElementById('buyer-country').value.trim().toLowerCase();
        const state = document.getElementById('buyer-state').value.trim();
        
        if (!country || !state) {
            alert("Please fill in your country and state.");
            return;
        }
        
        session.country = country;
        session.state = state;
        
        // Rule: Buyers start with 0-9 sequence
        session.registrationNumber = "0-" + nextBuyerSequence;
        nextBuyerSequence++;
        
        alert("Buyer Assigned ID: " + session.registrationNumber);
        // Next step will transition to inventory base display
        document.getElementById('view-buyer-location').classList.add('hidden');
document.getElementById('view-marketplace').classList.remove('hidden');
renderInventory(propertiesData);

    }
        
    }
    
    function processSellerRegistration() {
    const phone = document.getElementById('seller-phone').value.trim();
    const country = document.getElementById('seller-country').value.trim().toLowerCase();
    const state = document.getElementById('seller-state').value.trim();
    
    if (!phone || !country || !state) {
        alert("All fields are required for seller verification.");
        return;
    }
    
    session.phone = phone;
    session.country = country;
    session.state = state;
    
    session.registrationNumber = "1-" + nextSellerSequence;
    nextSellerSequence++;
    
    alert("Seller Verified ID: " + session.registrationNumber);
    
    document.getElementById('view-seller-phone').classList.add('hidden');
    document.getElementById('view-marketplace').classList.remove('hidden');
    renderInventory(propertiesData);
}

        // LAYER 5: INVENTORY RENDER ENGINE (DYNAMIC DOM GENERATOR)
    function renderInventory(items) {
        const grid = document.getElementById('inventory-grid');
        grid.innerHTML = ''; // Wipe shelf clean before rebuilding
        
        // Setup User Badge Info inside marketplace banner
        document.getElementById('display-user-id').innerText = "ID: " + session.registrationNumber;
        document.getElementById('display-user-locale').innerText = "LOCALE: " + session.state + ", " + session.country.toUpperCase();

        if (items.length === 0) {
            grid.innerHTML = `<p class="text-zinc-500 text-xs text-center py-8">No matching real estate listings found.</p>`;
            return;
        }

        // Determine currency symbols and rates dynamically
        let currency = "USD $";
        let rate = 1;
        const userCountry = session.country.toLowerCase();

        if (currencyRates[userCountry]) {
            currency = currencyRates[userCountry].symbol;
            rate = currencyRates[userCountry].rate;
        }

        // Loop through properties and generate HTML cards
        items.forEach(item => {
            // Default base calculation ($100k - $250k placeholder equivalents scaled to local currency rate)
            const basePriceUSD = item.id === 101 ? 150000 : item.id === 102 ? 220000 : item.id === 103 ? 95000 : 180000;
            const convertedPrice = (basePriceUSD * rate).toLocaleString();

            const cardHtml = `
                <div class="zinc-card rounded-xl p-4 border border-zinc-900 shadow-lg space-y-3">
                    <div class="h-32 bg-zinc-950 rounded-lg border border-zinc-900 flex items-center justify-center text-zinc-700 text-xs font-mono">
                        IMAGE PLACEHOLDER #${item.id}
                    </div>
                    <div class="space-y-1">
                        <div class="flex justify-between items-start">
                            <h4 class="text-sm font-bold text-white tracking-wide">${item.title}</h4>
                            <span class="text-xs font-mono text-orange-400 font-bold">${currency} ${convertedPrice}</span>
                        </div>
                        <p class="text-xs text-zinc-400">${item.area}</p>
                    </div>
                    <button onclick="openPropertyDetails(${item.id})" class="w-full bg-zinc-900 hover:bg-zinc-800 border border-zinc-800 text-white text-[11px] font-bold py-2 rounded-lg transition">
                        VIEW ASSET SPECIFICATIONS
                    </button>
                </div>
            `;
            grid.insertAdjacentHTML('beforeend', cardHtml);
        });
    }

    // Connect registration finishes to this new view layout
    // Go modify your processBuyerRegistration and processSellerRegistration to run these triggers:

        const phone = document.getElementById('seller-phone').value.trim();
        const country = document.getElementById('seller-country').value.trim().toLowerCase();
        const state = document.getElementById('seller-state').value.trim();
        
        if (!phone || !country || !state) {
            alert("All fields are required for seller verification.");
            return;
        }
        
        session.phone = phone;
        session.country = country;
        session.state = state;
        
        // Rule: Sellers start with 1 sequence
        session.registrationNumber = "1-" + nextSellerSequence;
        nextSellerSequence++;
        
        alert("Seller Verified ID: " + session.registrationNumber);
        // Next step will transition to inventory listing management
    }

        </script>
    </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
    
