# -*- coding: utf-8 -*-
"""Tot textul site-ului, intr-un singur loc.

Editezi aici, nu in template-uri. Datele de contact sunt marcate cu TODO.
Nota 1: in textele lungi apare cratima neseparabila U+2011 ("s‑a", "nu‑l"), ca browserul
sa nu rupa cuvantul la capat de rand. Arata identic cu o cratima obisnuita.
Nota 2: un pas din "steps" poate avea un al treilea element optional, un dict
{"file": <cale in static/>, "label": <textul linkului>}, pentru un formular descarcabil.
"""

BRAND = {
    "name": "Doctor Document",
    "parent": "VAIDA",
    "tagline": "Ordine în arhivă. Claritate în decizii.",
    "big_idea": "Când ai o problemă cu documentele, nu trebuie să știi ce să faci. "
                "Trebuie doar să știi pe cine să suni.",
    "promise": "Pleci de la noi știind ce ai de făcut și având încredere că problema ta este rezolvabilă.",
}

CONTACT = {
    # TODO: inlocuieste cu datele reale inainte de lansare
    "phone_display": "+40 700 000 000",
    "phone_href": "+40700000000",
    "email": "contact@doctordocument.ro",
    "city": "București",
    "address": "Str. Exemplu nr. 1, București",
    "hours": "Luni – vineri, 09:00 – 18:00",
}

HERO = {
    "eyebrow": "Consultanță · Prelucrare arhivă · Extragere date · Depozitare",
    "title": "Ai o problemă cu documentele?",
    "title_accent": "Spune‑ne ce s‑a întâmplat",
    "lead": "Nu trebuie să știi dinainte ce serviciu îți trebuie. Ne spui ce s‑a întâmplat, "
            "punem întrebările esențiale și îți spunem clar ce ai de făcut — fie rezolvăm, "
            "fie te îndrumăm.",
    "cta_primary": "Descrie‑ne problema",
    "cta_secondary": "Vezi ce facem",
}

# Cele doua drumuri de intrare in site: persoana fizica si organizatie.
AUDIENCES = [
    {
        "kind": "Persoane fizice",
        "title": "Îți trebuie un act din arhiva unei firme",
        "lead": "De cele mai multe ori, actul există. Problema e că firma nu mai există.",
        "items": [
            "Adeverință de venituri dintr-o societate desființată",
            "Adeverință de grupă de muncă",
            "Acte dintr-o firmă lichidată, divizată sau preluată",
            "Documente de familie moștenite, pe care vrei să le păstrezi",
        ],
        "cta": "Vezi cum obții actul",
        "slug": "extragere-date",
    },
    {
        "kind": "Companii și instituții",
        "title": "Ai o arhivă de pus în ordine",
        "lead": "De la o încăpere plină de cutii până la un fond pe care trebuie să-l predai corect.",
        "items": [
            "Ordonare, inventariere și legătorie, cu documentație completă",
            "Selecționare: ce se păstrează și ce se poate elimina legal",
            "Depozitare într-un depozit autorizat de Arhivele Naționale",
            "Control, mutare de sediu, lichidare sau preluare de arhivă",
        ],
        "cta": "Vezi cum lucrăm pe arhivă",
        "slug": "prelucrare-arhiva",
    },
]

INTRO = {
    "title": "Documentele nu sunt doar hârtii.",
    "body": [
        "În ele pot exista dovezi despre oameni, despre instituții, despre munca unor generații "
        "întregi și despre lucruri întâmplate cu mult înainte ca noi să ajungem acolo.",
        "Uneori documentul important este evident. Alteori este ascuns într-un teanc prăfuit, "
        "într-o încăpere abandonată sau într-o arhivă pe care nimeni nu a mai deschis-o de ani de zile.",
        "Rolul nostru este să găsim ordine în haos, să păstrăm ce merită păstrat și să facem "
        "informația accesibilă atunci când e nevoie de ea.",
    ],
    "stat": "20+ ani de experiență arhivistică în spate.",
}

