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
    </style>
</head>
<body class="min-h-screen flex flex-col p-4 max-w-md mx-auto select-none justify-between">
    
    <header class="border-b border-zinc-900 pb-3 flex justify-between items-center">
        <div class="flex items-center gap-2">
            <span class="text-orange-500 font-black tracking-tighter text-xl">LIGHTVIEW</span>
            <span class="text-zinc-500 text-[10px] font-mono mt-1">MARKETPLACE</span>
        </div>
        <div class="flex items-center gap-2">
            <div id="global-translate-element"></div>
            <span class="text-[10px] bg-emerald-950 text-emerald-400 px-2 py-0.5 rounded border border-emerald-900 font-mono">LIVE SYSTEM</span>
        </div>
    </header>
    <main class="flex-1 flex flex-col justify-center my-6">

        <div id="view-login" class="zinc-card rounded-xl p-6 shadow-2xl space-y-4">
            <div class="text-center space-y-1">
                <h3 id="login-title-header" class="text-base font-bold text-white tracking-wide font-mono">ACCESS CENTRAL GATEWAY</h3>
                <p id="login-subtitle" class="text-[11px] text-zinc-500 font-mono">Provide credentials to initialize session link</p>
            </div>
            
            <div id="email-input-group" class="space-y-3">
                <input type="email" id="login-mail" placeholder="ENTER YOUR GMAIL ADDRESS" class="w-full p-3 bg-zinc-950 border border-zinc-900 rounded text-xs text-zinc-300 font-mono focus:outline-none focus:border-zinc-700">
                <input type="password" id="login-pasw" maxlength="4" placeholder="ENTER 4-DIGIT PIN" class="w-full p-3 bg-zinc-950 border border-zinc-900 rounded text-xs text-center font-mono text-white tracking-widest focus:outline-none focus:border-zinc-700">
            </div>

            <button onclick="handleLoginRequest()" class="w-full p-3 bg-orange-600 hover:bg-orange-700 text-white font-bold rounded transition text-sm font-mono">INITIALIZE SECURE ACCESS</button>

            <div id="quick-pin-group" class="hidden space-y-3 p-2 text-center">
                <p class="text-xs text-zinc-400">Welcome Back!<br><span class="text-[10px] text-zinc-600">Enter device hardware PIN to quick session link</span></p>
                <input type="password" id="returning-pin" maxlength="4" placeholder="ENTER QUICK PIN" class="w-full p-3 bg-zinc-950 border border-zinc-900 rounded text-xs text-center font-mono text-white tracking-widest focus:outline-none focus:border-zinc-700">
                <button onclick="handleQuickPinUnlock()" class="w-full p-3 bg-zinc-800 hover:bg-zinc-700 text-white font-bold rounded text-xs font-mono">UNLOCK PROFILE</button>
                <button onclick="handleForgetSession()" class="text-[10px] text-zinc-500 underline block mx-auto mt-2">Clear Profile Session Data</button>
            </div>
        </div>
        <div id="view-role" class="hidden zinc-card rounded-xl p-6 shadow-2xl space-y-4">
            <div class="text-center">
                <h3 class="text-base font-bold text-white tracking-wide">ACCOUNT CLASSIFICATION</h3>
                <p class="text-xs text-zinc-400 mt-1">Are you searching for housing or listing a property asset?</p>
            </div>
            <div class="grid grid-cols-2 gap-3">
                <button onclick="selectRole('Buyer')" class="p-4 bg-zinc-900 hover:bg-zinc-800 border border-zinc-800 rounded-xl text-center text-xs font-bold text-zinc-300 transition">As Buyer / Client</button>
                <button onclick="selectRole('Seller')" class="p-4 bg-zinc-900 hover:bg-zinc-800 border border-zinc-800 rounded-xl text-center text-xs font-bold text-white transition">As Seller / Owner</button>
            </div>
        </div>

        <div id="view-buyer-location" class="hidden zinc-card rounded-xl p-6 shadow-2xl space-y-4">
            <h4 class="text-sm font-bold text-white font-mono">LOCATION MATRIX SETUP</h4>
            <p class="text-xs text-zinc-400">Specify your region to sync local asset currencies.</p>
            <input type="text" id="buyer-country" placeholder="Country (e.g. Nigeria)" class="w-full p-3 bg-zinc-950 border border-zinc-900 rounded text-xs text-white">
            <input type="text" id="buyer-state" placeholder="State / Province" class="w-full p-3 bg-zinc-950 border border-zinc-900 rounded text-xs text-white">
            <button onclick="processBuyerRegistration()" class="w-full p-3 bg-white text-black font-bold rounded text-xs transition">INITIALIZE MARKETPLACE ENTRY</button>
        </div>

        <div id="view-seller-phone" class="hidden zinc-card rounded-xl p-6 shadow-2xl space-y-4">
            <h4 class="text-sm font-bold text-white font-mono">SELLER VERIFICATION</h4>
            <p class="text-xs text-zinc-400">Sellers must authenticate localized telephone metadata parameters before listing.</p>
            <input type="tel" id="seller-phone" placeholder="Phone Number (e.g. +234...)" class="w-full p-3 bg-zinc-950 border border-zinc-900 rounded text-xs text-white font-mono">
            <input type="text" id="seller-country" placeholder="Country (e.g. Nigeria)" class="w-full p-3 bg-zinc-950 border border-zinc-900 rounded text-xs text-white">
            <input type="text" id="seller-state" placeholder="State / Province" class="w-full p-3 bg-zinc-950 border border-zinc-900 rounded text-xs text-white">
            <button onclick="processSellerRegistration()" class="w-full p-3 bg-orange-600 hover:bg-orange-700 text-white font-bold rounded text-xs font-mono">VERIFY SELLER IDENTIFICATION</button>
        </div>
        <div id="view-marketplace" class="hidden space-y-4">
            <div class="flex items-center justify-between border-b border-zinc-900 pb-3">
                <div class="flex flex-col">
                    <span id="display-user-id" class="text-xs text-white font-mono font-bold">ID: ACCOUNT PENDING</span>
                    <span id="display-user-locale" class="text-[10px] text-zinc-500 font-mono">LOCALE: LOCALIZATION ERROR</span>
                </div>
                <button onclick="handleLogout()" class="text-[10px] text-zinc-500 hover:text-orange-400 underline font-mono">LOGOUT PROFILE</button>
            </div>

            <div class="zinc-card rounded-xl p-4 space-y-3">
                <div class="flex justify-between items-center">
                    <span class="text-xs text-zinc-400 font-mono">Coin Wallet Balance:</span>
                    <span class="text-sm font-bold text-orange-400 font-mono"><span id="sh-coins">0</span> COINS</span>
                </div>
                <div class="flex justify-between items-center text-[11px] text-zinc-500 font-mono">
                    <span>Watched Ads Progress:</span>
                    <span><span id="sh-watched">0</span> / 10 ads</span>
                </div>
                <div class="grid grid-cols-2 gap-2">
                    <button onclick="watchAdsForBoost()" class="p-2.5 bg-zinc-900 hover:bg-zinc-800 border border-zinc-800 text-[11px] font-bold text-white rounded transition font-mono flex justify-center items-center gap-1"> Watch Ad Room</button>
                    <button id="btn-promote-asset" class="hidden p-2.5 bg-orange-950/40 hover:bg-orange-900/40 border border-orange-900 text-[11px] font-bold text-orange-400 rounded transition font-mono"> Apply Boost (1 Coin)</button>
                </div>
            </div>

            <div class="flex gap-2">
                <input type="text" id="market-search" oninput="executeInstantSearch()" placeholder="Search assets by city, region or area..." class="w-full p-2.5 bg-zinc-950 border border-zinc-900 rounded-lg text-xs text-zinc-300 focus:outline-none focus:border-zinc-700">
            </div>

            <div class="flex items-center justify-between text-zinc-500 font-mono text-[10px]">
                <span>GLOBAL SYSTEM REGISTER</span>
                <span>REAL ESTATE LISTINGS</span>
            </div>

            <div id="inventory-grid" class="grid grid-cols-1 gap-4"></div>
        </div>
        <div id="seller-management-panel" class="hidden zinc-card rounded-xl p-5 shadow-2xl space-y-4 mt-2">
            <h4 class="text-xs font-bold text-white tracking-wide font-mono text-center border-b border-zinc-900 pb-2">POST NEW REAL ESTATE ASSET</h4>
            <div class="space-y-3">
                <div>
                    <label class="text-[10px] font-mono text-zinc-400 block mb-1">ASSET DESCRIPTION OR NAME</label>
                    <input type="text" id="listing-title" placeholder="e.g. Luxury Duplex Apartment" class="w-full p-2.5 bg-zinc-950 border border-zinc-900 rounded text-xs text-white focus:outline-none">
                </div>
                <div>
                    <label class="text-[10px] font-mono text-zinc-400 block mb-1">LOCATION REGION OR CITY</label>
                    <input type="text" id="listing-area" placeholder="e.g. Ikeja, Lagos" class="w-full p-2.5 bg-zinc-950 border border-zinc-900 rounded text-xs text-white focus:outline-none">
                </div>
                <div>
                    <label class="text-[10px] font-mono text-zinc-400 block mb-1">ASSET VALUATION PRICE (USD $)</label>
                    <input type="number" id="listing-price" placeholder="e.g. 25000" class="w-full p-2.5 bg-zinc-950 border border-zinc-900 rounded text-xs font-mono text-white focus:outline-none">
                </div>
                <button onclick="handleCreateListing()" class="w-full p-3 bg-emerald-600 hover:bg-emerald-700 text-white font-bold rounded text-xs font-mono transition">COMMIT PROPERTY TO GLOBAL INDEX</button>
            </div>
        </div>

    </main>

    <footer class="text-center text-zinc-700 font-mono text-[9px] border-t border-zinc-910 pt-3 mt-4 space-y-1">
        <div>Lightview Real Estate Housing Hub v2.8.1</div>
        <div>Active Allocation Buffer: 512MB / 528MB Free Tier Baseline</div>
   </footer>
