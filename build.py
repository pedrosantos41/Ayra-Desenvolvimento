"""Gera o index.html do site (GitHub Pages) a partir de central-cx.html.

O central-cx.html é escrito sem <html>/<head> porque o claude.ai acrescenta essa moldura ao publicar.
Para abrir como site comum, este script coloca a moldura em volta. Rode depois de cada alteração:

    python3 build.py
"""
from pathlib import Path

corpo = Path("central-cx.html").read_text(encoding="utf-8")
pagina = (
    '<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
    '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
    "<style>body{margin:0;padding:0}img{max-width:100%}[hidden]:not([hidden=until-found i]){display:none!important}</style>"
    "</head><body>\n" + corpo + "\n</body></html>\n"
)
Path("index.html").write_text(pagina, encoding="utf-8")
print("index.html gerado:", len(pagina), "caracteres")
