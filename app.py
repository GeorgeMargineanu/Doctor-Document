# -*- coding: utf-8 -*-
"""Doctor Document - site de prezentare.

Rulare locala:  python app.py
Productie:      gunicorn app:app
"""
import json
import os
from datetime import datetime, timezone

from flask import Flask, abort, redirect, render_template, request, url_for

import content

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MESSAGES_FILE = os.path.join(BASE_DIR, "data", "mesaje.jsonl")

app = Flask(__name__)


@app.context_processor
def inject_globals():
    """Date disponibile in toate template-urile."""
    return {
        "brand": content.BRAND,
        "contact": content.CONTACT,
        "services": content.SERVICES,
        "year": datetime.now().year,
    }


@app.route("/")
def home():
    return render_template(
        "index.html",
        hero=content.HERO,
        intro=content.INTRO,
        trust=content.TRUST,
        audiences=content.AUDIENCES,
        process=content.PROCESS,
        values=content.VALUES,
        cta=content.CTA,
    )


@app.route("/servicii/<slug>/")
def service(slug):
    item = content.get_service(slug)
    if item is None:
        abort(404)
    return render_template(
        "service.html",
        service=item,
        others=content.other_services(slug),
        cta=content.CTA,
    )


@app.route("/servicii/")
def services_index():
    return redirect(url_for("home") + "#servicii")


@app.route("/contact/", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        form = {
            "nume": request.form.get("nume", "").strip(),
            "organizatie": request.form.get("organizatie", "").strip(),
            "email": request.form.get("email", "").strip(),
            "telefon": request.form.get("telefon", "").strip(),
            "mesaj": request.form.get("mesaj", "").strip(),
        }
        errors = {}
        if not form["nume"]:
            errors["nume"] = "Spune-ne cum te cheamă."
        if not form["email"] and not form["telefon"]:
            errors["email"] = "Lasă-ne un email sau un telefon, ca să putem răspunde."
        if "@" not in form["email"] and form["email"]:
            errors["email"] = "Adresa de email pare incompletă."
        if len(form["mesaj"]) < 10:
            errors["mesaj"] = "Descrie pe scurt situația, în câteva rânduri."

        if errors:
            return render_template("contact.html", form=form, errors=errors), 400

        save_message(form)
        return redirect(url_for("contact_sent"))

    return render_template("contact.html", form={}, errors={})


@app.route("/contact/multumim/")
def contact_sent():
    return render_template("contact_sent.html")


def save_message(form):
    """Scrie mesajul intr-un fisier JSONL.

    Simplu si fara dependinte. Daca vrei email sau CRM, inlocuieste corpul functiei.
    """
    os.makedirs(os.path.dirname(MESSAGES_FILE), exist_ok=True)
    record = dict(form, primit_la=datetime.now(timezone.utc).isoformat())
    with open(MESSAGES_FILE, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(record, ensure_ascii=False) + "\n")


@app.errorhandler(404)
def not_found(_error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5000)))
