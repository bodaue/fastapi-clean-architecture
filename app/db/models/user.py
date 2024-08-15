from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from db.mixins.int_id_pk import IntIdPkMixin
from db.mixins.timestamp import TimestampMixin
from db.models import Base


class User(IntIdPkMixin, TimestampMixin, Base):
    name: Mapped[str] = mapped_column(String(255))
