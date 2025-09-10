import hashlib

users = {
    "admin": hashlib.sha256("sicoob123".encode()).hexdigest(),
    "user": hashlib.sha256("senha123".encode()).hexdigest()
}

def validate_user(username, password):
    hashed = hashlib.sha256(password.encode()).hexdigest()
    return users.get(username) == hashed
