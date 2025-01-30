from django.utils.safestring import mark_safe

def site_info(request):
    return {
        "footer_text": mark_safe("© Copyright 2025. All Rights Reserved. Developed by <b>Omar Faruk</b>"),
    }
