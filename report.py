import os

import requests

SERVICE_CODE = "5a6b5ac2d0521c1134854b01"  # Blocked Driveway & Illegal Parking
NATURE_OF_REQUEST = "Blocking_Bicycle_Lane"

API_KEY = os.environ["SF311_API_KEY"]


def compact(d):
    return {k: v for k, v in d.items() if v is not None}


def report(
    lat,
    lng,
    media_url,
    description=None,
    email=None,
    first_name=None,
    last_name=None,
    phone=None,
    make_model=None,
    license=None,
    color=None,
):
    url = "http://mobile311-dev.sfgov.org/open311/v2/requests.json"
    response = requests.post(
        url,
        data=compact(
            {
                "api_key": API_KEY,
                "attribute[Nature_of_request]": NATURE_OF_REQUEST,
                "attribute[txtColor]": color,
                "attribute[txtModel]": make_model,
                "attribute[txtReg]": license,
                "email": email,
                "first_name": first_name,
                "last_name": last_name,
                "lat": lat,
                "long": lng,
                "media_url": media_url,
                "phone": phone,
                "service_code": SERVICE_CODE,
                "description": description,
            }
        ),
    )
    response.raise_for_status()
    return response.json()
