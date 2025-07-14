from datetime import datetime, timedelta, timezone
import secrets
import sqlalchemy as sa
import sqlalchemy.orm as so
from flask_login import UserMixin
from typing import Optional

from app import db
from app.api import PaginatedAPIMixin  # Upewnij się, że masz to w swoim kodzie

class User(PaginatedAPIMixin, UserMixin, db.Model):
    __tablename__ = 'user'

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    token: so.Mapped[Optional[str]] = so.mapped_column(sa.String(32), index=True, unique=True)
    token_expiration: so.Mapped[Optional[datetime]] = so.mapped_column(sa.DateTime)

    # ...

    def get_token(self, expires_in=3600):
        now = datetime.now(timezone.utc)
        if self.token and self.token_expiration and self.token_expiration > now + timedelta(seconds=60):
            return self.token
        self.token = secrets.token_hex(16)
        self.token_expiration = now + timedelta(seconds=expires_in)
        db.session.add(self)
        db.session.commit()
        return self.token

    def revoke_token(self):
        self.token_expiration = datetime.now(timezone.utc) - timedelta(seconds=1)
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def check_token(token: str) -> Optional['User']:
        user = db.session.scalar(sa.select(User).where(User.token == token))
        if user is None or user.token_expiration is None or user.token_expiration < datetime.now(timezone.utc):
            return None
        return user


