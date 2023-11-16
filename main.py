from fastapi import FastAPI, Depends, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from sqlalchemy.orm import Session
from database import getdb, engine  # Import the updated function
import models
from database import SessionLocal
import uvicorn

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def getdb():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

# Mount static files (CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Jinja2 Templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
async def login(request: Request, username: str = Form(...), password: str = Form(...)):
    # Add login validation logic here
    # Redirect to the post list page upon successful login
    return RedirectResponse(url="/posts", status_code=303)

@app.get("/posts", response_class=HTMLResponse)
async def posts_list(request: Request, db: Session = Depends(getdb)):
    # Display the list of posts from the database
    posts = db.query(models.BlogPost).all()
    return templates.TemplateResponse("posts.html", {"request": request, "posts": posts})


@app.get("/create-post", response_class=HTMLResponse)
async def create_post_form(request: Request):
    # Display the form to create a new post
    return templates.TemplateResponse("create_post.html", {"request": request})

@app.post("/submit-post")
async def submit_post(request: Request, title: str = Form(...), post_content: str = Form(...), db: Session = Depends(getdb)):
    # Submit and add the new post to the database
    post = models.BlogPost(title=title, content=post_content)
    db.add(post)
    db.commit()
    db.refresh(post)

    # Redirect to the post list page
    return RedirectResponse(url="/posts", status_code=303)

@app.post("/comment/{post_id}")
async def add_comment(request: Request, post_id: int, comment_content: str = Form(...), db: Session = Depends(getdb)):
    # Add a comment to the specific post in the database
    post = db.query(models.BlogPost).filter(models.BlogPost.id == post_id).first()

    if post:
        # Assuming you have a Comment model, create and add the comment to the post
        comment = models.Comment(content=comment_content)
        comment.blog_post = post  # Set the relationship

        db.add(comment)
        db.commit()
        db.refresh(comment)

    # Redirect back to the post list page
    return RedirectResponse(url="/posts", status_code=303)


# log out
@app.get("/logout")
async def logout(request: Request):
    # Add logout logic here
    return RedirectResponse(url="/", status_code=303)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)