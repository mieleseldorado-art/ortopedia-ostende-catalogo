
import requests
from bs4 import BeautifulSoup

url = "https://dema-argentina.com.ar/producto/F032-28_faja-tubular-post-quirurgica-abdominal-28-cm"

respuesta = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=30
)
respuesta.raise_for_status()

sopa = BeautifulSoup(respuesta.text, "html.parser")

print("Estado HTTP:", respuesta.status_code)
print("Título:", sopa.title.get_text(strip=True) if sopa.title else "No encontrado")

for selector in [
    'meta[property="product:price:amount"]',
    'meta[property="og:price:amount"]',
    '[itemprop="price"]'
]:
    elemento = sopa.select_one(selector)
    if elemento:
        print("Precio encontrado:", elemento.get("content") or elemento.get_text(strip=True))

