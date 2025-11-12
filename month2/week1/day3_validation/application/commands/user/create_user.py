from pydantic import BaseModel, EmailStr, Field, constr


class CreateUserCommand(BaseModel):
    email: EmailStr = Field(..., description="Электронная почта пользователя")
    password: constr(min_length=8) = Field(..., description="Пароль минимум 8 символов")