<script>
// ============================================================================
// LAYER 1: GLOBAL STATE, LIVE API CURRENCY REGISTRY & STATE BASELINE
// ============================================================================

// 1. Comprehensive Currency Exchange Registry (Fallback Baselines)
let currencyRates = {
    "united states": { symbol: "$", rate: 1.00 },
    "united kingdom": { symbol: "£", rate: 0.79 },
    "eurozone": { symbol: "€", rate: 0.93 },
    "nigeria": { symbol: "₦", rate: 1600.00 },
    "ghana": { symbol: "GH₵", rate: 15.10 },
    "kenya": { symbol: "KSh", rate: 129.50 },
    "south africa": { symbol: "R", rate: 18.20 },
    "canada": { symbol: "C$", rate: 1.37 },
    "australia": { symbol: "A$", rate: 1.51 },
    "india": { symbol: "₹", rate: 83.50 },
    "china": { symbol: "¥", rate: 7.25 },
    "japan": { symbol: "¥", rate: 157.30 },
    "united arab emirates": { symbol: "AED", rate: 3.67 },
    "saudi arabia": { symbol: "SAR", rate: 3.75 },
    "egypt": { symbol: "E£", rate: 47.90 }
};

// 2. Global Runtime Engine State Tracker
let appState = {
    user: null,         
    role: null,         
    country: "united states",
    stateRegion: "",
    coins: 0,           
    adProgress: 0,      
    activeSearch: ""
};

