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
    type= serializers.CharField(required=True)
    description= serializers.CharField(required=True)
    account= serializers.IntegerField(required=False)
    user= serializers.IntegerField(required=False)

    # def validate_account(self, value):
    #     """
    #         Validate the incoming payload.
    #         :param data: Received request data.
    #         :raises ValidationError: If the request contains invalid value.
    #     """
    #     print(type(value))
    #     if type(value)!=int:
    #         raise serializers.ValidationError({"account": "Account must be an integer"})
    #
    #     return value

    def to_internal_value(self, data):
        allowed_fields = {'id','type','description','account','user'}
        extra_fields = set(data.keys()) - allowed_fields
        arr_format = ", ".join(extra_fields)
        if extra_fields:
            raise serializers.ValidationError({"Extra fields provided": f"{arr_format}"})
        if "type" in data and not isinstance(data['type'], str):
            raise serializers.ValidationError({"type": "Type must be a string"})

        if "description" in data and not isinstance(data['description'], str):
            raise serializers.ValidationError({"description": "Description must be a string"})

        if "account" in data and not isinstance(data['account'], int):
            raise serializers.ValidationError({"account": "Account must be an integer"})

        if "user" in data and not isinstance(data['user'], int):
            raise serializers.ValidationError({"user": "Account must be an integer"})

        #Call parents class to_internal_value to ensure the normal workflow of parent class also happens
        #The normal workflow of parent class to_internal_value is responsible for converting incoming data (usually the request body in the form of JSON) into internal Python objects that can be processed later
        #So we ensure our checks and validation happens along with normal conversion from parent class also takes place
        #So whenever to_internal_value is called internally, first this function is called and then parent class to_internal_value
        return super().to_internal_value(data)
    #
    # #This is called after DRF deserializes the data and we want to perform any extra valdn
    # def validate_type(self, value):
    #     if(len(value) < 2):
    #         raise serializers.ValidationError({"type": "Type must be at least 2 characters"})
    #     return value
    #
    # #This is called after DRF deserializes the data and we want to perform any extra valdn
    # def validate_description(self, value):
    #     return value



