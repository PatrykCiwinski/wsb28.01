from requests import get
from dataclasses import dataclass
from pydantic import BaseModel
url="http://api.nbp.pl/api/exchangerates/rates/a/usd/last/10"
resp = get(url)
dane = resp.json()


class Rate(BaseModel):
    no: str
    effectiveDate: str
    mid: float

class TableA(BaseModel):
    table:str
    code: str
    currency: str
    rates: list[Rate]




table=TableA(**dane)
biggest_rate=max(table.rates,key=lambda rate:rate.mid)
print(biggest_rate.effectiveDate)