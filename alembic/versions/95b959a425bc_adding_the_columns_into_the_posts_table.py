"""adding the columns into the posts table

Revision ID: 95b959a425bc
Revises: 27c1402dbfc7
Create Date: 2022-02-20 18:15:29.804809

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95b959a425bc'
down_revision = '27c1402dbfc7'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('image' ,sa.String()))
    op.add_column('posts',sa.Column('published' , sa.Boolean(), server_default='TRUE', nullable=False))
    op.add_column('posts',sa.Column('created_at' ,sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')))
    # sa.Column('post_id' ,sa.Integer(), primary_key=True, nullable=False),
    # sa.Column('content' ,sa.String(), nullable=False)),
    # sa.Column('image' ,sa.String()    ),
    # sa.Column('published' , sa.Boolean(), server_default='TRUE', nullable=False),
    # sa.Column('created_at' ,sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')),
    # sa.Column('author' ,sa.String() , sa.ForeignKey("users.fullname",ondelete="CASCADE"), nullable=False),
    # sa.Column('author_details' ,sa.relationship("User"))
    pass


def downgrade():
    op.drop_column('posts', 'image')
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass

