# Doctor Document — site de prezentare

Site Flask, șase pagini: pagina principală (cu cele 4 servicii), câte o pagină per serviciu și contact.
Fără pas de build, fără bază de date.

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
python app.py
```

Deschide http://127.0.0.1:5000

## Structura

```
app.py              rute (/, /servicii/<slug>/, /contact/)
content.py          TOT textul site-ului — aici editezi
templates/          base.html + o pagină per tip, _icons.html (iconuri SVG), _cta.html
static/css/style.css  o singură foaie de stil (design system complet)
static/img/         logo.jpg (original), logo.png (decupat, fundal transparent),
                    logo-full.png (cu tagline), favicon.svg
static/documents/   formulare descărcabile (cererea de eliberare adeverință)
data/mesaje.jsonl   mesajele primite din formular (creat automat)
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

Mesajele se scriu în `data/mesaje.jsonl` (o linie JSON per mesaj). E varianta fără dependințe,
ca să meargă imediat. Pentru email sau CRM, înlocuiește corpul funcției `save_message()` din `app.py`
(ex. SMTP prin `smtplib`, un API de mail, sau webhook).

Nu există protecție anti-spam. Înainte de lansare merită adăugat un honeypot sau un captcha.

## Deploy

Aplicația e un WSGI standard, `app:app`. Există deja `Procfile`.

- **Render / Railway / Fly.io**: build `pip install -r requirements.txt`, start `gunicorn app:app`.
- **PythonAnywhere**: WSGI file care importă `app` din `app.py`.
- **VPS**: `gunicorn -w 2 -b 127.0.0.1:8000 app:app` în spatele nginx.

Pe Windows `gunicorn` nu rulează; local folosește `python app.py`, iar pe server (Linux) gunicorn.

Dacă alegi un host care păstrează fișierele efemer (Render free), `data/mesaje.jsonl` se pierde la
redeploy — încă un motiv să trimiți mesajele pe email.

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
