import datetime as dt

from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        if not visitor.get("vaccine"):
            raise NotVaccinatedError("All visitors should be vaccinated")
        if visitor["vaccine"].get("expiration_date") < dt.date.today():
            raise OutdatedVaccineError("Outdated vaccine")
        if not visitor.get("wearing_a_mask"):
            raise NotWearingMaskError("All visitors should wear masks")
        return f"Welcome to {self.name}"