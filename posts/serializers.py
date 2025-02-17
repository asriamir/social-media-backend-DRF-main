from rest_framework import serializers
from .models import Post
class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.name")  

    class Meta:
        model = Post
        fields = ["id", "user", "content", "image", "created_at"]

    def create(self, validated_data):
        """ اطمینان از این که پست با کاربر لاگین‌شده ذخیره می‌شود """
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            return Post.objects.create(user=request.user, **validated_data)
        raise serializers.ValidationError("کاربر احراز هویت نشده است.")


