from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import DateTime, BigInteger, ForeignKey

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)


class Blog(db.Model):
    __tablename__ = 'blog'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(unique=True, nullable=False)
    body: Mapped[str] = mapped_column(nullable=False)
    click: Mapped[int] = mapped_column(BigInteger, default=0)
    deleted: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=datetime.now(timezone.utc)
    )
    deleted_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=None, nullable=True
    )
    category_id: Mapped[int] = mapped_column(
        ForeignKey("category.id", ondelete="SET NULL"), 
        nullable=True
    )
    # relationship back to category
    category: Mapped["Category"] = relationship("Category", backref="blogs")


    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "body": self.body,
            "click": self.click,
            "deleted": self.deleted,
            "created_at": self.created_at,
            "deleted_at": self.deleted_at,
            "category_id": self.category_id,
            "category": self.category.name
        }


class Category(db.Model):
    __tablename__ = 'category'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }
