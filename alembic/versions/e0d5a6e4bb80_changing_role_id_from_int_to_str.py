"""changing role_id from int to str

Revision ID: e0d5a6e4bb80
Revises: cb64f5652350
Create Date: 2026-07-15 18:21:07.666170

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e0d5a6e4bb80'
down_revision: Union[str, Sequence[str], None] = 'cb64f5652350'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('roles', sa.Column('new_id', sa.Uuid(as_uuid=False), nullable=True))
    op.execute("UPDATE roles SET new_id = gen_random_uuid()")
    op.alter_column('roles', 'new_id', nullable=False)

    op.drop_constraint('roles_pkey', 'roles', type_='primary')
    op.drop_column('roles', 'id')
    op.alter_column('roles', 'new_id', new_column_name='id')
    op.create_primary_key('roles_pkey', 'roles', ['id'])


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column('roles', 'id', new_column_name='new_id')
    op.add_column('roles', sa.Column('id', sa.Integer(), autoincrement=True, nullable=True))
    op.drop_constraint('roles_pkey', 'roles', type_='primary')
    op.drop_column('roles', 'new_id')
    op.create_primary_key('roles_pkey', 'roles', ['id'])
