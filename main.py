from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, constr
import tpo
import mongodb
import phone_number
import website
import verifier

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


class TPOGenerate(BaseModel):
    website: str
    phone_number: str


mongodb_init = mongodb.setup_mongodb()


@app.post("/tpo/generate")
async def tpo_generate(login_data: TPOGenerate):
    valid_phone_number = phone_number.is_valid(login_data.phone_number)
    if not valid_phone_number:
        return verifier.non_valid_phone_number

    valid_website = website.is_valid(login_data.website)
    if not valid_website:
        return verifier.non_valid_website

    exist = await tpo.already_exists(
        login_data.phone_number, login_data.website, mongodb_init["collection"]
    )
    if exist:
        return verifier.tpo_already_exists(login_data.phone_number, login_data.website)

    tpo_code = await tpo.new_tpo(
        login_data.phone_number, login_data.website, mongodb_init["collection"]
    )
    if not tpo_code["ok"]:
        return verifier.tpo_failed_to_generate(
            login_data.phone_number, login_data.website
        )

    return verifier.tpo_generated(login_data.phone_number, login_data.website)


class TPOVerify(BaseModel):
    website: str
    phone_number: str
    tpo: constr(min_length=6, max_length=6)


@app.get("/tpo/verify")
async def tpo_verify(login_data: TPOVerify):
    valid_tpo = tpo.is_valid(login_data.tpo)
    if not valid_tpo:
        return verifier.tpo_non_valid

    valid_phone_number = phone_number.is_valid(login_data.phone_number)
    if not valid_phone_number:
        return verifier.non_valid_phone_number

    valid_website = website.is_valid(login_data.website)
    if not valid_website:
        return verifier.non_valid_website

    verify = await tpo.verify_tpo(
        login_data.website,
        login_data.phone_number,
        login_data.tpo,
        mongodb_init["collection"],
    )
    return verify
