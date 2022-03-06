from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.shortcuts import redirect, render
from django.urls import reverse
from proxy_scrape.models import ScrapeJob
from .tables import ScrapeJobTable
from .forms import ScrapeJobForm


# Create your views here.
def index(request):
    proxy = ScrapeJob.objects.all()  #gets all content from db
    sort = request.GET.get('sort', None) # sort by wherever index you wish
    if sort:
        proxy = ScrapeJob.objects.order_by(sort)
    table = ScrapeJobTable(proxy)
    context = { "proxy": proxy, "table": table, "add_url": reverse('add-item') }

    return render(request, "proxy_scrape/index.html", context)

def add_item(request):
    if request.method == "POST":
        form = ScrapeJobForm(request.POST)
        if form.is_valid():
            item = form.save()
            return redirect('index')
    else:
        form = ScrapeJobForm()
    context = {
        "form": form,
        "back_url": reverse("index") 
        
    }
    return render(request, "proxy_scrape/add_update.html", context)

def edit_item(request, pk):
    item = get_object_or_404(ScrapeJob, pk = pk)
    if request.method == "POST":
        form = ScrapeJobForm(request.POST, instance = item)
        if form.is_valid():
            item = form.save()
            return redirect('index')
    else:
        form = ScrapeJobForm(instance = item)
    context = {
        "form": form,
        "back_url": reverse("index")   
        
    }
    return render(request, "proxy_scrape/add_update.html", context)


def delete_item(request, pk):
    item = get_object_or_404(ScrapeJob, pk=pk)
    item.delete()
    return redirect("index")

