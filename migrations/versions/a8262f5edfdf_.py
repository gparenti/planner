"""empty message

Revision ID: a8262f5edfdf
Revises: c874d7945da3
Create Date: 2024-01-04 14:06:49.431186

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a8262f5edfdf'
down_revision = 'c874d7945da3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('creator_username', sa.String(length=64), nullable=True))
        batch_op.drop_constraint('fk_plan_bearbeiter', type_='foreignkey')
        batch_op.create_foreign_key('fk_todo_creator_username', 'user', ['creator_username'], ['username'])
        batch_op.drop_column('bearbeiter')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todo', schema=None) as batch_op:
        batch_op.add_column(sa.Column('bearbeiter', sa.INTEGER(), nullable=True))
        batch_op.drop_constraint('fk_todo_creator_username', type_='foreignkey')
        batch_op.create_foreign_key('fk_plan_bearbeiter', 'user', ['bearbeiter'], ['username'])
        batch_op.drop_column('creator_username')

    # ### end Alembic commands ###
