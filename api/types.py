# api/types.py
import graphene

class CKEditorFieldType(graphene.Scalar):
    @staticmethod
    def serialize(value):
        return str(value)

    @staticmethod
    def parse_value(value):
        return str(value)

    @staticmethod
    def parse_literal(ast):
        if isinstance(ast, graphene.StringValue):
            return ast.value
        return None
