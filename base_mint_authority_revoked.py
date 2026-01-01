import requests, time

def mint_revoked():
    print("Base — Mint Authority Revoked Detector")
    seen = set()

    while True:
        try:
            r = requests.get("https://api.dexscreener.com/latest/dex/pairs/base")
            for pair in r.json().get("pairs", []):
                addr = pair["pairAddress"]
                if addr in seen: continue

                age = time.time() - pair.get("pairCreatedAt", 0) / 1000
                if age > 600: continue

                if pair.get("mintAuthorityRevoked"):
                    token = pair["baseToken"]["symbol"]
                    print(f"MINT REVOKED\n"
                          f"{token} — no more minting possible\n"
                          f"Liq: ${pair['liquidity']['usd']:,.0f}\n"
                          f"https://dexscreener.com/base/{addr}\n"
                          f"→ Fixed supply forever — strong anti-inflation signal\n"
                          f"{'REVOKED'*20}")
                    seen.add(addr)

        except:
            pass
        time.sleep(4.3)

if __name__ == "__main__":
    mint_revoked()
