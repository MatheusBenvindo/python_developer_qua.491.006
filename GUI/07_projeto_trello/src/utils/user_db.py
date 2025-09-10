# utils/user_db.py

import hashlib

# Simula um banco de dados de usuários com senhas em hash
users = {
    "admin": hashlib.sha256("sicoob123".encode()).hexdigest(),
    "user": hashlib.sha256("senha123".encode()).hexdigest(),
}


def validate_user(username, password):
    if not (username and password):
        return False
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return users.get(username) == hashed_password
