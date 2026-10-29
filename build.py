# -*- coding: utf-8 -*-
"""Genereaza site-ul static in dist/, gata de urcat pe Cloudflare Pages.

Rulare:  python build.py
"""
import os
import shutil

import content
from app import app

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(BASE_DIR, "dist")

PAGES = (
    ["/", "/contact/", "/contact/multumim/"]
    + ["/servicii/{}/".format(s["slug"]) for s in content.SERVICES]
)

# Sintaxa Cloudflare Pages: sursa, destinatie, cod.
REDIRECTS = "/servicii/ /#servicii 301\n"


def write(rel_path, data):
    path = os.path.join(DIST, *rel_path.split("/"))
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as fh:
        fh.write(data)


def build():
    # Stergem doar fisierele vechi: pe OneDrive / cu Explorer deschis, Windows
    # blocheaza uneori stergerea folderelor.
    for root, _dirs, files in os.walk(DIST):
        for name in files:
            os.remove(os.path.join(root, name))
    os.makedirs(DIST, exist_ok=True)

    client = app.test_client()
    for url in PAGES:
        response = client.get(url)
        if response.status_code != 200:
            raise SystemExit("{} a raspuns cu {}".format(url, response.status_code))
        write(url.strip("/") + "/index.html" if url != "/" else "index.html", response.data)

    # Cloudflare Pages serveste automat 404.html pentru adrese inexistente.
    write("404.html", client.get("/__pagina-inexistenta__/").data)
    write("_redirects", REDIRECTS.encode("utf-8"))
    shutil.copytree(os.path.join(BASE_DIR, "static"), os.path.join(DIST, "static"), dirs_exist_ok=True)

    print("Gata: {} pagini in {}".format(len(PAGES) + 1, DIST))
    if content.FORM_ACCESS_KEY.startswith("COMPLETEAZA"):
        print("ATENTIE: FORM_ACCESS_KEY din content.py nu e completat; formularul nu va trimite.")


if __name__ == "__main__":
    build()
