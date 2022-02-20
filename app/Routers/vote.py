from fastapi import  Response, status, HTTPException, Depends, APIRouter
# import psycopg2
from sqlalchemy.orm import Session
# from sqlalchemy.sql.functions import func
from .. import  Schemas , models ,oauth2
from .. database import  get_db 
router = APIRouter(prefix="/votes",
tags=['Vote The Specific Post By Id '])


@router.post("/", status_code=status.HTTP_201_CREATED)
def vote_Post_By_Id(vote:Schemas.Vote , db: Session = Depends(get_db) , current_user: int = Depends(oauth2.get_current_user)):

    post = db.query(models.Post).filter(models.Post.post_id == vote.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id: {vote.post_id} does not exist")

    vote_query = db.query(models.Vote).filter(
        models.Vote.post_id == vote.post_id, models.Vote.user_id == current_user.user_id)

    found_vote = vote_query.first()

    if (vote.dir == 1):
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail=f"USER {current_user.user_id} has already voted on POST {vote.post_id}")
        new_vote = models.Vote(post_id=vote.post_id, user_id=current_user.user_id)
        db.add(new_vote)
        db.commit()
        return {"status": f"You voted the Post with CONTENT : [{post.content}]  Succesfully !"}
    else:
        if not found_vote:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Vote does not exist")

        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"status": f"You Unvoted the Post with CONTENT :  [{post.content}]  Succesfully !"}