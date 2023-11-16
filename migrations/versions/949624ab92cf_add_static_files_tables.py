"""add static files tables

Revision ID: 949624ab92cf
Revises: 488474a1ee97
Create Date: 2023-11-16 16:37:14.857305

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '949624ab92cf'
down_revision: Union[str, None] = '488474a1ee97'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('images',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=False),
    sa.Column('area_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['area_id'], ['areas.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_images_title'), 'images', ['title'], unique=False)
    op.create_table('videos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=False),
    sa.Column('area_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['area_id'], ['areas.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_videos_title'), 'videos', ['title'], unique=False)
    op.drop_constraint('tools_master_id_fkey', 'tools', type_='foreignkey')
    op.create_foreign_key(None, 'tools', 'masters', ['master_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tools', type_='foreignkey')
    op.create_foreign_key('tools_master_id_fkey', 'tools', 'tools', ['master_id'], ['id'])
    op.drop_index(op.f('ix_videos_title'), table_name='videos')
    op.drop_table('videos')
    op.drop_index(op.f('ix_images_title'), table_name='images')
    op.drop_table('images')
    # ### end Alembic commands ###
