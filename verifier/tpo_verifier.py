def tpo_already_exists(phone_number):
    return {
        "ok": True,
        "message": "TPO already exists for this phone number",
        "phone_number": phone_number,
    }


def tpo_failed_to_generate(phone_number):
    return {
        "ok": False,
        "message": "Failed to generate TPO",
        "phone_number": phone_number,
    }


def tpo_generated(phone_number):
    return {
        "ok": True,
        "message": "TPO generated successfully",
        "phone_number": phone_number,
    }


def tpo_non_valid():
    return {
        "ok": False,
        "message": "Invalid TPO",
        "error": "TPO must only contain numbers",
    }


def tpo_not_found():
    return {"ok": False, "message": "TPO not found for this phone number"}


def tpo_invalid():
    return {"ok": False, "message": "TPO is invalid"}


def tpo_valid():
    return {"ok": True, "message": "TPO is valid"}
