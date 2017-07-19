from colander import MappingSchema
from colander import SchemaNode
from colander import String


class LoginSchema(MappingSchema):
    username = SchemaNode(String())
    password = SchemaNode(String())
