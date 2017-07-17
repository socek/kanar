from colander import MappingSchema
from colander import SchemaNode
from colander import String


class LoginForm(MappingSchema):
    username = SchemaNode(String())
    password = SchemaNode(String())
