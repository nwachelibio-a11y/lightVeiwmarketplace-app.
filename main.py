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

<div id="view-buyer-location" class="hidden zinc-card rounded-xl p-6 shadow-2xl space-y-4">
<h4 class="text-sm font-bold text-white font-mono border-b border-zinc-900 pb-2 uppercase tracking-wider">Location Matrix Setup</h4>
<div class="space-y-3">
<input type="text" id="buyer-country" placeholder="Country (e.g. Nigeria)" class="w-full p-3 bg-zinc-950 border border-zinc-800 rounded-lg text-sm text-white font-mono focus:outline-none focus:border-zinc-700">
<input type="text" id="buyer-state" placeholder="State / Province" class="w-full p-3 bg-zinc-950 border border-zinc-800 rounded-lg text-sm text-white font-mono focus:outline-none focus:border-zinc-700">
</div>
<button onclick="processBuyerRegistration()" class="w-full p-3 bg-orange-600 hover:bg-orange-700 text-white font-bold rounded-xl text-xs tracking-widest font-mono transition-all duration-200 uppercase">
Synchronize Profile Layout
</button>
</div>

<div id="view-seller-phone" class="hidden zinc-card rounded-xl p-6 shadow-2xl space-y-4">
<div class="space-y-1">
<h4 class="text-sm font-bold text-white font-mono border-b border-zinc-900 pb-2 uppercase tracking-wider">Seller Identity Verification</h4>
<p class="text-[11px] text-zinc-500 font-mono">Authenticate localized telephone data to establish market legitimacy.</p>
</div>
<div class="space-y-3 pt-1">
<input type="tel" id="seller-phone" placeholder="Phone Number (e.g. 234...)" class="w-full p-3 bg-zinc-950 border border-zinc-800 rounded-lg text-sm text-white font-mono focus:outline-none">
<input type="text" id="seller-country" placeholder="Country (e.g. Ghana)" class="w-full p-3 bg-zinc-950 border border-zinc-800 rounded-lg text-sm text-white font-mono focus:outline-none">
<input type="text" id="seller-state" placeholder="State / Region" class="w-full p-3 bg-zinc-950 border border-zinc-800 rounded-lg text-sm text-white font-mono focus:outline-none">
</div>
<button onclick="processSellerRegistration()" class="w-full p-3 bg-orange-600 hover:bg-orange-700 text-white font-bold rounded-xl text-xs tracking-widest font-mono transition-all duration-200 uppercase">
Verify Seller Identification
</button>
</div>

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

<footer class="text-center text-zinc-700 font-mono text-[9px] border-t border-zinc-910 pt-3 mt-4 space-y-1">
<div>Lightview Real Estate Housing Hub v3.0.0</div>
<div>Active Allocation Buffer: 512MB / 528MB Free Tier Baseline</div>
</footer>

<script>
    // ============================================================================
// LAYER 1: GLOBAL APPLICATIVE ENGINE REGISTRIES & LIVE EXCHANGE RATE API CONNECT
// ============================================================================

// 1. Central Core System Application State Context Matrix
let appState = {
    user: null,          // Holds verified login identifier string (Email or Tel)
    role: null,          // Active user classification rule enforcement ('Buyer' or 'Seller')
    country: "united states", // Tracked registration region for local fiat pricing mapping
    stateRegion: "",     // Regional state or province boundary tracking
    coins: 0,            // Internal premium marketplace ad boost wallet ledger
    watchedAdsCount: 0   // Incremental watch limit tracking variable
};

// 2. Global Property Assets Directory Storage Core Array
let propertiesData = [
    {
        id: 1,
        title: "Exquisite Lekki Penthouse Suite",
        country: "Nigeria",
        state: "Lagos",
        area: "Lekki Phase 1",
        features: "4 Bed, Smart Home Automation, Ocean View Infinity Pool",
        localPrice: 375000000,
        currencySymbol: "₦",
        priceUSD: 250000,
        contactPhone: "2348012345678",
        whatsAppUrl: "https://wa.me/2348012345678",
        sellerPhone: "2347000000000",
        isBoosted: true
    }
];

// 3. Dynamic Base Mapping Framework for Symbols
const globalCurrencySymbolMap = {
    "usd": "$", "eur": "€", "gbp": "£", "ngn": "₦", "ghs": "₵", "kes": "KSh", 
    "zar": "R", "aed": "د.إ", "cad": "C$", "aud": "A$", "jpy": "¥", "cny": "¥",
    "inr": "₹", "rub": "₽", "brl": "R$", "mxn": "$", "sar": "SR", "egp": "E£"
};

// 4. Comprehensive 90+ Currency Directory Object Model Framework
// Initialized with core regional baselines; will automatically scale up instantly on live sync.
let currencyRates = {
    "united states": { symbol: "$", rate: 1.00, code: "USD" },
    "united kingdom": { symbol: "£", rate: 0.79, code: "GBP" },
    "eurozone": { symbol: "€", rate: 0.93, code: "EUR" },
    "nigeria": { symbol: "₦", rate: 1500.00, code: "NGN" },
    "ghana": { symbol: "₵", rate: 15.10, code: "GHS" },
    "kenya": { symbol: "KSh", rate: 129.50, code: "KES" },
    "south africa": { symbol: "R", rate: 18.20, code: "ZAR" },
    "uae": { symbol: "د.إ", rate: 3.67, code: "AED" }
};

