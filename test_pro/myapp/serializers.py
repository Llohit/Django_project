from rest_framework import serializers

# Why use serializer??
#
# Validation: Serializers allow you to define rules for the data being sent. They validate incoming data against specified fields and their types (e.g., ensuring that a field is required, that a string does not exceed a certain length, or that a value is an integer). If the data does not conform to the specified rules, the serializer will raise validation errors.
#
# Deserialization: Serializers convert complex data types, such as JSON or query parameters, into native Python data types that can be easily handled in your views. This process is called deserialization, and it transforms incoming data into a format that can be processed by your application.


# Data is
#
# {
# "id": 1,
# "type": "webhook_notification_configurations",
# "description": "sample_description",
# "account":4
#         }

class SampleSerializer(serializers.Serializer):
    id= serializers.CharField(required=False)
    type= serializers.CharField()
    description= serializers.CharField()
    account= serializers.IntegerField()