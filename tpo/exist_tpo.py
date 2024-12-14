from datetime import datetime


async def already_exists(phone_number, collection):
    document = collection.find_one({"phone_number": phone_number})

    if not document:
        return False

    if datetime.utcnow() > document["expiresAt"]:
        await collection.delete_one({"phone_number": phone_number})
        return False

    return True