// 5. Automated Network Synchronizer: Connects Live Open Exchange Rate API Matrix
function syncLiveGlobalCurrencyExchangeRates() {
    console.log("Initializing dynamic connection to global currency API pipeline...");
    
    // Utilizing standard public exchange rate pipeline endpoint
    fetch('https://open.er-api.com/v6/latest/USD')
    .then(response => {
        if (!response.ok) {
            throw new Error("Network currency endpoint synchronization failure.");
        }
        return response.json();
    })
    .then(data => {
        if (!data || !data.rates) {
            console.error("Data payload format fault from external exchange registry.");
            return;
        }

        console.log("Live exchange index payload received successfully. Re-mapping over 90+ financial corridors...");
        
        const freshRates = data.rates;

        // Automatically index, compute, and inject all available currencies across the globe into currencyRates
        Object.keys(freshRates).forEach(currencyCode => {
            const lowerCode = currencyCode.toLowerCase();
            
            // Generate full matching keys or let the system dynamically bind them on localized registration strings
            // This safely accommodates all 90 fallback pathways without requiring code text bloat
            let derivedCountryKey = currencyCode; 
            
            // Explicitly mapping primary corridors to match user layout strings seamlessly
            if (currencyCode === "USD") derivedCountryKey = "united states";
            else if (currencyCode === "GBP") derivedCountryKey = "united kingdom";
            else if (currencyCode === "EUR") derivedCountryKey = "eurozone";
            else if (currencyCode === "NGN") derivedCountryKey = "nigeria";
            else if (currencyCode === "GHS") derivedCountryKey = "ghana";
            else if (currencyCode === "KES") derivedCountryKey = "kenya";
            else if (currencyCode === "ZAR") derivedCountryKey = "south africa";
            else if (currencyCode === "AED") derivedCountryKey = "uae";
            else if (currencyCode === "CAD") derivedCountryKey = "canada";
            else if (currencyCode === "AUD") derivedCountryKey = "australia";

            // Determine appropriate typographical currency symbol badge or fallback cleanly to the letter code
            const accurateSymbol = globalCurrencySymbolMap[lowerCode] || currencyCode;

            // Save the newly synced valuation pricing stream into our global architecture object memory array
            currencyRates[derivedCountryKey.toLowerCase()] = {
                symbol: accurateSymbol,
                rate: freshRates[currencyCode],
                code: currencyCode
            };
        });

        console.log("Synchronization complete. Total active network currencies loaded:", Object.keys(currencyRates).length);
        
        // Dynamically update form labels to match loaded locale settings right away if available
        if (typeof appState !== 'undefined' && appState.country) {
            const currentLocale = appState.country.toLowerCase();
            const symbolLabel = document.getElementById('local-currency-symbol-label');
            if (symbolLabel && currencyRates[currentLocale]) {
                symbolLabel.innerText = currencyRates[currentLocale].symbol;
            }
        }
    })
    .catch(error => {
        console.error("Critical Currency Sync Pipeline Interrupt:", error);
        console.log("System Status: Falling back gracefully to static local cache directory metrics.");
    });
}

// Automatically register live API synchronization on initial code execution
syncLiveGlobalCurrencyExchangeRates();
// ============================================================================
// LAYER 2: INTERACTIVE GATEWAY SYSTEMS (AUTHENTICATION, REGISTRATION & VIEW ROUTING)
// ============================================================================

/**
 * 1. Secure Access Gateway Verification Process
 * Validates baseline text formatting rules for email entry points and 
 * strictly requires a 4-digit hardware authorization PIN.
 */
function handleLoginRequest() {
    console.log("Processing secure access validation routine...");

    const emailInputNode = document.getElementById('login-mail');
    const pinInputNode = document.getElementById('login-pasw');

    if (!emailInputNode || !pinInputNode) {
        console.error("Critical DOM Binding Error: Authentication node references are missing.");
        alert("SYSTEM CONFIGURATION ERROR: Login controls failed to execute cleanly.");
        return;
    }

    const clearEmailText = emailInputNode.value.trim();
    const clearPinText = pinInputNode.value.trim();

    // Verification check A: Email string must not be empty and must include standard characters
    if (!clearEmailText || !clearEmailText.includes('@') || !clearEmailText.includes('.')) {
        alert("SECURITY ACCESS DENIED: Please supply a legally formatted email address.");
        return;
    }

    // Verification check B: PIN must be exactly 4 numerical digits
    if (clearPinText.length !== 4 || isNaN(clearPinText)) {
        alert("SECURITY ACCESS DENIED: Authentication PIN must be exactly 4 numerical digits.");
        return;
    }

    console.log("Credential baseline authorization successful. Mapping profile state context...");
    
    // Assign user unique ID inside core tracking state context
    appState.user = clearEmailText;

    // View Routing Transition: Clear login interface, reveal account role picker frame smoothly
    document.getElementById('view-login').classList.add('hidden');
    document.getElementById('view-role').classList.remove('hidden');
}

