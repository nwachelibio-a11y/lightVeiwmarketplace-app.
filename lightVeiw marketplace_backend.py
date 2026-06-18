lightview_backend.py
    """Contacts Paystack servers to generate a secure checkout screen.

    Splits the money automatically based on your Split Code configuration.
    """
    url = "https://api.paystack.co/transaction/initialize"
    headers = {
        "Authorization": f"Bearer {PAYSTACK_SECRET_KEY}",
        "Content-Type": "application/json",
    }

    # Paystack processes currency in its lowest unit (e.g., Kobo or Cents).
    # 100000 Kobo = 1,000 local currency units. Change this to match your target price.
    payload = {
        "email": buyer_gmail,
        "amount": "100000",
        "split_code": OUR_TEAM_SPLIT_CODE,
        "callback_url": "http://127.0.0.1:8000/",  # Sends them back to your app homepage after paying
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=payload, headers=headers)

        res_data = response.json()
        if response.status_code == 200 and res_data.get("status"):
            # Sends the official secure checkout link back to the user's screen
            return {"checkout_url": res_data["data"]["authorization_url"]}
        else:
            raise HTTPException(
                status_code=400,
                detail=res_data.get("message", "Gateway failed to start."),
            )
    except Exception:
        raise HTTPException(
            status_code=500, detail="Unable to sync with payment servers."
        )


# --- CORE MARKETPLACE USER INTERFACE LAYOUT ---
@app.get("/", response_class=HTMLResponse)
def render_app_face():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>LightView Housing Hub</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-black text-zinc-100 font-mono min-h-screen flex flex-col p-4 max-w-md mx-auto border-x border-zinc-900">
        
        <header class="border-b border-zinc-900 pb-3 mb-4 flex justify-between items-center">
            <h1 class="text-lg font-black text-red-600 tracking-tighter">LIGHTVIEW HOUSING</h1>
            <span class="text-[9px] bg-emerald-950/50 border border-emerald-900 px-2 py-0.5 rounded text-emerald-400">⚡ Temu Split Active</span>
        </header>

  