// 3. Clean Slate Production Database (Strictly Zero Pre-loaded Listings)
let propertiesData = [];

// 4. Verification Framework & Live API Stream Fetcher
window.addEventListener('DOMContentLoaded', () => {
    console.log("System Status: Layer 1 Core Interface Assembled Successfully.");
    fetchLiveExchangeRates();
    checkExistingSession();
});

async function fetchLiveExchangeRates() {
    try {
        const response = await fetch('https://open.er-api.com/v6/latest/USD');
        if (!response.ok) throw new Error("API Data Request Halted");
        const data = await response.json();
        const liveRates = data.rates;
        
        // Loop through all predefined keys to update matching structural indices dynamically
        if (liveRates.NGN) currencyRates["nigeria"].rate = liveRates.NGN;
        if (liveRates.GHS) currencyRates["ghana"].rate = liveRates.GHS;
        if (liveRates.KES) currencyRates["kenya"].rate = liveRates.KES;
        if (liveRates.GBP) currencyRates["united kingdom"].rate = liveRates.GBP;
        if (liveRates.EUR) currencyRates["eurozone"].rate = liveRates.EUR;
        if (liveRates.ZAR) currencyRates["south africa"].rate = liveRates.ZAR;
        if (liveRates.CAD) currencyRates["canada"].rate = liveRates.CAD;
        if (liveRates.AUD) currencyRates["australia"].rate = liveRates.AUD;
        if (liveRates.INR) currencyRates["india"].rate = liveRates.INR;
        if (liveRates.AED) currencyRates["united arab emirates"].rate = liveRates.AED;
        
        console.log("System Registry Live Synced.");
    } catch (error) {
        console.warn("API stream unreachable. Defaulting to system fallback matrices.", error);
    }
}

