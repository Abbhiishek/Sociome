"""setting the foreign key 

Revision ID: e998f3b317bb
Revises: d53ac2320884
Create Date: 2022-02-20 18:18:37.757240

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e998f3b317bb'
down_revision = 'd53ac2320884'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('author', sa.String(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=[
                          'author'], remote_cols=['username'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'author')
    pass
