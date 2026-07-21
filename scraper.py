import json
import urllib.request

URL = "https://tina.radiomariomaria.live/api/nowplaying"

try:
    req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
        
        # Display output in runner logs
        print("Scraped Data:", json.dumps(data, indent=2))
        
        # Example: Save output locally to inspect or commit
        with open("nowplaying.json", "w") as f:
            json.dump(data, f, indent=2)

except Exception as e:
    print(f"Error fetching API: {e}")
    exit(1)
