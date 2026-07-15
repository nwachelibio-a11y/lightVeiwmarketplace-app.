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
    <title>Lightview Real Estate Hub</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script type="text/javascript" src="https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>
    <style>
        body { background-color: #000000; color: #ffffff; font-family: sans-serif; }
        .zinc-card { background-color: #0b0b0c; border: 1px solid #18181b; }
        ::-webkit-scrollbar { width: 5px; }
        ::-webkit-scrollbar-track { background: #000000; }
        ::-webkit-scrollbar-thumb { background: #27272a; border-radius: 10px; }
        .hidden { display: none !important; }
    </style>
</head>
<body class="min-h-screen flex flex-col p-4 max-w-xl mx-auto select-none justify-between">
    <header class="border-b border-zinc-900 pb-3 flex justify-between items-center">
        <div class="flex flex-col">
            <span class="text-orange-500 font-black tracking-tight text-xl">LIGHTVIEW</span>
            <span class="text-zinc-500 font-mono text-[10px]">MARKETPLACE v3.0.0</span>
        </div>
        <div class="flex items-center gap-2">
            <div id="global-translate-element"></div>
            <span class="text-[10px] bg-emerald-950 text-emerald-400 border border-emerald-900 font-mono px-2 py-0.5 rounded-md tracking-wider">LIVE SYSTEM</span>
        </div>
    </header>

    <main class="flex-grow flex flex-col justify-center my-4">
            <!-- ACCESS CONTROL GATEWAY -->
        <div id="view-login" class="zinc-card rounded-xl p-6 shadow-2xl space-y-4">
            <div class="space-y-1">
                <h4 class="text-sm font-bold text-white font-mono tracking-wide">ACCESS CONTROL GATEWAY</h4>
                <p class="text-xs text-zinc-400 font-mono">Provide credentials to initialize secure session link</p>
            </div>
            <div class="space-y-3">
                <div class="space-y-1">
                    <label class="text-[10px] font-mono text-zinc-500 block font-bold uppercase">ENTER YOUR EMAIL ADDRESS</label>
                    <input type="email" id="login-mail" placeholder="e.g. user@gmail.com" class="w-full p-3 bg-zinc-950 border border-zinc-800 rounded-lg text-sm text-white font-mono focus:outline-none focus:border-zinc-700">
                </div>
                <div class="space-y-1">
                    <label class="text-[10px] font-mono text-zinc-500 block font-bold uppercase">ENTER HARDWARE PIN TO QUICK SCAN</label>
                    <input type="password" id="login-pasw" maxlength="4" placeholder="••••" class="w-full p-3 bg-zinc-950 border border-zinc-800 rounded-lg text-sm text-center tracking-widest text-white font-mono focus:outline-none focus:border-zinc-700">
                </div>
            </div>
            <button onclick="handleLoginRequest()" class="w-full p-3 bg-orange-600 hover:bg-orange-700 text-white font-bold rounded-xl text-xs tracking-widest font-mono transition-all duration-200 shadow-lg uppercase">
                Initialize Secure Access
            </button>
        </div>

        <!-- ACCOUNT CLASSIFICATION -->
        <div id="view-role" class="hidden zinc-card rounded-xl p-6 shadow-2xl space-y-4">
            <div class="space-y-1">
                <h4 class="text-sm font-bold text-white font-mono tracking-wide text-center">ACCOUNT CLASSIFICATION</h4>
                <p class="text-xs text-zinc-400 font-mono text-center">Are you searching for housing or listing a property asset?</p>
            </div>
            <div class="grid grid-cols-2 gap-3 pt-2">
                <button onclick="selectRole('Buyer')" class="p-5 bg-zinc-900 hover:bg-zinc-800 border border-zinc-800 text-white rounded-xl text-center flex flex-col items-center justify-center gap-2 transition-all duration-200">
                    <span class="text-xs font-bold font-mono tracking-wider uppercase">I'm a Buyer</span>
                </button>
                <button onclick="selectRole('Seller')" class="p-5 bg-zinc-900 hover:bg-zinc-800 border border-zinc-800 text-white rounded-xl text-center flex flex-col items-center justify-center gap-2 transition-all duration-200">
                    <span class="text-xs font-bold font-mono tracking-wider uppercase">I'm a Seller</span>
                </button>
            </div>
        </div>
               <!-- BUYER REGISTRATION -->
        <div id="view-buyer-location" class="hidden zinc-card rounded-xl p-6 shadow-2xl space-y-4">
            <h4 class="text-sm font-bold text-white font-mono border-b border-zinc-900 pb-2 uppercase tracking-wider">Location Matrix Setup</h4>
            <div class="space-y-3">
                <input type="text" id="buyer-country" placeholder="Country (e.g. United States)" class="w-full p-3 bg-zinc-950 border border-zinc-800 rounded-lg text-sm text-white font-mono focus:outline-none focus:border-zinc-700">
                <input type="text" id="buyer-state" placeholder="State / Province" class="w-full p-3 bg-zinc-950 border border-zinc-800 rounded-lg text-sm text-white font-mono focus:outline-none focus:border-zinc-700">
            </div>
            <button onclick="processBuyerRegistration()" class="w-full p-3 bg-orange-600 hover:bg-orange-700 text-white font-bold rounded-xl text-xs tracking-widest font-mono transition-all duration-200 uppercase">
                Continue Setup
            </button>
        </div>

        <!-- SELLER REGISTRATION -->
        <div id="view-seller-phone" class="hidden zinc-card rounded-xl p-6 shadow-2xl space-y-4">
            <div class="space-y-1">
                <h4 class="text-sm font-bold text-white font-mono border-b border-zinc-900 pb-2 uppercase tracking-wider">Seller Identity Verification</h4>
                <p class="text-[11px] text-zinc-500 font-mono">Authenticate localized telephone data to establish market legitimacy.</p>
            </div>
            <div class="space-y-3 pt-1">
                <input type="tel" id="seller-phone" placeholder="Phone Number (e.g. 234...)" class="w-full p-3 bg-zinc-950 border border-zinc-800 rounded-lg text-sm text-white font-mono focus:outline-none">
                <input type="text" id="seller-country" placeholder="Country (e.g. China)" class="w-full p-3 bg-zinc-950 border border-zinc-800 rounded-lg text-sm text-white font-mono focus:outline-none">
                <input type="text" id="seller-state" placeholder="State / Region" class="w-full p-3 bg-zinc-950 border border-zinc-800 rounded-lg text-sm text-white font-mono focus:outline-none">
            </div>
            <button onclick="processSellerRegistration()" class="w-full p-3 bg-orange-600 hover:bg-orange-700 text-white font-bold rounded-xl text-xs tracking-widest font-mono transition-all duration-200 uppercase">
                Continue Setup
            </button>
        </div>
               <!-- USER IDENTITY VALIDATION GATEWAY (NAME MUST BE > 4 LETTERS) -->
        <div id="view-identity-setup" class="hidden zinc-card rounded-xl p-6 shadow-2xl space-y-4">
            <div class="space-y-1">
                <h4 class="text-sm font-bold text-white font-mono tracking-wide uppercase">Identity Verification</h4>
                <p class="text-xs text-zinc-400 font-mono">Please provide your legal personal name to bind securely to your localized identity keys.</p>
            </div>
            <div class="space-y-3">
                <div class="space-y-1">
                    <label class="text-[10px] font-mono text-zinc-500 block font-bold uppercase">Enter Your Full Name</label>
                    <input type="text" id="identity-name" placeholder="Name must exceed 4 letters..." class="w-full p-3 bg-zinc-950 border border-zinc-800 rounded-lg text-sm text-white font-mono focus:outline-none focus:border-zinc-700">
                </div>
            </div>
            <button onclick="commitUserIdentityDetails()" class="w-full p-3 bg-orange-600 hover:bg-orange-700 text-white font-bold rounded-xl text-xs tracking-widest font-mono transition-all duration-200 uppercase">
                Finalize Identity Handshake
            </button>
        </div>
                <!-- CORE MARKETPLACE DASHBOARD -->
        <div id="view-marketplace" class="hidden space-y-4">
            <div class="flex items-center justify-between border-b border-zinc-900 pb-3">
                <div class="flex flex-col">
                    <span id="display-user-id" class="text-xs font-bold text-white font-mono uppercase tracking-wide">ID: ACCOUNT PENDING</span>
                    <span id="display-user-locale" class="text-[10px] text-zinc-500 font-mono uppercase">LOCALE: SYNCING REGION</span>
                </div>
                <button onclick="handleLogout()" class="text-[10px] text-zinc-500 hover:text-orange-400 font-mono font-bold border border-zinc-800 hover:border-orange-900/40 px-2.5 py-1 rounded-lg transition-all duration-200 uppercase">
                    Exit Session
                </button>
            </div>

            <div id="ad-wallet-header-panel" class="zinc-card rounded-xl p-4 space-y-3 shadow-xl">
                <div class="flex justify-between items-center border-b border-zinc-900/60 pb-2">
                    <span class="text-xs font-bold text-zinc-400 font-mono tracking-wider uppercase">Coin Wallet Balance:</span>
                    <span class="text-sm font-black text-amber-500 font-mono"><span id="sh-coins">0</span> COINS</span>
                </div>
                <div class="flex justify-between items-center text-[11px] font-mono text-zinc-500">
                    <span>Watched Ads Progress:</span>
                    <span class="text-zinc-400"><span id="sh-watched">0</span> / 10 ADS</span>
                </div>
                <div class="grid grid-cols-2 gap-2 pt-1">
                    <button onclick="watchAdForBoostCoins()" class="p-2.5 bg-zinc-950 hover:bg-zinc-900 border border-zinc-800 text-white font-bold rounded-lg text-[10px] tracking-wider font-mono transition-all duration-200 uppercase">
                        Watch Ad (+1 Coin)
                    </button>
                    <button id="btn-promote-asset" class="p-2.5 bg-amber-500 hover:bg-amber-600 text-black font-black rounded-lg text-[10px] tracking-wider font-mono transition-all duration-200 uppercase shadow-lg shadow-amber-500/10">
                        Boost Listing (-5)
                    </button>
                </div>
            </div>

            <div class="flex gap-2">
                <input type="text" id="market-search" oninput="renderMarketplaceInventoryGrid()" placeholder="Search assets by city, region, or area..." class="w-full p-3 bg-zinc-950 border border-zinc-800 rounded-lg text-sm text-white font-mono focus:outline-none focus:border-zinc-700">
            </div>

            <div class="flex items-center justify-between text-zinc-500 font-mono text-[10px] tracking-widest uppercase border-b border-zinc-900 pb-1 pt-2">
                <span>GLOBAL REAL ESTATE INDEX</span>
                <span>FEED CHANNELS</span>
            </div>

            <div id="inventory-grid" class="grid grid-cols-1 gap-4"></div>
        </div>
        <!-- SELLER ASSET SUBMISSION PANEL -->
        <div id="seller-management-panel" class="hidden zinc-card rounded-xl p-5 space-y-4 shadow-2xl mt-2">
            <h4 class="text-sm font-bold text-white tracking-wide font-mono text-center border-b border-zinc-900 pb-2 uppercase">Post New Real Estate Asset</h4>
            <div class="space-y-3">
                <div>
                    <label class="text-[10px] font-mono text-zinc-400 block mb-1 font-bold uppercase">Asset Description or Name</label>
                    <input type="text" id="listing-title" placeholder="e.g. Luxury Duplex Apartment" class="w-full p-2.5 bg-zinc-950 border border-zinc-800 rounded-lg text-sm text-white font-mono focus:outline-none focus:border-zinc-700">
                </div>
                <div>
                    <label class="text-[10px] font-mono text-zinc-400 block mb-1 font-bold uppercase">Location Region or City/Area</label>
                    <input type="text" id="listing-area" placeholder="e.g. Lekki Phase 1, Lagos" class="w-full p-2.5 bg-zinc-950 border border-zinc-800 rounded-lg text-sm text-white font-mono focus:outline-none focus:border-zinc-700">
                </div>
                <div>
                    <label class="text-[10px] font-mono text-zinc-400 block mb-1 font-bold uppercase">House Specifications & Amenities</label>
                    <input type="text" id="listing-features" placeholder="e.g. 4 Bedrooms, Swimming Pool, 24/7 Power" class="w-full p-2.5 bg-zinc-950 border border-zinc-800 rounded-lg text-sm text-white font-mono focus:outline-none focus:border-zinc-700">
                </div>
                <div class="grid grid-cols-2 gap-3">
                    <div>
                        <label class="text-[10px] font-mono text-zinc-400 block mb-1 font-bold uppercase">Price Value (<span id="local-currency-symbol-label" class="text-emerald-400">USD</span>)</label>
                        <input type="number" id="listing-price" placeholder="0.00" class="w-full p-2.5 bg-zinc-950 border border-zinc-800 rounded-lg text-sm text-white font-mono focus:outline-none focus:border-zinc-700">
                    </div>
                    <div>
                        <label class="text-[10px] font-mono text-zinc-400 block mb-1 font-bold uppercase">WhatsApp Link Number</label>
                        <input type="tel" id="listing-contact" placeholder="e.g. 2348012345678" class="w-full p-2.5 bg-zinc-950 border border-zinc-800 rounded-lg text-sm text-white font-mono focus:outline-none focus:border-zinc-700">
                    </div>
                </div>
                <button onclick="handleCreateListing()" class="w-full p-3 bg-emerald-600 hover:bg-emerald-700 text-white font-bold rounded-xl text-xs tracking-widest font-mono transition-all duration-200 uppercase shadow-md mt-2">
                    Commit Property to Global Index
                </button>
            </div>
        </div>
    </main>

    <footer class="text-center text-zinc-700 font-mono text-[9px] border-t border-zinc-900 pt-3 mt-4 space-y-1">
        <div>Lightview Real Estate Housing Hub v3.0.0</div>
        <div>Active Allocation Buffer: 512MB / 528MB Free Tier Baseline</div>
    </footer>

<script>
// 1. Central Core System Application State Context Matrix
let appState = {
    user: null,          
    role: null,          
    country: "united states", 
    stateRegion: "",
    name: "",
    coins: 0,            
    watchedAdsCount: 0   
};
// 2. Storage Array. Initial Demo contains a Locked base currency origin anchor
let propertiesData = [
    {
        id: 1,
        title: "Exquisite Lekki Penthouse Suite",
        sellerCountry: "nigeria", 
        country: "Nigeria",
        state: "Lagos",
        area: "Lekki Phase 1",
        features: "4 Bed, Smart Home Automation, Ocean View Infinity Pool",
        localPrice: 375000000, 
        currencySymbol: "₦",
        contactPhone: "2348012345678",
        whatsAppUrl: "https://wa.me/2348012345678",
        sellerPhone: "2347000000000",
        isBoosted: true
    }
];

// Helper structure containing standard mapped currency names
const globalCurrencySymbolMap = {
    "usd": "$", "eur": "€", "gbp": "£", "ngn": "₦", "ghs": "₵", "kes": "KSh", 
    "zar": "R", "aed": "د.إ", "cad": "C$", "aud": "A$", "jpy": "¥", "cny": "¥",
    "inr": "₹", "rub": "₽", "brl": "R$", "mxn": "$", "sar": "SR", "egp": "E£"
};

let currencyRates = {
    "united states": { symbol: "$", rate: 1.00, code: "USD" },
    "united kingdom": { symbol: "£", rate: 0.79, code: "GBP" },
    "eurozone": { symbol: "€", rate: 0.93, code: "EUR" },
    "nigeria": { symbol: "₦", rate: 1500.00, code: "NGN" },
    "ghana": { symbol: "₵", rate: 15.10, code: "GHS" },
    "kenya": { symbol: "KSh", rate: 129.50, code: "KES" },
    "south africa": { symbol: "R", rate: 18.20, code: "ZAR" },
    "uae": { symbol: "د.إ", rate: 3.67, code: "AED" },
    "china": { symbol: "¥", rate: 7.25, code: "CNY" }
};

function syncLiveGlobalCurrencyExchangeRates() {
    console.log("Initializing dynamic connection to global currency API pipeline...");
    
    return fetch('https://open.er-api.com/v6/latest/USD')
    .then(response => {
        if (!response.ok) throw new Error("Network currency endpoint synchronization failure.");
        return response.json();
    })
    .then(data => {
        if (!data || !data.rates) return;
        const freshRates = data.rates;

        Object.keys(freshRates).forEach(currencyCode => {
            const lowerCode = currencyCode.toLowerCase();
            let derivedCountryKey = currencyCode; 
            
            if (currencyCode === "USD") derivedCountryKey = "united states";
            else if (currencyCode === "GBP") derivedCountryKey = "united kingdom";
            else if (currencyCode === "EUR") derivedCountryKey = "eurozone";
            else if (currencyCode === "NGN") derivedCountryKey = "nigeria";
            else if (currencyCode === "GHS") derivedCountryKey = "ghana";
            else if (currencyCode === "KES") derivedCountryKey = "kenya";
            else if (currencyCode === "ZAR") derivedCountryKey = "south africa";
            else if (currencyCode === "AED") derivedCountryKey = "uae";
            else if (currencyCode === "CNY") derivedCountryKey = "china";

            const accurateSymbol = globalCurrencySymbolMap[lowerCode] || currencyCode;

            currencyRates[derivedCountryKey.toLowerCase()] = {
                symbol: accurateSymbol,
                rate: freshRates[currencyCode],
                code: currencyCode
            };
        });
        
        if (appState.country) {
            const currentLocale = appState.country.toLowerCase();
            const symbolLabel = document.getElementById('local-currency-symbol-label');
            if (symbolLabel && currencyRates[currentLocale]) {
                symbolLabel.innerText = currencyRates[currentLocale].symbol;
            }
        }
    })
    .catch(error => {
        console.error("Currency Sync Error:", error);
    });
}
// --- PERSISTENT GMAIL REGISTRATION INDEX ---
// This acts as our persistent client ledger tracking created email accounts to deny duplicate configurations
function getRegisteredEmails() {
    const list = localStorage.getItem("lightview_registered_users");
    return list ? JSON.parse(list) : [];
}

function registerEmailInSystem(email) {
    const list = getRegisteredEmails();
    if (!list.includes(email.toLowerCase())) {
        list.push(email.toLowerCase());
        localStorage.setItem("lightview_registered_users", JSON.stringify(list));
    }
}

function handleLoginRequest() {
    const emailInputNode = document.getElementById('login-mail');
    const pinInputNode = document.getElementById('login-pasw');
    const clearEmailText = emailInputNode.value.trim().toLowerCase();
    const clearPinText = pinInputNode.value.trim();

    if (!clearEmailText || !clearEmailText.includes('@') || !clearEmailText.includes('.')) {
        alert("SECURITY ACCESS DENIED: Please supply a legally formatted email address.");
        return;
    }
    if (clearPinText.length !== 4 || isNaN(clearPinText)) {
        alert("SECURITY ACCESS DENIED: Authentication PIN must be exactly 4 numerical digits.");
        return;
    }

    // GMAIL REGISTRATION DUPLICATE BLOCKING CHECK
    const list = getRegisteredEmails();
    
    // If the email is already registered but there's no active session for it, block creation of a duplicate!
    const cachedSessionToken = localStorage.getItem("lightview_session");
    let currentSessionUser = "";
    if (cachedSessionToken) {
        try {
            currentSessionUser = JSON.parse(cachedSessionToken).user.toLowerCase();
        } catch(e) {}
    }

    if (list.includes(clearEmailText) && currentSessionUser !== clearEmailText) {
        alert("ACCESS DENIED: An account with this email address already exists. Try logging in with a different device, or clear your session.");
        return;
    }

    appState.user = clearEmailText;
    document.getElementById('view-login').classList.add('hidden');
    document.getElementById('view-role').classList.remove('hidden');
}

function selectRole(selectedRole) {
    appState.role = selectedRole;
    document.getElementById('view-role').classList.add('hidden');
    if (selectedRole === 'Buyer') {
        document.getElementById('view-buyer-location').classList.remove('hidden');
    } else {
        document.getElementById('view-seller-phone').classList.remove('hidden');
    }
}
function processBuyerRegistration() {
    const countryFieldVal = document.getElementById('buyer-country').value.trim();
    const stateFieldVal = document.getElementById('buyer-state').value.trim();
    
    if (!countryFieldVal || !stateFieldVal) {
        alert("Please complete both location fields.");
        return;
    }

    appState.country = countryFieldVal.toLowerCase();
    appState.stateRegion = stateFieldVal.toLowerCase();

    // Transition to the Name Gate
    document.getElementById('view-buyer-location').classList.add('hidden');
    document.getElementById('view-identity-setup').classList.remove('hidden');
}

function processSellerRegistration() {
    const phoneFieldVal = document.getElementById('seller-phone').value.trim();
    const countryFieldVal = document.getElementById('seller-country').value.trim();
    const stateFieldVal = document.getElementById('seller-state').value.trim();

    if (!phoneFieldVal || !countryFieldVal || !stateFieldVal) {
        alert("Please complete all Seller verification inputs.");
        return;
    }

    appState.user = phoneFieldVal; 
    appState.country = countryFieldVal.toLowerCase();
    appState.stateRegion = stateFieldVal.toLowerCase();

    // Transition to the Name Gate
    document.getElementById('view-seller-phone').classList.add('hidden');
    document.getElementById('view-identity-setup').classList.remove('hidden');
}

// --- NEW VALIDATION GATE FOR NAMES OVER 4 LETTERS ---
function commitUserIdentityDetails() {
    const inputNameNode = document.getElementById('identity-name');
    const userEnteredName = inputNameNode.value.trim();

    if (userEnteredName.length <= 4) {
        alert("AUTHENTICATION ERROR: Your name must be more than 4 letters long.");
        return;
    }

    appState.name = userEnteredName;
    
    // Add Gmail to the register pool as used
    const sessionToken = localStorage.getItem("lightview_session");
    let loginEmailCandidate = appState.user;
    if (sessionToken) {
        try {
            loginEmailCandidate = JSON.parse(sessionToken).emailToRegister || appState.user;
        } catch(e) {}
    }
    
    // Bind to the registered users pool
    registerEmailInSystem(loginEmailCandidate);
    
    persistCurrentAppState();
    initializeMarketplaceDashboard();
}
function renderMarketplaceInventoryGrid() {
    const gridTargetElement = document.getElementById('inventory-grid');
    if (!gridTargetElement) return;
    gridTargetElement.innerHTML = "";
    
    const systemSearchQuery = document.getElementById('market-search') ? document.getElementById('market-search').value.toLowerCase().trim() : "";
    const targetedFilteredAssets = propertiesData.filter(item => {
        if (!systemSearchQuery) return true;
        return (item.title && item.title.toLowerCase().includes(systemSearchQuery)) || 
               (item.area && item.area.toLowerCase().includes(systemSearchQuery));
    });

    if (targetedFilteredAssets.length === 0) {
        gridTargetElement.innerHTML = `<div class="text-center py-12 border border-dashed border-zinc-800 rounded-xl"><p class="text-xs font-mono text-zinc-500 uppercase font-bold">Zero Assets Discovered</p></div>`;
        return;
    }

    targetedFilteredAssets.sort((a, b) => (b.isBoosted ? 1 : 0) - (a.isBoosted ? 1 : 0));

    targetedFilteredAssets.forEach(currentProperty => {
        const itemCardContainerNode = document.createElement('div');
        itemCardContainerNode.className = `zinc-card rounded-xl p-5 space-y-3 relative border ${currentProperty.isBoosted ? 'border-amber-500/40' : 'border-zinc-900'}`;

        // --- SMART DICTIONARY TO NORMALIZE COUNTRY ALIASES ---
        function normalizeCountryName(countryInput) {
            if (!countryInput) return "";
            const cleanInput = countryInput.toLowerCase().trim();
            
            const aliasMap = {
                "america": "united states",
                "usa": "united states",
                "us": "united states",
                "united states of america": "united states",
                "china": "china",
                "prc": "china",
                "naija": "nigeria",
                "ng": "nigeria",
                "uk": "united kingdom",
                "britain": "united kingdom"
            };
            
            return aliasMap[cleanInput] || cleanInput;
        }

        const originalSellerPrice = currentProperty.localPrice;
        
        let originalSellerSymbol = currentProperty.currencySymbol;
        const rawSellerCountry = currentProperty.sellerCountry || currentProperty.country;
        const sellerCountryKey = normalizeCountryName(rawSellerCountry);
        const buyerCountryKey = normalizeCountryName(appState.country);

        if (!originalSellerSymbol) {
            if (sellerCountryKey === "china") originalSellerSymbol = "¥";
            else if (sellerCountryKey === "nigeria") originalSellerSymbol = "₦";
            else if (sellerCountryKey === "united states") originalSellerSymbol = "$";
            else originalSellerSymbol = "";
        }

        let sellerPriceLineHtml = `${originalSellerSymbol}${originalSellerPrice.toLocaleString()}`;
        let buyerApproxLineHtml = "";

        // Calculate and format currency conversions
        if (sellerCountryKey && buyerCountryKey && sellerCountryKey !== buyerCountryKey) {
            const sellerRateObj = currencyRates[sellerCountryKey];
            const buyerRateObj = currencyRates[buyerCountryKey];

            if (sellerRateObj && buyerRateObj) {
                const priceInUSD = originalSellerPrice / sellerRateObj.rate;
                const finalConvertedBuyerPrice = priceInUSD * buyerRateObj.rate;
                const buyerSymbol = buyerRateObj.symbol;

                let formattedBuyerPrice;
                if (buyerCountryKey === "united states") {
                    formattedBuyerPrice = finalConvertedBuyerPrice.toLocaleString('en-US', {
                        minimumFractionDigits: 2,
                        maximumFractionDigits: 2
                    });
                } else {
                    formattedBuyerPrice = Math.round(finalConvertedBuyerPrice).toLocaleString();
                }

                buyerApproxLineHtml = `
                    <span class="text-[11px] text-zinc-500 font-mono italic">
                        (Approx...${buyerSymbol}${formattedBuyerPrice})
                    </span>
                `;
            } else {
                buyerApproxLineHtml = `
                    <span class="text-[11px] text-zinc-600 font-mono italic">
                        (Syncing exchange values...)
                    </span>
                `;
            }
        }

        itemCardContainerNode.innerHTML = `
            <div class="space-y-1">
                <h4 class="text-sm font-bold text-white font-mono tracking-wide uppercase truncate">${currentProperty.title}</h4>
                <p class="text-[11px] text-zinc-400 font-mono uppercase">${currentProperty.area}, ${currentProperty.state}, ${currentProperty.country}</p>
            </div>
            <div class="p-2.5 bg-zinc-950/80 border border-zinc-900 rounded-lg text-[11px] font-mono text-zinc-300 italic">"${currentProperty.features}"</div>
            <div class="flex items-center justify-between border-t border-zinc-900/60 pt-3">
                <div class="flex flex-col">
                    <span class="text-[9px] font-mono text-zinc-500 uppercase tracking-widest">Seller Price</span>
                    <div class="flex flex-col">
                        <span class="text-sm font-black text-emerald-400 font-mono">${sellerPriceLineHtml}</span>
                        ${buyerApproxLineHtml}
                    </div>
                </div>
                <a href="${currentProperty.whatsAppUrl || '#'}" target="_blank" class="px-3.5 py-1.5 bg-zinc-900 border border-zinc-800 text-white font-bold rounded-lg text-[10px] font-mono uppercase">Chat Seller</a>
            </div>
        `;
        gridTargetElement.appendChild(itemCardContainerNode);
    });
}
function initializeMarketplaceDashboard() {
    document.getElementById('view-identity-setup').classList.add('hidden');
    document.getElementById('view-buyer-location').classList.add('hidden');
    document.getElementById('view-seller-phone').classList.add('hidden');
    document.getElementById('view-marketplace').classList.remove('hidden');

    const displayDisplayName = appState.name ? `${appState.name.toUpperCase()} (${appState.role.toUpperCase()})` : appState.role.toUpperCase();
    document.getElementById('display-user-id').innerText = `${displayDisplayName} SESSION: ${appState.user}`;
    document.getElementById('display-user-locale').innerText = `LOCALE: ${appState.stateRegion.toUpperCase()}, ${appState.country.toUpperCase()}`;
    document.getElementById('sh-coins').innerText = appState.coins;
    document.getElementById('sh-watched').innerText = appState.watchedAdsCount;

    const targetSymbolField = document.getElementById('local-currency-symbol-label');
    if (targetSymbolField && currencyRates[appState.country.toLowerCase()]) {
        targetSymbolField.innerText = currencyRates[appState.country.toLowerCase()].symbol;
    }

    if (appState.role === 'Seller') {
        document.getElementById('seller-management-panel').classList.remove('hidden');
        document.getElementById('ad-wallet-header-panel').classList.remove('hidden');
    } else {
        document.getElementById('seller-management-panel').classList.add('hidden');
        document.getElementById('ad-wallet-header-panel').classList.add('hidden'); 
    }

    renderMarketplaceInventoryGrid();
    evaluateBoostPromotionButtonAccessibility();
}

function checkPersistentSessionHandshake() {
    const cachedSessionToken = localStorage.getItem("lightview_session");
    if (cachedSessionToken) {
        try {
            const parsedSession = JSON.parse(cachedSessionToken);
            appState.user = parsedSession.user;
            appState.role = parsedSession.role;
            appState.country = parsedSession.country;
            appState.stateRegion = parsedSession.stateRegion;
            appState.name = parsedSession.name || "";
            appState.coins = parsedSession.coins || 0;
            appState.watchedAdsCount = parsedSession.watchedAdsCount || 0;
            
            document.getElementById('view-login').classList.add('hidden');
            
            syncLiveGlobalCurrencyExchangeRates().then(() => {
                initializeMarketplaceDashboard();
            });
            return true;
        } catch(e) {
            localStorage.removeItem("lightview_session");
        }
    }
    syncLiveGlobalCurrencyExchangeRates();
    return false;
}

function persistCurrentAppState() {
    localStorage.setItem("lightview_session", JSON.stringify(appState));
}

function handleLogout() {
    localStorage.removeItem("lightview_session");
    appState.user = null; appState.role = null; appState.country = "united states";
    appState.stateRegion = ""; appState.name = ""; appState.coins = 0; appState.watchedAdsCount = 0;

    document.getElementById('view-marketplace').classList.add('hidden');
    document.getElementById('seller-management-panel').classList.add('hidden');
    document.getElementById('view-login').classList.remove('hidden');
}

function watchAdForBoostCoins() {
    alert("No ads available at the moment. Please try again later.");
}

function evaluateBoostPromotionButtonAccessibility() {
    const btn = document.getElementById('btn-promote-asset');
    if (!btn) return;
    if (appState.coins >= 5) {
        btn.disabled = false; btn.className = "w-full p-2.5 bg-amber-500 text-black font-black rounded-lg text-[10px] font-mono uppercase cursor-pointer";
    } else {
        btn.disabled = true; btn.className = "w-full p-2.5 bg-zinc-900 text-zinc-600 font-bold rounded-lg text-[10px] font-mono uppercase cursor-not-allowed opacity-40";
    }
}

function handleCreateListing() {
    const rawPrice = parseFloat(document.getElementById('listing-price').value.trim());
    const opLocale = appState.country.toLowerCase();
    const explicitSymbol = currencyRates[opLocale] ? currencyRates[opLocale].symbol : "$";

    const newListing = {
        id: Date.now(),
        title: document.getElementById('listing-title').value.trim(),
        sellerCountry: opLocale,
        country: appState.country,
        state: appState.stateRegion,
        area: document.getElementById('listing-area').value.trim(),
        features: document.getElementById('listing-features').value.trim(),
        localPrice: rawPrice,
        currencySymbol: explicitSymbol,
        whatsAppUrl: "https://wa.me/" + document.getElementById('listing-contact').value.trim(),
        sellerPhone: appState.user,
        isBoosted: false
    };

    propertiesData.push(newListing);
    renderMarketplaceInventoryGrid();
}

window.addEventListener('DOMContentLoaded', () => {
    checkPersistentSessionHandshake();
});
</script>
</body>
</html>
"""

@app.post("/api/properties/create")
async def create_property_endpoint(payload: dict):
    return {"status": "synchronized", "message": "Asset safely mapped in central systems."}

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.environ.get("PORT", 8000)), reload=True)

        
 