TRUST = [
    ("20+", "ani de experiență arhivistică"),
    ("0 lei", "diagnostic înainte de orice ofertă"),
    ("4", "direcții: consultanță, prelucrare, extragere date și depozitare"),
]

SERVICES = [
    {
        "slug": "consultanta",
        "number": "01",
        "name": "Consultanță și diagnostic documentar",
        "short": "Consultanță",
        "tagline": "Primul telefon, înainte de orice decizie",
        "icon": "compass",
        "highlights": ["Diagnostic scris", "Plan pe pași", "Orientare către specialist"],
        "card_text": "Ne spui ce s‑a întâmplat, punem întrebările esențiale și îți spunem ce ai de făcut — "
                     "chiar dacă răspunsul înseamnă că lucrarea nu o facem noi.",
        "lead": "Acesta este serviciul din care pornește tot restul. Nu trebuie să vii cu o comandă. "
                "E suficient să vii cu problema.",
        "intro": "Uneori concluzia este o lucrare de câteva luni. Alteori sunt trei pași pe care îi poți "
                 "face singur săptămâna asta. Îți spunem varianta reală, nu pe cea convenabilă pentru noi.",
        "symptoms": [
            "Ai primit un control sau o solicitare oficială și nu știi ce trebuie să prezinți.",
            "Firma intră în lichidare sau insolvență și arhiva trebuie predată corect.",
            "Preiei o firmă, un sediu sau o activitate, iar la pachet vine o arhivă necunoscută.",
            "Nu știi ce termene de păstrare se aplică documentelor tale.",
            "Ai moștenit documente de familie sau un fond cu valoare istorică și nu știi ce urmează.",
            "Ai o problemă cu documentele și nu știi măcar pe cine să întrebi.",
        ],
        "steps": [
            ("Ascultăm",
             "Îți spui problema fără să fii grăbit. Nu presupunem și nu dăm soluții înainte să înțelegem."),
            ("Diagnosticăm",
             "Punem puține întrebări, dar bune, și identificăm problema reală — care nu e mereu cea anunțată."),
            ("Explicăm",
             "Spunem ce trebuie făcut, de ce, în ce ordine și ce se întâmplă dacă nu se face."),
            ("Rezolvăm",
             "Executăm soluția sau o construim împreună cu echipa ta, pe etape pe care le poți duce."),
            ("Orientăm",
             "Dacă soluția nu ține de noi — restaurare, juridic, o instituție anume — te îndrumăm către cine poate."),
        ],
        "deliverables": [
            "Diagnostic scris, în limbaj pe care îl poți folosi intern",
            "Plan pe pași, cu priorități, termene și ordine de mărime a costurilor",
            "Lista riscurilor, cu ce e urgent și ce poate aștepta",
            "Recomandarea următorului pas concret",
            "Contactul specialistului potrivit, când problema nu este a noastră",
        ],
        "note": "Promisiunea rămâne valabilă și dacă nu semnăm nimic: pleci cu claritate, direcție și "
                "următorul pas.",
        "faq": [
            ("Consultanța se plătește?",
             "Prima discuție și analiza la fața locului nu se tarifează. Diagnosticul scris se tarifează, "
             "iar suma o afli înainte să începem."),
            ("Dacă nu putem plăti lucrarea acum?",
             "Atunci pleci măcar cu planul și cu ordinea corectă a pașilor. Poți începe când ești pregătit."),
            ("Lucrați și cu persoane fizice?",
             "Da. Arhive de familie și documente moștenite intră în aceeași discuție."),
        ],
    },
    {
        "slug": "prelucrare-arhiva",
        "number": "02",
        "name": "Prelucrare și ordonare arhivă",
        "short": "Prelucrare arhivă",
        "tagline": "Arhiva fizică, pusă în ordine",
        "icon": "boxes",
        "highlights": ["Ordonare și inventariere", "Legătorie", "Selecționare legală"],
        "card_text": "Preluăm arhiva așa cum este — în cutii, în teancuri, într-o încăpere în care "
                     "nimeni nu a mai intrat de ani de zile — și o transformăm într-un fond ordonat, "
                     "inventariat și ușor de folosit.",
        "lead": "Nu ne sperie arhivele dificile. Cu cât situația pare mai complicată, cu atât "
                "întrebarea noastră e mai simplă: când ne putem apuca de treabă?",
        "intro": "Lucrăm pe arhive de firmă, de instituție sau moștenite, indiferent de starea în care "
                 "le găsim. Întâi ne uităm cu atenție. Abia apoi propunem un plan, cu etape și costuri "
                 "pe care le poți urmări.",
        "symptoms": [
            "Ai documente în mai multe locuri și nimeni nu știe exact ce se află în ele.",
            "Ai nevoie de un act vechi, iar căutarea durează zile.",
            "Te muți din sediu și trebuie să iei repede o decizie despre arhivă.",
            "Ai primit o solicitare oficială și nu găsești documentele cerute.",
            "Nu știi ce ai voie să distrugi și ce trebuie păstrat, iar nimeni nu-și asumă răspunsul.",
            "Firma intră în lichidare și arhiva trebuie predată corect.",
        ],
        "steps": [
            ("Evaluare la fața locului",
             "Vedem volumul real, starea documentelor și condițiile de depozitare. Fără estimări date din birou."),
            ("Ordonare și constituire",
             "Grupăm documentele pe creatori, ani și tipuri, apoi constituim unitățile arhivistice."),
            ("Legătorie",
             "Unitățile arhivistice sunt legate, numerotate și certificate, ca să reziste la manipulare și timp."),
            ("Inventariere",
             "Fiecare unitate primește descriere, termen de păstrare și loc exact în depozit."),
            ("Selecționare",
             "Separăm ce trebuie păstrat de ce se poate elimina legal și pregătim documentația aferentă."),
            ("Depozitare și acces",
             "Așezăm arhiva astfel încât un document să poată fi găsit de oricine, nu doar de noi."),
        ],
        "deliverables": [
            "Inventare pe termene de păstrare, tipărite și în format electronic",
            "Unități arhivistice legate, numerotate și etichetate",
            "Documentația de selecționare și eliminare",
            "Arhivă cu poziție fizică identificabilă și o procedură de acces scurtă",
            "Nomenclator arhivistic pentru documentele viitoare",
        ],
        "note": "Selecția face parte din munca arhivistică. Nu se poate păstra tot — dar nimic cu "
                "valoare nu dispare pentru că a fost ascuns într-un teanc de hârtii.",
        "faq": [
            ("Arhiva noastră e într-o stare foarte proastă. O luați așa?",
             "Da. Starea arhivei nu este un motiv de refuz, este primul lucru pe care îl evaluăm. "
             "Ne interesează volumul, riscurile și ordinea în care atacăm problema."),
            ("Cât durează?",
             "Depinde de volum și de stare. După evaluare îți dăm un interval realist. Când nu știm încă, "
             "spunem că nu știm încă și revenim cu un răspuns."),
            ("Putem lucra pe etape, cu buget împărțit?",
             "Da. Ritmul, etapele și amploarea se pot adapta. Standardul de lucru nu."),
        ],
    },
    {
        "slug": "extragere-date",
        "number": "03",
        "name": "Extragere date și eliberare documente",
        "short": "Extragere date",
        "tagline": "Actul de care ai nevoie, găsit în arhivă",
        "icon": "search",
        "highlights": ["Adeverințe de venituri", "Adeverințe de grupă de muncă", "Copii certificate"],
        "card_text": "Căutăm în arhivă documentul care îți trebuie — adeverință de venituri, de grupă de "
                     "muncă, un act dintr-un dosar vechi — și ți-l eliberăm în forma cerută de instituție.",
        "lead": "Cele mai multe telefoane încep la fel: „Firma la care am lucrat nu mai există. "
                "De unde îmi iau adeverința?”",
        "intro": "Dacă arhiva societății a ajuns la noi, căutăm și eliberăm actul potrivit. Dacă nu, "
                 "încercăm să aflăm unde se află și ce cerere trebuie să depui.",
        "symptoms": [
            "Ai lucrat la o societate desființată și ai nevoie de adeverință de venituri.",
            "Îți trebuie o adeverință de grupă de muncă, iar firma nu mai există.",
            "O instituție îți cere un document pe care nu știi de unde să-l iei.",
            "Ai nevoie de un act dintr-o arhivă veche pentru un dosar aflat pe rol.",
            "Cauți documente dintr-o firmă preluată, divizată sau lichidată.",
            "Nu știi unde a ajuns arhiva fostului angajator.",
        ],
        "steps": [
            ("Ne spui ce act îți trebuie",
             "Numele societății, perioada în care ai lucrat și instituția care cere documentul. Atât."),
            ("Verificăm unde se află arhiva",
             "Dacă fondul este la noi, mergem mai departe. Dacă nu, îți spunem cine îl deține."),
            ("Depui cererea",
             "Dacă arhiva este la noi, completezi cererea de eliberare și ne-o trimiți sau o aduci la sediu.",
             {"file": "documents/Cerere de eliberare adeverinta 2026.pdf",
              "label": "Descarcă cererea de eliberare (PDF)"}),
            ("Căutarea în fond",
             "State de plată, dosare de personal, registre — căutăm în unitățile arhivistice relevante."),
            ("Eliberarea documentului",
             "Adeverința sau copia certificată, în forma cerută de instituție, cu număr de înregistrare."),
            ("Ridicare sau expediere",
             "Ridici documentul de la sediu sau ți-l trimitem, cum îți este mai ușor."),
        ],
        "deliverables": [
            "Adeverință de venituri sau de grupă de muncă, în forma cerută de instituție",
            "Copii certificate după documentele găsite",
            "Răspuns scris și atunci când documentul nu există în fond",
            "Indicarea deținătorului arhivei, dacă fondul nu este la noi",
        ],
        "note": "Dacă documentul nu există în arhivă, îți spunem asta în scris. Un răspuns clar te ajută "
                "mai mult decât o căutare fără capăt.",
        "faq": [
            ("Cât durează?",
             "Depinde de fond și de cât de exact știm perioada. Primești un termen când depui cererea, "
             "nu o estimare vagă."),
            ("Ce trebuie să pregătesc?",
             "Actul de identitate, numele societății și perioada în care ai lucrat acolo, plus cererea "
             "completată. Restul întrebăm noi."),
            ("Dacă arhiva firmei nu este la voi?",
             "Îți spunem cine o deține — alt operator, lichidatorul sau o instituție — și ce cerere trebuie "
             "să depui acolo."),
        ],
    },
    {
        "slug": "depozitare-fizica",
        "number": "04",
        "name": "Depozitare fizică",
        "short": "Depozitare fizică",
        "tagline": "Depozit autorizat de Arhivele Naționale",
        "icon": "shield",
        "highlights": ["Depozit autorizat", "Condiții controlate", "Acces la cerere"],
        "card_text": "Ținem arhiva ta într-un depozit autorizat de Arhivele Naționale: condiții "
                     "controlate termic, protecție împotriva prafului și acces doar pe baza solicitării tale.",
        "lead": "Documentele nu se strică peste noapte. Se strică încet, într-un subsol umed sau într-o "
                "magazie în care nu se mai uită nimeni.",
        "intro": "Preluăm arhiva, o luăm în evidență la intrare și o păstrăm în condiții controlate. "
                 "Rămâne a ta: o poți consulta, completa sau ridica, integral, oricând.",
        "symptoms": [
            "Nu mai ai spațiu în sediu, iar arhiva ocupă o încăpere întreagă.",
            "Documentele stau într-un subsol, într-o magazie sau într-un spațiu cu igrasie.",
            "Te muți din sediu și nu ai unde să duci arhiva.",
            "Ai nevoie de documente rar, dar trebuie să le poți scoate repede când sunt cerute.",
            "Vrei să știi exact cine are acces la documentele tale.",
            "Plătești chirie pentru un spațiu în care ții, de fapt, cutii.",
        ],
        "steps": [
            ("Evaluare și preluare",
             "Vedem volumul și starea arhivei, stabilim condițiile și o preluăm cu proces-verbal."),
            ("Evidența la intrare",
             "Fiecare unitate arhivistică primește poziție în depozit și intră în evidența noastră."),
            ("Păstrare în condiții controlate",
             "Depozit autorizat de Arhivele Naționale, cu temperatură și umiditate monitorizate și "
             "protecție împotriva prafului și a accesului neautorizat."),
            ("Acces controlat",
             "Documentele se scot doar la solicitarea ta, cu evidența a cine, când și ce a consultat."),
            ("Consultare, copii sau retur",
             "Îți trimitem copia, îți punem documentul la dispoziție sau îți returnăm arhiva, când ceri."),
        ],
        "deliverables": [
            "Proces-verbal de preluare și evidența unităților depozitate",
            "Poziție exactă în depozit pentru fiecare unitate arhivistică",
            "Condiții de păstrare monitorizate: temperatură, umiditate, protecție la praf",
            "Acces la documente la cerere, cu evidența consultărilor",
            "Returnarea arhivei, integral, la încheierea contractului",
        ],
        "note": "Depozitul este autorizat de Arhivele Naționale. Arhiva rămâne a ta — noi răspundem de "
                "condițiile în care este păstrată.",
        "faq": [
            ("Arhiva rămâne a noastră?",
             "Da. Depozitarea nu schimbă proprietatea. O poți consulta, completa sau ridica, integral, oricând."),
            ("Cât de repede pot primi un document din depozit?",
             "Ne spui ce îți trebuie și îl scoatem. Termenul de răspuns se stabilește la contract, "
             "nu îl afli pe parcurs."),
            ("Dacă arhiva nu este ordonată?",
             "O prelucrăm înainte de depozitare. Un fond neordonat ocupă mai mult spațiu și se caută greu."),
        ],
    },
]

