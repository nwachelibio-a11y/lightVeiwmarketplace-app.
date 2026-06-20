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
            
                            <div id="view-login" class="zinc-card rounded-xl p-6 text-center shadow-2xl space-y-4">
                    <div class="text-center space-y-1">
                        <h3 id="login-title-header" class="text-base font-bold text-white tracking-wide font-mono">[ACCESS CENTRAL GATEWAY]</h3>
                        <p id="login-subtitle" class="text-[11px] text-zinc-500">Provide credentials to initialize session link</p>
                    </div>

                    <div id="email-input-group" class="space-y-3">
                        <input type="text" id="login-email" placeholder="Enter Gmail Address (e.g. name@gmail.com)" class="w-full bg-zinc-950 border border-zinc-900 rounded-lg px-3 py-2 text-xs text-white focus:outline-none focus:border-zinc-700 tracking-wide font-mono">
                        
                        <div id="setup-pin-group" class="space-y-1 text-left">
                            <label class="text-[9px] text-zinc-500 font-mono tracking-wide">[CREATE 4-DIGIT SECURITY PIN]</label>
                            <input type="password" id="login-pin" maxlength="4" placeholder="••••" class="w-full bg-zinc-950 border border-zinc-900 rounded-lg px-3 py-2 text-center text-sm font-bold text-white focus:outline-none focus:border-zinc-700 tracking-widest font-mono">
                        </div>

                        <button onclick="handleGmailLogin()" class="w-full bg-orange-600 hover:bg-orange-700 text-white text-xs font-bold py-2.5 rounded-lg transition tracking-wide font-mono">
                            INITIALIZE SECURE ACCESS
                        </button>
                    </div>

                    <div id="quick-pin-group" class="hidden space-y-3 p-2 text-center">
                        <p class="text-xs text-zinc-400">Welcome Back</p>
                        <p id="quick-login-email" class="text-xs text-orange-400 font-bold font-mono"></p>
                        <input type="password" id="returning-pin" maxlength="4" placeholder="ENTER PIN TO UNLOCK" class="w-full bg-zinc-900 border border-zinc-800 rounded-lg px-3 py-2 text-center text-sm font-bold text-white focus:outline-none focus:border-zinc-700 tracking-widest font-mono">
                        <button onclick="handleQuickPinUnlock()" class="w-full bg-white hover:bg-zinc-200 text-black text-xs font-bold py-2 rounded-lg transition tracking-wide font-mono">
                            UNLOCK PROFILE
                        </button>
                        <button onclick="handleForgetSession()" class="text-[10px] text-zinc-600 underline block mx-auto pt-1">Use a different account</button>
                    </div>
                </div>


            <div id="view-role" class="hidden zinc-card rounded-xl p-6 text-center shadow-2xl">
                <h3 class="text-base font-bold mb-1">Select Account Type</h3>
                <p class="text-xs text-zinc-400 mb-6">Are you searching for housing or listing a property?</p>
                                <div class="grid grid-cols-2 gap-3">
                    <button onclick="selectRole('buyer')" class="p-4 bg-zinc-900 hover:bg-zinc-800 border border-zinc-800 rounded-xl transition flex flex-col items-center justify-center space-y-1">
                        <span class="text-xs font-mono text-zinc-500 font-bold">[BUYER]</span>
                        <span class="text-xs font-bold text-white">I am a Buyer</span>
                    </button>
                    <button onclick="selectRole('seller')" class="p-4 bg-zinc-900 hover:bg-zinc-800 border border-zinc-800 rounded-xl transition flex flex-col items-center justify-center space-y-1">
                        <span class="text-xs font-mono text-zinc-500 font-bold">[SELLER]</span>
                        <span class="text-xs font-bold text-white">I am a Seller</span>
                    </button>
                </div>
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
                        <div id="view-marketplace" class="hidden space-y-3">
                    <div class="flex items-center justify-between border-b border-zinc-900 pb-2 text-[10px] font-mono tracking-wide">
                        <div class="flex flex-col space-y-0.5">
                            <span id="display-user-id" class="text-white"></span>
                            <span id="display-user-locale" class="text-zinc-500"></span>
                        </div>
                        <button onclick="handleLogout()" class="text-orange-500 font-bold hover:text-orange-400">[LOGOUT ACCOUNT]</button>
                    </div>

                    <input type="text" id="market-search" oninput="executeInstantSearch()" placeholder="Search by area or city..." class="w-full bg-zinc-950 border border-zinc-900 rounded-lg px-3 py-2 text-xs text-white focus:outline-none focus:border-zinc-800 tracking-wide font-mono">

                    <div id="seller-management-panel" class="hidden zinc-card rounded-xl p-4 border border-zinc-900 bg-zinc-950 space-y-3">
                        <h4 class="text-xs font-bold text-white font-mono tracking-wide border-b border-zinc-900 pb-1">[POST NEW REAL ESTATE ASSET]</h4>
                        <div class="space-y-2">
                            <input type="text" id="listing-title" placeholder="Property Title" class="w-full bg-zinc-900 border border-zinc-800 rounded-lg px-3 py-2 text-xs text-white focus:outline-none focus:border-zinc-700">
                            <input type="text" id="listing-area" placeholder="Specific City / Area" class="w-full bg-zinc-900 border border-zinc-800 rounded-lg px-3 py-2 text-xs text-white focus:outline-none focus:border-zinc-700">
                            <input type="number" id="listing-price" placeholder="Base Value Price in USD ($)" class="w-full bg-zinc-900 border border-zinc-800 rounded-lg px-3 py-2 text-xs text-white focus:outline-none focus:border-zinc-700">
                            <button onclick="handleCreateListing()" class="w-full bg-white hover:bg-zinc-200 text-black text-xs font-bold py-2 rounded-lg transition tracking-wide font-mono">
                                SUBMIT ASSET TO GLOBAL MARKETPLACE
                            </button>
                        </div>
                    </div>

                    <div id="inventory-grid" class="grid grid-cols-1 gap-4"></div>
