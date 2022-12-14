"""empty message

Revision ID: 58f2ecb01d49
Revises: ff72399f5786
Create Date: 2022-10-27 15:28:40.242628

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58f2ecb01d49'
down_revision = 'ff72399f5786'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pokedex', sa.Column('current_user.id', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pokedex', 'current_user.id')
    # ### end Alembic commands ###
