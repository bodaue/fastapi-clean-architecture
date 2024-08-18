from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.models.mixins.int_id_pk import IntIdPkMixin
from app.db.models.mixins.timestamp import TimestampMixin
from app.db.models import Base


class User(IntIdPkMixin, TimestampMixin, Base):
    name: Mapped[str] = mapped_column(String(255))
