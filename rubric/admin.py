from django.contrib import admin
from .models import SuperRubric, SubRubric, Bb, AdditionalImage
from .forms import SubRubricForm

# Register your models here.

class SubRubricInline(admin.TabularInline):
    model = SubRubric

class SuperRubricAdmin(admin.ModelAdmin):
    exclude = ('super_rubric',)
    inlines = (SubRubricInline,)

class SubRubricAdmin(admin.ModelAdmin):
    form = SubRubricForm

class AdditionalImage(admin.TabularInline):
    model = AdditionalImage

class BbAdmin(admin.ModelAdmin):
    list_display = ('rubric', 'title', 'content', 'author', 'created_at')
    fields = (
        ('rubric', 'author'),
        'title',
        'content',
        'price',
        'contacts',
        'image',
        'is_active'
    )
    inlines = (AdditionalImage,)

admin.site.register(SuperRubric, SuperRubricAdmin)
admin.site.register(SubRubric, SubRubricAdmin)
admin.site.register(Bb, BbAdmin)