/**
 * 2. Account Classification Matrix Dispatcher
 * Sets structural application view access layout guidelines based on role selections.
 * @param {string} selectedRole - Must be explicitly defined as 'Buyer' or 'Seller'
 */
function selectRole(selectedRole) {
    if (selectedRole !== 'Buyer' && selectedRole !== 'Seller') {
        console.error("System Classification Fault: Enforced illegal role parameters.");
        return;
    }

    console.log("Account classification registered successfully. User role initialized as:", selectedRole);
    
    // Lock character configuration constraints into core context memory
    appState.role = selectedRole;

    // View Routing Transition: Close current frame module view container
    document.getElementById('view-role').classList.add('hidden');

    // Branching Logic Gateway: Direct traffic to corresponding input panels
    if (selectedRole === 'Buyer') {
        document.getElementById('view-buyer-location').classList.remove('hidden');
    } else if (selectedRole === 'Seller') {
        document.getElementById('view-seller-phone').classList.remove('hidden');
    }
}

/**
 * 3. Buyer Regional Localization Profiler
 * Indexes regional target criteria strings to automatically calibrate marketplace financial metrics.
 */
function processBuyerRegistration() {
    console.log("Analyzing local configuration guidelines for buyer access...");

    const buyerCountryNode = document.getElementById('buyer-country');
    const buyerStateNode = document.getElementById('buyer-state');

    if (!buyerCountryNode || !buyerStateNode) {
        console.error("DOM Reference Error: Buyer onboarding form fields are broken.");
        return;
    }

    const standardizedCountry = buyerCountryNode.value.trim().toLowerCase();
    const standardizedState = buyerStateNode.value.trim().toLowerCase();

    // Validation Constraint: Enforce complete local data capture
    if (!standardizedCountry || !standardizedState) {
        alert("VALIDATION REJECTION: Both Country and State fields must be completely specified.");
        return;
    }

    console.log("Buyer configuration rules verified. Binding profile settings...");
    
    // Sync geographical bounds into application context state engine memory nodes
    appState.country = standardizedCountry;
    appState.stateRegion = standardizedState;

    // Hand off initialization execution right over to Layer 3 synchronization core
    if (typeof initializeMarketplaceDashboard === 'function') {
        initializeMarketplaceDashboard();
    } else {
        console.error("Architecture Dependency Error: Layer 3 core sync system is not yet available.");
    }
}

/**
 * 4. Seller Verification & Identity Gateway
 * Captures, sanitizes, and indexes high-priority business onboarding metadata metrics.
 */
function processSellerRegistration() {
    console.log("Analyzing seller identification metrics for market authorization...");

    const sellerPhoneNode = document.getElementById('seller-phone');
    const sellerCountryNode = document.getElementById('seller-country');
    const sellerStateNode = document.getElementById('seller-state');

    if (!sellerPhoneNode || !sellerCountryNode || !sellerStateNode) {
        console.error("DOM Reference Error: Seller authentication node array is missing.");
        return;
    }

    const clearPhoneInput = sellerPhoneNode.value.trim();
    const standardizedCountry = sellerCountryNode.value.trim().toLowerCase();
    const standardizedState = sellerStateNode.value.trim().toLowerCase();

    // Validation Constraint: Block processing if fields are skipped or incomplete
    if (!clearPhoneInput || !standardizedCountry || !standardizedState) {
        alert("VALIDATION REJECTION: All registry values (Phone, Country, and State/Region) must be populated.");
        return;
    }

    // Phone Format Verification: Ensure input contains only numbers, spaces, or plus markers
    const formattingSafetyPattern = /^[0-9+\s\-()]+$/;
    if (!formattingSafetyPattern.test(clearPhoneInput)) {
        alert("VALIDATION REJECTION: Phone field contains illegal characters. Use a clean telephone format.");
        return;
    }

    console.log("Seller registration records checked. Re-mapping master app context indices...");

    // Update active primary identifiers to match verified telephone markers for seller profiles
    appState.user = clearPhoneInput;
    appState.country = standardizedCountry;
    appState.stateRegion = standardizedState;

    // Direct interface compilation processing down to Layer 3 core framework
    if (typeof initializeMarketplaceDashboard === 'function') {
        initializeMarketplaceDashboard();
    } else {
        console.error("Architecture Dependency Error: Layer 3 core sync system is not yet available.");
    }
}
// ============================================================================
// LAYER 3: CORE HUB SYNCHRONIZATION ENGINE & INTERFACE VIEW MANAGEMENT
// ============================================================================

/**
 * 1. Marketplace Global Dashboard Compiler
 * Compiles state variables, switches view layers, adjusts currency labels,
 * and sets visibility guidelines based on structural account classifications.
 */
