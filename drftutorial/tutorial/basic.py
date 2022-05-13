import json, os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tutorial.settings")
django.setup()
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

class Comment:

    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content

class CommentSerializer(serializers.Serializer):

    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)


comment = Comment(email='leila@example.com', content='foo bar')
print("comment: ", comment, "\n\n")

serializer = CommentSerializer(comment)
print("serializer: ", serializer, "\n\n")

serialized_data = serializer.data
print("data: ", serialized_data, "\n\n")

#converint to JSON
#json_string = json.dumps(serializer.data)
#print("json string: ", json_string, "\n\n" )

#converint to JSON byte string
json_string = JSONRenderer().render(serialized_data)

import io
from rest_framework.parsers import JSONParser
stream = io.BytesIO(json_string)
data = JSONParser().parse(stream)
print("parsed data: ", data, "\n\n" )

serializer = CommentSerializer(data=data)
if(serializer.is_valid()):
    print(serializer.validated_data)