PROCESS = {
    "title": "Cum lucrăm",
    "lead": "Același drum, indiferent cu ce problemă vii.",
    "steps": [
        ("01", "Ascultăm", "Îți spui problema fără să fii grăbit."),
        ("02", "Diagnosticăm", "Punem întrebările esențiale și identificăm problema reală."),
        ("03", "Explicăm", "Spunem clar ce trebuie făcut și de ce."),
        ("04", "Rezolvăm", "Executăm soluția sau o construim împreună cu tine."),
        ("05", "Orientăm", "Dacă soluția nu ține de noi, te îndrumăm către cine poate."),
    ],
}

VALUES = [
    ("Responsabilitate", "Ne asumăm ce facem și ce lăsăm în urma noastră.",
     "Dacă este responsabilitatea noastră, ne ocupăm de ea."),
    ("Grijă", "Acordăm atenție oamenilor, documentelor și lucrurilor pe care le facem.",
     "Ne uităm cu atenție înainte să tragem concluzii."),
    ("Proactivitate", "Nu așteptăm ca problema să devină criză pentru a acționa.",
     "Nu doar rezolvăm problema de azi. Încercăm să evităm problema de mâine."),
    ("Expertiză", "Știm ce facem și avem standarde pe care le respectăm.",
     "Complex pentru noi. Clar pentru client."),
]

CTA = {
    "title": "Spune‑ne ce s‑a întâmplat",
    "lead": "Nu ai nevoie de o cerere pregătită, de termeni tehnici sau de un buget aprobat. "
            "E suficient să descrii situația.",
}


def get_service(slug):
    """Serviciul cu slug-ul dat sau None."""
    for service in SERVICES:
        if service["slug"] == slug:
            return service
    return None


def other_services(slug):
    """Celelalte servicii, pentru navigarea de la finalul paginii."""
    return [s for s in SERVICES if s["slug"] != slug]
