from django.contrib import admin

from .models import Question
from .models import Choice

# Register your models here.
# 注册模型到后台管理
admin.site.register(Question)
admin.site.register(Choice)
