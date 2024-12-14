from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, constr
import tpo
import mongodb
import phone_number
import verifier

app = FastAPI()


class LoginSet(BaseModel):
    phone_number: str


class LoginVerify(BaseModel):
    tpo: constr(min_length=6, max_length=6)
    phone_number: str


mongodb_init = mongodb.setup_mongodb()


@app.post("/login/set")
async def login_set(login_data: LoginSet):
    if not mongodb_init["ok"]:
        raise HTTPException(status_code=500, detail="Database connection failed")

    valid = phone_number.is_valid(login_data.phone_number)
    if not valid:
        return verifier.non_valid_phone_number

    exist = await tpo.already_exists(
        login_data.phone_number, mongodb_init["collection"]
    )
    if exist:
        return verifier.tpo_already_exists(login_data.phone_number)

    tpo_code = await tpo.new_tpo(login_data.phone_number, mongodb_init["collection"])
    if not tpo_code["ok"]:
        return verifier.tpo_failed_to_generate(login_data.phone_number)

    return verifier.tpo_generated(login_data.phone_number)


@app.get("/login/verify")
async def login_verify(login_data: LoginVerify):
    if not mongodb_init["ok"]:
        raise HTTPException(status_code=500, detail="Database connection failed")

    valid_tpo = tpo.is_valid(login_data.tpo)
    if not valid_tpo:
        return verifier.tpo_non_valid()

    valid_phone_number = phone_number.is_valid(login_data.phone_number)
    if not valid_phone_number:
        return verifier.non_valid_phone_number

    verify = await tpo.verify_tpo(
        login_data.phone_number, login_data.tpo, mongodb_init["collection"]
    )
    return verify
