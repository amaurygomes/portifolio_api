# api/converters.py
from graphene_django.converter import convert_django_field
from .types import CKEditorFieldType
from django_ckeditor_5.fields import CKEditor5Field

@convert_django_field.register(CKEditor5Field)
def convert_ckeditor_field(field, registry=None):
    return CKEditorFieldType()
