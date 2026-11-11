from sqlmodel import Field , SQLModel

class Survey(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    age: int
    birthday: str
    address: str
    country: str
    nationality: str
    schoolid: int
    grade: str
    number: int
    emergency: int