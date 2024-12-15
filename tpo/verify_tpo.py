from datetime import datetime
import verifier


async def verify_tpo(website, phone_number, tpo, collection):
    document = collection.find_one({"phone_number": phone_number, "website": website})

    if not document or datetime.utcnow() > document["expiresAt"]:
        return verifier.tpo_not_found(phone_number, website)

    if document["tpo"] != tpo:
        return verifier.tpo_invalid(phone_number, website)

    return verifier.tpo_valid(phone_number, website)
