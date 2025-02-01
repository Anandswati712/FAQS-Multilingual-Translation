from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
from googletrans import Translator
from django.core.cache import cache

class FAQ(models.Model):
    question = models.TextField(verbose_name=_("Question"))
    answer = RichTextField(verbose_name=_("Answer"))
    
    # Language-specific fields (optional - depends on your use case)
    # question_es = models.TextField(null=True, blank=True)
    # answer_es = models.TextField(null=True, blank=True)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        cache.clear()
        
    def get_translated_text(self, field_name, lang_code):
        """
        Retrieve translated text dynamically based on language code.
        Defaults to the primary field if the translation is unavailable.
        """
        # First, check if a translation exists in the language-specific field
        field_name_lang = f"{field_name}_{lang_code}"
        text = getattr(self, field_name_lang, None)
        
        if text:
            return text
        
        # If not, use Google Translate and cache the result
        text = getattr(self, field_name, "")
        if not text:
            return ""
        
        cache_key = f"faq_translation_{self.id}_{lang_code}"
        translated_text = cache.get(cache_key)
        
        if not translated_text:
            # Translate using googletrans API
            translator = Translator()
            translated_text = translator.translate(text, src='en', dest=lang_code).text
            cache.set(cache_key, translated_text, timeout=86400)  # Cache for 1 day
        
        # Save the translation in the language-specific field
        setattr(self, field_name_lang, translated_text)
        self.save() 
        
        return translated_text
        
    def get_translated_question(self, lang_code):
        return self.get_translated_text('question', lang_code)

    def get_translated_answer(self, lang_code):
        return self.get_translated_text('answer', lang_code)

    def __str__(self):
        return self.question[:50]
