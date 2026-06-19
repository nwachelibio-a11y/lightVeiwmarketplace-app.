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
        <title>LightView Marketplace</title>
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
                <span class="text-zinc-500 text-[10px] font-mono">USER SETUP</span>
            </div>
            <span class="text-[10px] bg-emerald-950 text-emerald-400 px-2 py-0.5 rounded border border-emerald-900 font-mono">🟢 Live</span>
        </header>

        <main class="flex-1 flex flex-col justify-center my-6">
            
            <div id="view-login" class="zinc-card rounded-xl p-6 text-center shadow-2xl">
                <div class="w-12 h-12 bg-zinc-900 border border-zinc-800 text-orange-500 rounded-full flex items-center justify-center mx-auto mb-4 text-xl font-black">G</div>
                <h2 class="text-lg font-bold mb-1">Sign in to LightView</h2>
                <p class="text-xs text-zinc-400 mb-5">Connect with your official Google account to browse real estate inventory.</p>
                <input type="email" id="login-email" placeholder="username@gmail.com" class="w-full bg-zinc-950 border border-zinc-800 rounded-lg px-3 py-2.5 text-sm text-center focus:outline-none focus:border-orange-500 mb-4 text-white">
                <button onclick="handleGmailLogin()" class="w-full bg-orange-600 hover:bg-orange-700 text-white text-xs font-bold py-3 rounded-lg transition-all tracking-wider">
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

            <div id="view-complete" class="hidden zinc-card rounded-xl p-6 text-center shadow-2xl">
                <div class="w-12 h-12 bg-orange-950 text-orange-500 rounded-full flex items-center justify-center mx-auto mb-4 text-xl">🔒</div>
                <h2 class="text-lg font-bold mb-1">Profile Synchronized</h2>
                <p id="profile-summary" class="text-xs text-zinc-400 font-mono mb-4 bg-zinc-950 p-3 rounded border border-zinc-900 text-left whitespace-pre-line"></p>
                <div class="inline-flex items-center gap-2 text-xs text-orange-400 animate-pulse font-mono">
                    ⏳ Ready for Marketplace Inventory injection...
                </div>
            </div>

        </main>

        <footer class="text-center text-[10px] text-zinc-600 font-mono pt-3 border-t border-zinc-900">
            LightView Housing Hub © 2026
        </footer>

        <script>
            let session = { email: "", role: "", phone: "", country: "", state: "" };

            function handleGmailLogin() {
                const emailInput = document.getElementById('login-email').value;
                if(!emailInput || !emailInput.includes('@gmail.com')) {
                    alert("A valid @gmail.com address is required.");
                    return;
                }
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
                if(!phoneInput) { alert("Phone information parameters required."); return; }
                session.phone = phoneInput;
                session.country = "Global Target";
                session.state = "All-Active";
                showFinalSummary();
            }

            function saveBuyerLocation() {
                const countryInput = document.getElementById('buyer-country').value;
                const stateInput = document.getElementById('buyer-state').value;
                if(!countryInput || !stateInput) { alert("All geographical fields are required."); return; }
                session.country = countryInput;
                session.state = stateInput;
                session.phone = "Not Required (Buyer Mode)";
                showFinalSummary();
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
        <title>LightView Marketplace</title>
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
                <span class="text-zinc-500 text-[10px] font-mono">USER SETUP</span>
            </div>
            <span class="text-[10px] bg-emerald-950 text-emerald-400 px-2 py-0.5 rounded border border-emerald-900 font-mono">🟢 Live</span>
        </header>

        <main class="flex-1 flex flex-col justify-center my-6">
            
            <div id="view-login" class="zinc-card rounded-xl p-6 text-center shadow-2xl">
                <div class="w-12 h-12 bg-zinc-900 border border-zinc-800 text-orange-500 rounded-full flex items-center justify-center mx-auto mb-4 text-xl font-black">G</div>
                <h2 class="text-lg font-bold mb-1">Sign in to LightView</h2>
                <p class="text-xs text-zinc-400 mb-5">Connect with your official Google account to browse real estate inventory.</p>
                <input type="email" id="login-email" placeholder="username@gmail.com" class="w-full bg-zinc-950 border border-zinc-800 rounded-lg px-3 py-2.5 text-sm text-center focus:outline-none focus:border-orange-500 mb-4 text-white">
                <button onclick="handleGmailLogin()" class="w-full bg-orange-600 hover:bg-orange-700 text-white text-xs font-bold py-3 rounded-lg transition-all tracking-wider">
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

            <div id="view-complete" class="hidden zinc-card rounded-xl p-6 text-center shadow-2xl">
                <div class="w-12 h-12 bg-orange-950 text-orange-500 rounded-full flex items-center justify-center mx-auto mb-4 text-xl">🔒</div>
                <h2 class="text-lg font-bold mb-1">Profile Synchronized</h2>
                <p id="profile-summary" class="text-xs text-zinc-400 font-mono mb-4 bg-zinc-950 p-3 rounded border border-zinc-900 text-left whitespace-pre-line"></p>
                <div class="inline-flex items-center gap-2 text-xs text-orange-400 animate-pulse font-mono">
                    ⏳ Ready for Marketplace Inventory injection...
                </div>
            </div>

        </main>

        <footer class="text-center text-[10px] text-zinc-600 font-mono pt-3 border-t border-zinc-900">
            LightView Housing Hub © 2026
        </footer>

        <script>
            let session = { email: "", role: "", phone: "", country: "", state: "" };

            function handleGmailLogin() {
                const emailInput = document.getElementById('login-email').value;
                if(!emailInput || !emailInput.includes('@gmail.com')) {
                    alert("A valid @gmail.com address is required.");
                    return;
                }
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
                if(!phoneInput) { alert("Phone information parameters required."); return; }
                session.phone = phoneInput;
                session.country = "Global Target";
                session.state = "All-Active";
                showFinalSummary();
            }

            function saveBuyerLocation() {
                const countryInput = document.getElementById('buyer-country').value;
                const stateInput = document.getElementById('buyer-state').value;
                if(!countryInput || !stateInput) { alert("All geographical fields are required."); return; }
                session.country = countryInput;
                session.state = stateInput;
                session.phone = "Not Required (Buyer Mode)";
                showFinalSummary();
            }

            function showFinalSummary() {
                document.getElementById('view-seller-phone').classList.add('hidden');
                document.getElementById('view-buyer-location').classList.add('hidden');
                document.getElementById('view-complete').classList.remove('hidden');
                
                document.getElementById('profile-summary').innerText = 
                    `User: ${session.email}\\nRole: ${session.role.toUpperCase()}\\nPhone: ${session.phone}\\nRegion: ${session.state}, ${session.country}`;
            }
        </script>
    </body>
    </html>
    """
            }

            function showFinalSummary() {
                document.getElementById('view-seller-phone').classList.add('hidden');
                document.getElementById('view-buyer-location').classList.add('hidden');
                document.getElementById('view-complete').classList.remove('hidden');
                
                document.getElementById('profile-summary').innerText = 
                    `User: ${session.email}\\nRole: ${session.role.toUpperCase()}\\nPhone: ${session.phone}\\nRegion: ${session.state}, ${session.country}`;
            }
        </script>
    </body>
    </html>
    """
    
