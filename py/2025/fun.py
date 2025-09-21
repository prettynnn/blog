import httpx

url = "https://api.dexscreener.com/latest/dex/search"

params = {
    "q": "XBT/SOL,AVNT/USDC,ASTER/USDT"
}

def function():
    with httpx.Client() as session:
       result = session.get(url, params=params)
       data = result.json()
       seen = set()
       
    for pair in data["pairs"]:
            chain = pair["chainId"]
            name = pair["baseToken"]["name"]
            symbol = pair["baseToken"]["symbol"]
            if symbol in seen:
                continue
            seen.add(symbol)
            
            addressToken = pair["baseToken"]["address"]
            
            print(f"token : {name} | symbol : {symbol} | address token : {addressToken} | chain : {chain} ")
            
function()
