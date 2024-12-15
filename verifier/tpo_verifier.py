def tpo_already_exists(phone_number, website):
    return {
        "ok": True,
        "message": "TPO already exists for this phone number",
        "phone_number": phone_number,
        "website": website,
    }


def tpo_failed_to_generate(phone_number, website):
    return {
        "ok": False,
        "message": "Failed to generate TPO",
        "phone_number": phone_number,
        "website": website,
    }


def tpo_generated(phone_number, website):
    return {
        "ok": True,
        "message": "TPO generated successfully",
        "phone_number": phone_number,
        "website": website,
    }


tpo_non_valid = {
    "ok": False,
    "message": "Invalid TPO",
    "error": "TPO must only contain numbers",
}


def tpo_not_found(phone_number, website):
    return {
        "ok": False,
        "message": "TPO not found for this phone number",
        "phone_number": phone_number,
        "website": website,
    }


def tpo_invalid(phone_number, website):
    return {
        "ok": False,
        "message": "TPO is invalid",
        "phone_number": phone_number,
        "website": website,
    }


def tpo_valid(phone_number, website):
    return {
        "ok": True,
        "message": "TPO is valid",
        "phone_number": phone_number,
        "website": website,
    }
