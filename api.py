import requests
from tinydb import Query, TinyDB

from config import AD_LIST_URL, BASE_URL

db = TinyDB("adverts.json")
headers = {
    "Host": "lalafo.kg",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0",
    "device": "pc",
    "language": "ru_RU",
    "country-id": "12",
}


class Advert(Query):
    id: str


def get_ads() -> list:
    advert = Advert()
    json_response = requests.get(AD_LIST_URL, headers=headers).json()
    list_of_ads = []
    for ad in json_response["items"]:
        if (
            ad["city"] == "Бишкек"
            and not ad.get("is_vip")
            and not db.search(advert.id == ad["id"])
        ):
            list_of_ads.append(get_ad_info(ad))
            db.insert({"id": ad["id"]})
    return list_of_ads


def get_ad_info(ad: dict) -> dict:
    return {
        "id": ad["id"],
        "price": f"{ad['old_price']} -> {ad.get('price')} {ad.get('currency')}"
        if ad.get("old_price")
        else f"{ad.get('price')} {ad.get('currency')}",
        "title": ad.get("title"),
        "params": [],
        "description": ad.get("description"),
        "url": BASE_URL + ad.get("url"),
        "phone": ad.get("mobile"),
    }
