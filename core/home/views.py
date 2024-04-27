from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    ldt_peopple = [
        {"name": "Taukir1", "age": 21},
        {"name": "Taukir2", "age": 17},
        {"name": "Taukir3", "age": 23},
        {"name": "Taukir4", "age": 24},
    ]
    wholetext = """
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam, ab earum. Similique quis est mollitia. Dolorum, eos! Tenetur nam autem accusamus dolorum ut consequatur, possimus ad similique voluptatibus, amet alias pariatur aperiam explicabo voluptas labore quis eius. Numquam officia cumque odio. Nisi veniam sunt commodi dolore, eveniet eum. Ducimus quas quo voluptas aliquid unde reprehenderit ut aut quos libero optio iste temporibus, fuga voluptatem quaerat, doloremque aliquam ipsa saepe placeat animi veniam tempora, distinctio tempore! Libero ratione perspiciatis amet, nobis dignissimos ullam iusto. Magni quae laudantium molestias quibusdam quis quaerat consequuntur error. Ut, veniam expedita possimus laborum vero magnam ratione!
    """

    ls_vegetables = ["tomato", "potato", "carrot"]

    context = {
        "title": "Django Home Page",
        "ldt_peopple": ldt_peopple,
        "wholetext": wholetext,
        "a_vegetables": ls_vegetables,
    }

    return render(request, "home/index.html", context)


def success_page(request):
    print("this is proff of running success page")
    print("*" * 10)
    return HttpResponse(
        """ <h1>Hello this is the success page.</h1>
            <hr>
            <p>
                this is the second parameter that is populated.
            </p>
    """
    )


def about_page(request):
    context = {"title": "Django About Page"}
    return render(request, "home/about.html", context)


def contact_page(request):
    context = {"title": "Django Contact Page"}
    return render(request, "home/contact.html", context)
