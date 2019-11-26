from django.contrib.auth.models import User, Group
from rest_framework import serializers 

class User_Serializers( serializers.HyperlinkedModelSerializer ):
    class Meta:
		model = User 
		fields = [
			'URL',
            'Username',
            'Email',
            'Groups',
        ]
class Group_Serialilizers(serializers.HyperlinkedModelSerialzer ):
	class Meta:
		model = Group 
		fields = [
            'URL',
            'Username'
        ]