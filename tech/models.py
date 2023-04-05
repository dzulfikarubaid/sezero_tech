from django.db import models

# Create your models here.
from django_editorjs import EditorJsField
# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=60)
    body = EditorJsField(
        editorjs_config={
            "tools": {
                "Table": {
                    "disabled": False,
                    "inlineToolbar": True,
                    "config": {"rows": 2, "cols": 3,},
                }
            }
        }
    )