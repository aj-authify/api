from datetime import datetime
import verifier


async def verify_tpo(phone_number, tpo, collection):
    document = collection.find_one({"phone_number": phone_number})

    if not document or datetime.utcnow() > document["expiresAt"]:
        return verifier.tpo_not_found()

    if document["tpo"] != tpo:
        return verifier.tpo_invalid()

    return verifier.tpo_valid()