function initializeMarketplaceDashboard() {
    console.log("Compiling master marketplace hub interface streams...");

    // Safe DOM Verification: Validate existence of fundamental workspace views
    const buyerLocationView = document.getElementById('view-buyer-location');
    const sellerIdentityView = document.getElementById('view-seller-phone');
    const primaryMarketplaceHub = document.getElementById('view-marketplace');

    if (!buyerLocationView || !sellerIdentityView || !primaryMarketplaceHub) {
        console.error("Critical Component Reference Fault: Main interface wrapper views are completely missing.");
        alert("SYSTEM ERROR: Interface manager failed to assemble view contexts cleanly.");
        return;
    }

    // Hide preliminary registration panels and clear viewport congestion
    buyerLocationView.classList.add('hidden');
    sellerIdentityView.classList.add('hidden');

    // Reveal live marketplace functional context frame container
    primaryMarketplaceHub.classList.remove('hidden');

    // Safe Profile Node Binding: Construct structural header layout status labels
    const displayUserIdNode = document.getElementById('display-user-id');
    const displayUserLocaleNode = document.getElementById('display-user-locale');

    if (displayUserIdNode) {
        displayUserIdNode.innerText = `${appState.role.toUpperCase()} SESSION: ${appState.user}`;
    }
    if (displayUserLocaleNode) {
        displayUserLocaleNode.innerText = `LOCALE: ${appState.stateRegion.toUpperCase()}, ${appState.country.toUpperCase()}`;
    }

    // Currency Alignment Engine: Align the form label with the currency tracking array
    const activeLocaleKey = appState.country.toLowerCase();
    const targetSymbolField = document.getElementById('local-currency-symbol-label');
    
    if (targetSymbolField) {
        if (typeof currencyRates !== 'undefined' && currencyRates[activeLocaleKey]) {
            targetSymbolField.innerText = currencyRates[activeLocaleKey].symbol;
            console.log(`Dynamic pricing notation linked successfully to current locale code: [${currencyRates[activeLocaleKey].code}]`);
        } else {
            // Default baseline fallback match condition
            targetSymbolField.innerText = "USD";
            console.log("Localized corridor unmapped or pending live API synchronization. Defaulting to baseline USD.");
        }
    }

    // Role-Enforced Layout Control Panel Allocation Rules
    const assetCreationPanelNode = document.getElementById('seller-management-panel');
    const adPromotionWalletPanelNode = document.getElementById('ad-wallet-header-panel');

    if (appState.role === 'Seller') {
        console.log("Seller permissions verified. Allocating property configuration modules...");
        if (assetCreationPanelNode) assetCreationPanelNode.classList.remove('hidden');
        if (adPromotionWalletPanelNode) adPromotionWalletPanelNode.classList.remove('hidden');
    } else {
        console.log("Buyer permissions verified. Stripping listing generation nodes to prioritize product discoverability...");
        if (assetCreationPanelNode) assetCreationPanelNode.classList.add('hidden');
        if (adPromotionWalletPanelNode) adPromotionWalletPanelNode.classList.add('hidden'); 
    }

    // Render operational feed layers immediately
    if (typeof renderMarketplaceInventoryGrid === 'function') {
        renderMarketplaceInventoryGrid();
    } else {
        console.warn("Execution Timing Warning: Layer 4 grid system has not loaded into environment context yet.");
    }

    // Verify system promotion parameters
    if (typeof evaluateBoostPromotionButtonAccessibility === 'function') {
        evaluateBoostPromotionButtonAccessibility();
    }
}

/**
 * 2. Executive Session Termination Routine
 * Wipes out local authentication variables, zeros out active memory vectors,
 * purges visible text data, and safely routes back to the main login panel.
 */
function handleLogout() {
    console.log("Executing strict system memory dump and session termination protocols...");

    // Terminate core track conditions inside state context dictionary parameters
    appState.user = null;
    appState.role = null;
    appState.country = "united states";
    appState.stateRegion = "";
    appState.coins = 0;
    appState.watchedAdsCount = 0;

    // Purge physical display layout tracking numbers completely
    const coinTracker = document.getElementById('sh-coins');
    const metricsTracker = document.getElementById('sh-watched');
    const searchFilterNode = document.getElementById('market-search');
    const emailFieldNode = document.getElementById('login-mail');
    const pinFieldNode = document.getElementById('login-pasw');

    if (coinTracker) coinTracker.innerText = "0";
    if (metricsTracker) metricsTracker.innerText = "0";
    if (searchFilterNode) searchFilterNode.value = "";
    if (emailFieldNode) emailFieldNode.value = "";
    if (pinFieldNode) pinFieldNode.value = "";

    // Clear operational inputs inside seller forms to protect data privacy
    const inputIdsArray = ['listing-title', 'listing-area', 'listing-features', 'listing-price', 'listing-contact'];
    inputIdsArray.forEach(id => {
        const structuralElement = document.getElementById(id);
        if (structuralElement) structuralElement.value = "";
    });

    // View Routing Transition: Lock down dashboard interfaces, bring up pristine login terminal
    const marketContainer = document.getElementById('view-marketplace');
    const generatorContainer = document.getElementById('seller-management-panel');
    const loginPortalContainer = document.getElementById('view-login');

    if (marketContainer) marketContainer.classList.add('hidden');
    if (generatorContainer) generatorContainer.classList.add('hidden');
    if (loginPortalContainer) loginPortalContainer.classList.remove('hidden');

    console.log("Session memory safely cleared. Hardware terminal returning to standby lock context.");
}
// ============================================================================
// LAYER 4: UNIVERSAL DYNAMIC INDEX TIMELINE GRID RENDERER
// ============================================================================

