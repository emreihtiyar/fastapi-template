import pydantic

class UserResponse(pydantic.BaseModel):
    id: int
    name: str
    email: str
    role: str
    active: bool
    created_date: str
    updated_date: str
    last_password_change: str


class UserCreate(pydantic.BaseModel):
    name: str
    email: str
    password: str
