from sqlalchemy import Table, Column, String, Integer, Boolean, DateTime, sql
from core.database import Base
from core.database import session


class URL(Base):
    __tablename__ = "storage_url"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    raw_url = Column(String)
    date = Column(DateTime(timezone=True), server_default=sql.func.now())
    short_url = Column(String)


# url_maker = URL.__tablename__

c1 = URL(
    raw_url = 'fff',
    short_url = 'ffgh',
)


session.add(c1)
session.commit()
session.close()