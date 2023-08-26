"""Initial migration

Revision ID: f1264b3ac68c
Revises: 
Create Date: 2023-08-12 20:17:50.486595

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1264b3ac68c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('accounts',
    sa.Column('account_id', sa.String(length=64), nullable=False),
    sa.Column('balance', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('account_id')
    )
    op.create_table('transactions',
    sa.Column('transaction_id', sa.String(length=64), nullable=False),
    sa.Column('account_id', sa.String(length=64), nullable=True),
    sa.Column('created_at', sa.String(length=64), nullable=True),
    sa.Column('amount', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['account_id'], ['accounts.account_id'], ),
    sa.PrimaryKeyConstraint('transaction_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transactions')
    op.drop_table('accounts')
    # ### end Alembic commands ###
