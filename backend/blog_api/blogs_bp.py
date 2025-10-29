from pydantic import ValidationError
from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from sqlalchemy.exc import IntegrityError
from blog_api.models import Blog, Category, db

from blog_api.validation_models import BlogValidated, CategoryValidated

bp = Blueprint('blog', __name__, url_prefix='/api')
api = Api(bp)


class BaseListApi(Resource):
    """Base class for list APIs."""
    model = None
    validator = None # Pydantic model or validator class

    def get(self):
        if self.model is None:
            raise NotImplementedError("Variable <model> must be set in subclass.")
        
        stmt = db.select(self.model)
        items = db.session.execute(stmt).scalars()
        return jsonify({
            "code": 0,
            "msg": "ok",
            "data": [item.to_dict() for item in items]
        })
    
    def create_instance(self, data: dict):
        if not self.model or not self.validator:
            raise NotImplementedError("Variable <model> or <validator> must be set in subclass.")
            
        try:
            validated = self.validator(**data)
        except ValidationError as e:
            print(e.errors())
            return jsonify({
                "code": -1,
                "msg": "Post data validation error.",
                "errors": e.errors()
            })
        
        # Create and commit
        instance = self.model(**validated.dict())
        db.session.add(instance)
        db.session.commit()
        return jsonify({
            "code": 0,
            "msg": f"A new {self.model.__name__.lower()} has been created with id {instance.id}.",
            "data": instance.id
        })


class BaseSingleApi(Resource):
    model = None

    def check(self):
        if self.model is None:
            raise NotImplementedError("Variable <model> must be set in subclass.")

    def get(self, pk):
        """Get details of an item."""
        self.check()

        stmt = db.select(self.model).where(self.model.id == pk)
        item = db.session.execute(stmt).scalar_one_or_none()
        if not item:
            return jsonify({
                "code": -1,
                "msg": f"Can not find the {self.model.__name__.lower()} with id == {pk}"
            })
        return jsonify({
            "code": 0,
            "msg": "ok",
            "data": item.to_dict()
        })

    def delete(self, pk):
        """Delete an item."""
        self.check()

        stmt = db.select(self.model).where(self.model.id == pk)
        item = db.session.execute(stmt).scalar_one_or_none()
        if not item:
            return jsonify({
                "code": -1,
                "msg": f"Can not find the {self.model.__name__.lower()} with id == {pk}"
            })

        db.session.delete(item)
        db.session.commit()
        return jsonify(
            {
                "code": 0,
                "msg": f"The {self.model.__name__.lower()} has been removed."
            }
        )

class CategoryListApi(BaseListApi):
    model = Category
    validator = CategoryValidated
    
    def post(self):
        """Create one category."""
        data = request.json or {}
        return self.create_instance(data)
        

class BlogListApi(BaseListApi):
    model = Blog
    validator = BlogValidated
    
    def post(self):
        """Create one blog"""
        data = request.json or {}
        return self.create_instance(data)


class BlogSingleApi(BaseSingleApi):
    model = Blog 


class CategorySingleApi(BaseSingleApi):
    model = Category 

api.add_resource(BlogListApi, '/blogs')
api.add_resource(CategoryListApi, '/categories')
api.add_resource(BlogSingleApi, '/blogs/<int:pk>')
api.add_resource(CategorySingleApi, '/categories/<int:pk>')
