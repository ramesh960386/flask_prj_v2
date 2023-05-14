from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from src.models import Task

class TaskSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Task
        include_fk = True
        load_instance = True
        # fields = ('id', 'name', 'email')

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)
