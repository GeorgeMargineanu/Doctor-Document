# Doctor Document — site de prezentare

Site Flask, șase pagini: pagina principală (cu cele 4 servicii), câte o pagină per serviciu și contact.
Se scrie în Flask, se publică drept site static (fișiere HTML) pe Cloudflare Pages, gratuit.

Cele patru direcții, în ordinea din meniu: **consultanță**, **prelucrare arhivă** (ordonare,
inventariere, legătorie, selecționare), **extragere date** (adeverințe de venituri și de grupă de muncă
din arhive de societăți desființate) și **depozitare fizică** (depozit autorizat de Arhivele Naționale).
Pagina principală are o secțiune care desparte explicit cele două drumuri — persoană fizică și
persoană juridică — sub titlul „Cu ce vii la noi".

Termenul „digitalizare" nu se folosește pe site. Termenul corect este „digitizare", iar serviciul nu
este ofertat momentan.

## Rulare locală

```bash
python -m venv .venv
.venv\Scripts\activate          # pe macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python app.py                   # previzualizare la http://127.0.0.1:5000
python build.py                 # generează site-ul static în dist/
```

## Structura

```
app.py              rute (/, /servicii/<slug>/, /contact/) — folosit pentru previzualizare și build
build.py            generează site-ul static în dist/ (pagini, 404.html, _redirects, static/)
content.py          TOT textul site-ului — aici editezi; tot aici cheia formularului
templates/          base.html + o pagină per tip, _icons.html (iconuri SVG), _cta.html
static/css/style.css  o singură foaie de stil (design system complet)
static/img/         logo.jpg (original), logo.png (decupat, fundal transparent),
                    logo-full.png (cu tagline), favicon.svg
static/documents/   formulare descărcabile (cererea de eliberare adeverință)
dist/               site-ul generat, care se urcă pe hosting (nu se urcă în git)
```

## Ce se editează unde

- **Text, servicii, valori, FAQ** → `content.py`. Un serviciu nou = încă un dict în `SERVICES`
  (cu `slug` unic); apare automat în meniu, pe pagina principală, în footer și primește pagina lui.
  Ordinea din `SERVICES` este ordinea din meniu și de pe pagina principală.
- **Formulare descărcabile** → pui fișierul în `static/documents/` și adaugi un al treilea element la
  pasul respectiv din `steps`: `{"file": "documents/<nume>.pdf", "label": "Descarcă ..."}`. Apare
  automat ca buton de descărcare sub pasul acela.
- **Date de contact** → `CONTACT` din `content.py`. Sunt marcate cu `TODO`, acum sunt valori-placeholder
  (telefon, email, adresă).
- **Culori, tipografie** → variabilele `:root` din `static/css/style.css`.

## Formularul de contact

Formularul trimite direct din browser către **Web3Forms** (gratuit, 250 de mesaje/lună), care
trimite emailul la adresa asociată cheii. Nu există server, deci nici parole pe server.

- Cheia se ia de pe https://web3forms.com: introduci adresa unde vrei să primești mesajele
  (`contact@vaidaseverin.ro`) și cheia vine pe email. O pui în `FORM_ACCESS_KEY` din `content.py`.
  Cheia e publică (apare în pagină), nu e o parolă.
- Câmpul `email` al vizitatorului devine `Reply-To`, deci dai Reply și îi răspunzi lui.
- Validarea (nume, email sau telefon, mesaj) se face în pagină, cu aceleași mesaje în română.
- Anti-spam: câmpul ascuns `botcheck`.

## Publicare (gratuit): Cloudflare Pages + doctordocument.ro

### 1. Domeniul în Cloudflare (o singură dată)

1. Cont gratuit pe https://dash.cloudflare.com → **Add a domain** → `doctordocument.ro` → plan **Free**.
2. Cloudflare îți dă două nameservere (ceva de forma `xxx.ns.cloudflare.com`).
3. La firma de unde a fost cumpărat domeniul, la setările domeniului, înlocuiești nameserverele cu
   cele două de la Cloudflare. Durează de la câteva minute la câteva ore până devine activ.

### 2. Site-ul

1. `python build.py` → apare folderul `dist/`.
2. Cloudflare → **Workers & Pages** → **Create** → **Pages** → **Upload assets** → nume proiect
   `doctordocument` → tragi în pagină conținutul folderului `dist/` → **Deploy**.
   Site-ul apare imediat la `https://doctordocument.pages.dev`.
3. În proiect → **Custom domains** → adaugi `doctordocument.ro`, apoi și `www.doctordocument.ro`.
   Cloudflare pune singur DNS-ul și certificatul HTTPS.

La orice modificare: `python build.py` și urci din nou `dist/` (proiectul → **Create deployment**).

### 3. Emailul afișat pe site

Pe site apare `contact@doctordocument.ro` (din `CONTACT` în `content.py`). Ca să primească cineva
ce se scrie acolo: Cloudflare → domeniul → **Email** → **Email Routing** → creezi
`contact@doctordocument.ro` cu redirecționare către `contact@vaidaseverin.ro` (gratuit).
Altfel, schimbi adresa din `content.py` cu una existentă.

### 4. Înainte de a da drumul

- [ ] Datele reale în `CONTACT` din `content.py` (telefon, email, adresă) — acum sunt placeholder.
- [ ] `FORM_ACCESS_KEY` completat în `content.py`.
- [ ] Trimis un mesaj real prin formular, de pe telefon, și verificat că ajunge în Inbox, nu în spam.
- [ ] Decis dacă rămâne „0 lei — diagnostic înainte de orice ofertă" sau se corectează (vezi `TRUST`).
- [ ] Pagină de politică de confidențialitate, dacă strângi date prin formular (GDPR).

## Note de brand și design

Paleta vine direct din logo: albastru `#0025cc`, verde `#4ba625`, alb. Sunt variabile CSS în
`:root` (`--blue`, `--green`, `--navy`, `--surface`…) — schimbi acolo, se schimbă peste tot.
Tipografie: Poppins pentru titluri (apropiat de wordmark), Inter pentru text.

Verdele e folosit ca accent, nu ca a doua culoare de bază: punct final, bife, iconuri, kickere.
Albastrul duce acțiunile (butoane, linkuri, secțiuni pline).

Motivul de linii verticale din logo (`.stripes`) revine ca element decorativ în hero, în banda de
promisiune și pe paginile de serviciu.

`static/img/logo.png` este logo-ul decupat pe bounding box, cu albul făcut transparent, ca să nu
apară o bandă albă în header. Dacă primești logo-ul în SVG, înlocuiește-l și șterge PNG-urile
generate. În footer wordmark-ul e text (verde + alb), pentru că logo-ul are fundal deschis.

Textele urmează Brand DNA v1.0: fără limbaj pompos, fără metaforă medicală vizuală
(fără stetoscoape, cruci, seringi).