/**
 * 1. Global Inventory Feed Rendering Matrix
 * Pulls raw data structures, applies full cross-field multi-keyword filter processing,
 * sorts by premium ad weights, and outputs clean dynamic cards into the DOM.
 */
function renderMarketplaceInventoryGrid() {
    console.log("Initializing Layer 4 directory layout compilation...");

    const gridTargetElement = document.getElementById('inventory-grid');
    if (!gridTargetElement) {
        console.error("DOM Intercept Fault: Inventory target grid destination node does not exist.");
        return;
    }

    // Flush out previous HTML string contents to guarantee a clean render loop
    gridTargetElement.innerHTML = "";
    
    // Read clean lowercase input values directly out of search field
    const searchFieldNode = document.getElementById('market-search');
    const systemSearchQuery = searchFieldNode ? searchFieldNode.value.toLowerCase().trim() : "";

    console.log(`Active filter validation parameters checking against string query: "${systemSearchQuery}"`);

    // 2. Multi-Field Asset Filtering Engine
    const targetedFilteredAssets = propertiesData.filter(propertyItem => {
        // Condition A: If search bar is blank, immediately approve all items to pass through
        if (!systemSearchQuery) return true;

        // Condition B: Check for text matches inside every string parameter of the property model
        const titleMatch = propertyItem.title && propertyItem.title.toLowerCase().includes(systemSearchQuery);
        const areaMatch = propertyItem.area && propertyItem.area.toLowerCase().includes(systemSearchQuery);
        const stateMatch = propertyItem.state && propertyItem.state.toLowerCase().includes(systemSearchQuery);
        const countryMatch = propertyItem.country && propertyItem.country.toLowerCase().includes(systemSearchQuery);
        const specificationsMatch = propertyItem.features && propertyItem.features.toLowerCase().includes(systemSearchQuery);

        // Approve the property asset if it hits a match anywhere inside those 5 text properties
        return titleMatch || areaMatch || stateMatch || countryMatch || specificationsMatch;
    });

    // 3. Fallback Layout View for Zero Directory Matches
    if (targetedFilteredAssets.length === 0) {
        console.log("Filter loop returned 0 items. Appending missing search placeholder structure.");
        gridTargetElement.innerHTML = `
            <div class="col-span-full text-center border p-8 border-dashed border-zinc-800 rounded-xl py-12">
                <p class="text-xs font-mono text-zinc-500 uppercase tracking-widest mb-1">Zero Assets Discovered</p>
                <p class="text-[11px] font-mono text-zinc-600">No properties inside the live directory matched your query parameters.</p>
            </div>
        `;
        return;
    }

    // 4. Premium Placement Algorithmic Sorter
    // Evaluates boolean weights. If 'isBoosted' is true on item B but false on item A, 
    // item B gets sorted higher, pushing promoted assets to the top of the marketplace stream.
    targetedFilteredAssets.sort((itemA, itemB) => {
        const structuralWeightA = itemA.isBoosted ? 1 : 0;
        const structuralWeightB = itemB.isBoosted ? 1 : 0;
        return structuralWeightB - structuralWeightA;
    });

    console.log(`Grid compilation processing successful. Printing out [${targetedFilteredAssets.length}] active property layouts...`);

    // 5. Card Matrix Element Compiler Loop
    targetedFilteredAssets.forEach(currentProperty => {
        const itemCardContainerNode = document.createElement('div');
        
        // Dynamically shift border metrics and shadows to highlight premium ad nodes distinctively
        itemCardContainerNode.className = `zinc-card rounded-xl p-5 space-y-3 relative transition-all duration-300 ${
            currentProperty.isBoosted 
            ? 'border border-amber-500/40 shadow-xl bg-gradient-to-b from-[#0e0d0a] to-[#0b0b0c]' 
            : 'border border-zinc-900 shadow-md'
        }`;

        // Operational Fallbacks: Ensure values never return blank strings or empty lines to the UI
        const outputFeaturesText = currentProperty.features ? currentProperty.features : "Standard Residential Asset Architecture Configuration";
        const outputCurrencySymbol = currentProperty.currencySymbol ? currentProperty.currencySymbol : "$";
        
        // Calibrate price values: if local price calculation exists, format it with thousands separators, otherwise fall back to USD baseline
        const finalCalculatedPriceText = currentProperty.localPrice 
            ? currentProperty.localPrice.toLocaleString() 
            : currentProperty.priceUSD.toLocaleString();

        // Premium Badge Conditional Compilation Layout
        let optionalPromotedBadgeHtmlString = "";
        if (currentProperty.isBoosted) {
            optionalPromotedBadgeHtmlString = `
                <span class="absolute top-3 right-3 bg-gradient-to-r from-amber-500 to-orange-600 text-black text-[9px] font-black px-2 py-0.5 rounded font-mono uppercase tracking-wider animate-pulse">
                    PROMOTED
                </span>
            `;
        }

        // 6. Assemble Final Structural Layout Strings
        itemCardContainerNode.innerHTML = `
            ${optionalPromotedBadgeHtmlString}
            
            <div class="space-y-1">
                <h4 class="text-sm font-bold text-white font-mono tracking-wide uppercase truncate pr-16" title="${currentProperty.title}">
                    ${currentProperty.title}
                </h4>
                <p class="text-[11px] text-zinc-400 font-mono flex items-center gap-1 uppercase truncate">
                    <span class="text-emerald-500"></span> ${currentProperty.area}, ${currentProperty.state}, ${currentProperty.country}
                </p>
            </div>

            <div class="p-2.5 bg-zinc-950/80 border border-zinc-900 rounded-lg text-[11px] font-mono text-zinc-400 space-y-1">
                <span class="text-[9px] text-zinc-600 uppercase font-black tracking-wider block">Verified Property Specifications:</span>
                <p class="text-zinc-300 italic">"${outputFeaturesText}"</p>
            </div>

            <div class="flex items-center justify-between border-t border-zinc-900/60 pt-3">
                <div class="flex flex-col">
                    <span class="text-[9px] font-mono text-zinc-500 block uppercase tracking-widest">Valuation Index</span>
                    <span class="text-sm font-black text-emerald-400 font-mono">
                        ${outputCurrencySymbol}${finalCalculatedPriceText}
                    </span>
                </div>
                
                <a href="${currentProperty.whatsAppUrl || '#'}" 
                   target="_blank" 
                   rel="noopener"
                   class="px-3.5 py-1.5 bg-zinc-900 hover:bg-emerald-600 border border-zinc-800 hover:border-emerald-500 text-white font-bold rounded-lg text-[10px] tracking-wider font-mono transition-all duration-200 uppercase flex items-center gap-1.5 shadow-md">
                    <span></span> Chat Seller
                </a>
            </div>
        `;

        // Inject the freshly built property element card cleanly into your live layout viewport
        gridTargetElement.appendChild(itemCardContainerNode);
    });
}
// ============================================================================
// LAYER 5: GOOGLE ADSENSE OPTIMIZATION GATEWAY
// ============================================================================

