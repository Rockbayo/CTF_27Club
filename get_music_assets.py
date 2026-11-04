import urllib.request
import urllib.parse
import json
import os

queries = {
    'hendrix': 'jimi hendrix purple haze',
    'joplin': 'janis joplin cry baby',
    'morrison': 'the doors light my fire',
    'winehouse': 'amy winehouse back to black',
    'cobain': 'nirvana smells like teen spirit'
}

results = {}

for key, term in queries.items():
    try:
        url = f"https://itunes.apple.com/search?term={urllib.parse.quote(term)}&entity=song&limit=1"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            if data['results']:
                r = data['results'][0]
                results[key] = {
                    'track': r.get('trackName'),
                    'artist': r.get('artistName'),
                    'preview': r.get('previewUrl'),
                    'artwork': r.get('artworkUrl100').replace('100x100bb', '600x600bb')
                }
                print(f"[+] Encontrado {key}: {r.get('trackName')} - {r.get('previewUrl')}")
    except Exception as e:
        print(f"[!] Error buscando {key}: {e}")

with open('music_tracks.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2)

print("[*] Guardado en music_tracks.json")

