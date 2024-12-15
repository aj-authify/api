import random
import datetime


async def new_tpo(phone_number, website, collection):
    tpo = generate_tpo()

    expires_at = expire_date()
    tpo_document = {
        "phone_number": phone_number,
        "website": website,
        "tpo": tpo,
        "expiresAt": expires_at,
    }

    try:
        collection.insert_one(tpo_document)
        return {"ok": True, "tpo": tpo}
    except Exception as e:
        return {"ok": False, "error": e}


def generate_tpo(length=6):
    return "".join(str(random.randint(0, 9)) for _ in range(length))


def expire_date(after=60):
    return datetime.datetime.utcnow() + datetime.timedelta(seconds=after)