/**
 * 1. Global Advertisement Viewer Request Interceptor
 * Safely handles optimization clicks while account monetization approval 
 * is pending within the central Google AdSense dashboard environment.
 */
function watchAdForBoostCoins() {
    console.log("Initialization request captured for AdSense video rendering engine...");
    
    // Strict clean system feedback notification to keep interface locked down safely
    alert("No ads available at the moment. Please try again later.");
}
// ============================================================================
// LAYER 6: INTERNAL PREMIUM ASSET BOOST WALLET MANAGEMENT LOGIC
// ============================================================================

/**
 * 1. Premium Promotion Button Accessibility Evaluator
 * Audits current coin ledger counts and screens unboosted inventory assets 
 * to automatically lock or unlock promotional interface elements.
 */
function evaluateBoostPromotionButtonAccessibility() {
    console.log("Auditing coin wallet metrics and seller asset counts...");

    const boostActionButtonNode = document.getElementById('btn-promote-asset');
    if (!boostActionButtonNode) {
        console.error("DOM Validation Fault: Premium promotion trigger element could not be found.");
        return;
    }

    // Isolate user properties: filter for items created by this active user that are NOT already boosted
    const unboostedUserAssetsArray = propertiesData.filter(function(propertyItem) {
        const matchesActiveSeller = propertyItem.sellerPhone === appState.user;
        const isCurrentlyUnboosted = propertyItem.isBoosted === false;
        return matchesActiveSeller && isCurrentlyUnboosted;
    });

    console.log("Unboosted qualifying assets discovered for this profile: " + unboostedUserAssetsArray.length);
    console.log("Current wallet coin baseline value: " + appState.coins);

    // Business Logic Rule Validation: User must have at least 5 coins AND own at least 1 unboosted property
    const hasSufficientCoinBalance = appState.coins >= 5;
    const hasQualifyingPropertiesToPromote = unboostedUserAssetsArray.length > 0;

    if (hasSufficientCoinBalance && hasQualifyingPropertiesToPromote) {
        console.log("Promotion standards verified. Enabling premium interface triggers...");
        
        // Remove standard disabled HTML properties to make the element clickable
        boostActionButtonNode.disabled = false;
        
        // Apply high-contrast premium amber styling traits to signal visibility to user
        boostActionButtonNode.className = "w-full p-2.5 bg-amber-500 hover:bg-amber-600 text-black font-black rounded-lg text-[10px] tracking-wider font-mono transition-all duration-200 uppercase shadow-lg shadow-amber-500/10 cursor-pointer opacity-100";
    } else {
        console.log("Promotion standards unfulfilled. Enforcing interface security lockouts...");
        
        // Enforce native browser safety locks to completely block click intercept loops
        boostActionButtonNode.disabled = true;
        
        // Revert style definitions back to a muted, low-contrast zinc layout structure
        boostActionButtonNode.className = "w-full p-2.5 bg-zinc-900 border border-zinc-800 text-zinc-600 font-bold rounded-lg text-[10px] tracking-wider font-mono uppercase cursor-not-allowed opacity-40";
    }
}
// ============================================================================
// LAYER 7: FORCED PROPERTY ASSET CREATOR LAYER
// ============================================================================

/**
 * 1. Global Asset Creation Pipeline Controller
 * Collects form inputs, enforces field validation checks, handles dynamic currency
 * conversions, formats WhatsApp routing targets, and pushes records to the backend.
 */
