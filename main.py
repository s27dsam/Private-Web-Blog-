from fastapi import FastAPI, Depends, Request, Form, status, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse

app = FastAPI()

# Mount static files (CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Jinja2 Templates
templates = Jinja2Templates(directory="templates")

# Maintain a list to store posts, where each post is a dictionary with title and comments
posts = []

# Assuming you have a login system in place
@app.get("/", response_class=HTMLResponse)
async def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
async def login(request: Request, username: str = Form(...), password: str = Form(...)):
    # Add login validation logic here
    # Redirect to the post list page upon successful login
    return RedirectResponse(url="/posts", status_code=303)

@app.get("/posts", response_class=HTMLResponse)
async def posts_list(request: Request):
    # Display the list of posts
    return templates.TemplateResponse("posts.html", {"request": request, "posts": posts})

@app.get("/create-post", response_class=HTMLResponse)
async def create_post_form(request: Request):
    # Display the form to create a new post
    return templates.TemplateResponse("create_post.html", {"request": request})

@app.post("/submit-post")
async def submit_post(request: Request, title: str = Form(...), post_content: str = Form(...)):
    # Submit and add the new post to the list of posts
    post = {"title": title, "content": post_content, "comments": []}
    posts.append(post)
    # Redirect to the post list page
    return RedirectResponse(url="/posts", status_code=303)

@app.post("/comment/{post_id}")
async def add_comment(request: Request, post_id: int, comment_content: str = Form(...)):
    # Add a comment to the specific post
    if 0 <= post_id < len(posts):
        posts[post_id]["comments"].append(comment_content)
    # Redirect back to the post list page
    return RedirectResponse(url="/posts", status_code=303)

@app.get("/logout")
async def logout(request: Request):
    # Add logout logic here
    return RedirectResponse(url="/", status_code=303)