function googleTranslateElementInit() {
    new google.translate.TranslateElement({
        pageLanguage: 'en',
        layout: google.translate.TranslateElement.InlineLayout.SIMPLE
    }, 'global-translate-element');
}
// ============================================================================
// LAYER 2: SESSION PERSISTENCE & GATEWAY SECURITY AUTHENTICATION
// ============================================================================

// 1. Check for Saved Local Memory Session on Page Boot up
function checkExistingSession() {
    const savedUser = localStorage.getItem('lightview_session_user');
    const savedRole = localStorage.getItem('lightview_session_role');
    const savedCountry = localStorage.getItem('lightview_session_country');
    const savedState = localStorage.getItem('lightview_session_state');
    const savedCoins = localStorage.getItem('lightview_session_coins');
    const savedProgress = localStorage.getItem('lightview_session_ad_progress');

    if (savedUser && savedRole) {
        // Hydrate global memory state instantly from local device storage
        appState.user = savedUser;
        appState.role = savedRole;
        appState.country = savedCountry ? savedCountry.toLowerCase() : "united states";
        appState.stateRegion = savedState || "";
        appState.coins = savedCoins ? parseInt(savedCoins) : 0;
        appState.adProgress = savedProgress ? parseInt(savedProgress) : 0;

        // Sync visual UI elements
        document.getElementById('sh-coins').innerText = appState.coins;
        document.getElementById('sh-watched').innerText = appState.adProgress;

        // Bypass gateway screens directly to active marketplace layout panels
        routeSessionToMarketplace();
    } else {
        // No valid data found: Display central gateway login input configurations
        document.getElementById('view-login').classList.remove('hidden');
    }
}

// 2. Main Login Event Request Processor
function handleLoginRequest() {
    const emailInput = document.getElementById('login-mail').value.trim();
    const pinInput = document.getElementById('login-pasw').value.trim();

    // Strict Input Domain Verification Mapping
    if (!emailInput || !emailInput.toLowerCase().includes('@gmail.com')) {
        alert("SECURITY EXCEPTION: Provide a valid authenticated Gmail account address.");
        return;
    }
    if (pinInput.length !== 4 || isNaN(pinInput)) {
        alert("SECURITY EXCEPTION: System authorization PIN must be exactly 4 numerical units.");
        return;
    }

    // Capture baseline identifier matrix fields
    appState.user = emailInput;
    
    // Switch login gateway out and toggle profile role classification display open
    document.getElementById('view-login').classList.add('hidden');
    document.getElementById('view-role').classList.remove('hidden');
}

// 3. Save Active State Arrays into Persistent LocalStorage Matrices
function saveStateToDeviceLocalStorage() {
    localStorage.setItem('lightview_session_user', appState.user);
    localStorage.setItem('lightview_session_role', appState.role);
    localStorage.setItem('lightview_session_country', appState.country);
    localStorage.setItem('lightview_session_state', appState.stateRegion);
    localStorage.setItem('lightview_session_coins', appState.coins);
    localStorage.setItem('lightview_session_ad_progress', appState.adProgress);
}

// 4. Session Destruction Framework (Logout Procedure)
function handleLogout() {
    // Purge local storage blocks
    localStorage.clear();
    
    // Reset runtime configuration track variables
    appState.user = null;
    appState.role = null;
    appState.country = "united states";
    appState.stateRegion = "";
    appState.coins = 0;
    appState.adProgress = 0;

    // Hard reload frame viewport clean slate orientation parameters
    window.location.reload();
}
// ============================================================================
// LAYER 3: ROLE REGISTRATION & STRUCTURAL ROUTING CONTEXT
// ============================================================================

// 1. Assign Role Classification Strategy
function selectRole(chosenRole) {
    appState.role = chosenRole;
    
    // Hide classification panel instantly
    document.getElementById('view-role').classList.add('hidden');
    
    // Route interface to specific demographic form panels
    if (chosenRole === 'Buyer') {
        document.getElementById('view-buyer-location').classList.remove('hidden');
    } else if (chosenRole === 'Seller') {
        document.getElementById('view-seller-phone').classList.remove('hidden');
    }
}

// 2. Process and Validate Buyer Meta Parameters
function processBuyerRegistration() {
    const countryVal = document.getElementById('buyer-country').value.trim().toLowerCase();
    const stateVal = document.getElementById('buyer-state').value.trim();

    if (!countryVal || !stateVal) {
        alert("REGISTRATION FAULT: All location field matrices must be completed.");
        return;
    }

    // Lock parameters into active state arrays
    appState.country = countryVal;
    appState.stateRegion = stateVal;

    // Save session variables and jump into live marketplace layout shell
    saveStateToDeviceLocalStorage();
    routeSessionToMarketplace();
}