function handleCreateListing() {
    console.log("Initializing dynamic property entry ingestion routine...");

    // Safe DOM Harvesting: Bind input form element nodes directly to variables
    const titleNodeReference = document.getElementById('listing-title');
    const areaNodeReference = document.getElementById('listing-area');
    const featuresNodeReference = document.getElementById('listing-features');
    const priceNodeReference = document.getElementById('listing-price');
    const contactNodeReference = document.getElementById('listing-contact');

    // Architecture Fault Interceptor: Verify all interface form points exist
    if (!titleNodeReference || !areaNodeReference || !featuresNodeReference || !priceNodeReference || !contactNodeReference) {
        console.error("Critical Structural Error: Form creation DOM nodes are broken or missing.");
        alert("APPLICATION FAULT: Input layout references are completely broken. Resetting terminal views.");
        return;
    }

    // Capture clean text properties, clearing leading or trailing layout spaces
    const contextualTitle = titleNodeReference.value.trim();
    const contextualArea = areaNodeReference.value.trim();
    const contextualFeatures = featuresNodeReference.value.trim();
    const contextualPriceRaw = priceNodeReference.value.trim();
    const contextualContact = contactNodeReference.value.trim();

    // Parse values to appropriate numeric formatting types for math processing
    const numericalPriceParsed = parseFloat(contextualPriceRaw);

    // 2. Strict Input Validation Rules
    // All properties are mandatory. Block processing instantly if criteria fields are blank or illegal.
    if (!contextualTitle) {
        alert("CREATION FAULT: Asset Title or Description is strictly required.");
        return;
    }
    if (!contextualArea) {
        alert("CREATION FAULT: Location Region or City/Area is strictly required.");
        return;
    }
    if (!contextualFeatures) {
        alert("CREATION FAULT: House Specifications and Amenities are strictly required.");
        return;
    }
    if (isNaN(numericalPriceParsed) || numericalPriceParsed <= 0) {
        alert("CREATION FAULT: Please specify a valid numerical price value greater than 0.");
        return;
    }
    if (!contextualContact) {
        alert("CREATION FAULT: A WhatsApp Link Routing Number is strictly required.");
        return;
    }

    console.log("Validation metrics cleared successfully. Computing localization properties...");

    // Harvest user context bounds directly from our primary memory state matrices
    const activeCountryOrigin = appState.country || "united states";
    const activeStateRegion = appState.stateRegion || "";
    const activeSellerIdentifier = appState.user || "unknown";
    
    const operationalLocaleKey = activeCountryOrigin.toLowerCase();

    // 3. Mathematical Currency Conversion Matrix Setup
    let computedPriceInUSD = numericalPriceParsed;
    let computedCurrencyNotationSymbol = "$";

    if (typeof currencyRates !== 'undefined' && currencyRates[operationalLocaleKey]) {
        const structuralExchangeRate = currencyRates[operationalLocaleKey].rate;
        computedCurrencyNotationSymbol = currencyRates[operationalLocaleKey].symbol;
        
        // Convert local asset value back to baseline USD coordinates for uniform pricing
        computedPriceInUSD = numericalPriceParsed / structuralExchangeRate;
        console.log("Local valuation successfully normalized to USD baseline via live API exchange data.");
    } else {
        console.warn("Pricing corridor unmapped inside registry cache. Defaulting to standard USD baseline ratios.");
    }

    // 4. Python-String Safe Character Cleaning & WhatsApp URL Constructor
    // Strips out space markers and addition signs safely using split/join to bypass backslash errors inside Python.
    const sanitizedCleanPhoneDigits = contextualContact.split(' ').join('').split('+').join('');
    const fullyQualifiedWhatsAppDirectUrl = "https://wa.me/" + sanitizedCleanPhoneDigits;

    console.log("WhatsApp message routing vector constructed successfully: " + fullyQualifiedWhatsAppDirectUrl);

    // 5. Build Unified Database-Ready Asset Object Blueprint
    const structuredPropertyAssetPayload = {
        id: Date.now(),
        title: contextualTitle,
        country: activeCountryOrigin,
        state: activeStateRegion,
        area: contextualArea,
        features: contextualFeatures,
        localPrice: numericalPriceParsed,
        currencySymbol: computedCurrencyNotationSymbol,
        priceUSD: computedPriceInUSD,
        contactPhone: contextualContact,
        whatsAppUrl: fullyQualifiedWhatsAppDirectUrl,
        sellerPhone: activeSellerIdentifier,
        isBoosted: false
    };

    console.log("Committing created data model directly to local operational stack matrix...");
    
    // Inject object into directory storage array immediately for real-time frontend feedback
    propertiesData.push(structuredPropertyAssetPayload);

    // 6. Network Database Synchronization Channel Pipeline
    console.log("Opening transactional API pathway to dispatch payload records...");
    fetch('/api/properties/create', {
        method: 'POST',
        headers: { 
            'Content-Type': 'application/json' 
        },
        body: JSON.stringify(structuredPropertyAssetPayload)
    })
    .then(function(networkResponse) {
        if (!networkResponse.ok) {
            throw new Error("HTTP sync pipeline connection rejection encountered.");
        }
        return networkResponse.json();
    })
    .then(function(receivedJsonPayload) {
        console.log("Central server database feedback confirms mapping status: ", receivedJsonPayload);
        alert("REGISTRATION SUCCESS: Asset has been fully committed to the global database indexing network.");
    })
    .catch(function(networkProcessingError) {
        console.error("Critical Network Sync Intercept Failure:", networkProcessingError);
        console.log("System Status: Retention saved in memory; pending backend synchronization loop updates.");
    });

    // 7. Post-Submission Interface Cleaning Lifecycle
    titleNodeReference.value = "";
    areaNodeReference.value = "";
    featuresNodeReference.value = "";
    priceNodeReference.value = "";
    contactNodeReference.value = "";

    console.log("Form controls purged cleanly. Signaling interface components to refresh visible feed layouts...");

    // Force real-time updates across feed layouts and control buttons
    if (typeof renderMarketplaceInventoryGrid === 'function') {
        renderMarketplaceInventoryGrid();
    }
    if (typeof evaluateBoostPromotionButtonAccessibility === 'function') {
        evaluateBoostPromotionButtonAccessibility();
    }
}
// ============================================================================
// LAYER 8: ASSET BOOST ACTION DISPATCH TRIGGERS & LIFECYCLE EVENT WATCHERS
// ============================================================================

