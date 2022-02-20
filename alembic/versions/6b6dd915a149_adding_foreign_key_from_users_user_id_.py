"""Adding foreign key from users.user_id to posts.author

Revision ID: 6b6dd915a149
Revises: 277170358994
Create Date: 2022-02-20 16:04:36.404810

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b6dd915a149'
down_revision = '277170358994'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('author', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=[
                          'author'], remote_cols=['user_id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'author')
    pass
