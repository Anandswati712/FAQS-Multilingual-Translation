from django.contrib import admin
from .models import FAQ
from django.utils.translation import get_language, activate
# Register your models here.

# @admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['question','answer', 'display_translations']
    search_fields = ['question', 'answer']
    
    def display_translations(self, obj):
        # Return translations as a formatted string (for admin display)
        lang_code = get_language() or 'en'
        translated_question = obj.get_translated_question(lang_code)
        translated_answer = obj.get_translated_answer(lang_code)
        return f"Question: {translated_question}, Answer: {translated_answer}"
    
    display_translations.short_description = "Translations"
admin.site.register(FAQ, FAQAdmin)