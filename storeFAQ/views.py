

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FAQ
from .serializers import FAQSerializer
from django.http import HttpResponse
from rest_framework import status
from django.http import Http404

def home(request):
    return HttpResponse("Welcome to the FAQ API!")

class faq_list(APIView):
    def get(self, request):
        try:
            lang = request.GET.get('lang', 'en')  # default to English if no lang param is provided
            faqs = FAQ.objects.all()
            if not faqs:
                raise Http404(_("No FAQs found."))
            # faq_data = []
            # for faq in faqs:
            #     translated_question = faq.get_translated_question(lang)
            #     translated_answer = faq.get_translated_answer(lang)
            #     print(f"Processing FAQ - Question: {translated_question}, Answer: {translated_answer}")

            #     faq_data.append({
            #         'question': translated_question,
            #         'answer': translated_answer
            #     })
            serializer = FAQSerializer(faqs, many=True, context={'lang': lang})
            
            return Response(serializer.data,  status=status.HTTP_200_OK)

        except Http404 as e:
            return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({"error": _("An unexpected error occurred.")}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)