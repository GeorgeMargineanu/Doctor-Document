# -*- coding: utf-8 -*-
"""Doctor Document - site de prezentare.

Previzualizare locala:  python app.py
Site static pentru publicare:  python build.py  (rezulta folderul dist/)
"""
import os
from datetime import datetime

from flask import Flask, abort, redirect, render_template, url_for

import content

app = Flask(__name__)


@app.context_processor
def inject_globals():
    """Date disponibile in toate template-urile."""
    return {
        "brand": content.BRAND,
        "contact": content.CONTACT,
        "services": content.SERVICES,
        "site_url": content.SITE_URL,
        "form_access_key": content.FORM_ACCESS_KEY,
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
    # Pe site-ul publicat redirectul il face fisierul _redirects (vezi build.py).
    return redirect(url_for("home") + "#servicii")


@app.route("/contact/")
def contact():
    return render_template("contact.html")


@app.route("/contact/multumim/")
def contact_sent():
    return render_template("contact_sent.html")


@app.errorhandler(404)
def not_found(_error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5000)))