// 3. Process and Validate Seller Meta Parameters
function processSellerRegistration() {
    const phoneVal = document.getElementById('seller-phone').value.trim();
    const countryVal = document.getElementById('seller-country').value.trim().toLowerCase();
    const stateVal = document.getElementById('seller-state').value.trim();

    if (!phoneVal || !countryVal || !stateVal) {
        alert("REGISTRATION FAULT: Phone number, country, and state fields are strictly required.");
        return;
    }

    // Lock parameters into active state arrays
    appState.user = phoneVal; // Re-index profile ID parameter using telephone string
    appState.country = countryVal;
    appState.stateRegion = stateVal;

    // Save session variables and jump into live marketplace layout shell
    saveStateToDeviceLocalStorage();
    routeSessionToMarketplace();
}

// 4. Global Structural Interface Router Window Controller
function routeSessionToMarketplace() {
    // Hide all gateway structures completely
    document.getElementById('view-login').classList.add('hidden');
    document.getElementById('view-role').classList.add('hidden');
    document.getElementById('view-buyer-location').classList.add('hidden');
    document.getElementById('view-seller-phone').classList.add('hidden');

    // Sync header demographic data strings
    document.getElementById('display-user-id').innerText = `ID: ${appState.user.toUpperCase()}`;
    document.getElementById('display-user-locale').innerText = `LOCALE: ${appState.stateRegion.toUpperCase()}, ${appState.country.toUpperCase()} (${appState.role.toUpperCase()})`;

    // Reveal main marketplace asset grid shell
    document.getElementById('view-marketplace').classList.remove('hidden');

    // If the account role is a Seller, expose the property submission creator widget panel
    if (appState.role === 'Seller') {
        document.getElementById('seller-management-panel').classList.remove('hidden');
    } else {
        document.getElementById('seller-management-panel').classList.add('hidden');
    }

    // Initialize clean marketplace feed rendering cycle
    renderMarketplaceInventoryGrid();
}
// ============================================================================
// LAYER 4: UNIVERSAL CURRENCY WITH DYNAMIC GRID RENDERER (UPGRADED)
// ============================================================================

function renderMarketplaceInventoryGrid() {
    const gridTarget = document.getElementById('inventory-grid');
    if (!gridTarget) return;

    gridTarget.innerHTML = ""; // Clear existing layout views cleanly
    
    // Read active user search inputs
    const searchQuery = document.getElementById('market-search') ? document.getElementById('market-search').value.toLowerCase().trim() : "";

    // Filter listings based on user query matches
    const filteredAssets = propertiesData.filter(item => {
        const matchesQuery = !searchQuery || 
                             item.title.toLowerCase().includes(searchQuery) || 
                             item.area.toLowerCase().includes(searchQuery) || 
                             item.country.toLowerCase().includes(searchQuery) ||
                             (item.features && item.features.toLowerCase().includes(searchQuery));
        return matchesQuery;
    });

    if (filteredAssets.length === 0) {
        gridTarget.innerHTML = `
            <div class="col-span-full text-center border p-8 border-dashed border-zinc-800 rounded-xl py-12">
                <p class="text-xs font-mono text-zinc-500 uppercase tracking-widest">No matching assets found in global directory</p>
            </div>
        `;
        return;
    }

    // Sort listings: Always push boosted assets to the top of the timeline stream automatically
    filteredAssets.sort((a, b) => (b.isBoosted ? 1 : 0) - (a.isBoosted ? 1 : 0));

    // Loop through properties and print out data-rich listing panels
    filteredAssets.forEach(item => {
        const cardWrapper = document.createElement('div');
        
        // Dynamically style border colors to make premium boosted items stand out
        cardWrapper.className = `zinc-card rounded-xl p-5 shadow-2xl space-y-3 relative transition-all duration-300 ${
            item.isBoosted ? 'border border-amber-500/40 shadow-amber-900/10' : 'border border-zinc-900'
        }`;

        // Fallback display checks to handle missing values elegantly
        const displayFeatures = item.features ? item.features : "Standard Housing Unit Configuration";
        const displaySymbol = item.currencySymbol ? item.currencySymbol : "$";
        const displayPrice = item.localPrice ? item.localPrice.toLocaleString() : item.priceUSD.toLocaleString();

        // Build premium badge indicator conditionally
        let premiumBadgeHtml = "";
        if (item.isBoosted) {
            premiumBadgeHtml = `
                <span class="absolute top-3 right-3 bg-gradient-to-r from-amber-500 to-orange-600 text-black text-[9px] font-black px-2 py-0.5 rounded-md font-mono animate-pulse uppercase tracking-wider">
                    PROMOTED
                </span>
            `;
        }

        // Write fully dynamic structural layout string values
        cardWrapper.innerHTML = `
            ${premiumBadgeHtml}
            
            <div class="space-y-1">
                <h4 class="text-sm font-bold text-white font-mono tracking-wide uppercase truncate pr-16">${item.title}</h4>
                <p class="text-[11px] text-zinc-400 font-mono flex items-center gap-1">
                    <span class="text-emerald-500"></span> ${item.area.toUpperCase()}, ${item.state.toUpperCase()}, ${item.country.toUpperCase()}
                </p>
            </div>

            <div class="p-2.5 bg-zinc-950/60 border border-zinc-900/60 rounded-lg text-[11px] font-mono text-zinc-400 space-y-1">
                <span class="text-[9px] text-zinc-600 uppercase font-bold tracking-wider block">Property Specifications:</span>
                <p class="text-zinc-300 italic">"${displayFeatures}"</p>
            </div>

            <div class="flex items-center justify-between border-t border-zinc-900 pt-3">
                <div>
                    <span class="text-[9px] font-mono text-zinc-500 block uppercase tracking-widest">Valuation Price</span>
                    <span class="text-sm font-black text-emerald-400 font-mono">${displaySymbol}${displayPrice}</span>
                </div>
                
                <a href="${item.whatsAppUrl || '#'}" target="_blank" class="px-3.5 py-1.5 bg-zinc-900 hover:bg-emerald-600 border border-zinc-800 hover:border-emerald-500 text-white hover:text-white font-bold rounded-lg text-[10px] tracking-wider font-mono transition-all duration-200 uppercase flex items-center gap-1.5 shadow-md">
                    <span></span> Chat Seller
                </a>
            </div>
        `;

        gridTarget.appendChild(cardWrapper);
    });
}