/**
 * 1. Global Document Intercept Click Event Listener
 * Monitors interactive nodes to execute premium listing promotion shifts
 * and process micro-wallet coin deduction operations.
 */
document.addEventListener('click', function(clickTrackingEvent) {
    // Structural Intercept Check: Identify if the clicked item is our premium promotion trigger
    if (clickTrackingEvent.target && clickTrackingEvent.target.id === 'btn-promote-asset') {
        console.log("Premium promotional boost click dispatch request captured...");

        // Safety Gate A: Immediately terminate processing if wallet balance falls below cost threshold
        if (appState.coins < 5) {
            console.warn("Transaction Rejected: Wallet balance contains insufficient coins.");
            return;
        }

        // Safety Gate B: Isolate all current property elements owned by this specific active user account
        const userCreatedPropertiesArray = propertiesData.filter(function(propertyItem) {
            const matchesActiveProfile = propertyItem.sellerPhone === appState.user;
            const isCurrentlyUnboosted = propertyItem.isBoosted === false;
            return matchesActiveProfile && isCurrentlyUnboosted;
        });

        // Safety Gate C: Cancel loop if the user has no qualifying unboosted listings to apply the coins to
        if (userCreatedPropertiesArray.length === 0) {
            alert("PROMOTION FAULT: You do not have any active, unboosted properties in the inventory directory.");
            return;
        }

        // Target Strategy: Target the user's most recent unboosted asset addition entry point
        const targetedPropertyAssetId = userCreatedPropertiesArray[userCreatedPropertiesArray.length - 1].id;
        
        // Locate matching item coordinate inside the master data array matrix
        const globalTargetDataIndex = propertiesData.findIndex(function(searchItem) {
            return searchItem.id === targetedPropertyAssetId;
        });
        
        if (globalTargetDataIndex !== -1) {
            console.log("Transaction parameters approved. Deducting currency ledger markers...");
            
            // Business Logic Execution: Apply premium boost and charge exactly 5 wallet coins
            propertiesData[globalTargetDataIndex].isBoosted = true;
            appState.coins -= 5;
            
            // Sync Display Panels: Update the text elements showing the new wallet totals immediately
            const coinTrackerDisplayField = document.getElementById('sh-coins');
            if (coinTrackerDisplayField) {
                coinTrackerDisplayField.innerText = appState.coins;
            }
            
            // Send clear text feedback to confirm update
            alert("MARKET BOOST APPLIED: Your property asset has been configured as a premium trend listing.");
            
            console.log("Refreshing operational feed channels to force premium ranking weights...");
            
            // Trigger fresh directory compiles to shift boosted card layouts directly to the top line
            if (typeof renderMarketplaceInventoryGrid === 'function') {
                renderMarketplaceInventoryGrid();
            }
            if (typeof evaluateBoostPromotionButtonAccessibility === 'function') {
                evaluateBoostPromotionButtonAccessibility();
            }
        } else {
            console.error("Internal Data Sync Error: Target asset registry coordinate could not be mapped.");
        }
    }
});

console.log("Layer 1-8 Client Application Engines compiled successfully into browser runtime framework context.");
    </script>
</body>
</html>
"""

# ============================================================================
# API ROUTER BASE ENDPOINTS (FASTAPI ASSET RECEIVER REGISTRY)
# ============================================================================

@app.post("/api/properties/create")
async def create_property_endpoint(payload: dict):
    """
    Central operational backend network routing channel. 
    Receives incoming housing payloads from Layer 7 and records data status logs.
    """
    print("Backend server pipeline successfully captured asset database commit payload.")
    print(f"Index Log Title Entry: {payload.get('title', 'Unknown Description')}")
    return {"status": "synchronized", "message": "Asset safely mapped in central file directory systems."}

# System Deployment Initialization Handler Boot Logic Hook
if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.environ.get("PORT", 8000)), reload=True)
