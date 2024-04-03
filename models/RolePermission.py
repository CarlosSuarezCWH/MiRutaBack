from sqlalchemy import Table, Column, Integer, ForeignKey
from config.database import meta

RolePermission = Table(
    "roles_permissions",
    meta,
    Column("role_id", Integer, ForeignKey('roles.id'), primary_key=True),
    Column("permission_id", Integer, ForeignKey('permissions.id'), primary_key=True)
)
