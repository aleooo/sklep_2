from django.shortcuts import render

from utils.analysis import ranking

def main(request):
    r = ranking()
    return render(request, 'content/analysis/analysis.html', {'ranking': r})
