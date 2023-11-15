from fastapi import FastAPI, Depends, Request, Form, status, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from starlette.responses import RedirectResponse
from database import SessionLocal, engine
from sqlalchemy.orm import Session
import models
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
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
async def login(username: str = Form(...), password: str = Form(...)):
    # Here you should add the logic to validate the username and password
    if username != "sam" or password != "sam":
        raise HTTPException(status_code=400, detail="Invalid username or password")
    return RedirectResponse(url="/main-page", status_code=303)


@app.get("/main-page")
async def main_page(request: Request):
    # Logic for the main page
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/post-blog", response_class=HTMLResponse)
async def post_blog_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/post-blog")
async def post_blog(title: str = Form(...), content: str = Form(...), db: Session = Depends(get_db)):
    new_blog_post = models.BlogPost(title=title, content=content)
    db.add(new_blog_post)
    db.commit()
    db.refresh(new_blog_post)
    return RedirectResponse(url="/main-page", status_code=303)


def get_all_blog_posts(db: Session):
    return db.query(models.BlogPost).all()


@app.get("/main-page")
async def main_page(request: Request, db: Session = Depends(get_db)):
    # Fetch blog posts from the database
    blog_posts = get_all_blog_posts(db)
    # Pass them to the template
    return templates.TemplateResponse("index.html", {"request": request, "blog_posts": blog_posts})

