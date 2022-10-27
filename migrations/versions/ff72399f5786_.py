"""empty message

Revision ID: ff72399f5786
Revises: e75b9983e58b
Create Date: 2022-10-26 20:06:47.972384

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff72399f5786'
down_revision = 'e75b9983e58b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('pokemon_id_fkey', 'pokemon', type_='foreignkey')
    op.drop_column('pokemon', 'id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pokemon', sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('pokemon_id_fkey', 'pokemon', 'user', ['id'], ['id'])
    # ### end Alembic commands ###
