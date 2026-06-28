# 📱 Vaneo's Regen Radar - iPhone PWA Installatie

## Het probleem
Safari op iPhone blokkeert API-calls (fetch) als je een lokaal HTML-bestand opent.
De app MOET via een webserver (HTTP/HTTPS) worden geserveerd.

## Optie 1: Gratis online hosten (AANBEVOLEN)

### GitHub Pages (gratis & makkelijk):
1. Maak een gratis account op github.com
2. Maak een nieuwe repository (bv. "regenradar")
3. Upload deze 4 bestanden naar de repository
4. Ga naar Settings → Pages → Select "main" branch
5. Je app is nu live op: `https://jouwgebruikersnaam.github.io/regenradar/`
6. Open deze URL in Safari op je iPhone 11
7. Tik op **Delen** (vierkantje met pijl) → **"Zet op beginscherm"**
8. Klaar! De app werkt nu als standalone app zonder Safari UI

### Alternatieven:
- **Netlify Drop**: sleep de map naar netlify.com/drop
- **Vercel**: gratis hosting, drag & drop
- **Surge.sh**: gratis via command line

## Optie 2: Lokaal netwerk (thuis)

Als je de app alleen thuis op je iPhone wilt gebruiken:

### Stap 1: Start de server op je computer
Open Terminal/Command Prompt in deze map en run:

```bash
# Python 3
python3 -m http.server 8080

# Of Python 2
python -m SimpleHTTPServer 8080

# Of Node.js
npx serve .
```

### Stap 2: Vind je lokale IP
- **Mac/Linux**: `ifconfig` of `ip addr` → zoek naar 192.168.x.x
- **Windows**: `ipconfig` → IPv4 Address

### Stap 3: Open op iPhone
Open Safari op je iPhone 11 en ga naar:
```
http://192.168.x.x:8080
```
(Vervang 192.168.x.x door je echte IP)

### Stap 4: Installeer
- Tik op **Delen** → **"Zet op beginscherm"**
- De app verschijnt als icoon op je homescreen

## iPhone 11 specifieke tips

- **iOS 13+**: PWA's werken goed, maar refresh soms niet automatisch.
  Als je een update doet: verwijder de app van je beginscherm en voeg opnieuw toe.

- **Status bar**: De app draait fullscreen zonder Safari toolbar.
  De notch/safe area wordt automatisch gerespecteerd.

- **Offline**: De app shell wordt gecached, maar neerslagdata vereist internet.

## Bestanden in deze package
- `index.html` - De app (met PWA meta tags)
- `manifest.json` - PWA configuratie
- `service-worker.js` - Offline caching
- `icon-192.png` & `icon-512.png` - App iconen
- `start_server.py` - Lokale server script
