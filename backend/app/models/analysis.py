from datetime import datetime
from sqlalchemy import String, Float, ForeignKey, Text, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.session import Base


class Analysis(Base):
    __tablename__ = "analyses"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    input_text: Mapped[str] = mapped_column(Text)
    bias: Mapped[str] = mapped_column(String(16))        # "left" | "center" | "right"
    bias_score: Mapped[float] = mapped_column(Float)
    sentiment: Mapped[str] = mapped_column(String(32))
    sentiment_score: Mapped[float] = mapped_column(Float)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    user: Mapped["User"] = relationship(back_populates="analyses")
