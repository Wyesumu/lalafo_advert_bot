from api import get_ads
from main import db, notify_about_ads


def task():
    ads = get_ads()
    print(f"fetched {len(ads)} ads")
    users = db.all()
    print(len(users), "users in db")
    for user in users:
        notify_about_ads(user["id"], ads)


if __name__ == "__main__":
    task()
