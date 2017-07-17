from colander import Invalid
from colander import MappingSchema
from colander import SchemaNode
from colander import String


class LoginForm(MappingSchema):
    username = SchemaNode(String())
    password = SchemaNode(String())

    def validator(self, node: "NewsletterSend", appstruct: dict):
        if appstruct['username'] != 'socek':
            raise Invalid(node["username"], "Username and/or password do not match.")

