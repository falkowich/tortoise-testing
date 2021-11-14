from enum import unique
from tortoise import fields, models


class Profession(models.Model):
    name = fields.CharField(max_length=255, unique=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Drawer: {self.name}"


class User(models.Model):
    name = fields.CharField(max_length=255)
    first_name = fields.CharField(max_length=255)
    last_name = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    profession = fields.ForeignKeyField("models.Profession", related_name="users")

    def __str__(self) -> str:
        return f"Socks: {self.name}"