// ============================================================================
// LAYER 5: AD ROOM WATCHING & COIN MINTING ENGINE
// ============================================================================

// 1. Core Ad Simulation Room Triggers
function watchAdsForBoost() {
    // Generate a sleek modal overlay box covering the mobile screen viewport completely
    const adOverlay = document.createElement('div');
    adOverlay.id = "ad-simulation-overlay";
    adOverlay.className = "fixed inset-0 bg-black z-50 flex flex-col justify-center items-center p-6 text-center select-none";
    
    // Pick a random product ad topic to simulate live networks
    const adPool = [
        "Lightview Premium AI Chip Hosting Node Cluster",
        "Apex Global Properties Tokenized Real Estate Funds",
        "Xia Custom Native Operating System Hardware Matrix",
        "BoostCoin Verified Direct Traffic Advertising Network"
    ];
    const chosenAdText = adPool[Math.floor(Math.random() * adPool.length)];

    adOverlay.innerHTML = `
        <div class="space-y-6 max-w-xs font-mono">
            <div class="text-orange-500 font-black tracking-tighter text-2xl animate-pulse">LIGHTVIEW AD LINK</div>
            <div class="p-4 border border-zinc-900 rounded-xl bg-zinc-950 text-xs text-zinc-400 leading-relaxed">
                <span class="text-white block font-bold mb-2">SPONSORED ASSIGNMENT:</span>
                "${chosenAdText}"
            </div>
            <div id="ad-countdown-timer" class="text-sm font-bold text-white tracking-widest bg-zinc-900 px-4 py-2.5 rounded-lg border border-zinc-800">
                LOCK TIMEOUT: 3s
            </div>
            <p class="text-[10px] text-zinc-600">Coin token rewards will distribute securely once internal timer cycles fully clear.</p>
        </div>
    `;

    document.body.appendChild(adOverlay);

    // Initialize 3-Second Secure Timer Loop
    let secondsLeft = 3;
    const timerInterval = setInterval(() => {
        secondsLeft--;
        const timerUI = document.getElementById('ad-countdown-timer');
        
        if (timerUI) {
            timerUI.innerText = `LOCK TIMEOUT: ${secondsLeft}s`;
        }

        if (secondsLeft <= 0) {
            clearInterval(timerInterval);
            // Destroy ad panel room viewport element cleanly
            document.body.removeChild(adOverlay);
            // Process the view tick increment execution routing
            creditUserAdProgressRecord();
        }
    }, 1000);
}

// 2. Process Count Increments & Mint Earned Coins Safely
function creditUserAdProgressRecord() {
    appState.adProgress++;

    // System logic check: Has user accumulated 10 complete ad room cycles?
    if (appState.adProgress >= 10) {
        appState.adProgress = 0; // Reset counter back to zero threshold
        appState.coins++;        // Mint exactly 1 Boost Coin token into balance
        alert("TRANSACTION SUCCESS: 10/10 Ads Completed! 1 Boost Coin has been successfully minted to your Wallet balance.");
    } else {
        // Simple visual system toast alert tracking current balance
        alert(`AD VERIFIED: Progress tracker logged (${appState.adProgress} / 10). Watch more ads to generate your next Boost Coin!`);
    }

    // Update screen UI values instantly
    document.getElementById('sh-coins').innerText = appState.coins;
    document.getElementById('sh-watched').innerText = appState.adProgress;

    // Check if the property promotion trigger buttons should alter visibility rules
    evaluateBoostPromotionButtonAccessibility();

    // Commit new balance records safely to device local cache storage
    saveStateToDeviceLocalStorage();
}
// ============================================================================
// LAYER 6: LIVE ASSET PROMOTION & GLOBAL SORTING ENGINE
// ============================================================================

// 1. Evaluate Button Accessibility for Promoting Items
function evaluateBoostPromotionButtonAccessibility() {
    const promoteBtn = document.getElementById('btn-promote-asset');
    if (!promoteBtn) return;

    // Only show promote button configurations if user is a Seller and possesses at least 1 coin
    if (appState.role === 'Seller' && appState.coins >= 1) {
        promoteBtn.classList.remove('hidden');
    } else {
        promoteBtn.classList.add('hidden');
    }
}

// 2. Main Executive Trigger: Apply Boost Token and Sync across the Network
function applyBoostTokenToAsset(propertyId) {
    if (appState.coins < 1) {
        alert("TRANSACTION ERROR: Insufficient coin balance. Watch more ads to generate system tokens.");
        return;
    }

    // Find the asset locally first to update the UI instantly
    const targetProperty = propertiesData.find(item => item.id === propertyId);
    
    if (targetProperty) {
        if (targetProperty.isBoosted) {
            alert("SYSTEM NOTICE: This real estate asset has already been boosted to maximum visibility.");
            return;
        }

        // Deduct coin balance
        appState.coins--;
        targetProperty.isBoosted = true;

        // ==========================================
        // NETWORK UPDATE: Tell the backend to boost it globally
        // ==========================================
        fetch('/api/properties/boost', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ id: propertyId })
        })
        .then(res => res.json())
        .then(data => {
            console.log("Global Boost Status:", data.message);
            alert(`PROMOTION SUCCESS: "${targetProperty.title.toUpperCase()}" has been boosted globally!`);
        })
        .catch(err => {
            console.error("Network boost synchronization failed:", err);
        });

        // Update UI panels instantly
        document.getElementById('sh-coins').innerText = appState.coins;
        
        evaluateBoostPromotionButtonAccessibility();
        renderMarketplaceInventoryGrid();
        saveStateToDeviceLocalStorage(); // Keeps user account session and coins saved locally
    } else {
        alert("CRITICAL ERROR: Selected property item index could not be located in system register.");
    }
}
// ============================================================================
// LAYER 7: FORCED STRUCTURAL PROPERTY ASSET CREATOR & SYNC ENGINE
// ============================================================================

