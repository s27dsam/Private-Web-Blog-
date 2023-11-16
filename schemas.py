# from fastapi_sqlalchemy import sqlalchemy_to_pydantic
# from sqlalchemy import or_
# from . import models

# # Automatically generate Pydantic models for the BlogPost and Comment models
# BlogPost_Pydantic = sqlalchemy_to_pydantic(models.BlogPost)
# Comment_Pydantic = sqlalchemy_to_pydantic(models.Comment)

# # Customize the BlogPostIn schema to exclude the comments field
# class BlogPostIn(BlogPost_Pydantic):
#     class Config:
#         orm_mode = True

#     comments = []