"""initial

Revision ID: c26f3f711c90
Revises: 
Create Date: 2024-02-05 20:39:50.264052

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c26f3f711c90'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('national_parks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('state', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_visited_parks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_of_visit', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('park_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['park_id'], ['national_parks.id'], name=op.f('fk_user_visited_parks_park_id_national_parks')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_user_visited_parks_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_visited_parks')
    op.drop_table('users')
    op.drop_table('national_parks')
    # ### end Alembic commands ###
