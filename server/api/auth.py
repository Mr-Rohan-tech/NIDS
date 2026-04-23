from fastapi import APIRouter, HTTPException, Header
from pydantic import BaseModel
from typing import Optional
import uuid

router = APIRouter(prefix="/auth", tags=["Auth"])

# 🧠 Temporary in-memory database
users_db = []
tokens_db = {}

# =========================
# 📦 SCHEMAS
# =========================

class RegisterUser(BaseModel):
    name: str
    email: str
    password: str
    company: Optional[str] = None


class LoginUser(BaseModel):
    email: str
    password: str


class ResetPassword(BaseModel):
    token: str
    password: str


class UpdateProfile(BaseModel):
    name: Optional[str] = None
    company: Optional[str] = None


# =========================
# 🔐 REGISTER
# =========================

@router.post("/register")
def register(user: RegisterUser):
    for u in users_db:
        if u["email"] == user.email:
            raise HTTPException(status_code=400, detail="User already exists")

    new_user = {
        "id": str(uuid.uuid4()),
        "name": user.name,
        "email": user.email,
        "password": user.password,
        "company": user.company,
        "role": "client"
    }

    users_db.append(new_user)

    return {
        "message": "User registered successfully",
        "user": {
            "name": user.name,
            "email": user.email,
            "role": "client"
        }
    }


# =========================
# 🔑 LOGIN
# =========================

@router.post("/login")
def login(user: LoginUser):
    for u in users_db:
        if u["email"] == user.email and u["password"] == user.password:
            token = str(uuid.uuid4())
            tokens_db[token] = u

            return {
                "token": token,
                "user": {
                    "name": u["name"],
                    "email": u["email"],
                    "role": u["role"]
                }
            }

    raise HTTPException(status_code=401, detail="Invalid email or password")


# =========================
# 👤 PROFILE
# =========================

@router.get("/profile")
def get_profile(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="No token provided")

    token = authorization.replace("Bearer ", "")
    user = tokens_db.get(token)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")

    return {
        "user": {
            "name": user["name"],
            "email": user["email"],
            "company": user.get("company"),
            "role": user["role"]
        }
    }


@router.put("/profile")
def update_profile(data: UpdateProfile, authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="No token provided")

    token = authorization.replace("Bearer ", "")
    user = tokens_db.get(token)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")

    if data.name:
        user["name"] = data.name
    if data.company:
        user["company"] = data.company

    return {
        "message": "Profile updated",
        "user": user
    }


# =========================
# 🔁 FORGOT PASSWORD
# =========================

@router.post("/forgot-password")
def forgot_password(data: dict):
    email = data.get("email")

    for u in users_db:
        if u["email"] == email:
            return {"message": "Reset link sent (dummy)"}

    raise HTTPException(status_code=404, detail="User not found")


# =========================
# 🔁 RESET PASSWORD
# =========================

@router.post("/reset-password")
def reset_password(data: ResetPassword):
    # Dummy reset (no token validation for now)
    return {"message": "Password reset successful"}