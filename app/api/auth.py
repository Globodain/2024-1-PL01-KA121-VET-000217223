@token_auth.verify_token
def verify_token(token):
    g.current_user = User.check_token(token) or None
    return g.current_user is not None
