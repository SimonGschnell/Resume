"""test

Revision ID: b30ecb5f4462
Revises: 8de4994bd57d
Create Date: 2020-03-05 19:35:51.019034

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b30ecb5f4462'
down_revision = '8de4994bd57d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('contact')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contact',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=64), nullable=True),
    sa.Column('email', sa.VARCHAR(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('people')
    # ### end Alembic commands ###