function handleCreateListing() {
    console.log("Initializing Property Submission Engine...");

    // 1. Safe DOM Element Fetching with Fallbacks to prevent silent null crashes
    const elTitle = document.getElementById('listing-title');
    const elArea = document.getElementById('listing-area');
    const elFeatures = document.getElementById('listing-features');
    const elPrice = document.getElementById('listing-price');
    const elContact = document.getElementById('listing-contact');

    if (!elTitle || !elArea || !elFeatures || !elPrice || !elContact) {
        console.error("DOM Error: One or more input elements are missing from the HTML structure.");
        alert("APPLICATION FAULT: Form elements could not be found. Please refresh the page.");
        return;
    }

    const titleInput = elTitle.value.trim();
    const areaInput = elArea.value.trim();
    const featuresInput = elFeatures.value.trim();
    const priceInput = parseFloat(elPrice.value.trim());
    const contactInput = elContact.value.trim();

    // 2. Strict Input Validation Constraints
    if (!titleInput || !areaInput || !featuresInput || isNaN(priceInput) || priceInput <= 0 || !contactInput) {
        alert("CREATION FAULT: All structural fields (Title, Area, Amenities, Price, and Contact Number) are strictly required.");
        return;
    }

    const targetCountry = appState.country || "united states";
    const targetState = appState.stateRegion || "";
    const sellerPhoneNum = appState.user || "unknown";
    const currentLocale = targetCountry.toLowerCase();

    // 3. Dynamic Currency Mapping Engine
    let basePriceInUSD = priceInput;
    let displaySymbol = "$";

    if (typeof currencyRates !== 'undefined' && currencyRates[currentLocale]) {
        const conversionRate = currencyRates[currentLocale].rate;
        displaySymbol = currencyRates[currentLocale].symbol;
        basePriceInUSD = priceInput / conversionRate; 
    }

    // 4. Safe Python-Compatible String Manipulation (Strips spaces and plus signs)
    const cleanPhoneDigits = contactInput.split(' ').join('').split('+').join(''); 
    const whatsAppDirectUrl = "https://wa.me/" + cleanPhoneDigits;

    // 5. Build Final Structural Listing Asset Object
    const uniquePropertyAsset = {
        id: Date.now(),
        title: titleInput,
        country: targetCountry,
        state: targetState,
        area: areaInput,
        features: featuresInput,
        localPrice: priceInput,
        currencySymbol: displaySymbol,
        priceUSD: basePriceInUSD,
        contactPhone: contactInput,
        whatsAppUrl: whatsAppDirectUrl,
        sellerPhone: sellerPhoneNum,
        isBoosted: false
    };

    console.log("Pushing created asset to local tracking storage:", uniquePropertyAsset);
    
    if (typeof propertiesData !== 'undefined') {
        propertiesData.push(uniquePropertyAsset);
    }

    // 6. Network Database Sync Gateway
    fetch('/api/properties/create', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(uniquePropertyAsset)
    })
    .then(res => res.json())
    .then(data => {
        console.log("Global System Server Sync Response:", data);
        alert("ASSET REGISTRATION SUCCESS: committed to live index!");
    })
    .catch(err => {
        console.error("Critical Network Sync Error:", err);
    });

    // Clean form elements out safely
    elTitle.value = "";
    elArea.value = "";
    elFeatures.value = "";
    elPrice.value = "";
    elContact.value = "";

    // Refresh UI display panels
    if (typeof renderMarketplaceInventoryGrid === "function") {
        renderMarketplaceInventoryGrid();
    }
}

// ============================================================================
// LAYER 8: LIVE GLOBAL MARKETPLACE SYNC ENGINE
// ============================================================================

// 1. Live Server Data Downloader Pipeline
function synchronizeMarketplaceDatabaseWithServer() {
    // Request the global shared house listings matrix from your Python backend
    fetch('/api/properties/stream')
    .then(response => {
        if (!response.ok) throw new Error("Server Database Unreachable");
        return response.json();
    })
    .then(serverData => {
        // Sync our local array directly with the live global database array
        propertiesData = serverData;
        
        // Re-render the visual display cards for the user instantly
        renderMarketplaceInventoryGrid();
    })
    .catch(error => {
        console.error("Network Stream Fault: Could not fetch central database assets.", error);
    });
}

// 2. Inject Stream Synchronization into App Initialization
// This completely updates the old local storage initialization rule from earlier
window.addEventListener('DOMContentLoaded', () => {
    // 1. Instantly pull down live properties posted by anyone globally
    synchronizeMarketplaceDatabaseWithServer();
    
    // 2. Set up an automatic background polling refresh every 10 seconds 
    // This makes sure buyers see new listings without manually reloading the app
    setInterval(synchronizeMarketplaceDatabaseWithServer, 10000);
});

</script>


</body>
</html>
"""
        
from fastapi import Request
import json

# Global storage list held inside your server memory
SERVER_PROPERTIES_DATABASE = []

@app.post("/api/properties/create")
async def backend_save_property(request: Request):
    global SERVER_PROPERTIES_DATABASE
    data = await request.json()
    SERVER_PROPERTIES_DATABASE.append(data)
    return {"status": "SUCCESS", "message": "Asset locked to global server matrix"}

@app.get("/api/properties/stream")
def backend_stream_properties():
    global SERVER_PROPERTIES_DATABASE
    return SERVER_PROPERTIES_DATABASE

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
    
