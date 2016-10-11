from django.http import JsonResponse

from .search import perform_category_query


def query_categories(request):
    """
    A simple AJAX view that returns suggested product categories based on supplied product terms
    """

    query_words = request.GET.get('q', None)

    if query_words is None:
        return {}

    categories, suggestion = perform_category_query(query_words)

    if len(categories) == 0 and suggestion is not None:
        query_words = suggestion
        categories, suggestion = perform_category_query(query_words)

    resp = {
        "query": query_words,
        "categories": categories,
        "suggestion": suggestion
    }

    return JsonResponse(resp)