</div>

        </main>

        <footer class="text-center text-[10px] text-zinc-600 font-mono pt-3 border-t border-zinc-900">
            LightView Housing Hub © 2026
        </footer>

        <script>
            // LAYER 1: GLOBAL DATA REGISTRY
    let session = {
        email: "",
        role: "",
        phone: "",
        country: "",
        state: "",
        registrationNumber: "",
        watchedAdsCount: 0
    };

    let nextBuyerSequence = 1;
    let nextSellerSequence = 1;

    let propertiesData = [];

    const currencyRates = {
        "united states": { symbol: "USD $", rate: 1 },
        "united kingdom": { symbol: "GBP £", rate: 0.79 },
        "eurozone": { symbol: "EUR €", rate: 0.93 },
        "canada": { symbol: "CAD $", rate: 1.37 },
        "australia": { symbol: "AUD $", rate: 1.51 },
        "japan": { symbol: "JPY ¥", rate: 157 },
        "china": { symbol: "CNY ¥", rate: 7.25 },
        "india": { symbol: "INR ₹", rate: 83.5 },
        "south africa": { symbol: "ZAR R", rate: 18.2 },
        "united arab emirates": { symbol: "AED", rate: 3.67 },
        "saudi arabia": { symbol: "SAR", rate: 3.75 },
        "brazil": { symbol: "BRL R$", rate: 5.36 },
        "mexico": { symbol: "MXN $", rate: 18.4 },
        "nigeria": { symbol: "NGN", rate: 1600 },
        "ghana": { symbol: "GHS ₵", rate: 15 },
        "kenya": { symbol: "KES KSh", rate: 129 }
    };

    // LAYER 2: CORE AUTHENTICATION TRIGGERS & SESSION PERSISTENCE (PIN PROTECTED)
    function handleGmailLogin() {
        const emailInput = document.getElementById('login-email').value.trim();
        const pinInput = document.getElementById('login-pin').value.trim();

        if (!emailInput || !emailInput.includes('@gmail.com')) {
            alert("Provide a valid Gmail address.");
            return;
        }
        if (pinInput.length !== 4 || isNaN(pinInput)) {
            alert("Security PIN must be exactly 4 numbers.");
            return;
        }
        
        session.email = emailInput;
        session.pin = pinInput; // Lock password into temporary memory
        
        document.getElementById('view-login').classList.add('hidden');
        document.getElementById('view-role').classList.remove('hidden');
    }

    function handleQuickPinUnlock() {
        const inputPin = document.getElementById('returning-pin').value.trim();
        const localProfile = JSON.parse(localStorage.getItem('savedUserProfile'));

        if (inputPin === localProfile.pin) {
            // PIN Matches perfectly! Restore entire session state
            session = localProfile;
            
            document.getElementById('view-login').classList.add('hidden');
            document.getElementById('view-marketplace').classList.remove('hidden');
            
            // If they are a seller, make sure their management panel unhides
            if (session.role === 'seller') {
                document.getElementById('seller-management-panel').classList.remove('hidden');
            }
            
            alert("Access authorized. Welcome back!");
            renderInventory(propertiesData);
        } else {
            alert("INVALID SECURITY PIN. ACCESS DENIED.");
            document.getElementById('returning-pin').value = '';
        }
    }

    function handleForgetSession() {
        localStorage.removeItem('savedUserProfile');
        location.reload();
    }

    // SYSTEM INTERCEPT ON APP BOOTUP
    window.addEventListener('DOMContentLoaded', () => {
        // Restore inventory data safely
        const storedInventory = localStorage.getItem('globalPropertiesBackup');
        if (storedInventory) {
            propertiesData = JSON.parse(storedInventory);
        }

        // Check if device already has a registered profile
        const savedProfile = localStorage.getItem('savedUserProfile');
        if (savedProfile) {
            const profile = JSON.parse(savedProfile);
            
            // Hide normal login fields, activate the Quick PIN UI wrapper
            document.getElementById('email-input-group').classList.add('hidden');
            document.getElementById('quick-pin-group').classList.remove('hidden');
            document.getElementById('quick-login-email').innerText = profile.email;
            document.getElementById('login-title-header').innerText = "[SECURE PIN UNLOCK]";
            document.getElementById('login-subtitle').innerText = "Device profile detected. Enter numeric password.";
        }
    });

          
     // LAYER 3 & 4: INTERACTION LOGIC & REGISTRATION
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
        session.registrationNumber = "0-" + nextBuyerSequence;
        nextBuyerSequence++;
        
        alert("Buyer Assigned ID: " + session.registrationNumber);
        
        document.getElementById('view-buyer-location').classList.add('hidden');
        document.getElementById('view-marketplace').classList.remove('hidden');
               localStorage.setItem('savedUserProfile', JSON.stringify(session));
               
        renderInventory(propertiesData);
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
        
                localStorage.setItem('savedUserProfile', JSON.stringify(session));
        document.getElementById('view-seller-phone').classList.add('hidden');
        document.getElementById('view-marketplace').classList.remove('hidden');
        renderInventory(propertiesData);
    }
        // LAYER 5: INVENTORY RENDER ENGINE
    function renderInventory(items) {
        const grid = document.getElementById('inventory-grid');
        grid.innerHTML = '';
        
        document.getElementById('display-user-id').innerText = "ID: " + session.registrationNumber;
        document.getElementById('display-user-locale').innerText = "LOCALE: " + session.state + ", " + session.country.toUpperCase();

        if (items.length === 0) {
            grid.innerHTML = `<p class="text-zinc-500 text-xs text-center py-8">No matching real estate listings found.</p>`;
            return;
        }

        let currency = "USD $";
        let rate = 1;
        const userCountry = session.country.toLowerCase().trim();

        if (currencyRates[userCountry]) {
            currency = currencyRates[userCountry].symbol;
            rate = currencyRates[userCountry].rate;
        } else if (userCountry !== "") {
            // Smart Fallback for all 195 countries: cuts the first 3 letters of their country name to make a currency code
            currency = userCountry.substring(0, 3).toUpperCase() + " $";
            rate = 1; 
        }

        items.forEach(item => {
            const convertedPrice = (item.priceUSD * rate).toLocaleString();

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
                    <button onclick="triggerAdGate(${item.id})" class="w-full bg-zinc-900 hover:bg-zinc-800 border border-zinc-800 text-white text-[11px] font-bold py-2 rounded-lg transition">
                        VIEW ASSET SPECIFICATIONS
                    </button>
                </div>
            `;
            grid.insertAdjacentHTML('beforeend', cardHtml);
        });
    }

     // LAYER 6: INSTANT SEARCH SYSTEM
    function executeInstantSearch() {
        const query = document.getElementById('market-search').value.toLowerCase().trim();
        const filtered = propertiesData.filter(item => 
            item.title.toLowerCase().includes(query) || 
            item.area.toLowerCase().includes(query)
        );
        renderInventory(filtered);
    }

    // LAYER 7: GOOGLE ADS INTEGRATION & FEATURES GATING
    function triggerAdGate(propertyId) {
        alert("Loading secure verification ad panel... Please wait 3 seconds.");
        
        setTimeout(() => {
            session.watchedAdsCount++;
            alert("Ad completed! Total watched: " + session.watchedAdsCount + ". Loading property asset details...");
            openPropertyDetails(propertyId);
        }, 3000);
    }
    // LOGOUT & SESSION EXTENSION SCRIPT
     function handleLogout() {
        localStorage.removeItem('savedUserProfile');
        location.reload();
    }
   

    // LAYER 7: SELLER ASSET MANAGEMENT ENGINE (PERSISTENT CORES)
    function handleCreateListing() {
        const title = document.getElementById('listing-title').value.trim();
        const area = document.getElementById('listing-area').value.trim();
        const priceUSD = parseFloat(document.getElementById('listing-price').value);

        if (!title || !area || isNaN(priceUSD) || priceUSD <= 0) {
            alert("Please accurately complete all property specification fields.");
            return;
        }

        const newAsset = {
            id: Date.now(),
            title: title,
            area: area,
            priceUSD: priceUSD,
            sellerEmail: session.email
        };

        propertiesData.push(newAsset);
        localStorage.setItem('globalPropertiesBackup', JSON.stringify(propertiesData));
        
        document.getElementById('listing-title').value = '';
        document.getElementById('listing-area').value = '';
        document.getElementById('listing-price').value = '';

        alert("Asset successfully published to global index!");
        renderInventory(propertiesData);
    }

    function handleDeleteListing(assetId) {
        if (confirm("Are you certain you want to completely withdraw this property from the marketplace?")) {
            propertiesData = propertiesData.filter(item => item.id !== assetId);
            localStorage.setItem('globalPropertiesBackup', JSON.stringify(propertiesData));
            renderInventory(propertiesData);
        }
    }

    // AUTOMATIC SYSTEM DATA RESTORE ON LOAD
    window.addEventListener('DOMContentLoaded', () => {
        const storedInventory = localStorage.getItem('globalPropertiesBackup');
        if (storedInventory) {
            propertiesData = JSON.parse(storedInventory);
        }
    });

    function openPropertyDetails(id) {
        alert("Displaying backend architecture specifications for asset metadata contract #" + id);
    }
     
        </script>
    </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
    
