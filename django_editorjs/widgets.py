import json
from django.forms import widgets, Media
from django.template.loader import render_to_string


class EditorJsWidget(widgets.Textarea):
    def __init__(self, editorjs_config, *args, **kwargs):
        super(EditorJsWidget, self).__init__(*args, **kwargs)
        self._editorjs_config = editorjs_config

    @property
    def media(self):
        return Media(
        )

    def render(self, name, value, **kwargs):
        ctx = {
            "name": name,
            "id": kwargs["attrs"]["id"],
            "value": value,
            "editorjs_config": json.dumps(self._editorjs_config),
        }
        return render_to_string("editorjs.html", ctx)
