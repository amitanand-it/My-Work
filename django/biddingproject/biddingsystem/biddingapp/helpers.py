from django.shortcuts import redirect
from functools import wraps

def admin_required(view_func):

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):

        if request.session.get("admin") == True:
            return view_func(request, *args, **kwargs)
        else:
            return redirect("/")

    return wrapper


def login_required(login_url=None):

    def top_wrapper(view_func):

        @wraps(view_func)
        def wrapper(request, *args, **kwargs):

            if request.session.get("vendor"):
                return view_func(request, *args, **kwargs)
            else:
                if login_url:
                    return redirect(login_url)
                else:
                    return view_func(request, *args, **kwargs)

        return wrapper

    return top_wrapper