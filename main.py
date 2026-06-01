import jwt

class SecureJwtValidator:
    """
    JWT Token Signature Validator
    Validates token payloads against HS256 signatures safely.
    """
    def __init__(self, key="secure-shared-key"):
        self.key = key

    def validate_payload(self, token):
        try:
            return jwt.decode(token, self.key, algorithms=["HS256"])
        except jwt.InvalidTokenError:
            return None

if __name__ == "__main__":
    validator = SecureJwtValidator()
    print("JWT Validation utility compiled successfully!")
