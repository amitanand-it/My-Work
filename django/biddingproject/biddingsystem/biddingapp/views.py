from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.shortcuts import redirect
from biddingapp.models import Vendor, Item, VendorsBid, VendorLogins, BidAllotment
from biddingapp.helpers import login_required, admin_required


def home(request):
    if request.session.get("vendor"):
        return redirect("/placebid/")
    elif(request.session.get("admin") == True):
        return redirect("/adminpanel/")
    else:
        return render(request, "biddingapp/home.html", {})

@csrf_exempt
def register_vendor(request):

    if request.method == "POST":
        args = request.POST
        # context = dict(args = args)
        company_name = args.get("companyName")
        contact_person = args.get("contactPerson")
        email = args.get("email")
        phone = args.get("phone")
        password = args.get("password")
        confirm_password = args.get("confirmPassword")

        if password != confirm_password:
            context = {"error": "Password and Confirm Password should be same"}
            return render(request, "biddingapp/error.html", context)

        try:
            vendor = Vendor(
                company_name = company_name,
                contact_person = contact_person,
                email = email,
                phone = phone,
            )
            vendor.save()

            login = VendorLogins(
                vendor=vendor,
                username=email,
                password=password,
            )
            login.save()

        except Exception as e:
            context = {"error": f"{e}"}
            return render(request, "biddingapp/error.html", context)
        else:
            if request.session.get("admin") == True:
                return redirect("/list-vendors/")
            else:
                return redirect("/placebid/")


    return render(request, "biddingapp/register_vendor.html", {})

@csrf_exempt
@login_required(login_url="/login/")
def placebid(request):

    vendor_id = request.session.get("vendor")

    if request.method == "POST":
        args = request.POST
        item_id = args.get("itemSelect")
        bid_amount = int(args.get("bidAmount", 0))

        selected_item = Item.objects.get(id=item_id)
        if bid_amount < selected_item.starting_bid: 
            context = {"error": f"Bid amount should be greater than starting bid"}
            return render(request, "biddingapp/error.html", context) 


        bid = VendorsBid(
            vendor_id = vendor_id,
            item_id = item_id, 
            bid_amount = bid_amount,
        )
        bid.save()

        return redirect("/placebid/")


    return render(request, "biddingapp/placebid.html", {
        "items_list" : Item.objects.all(),
        "bids_list" : VendorsBid.objects.filter(vendor_id=vendor_id).all(),
    })

def placebid_thanks(request):
    return render(request, "biddingapp/placebid_thanks.html", {})

@admin_required
def view_bids(request):
    return render(request, "", {})

@admin_required
def adminpanel(request):
    bids_list = VendorsBid.objects.all().order_by("item_id","-bid_amount","created_at")

    data_list = [] 
    old_item_id= ''



    for data in bids_list:

        vendor = data.vendor
        contact_person = vendor.contact_person
        company_name = vendor.company_name
        email = vendor.email
        phone = vendor.phone
        details = f"Contact Person: {contact_person} | Company Name:{company_name} | Email: {email} | Phone: {phone}"
        data.details = details
        data_list.append(data)

        item = data.item

        if item.id != old_item_id: 
            data.possible_winner = True
            old_item_id = item.id
        else:
            data.possible_winner = False


    return render(request, "biddingapp/adminpanel.html", {
        "bids_list" : data_list
    })


@csrf_exempt
def bid_allotment(request):

    # data_list = [] 
    args = request.GET
    item_id = args.get("item_id")

    bids_alloted = BidAllotment.objects.filter(item_id=item_id).all()

    if not bids_alloted:
        bids_list = VendorsBid.objects.filter(item_id=item_id).order_by("item_id","-bid_amount","created_at")

        old_item_id= ''

        for data in bids_list:

            item = data.item
            vendor = data.vendor

            if item.id != old_item_id: 
                data.possible_winner = True
                old_item_id = item.id
                # data_list.append(data)
                allotment = BidAllotment (
                    item_id = item.id,
                    vendor_id = vendor.id,
                    bid_amount = data.bid_amount,
                )
                allotment.save()
    
    return redirect("/bid-results/")

def support(request):
    return render(request, "biddingapp/support.html", {})

@csrf_exempt
@admin_required
def add_items(request):
    if request.method == "POST":
        args = request.POST
        item_name = args.get("itemName")
        item_description = args.get("itemDescription") 
        starting_bid = args.get("startingBid") 

        item = Item(
            name = item_name,
            description = item_description,
            starting_bid = starting_bid,
        )
        item.save()
        return redirect("/add-items/")
    
    return render(request, "biddingapp/add_items.html", {})

@csrf_exempt
def login(request):

    if request.method == "POST":
        args = request.POST
        username = args.get("username")
        password = args.get("password") 
        next_url = args.get("next_url") 

        if username == "admin" and password == "admin":
            request.session["admin"] = True
            return redirect("/adminpanel/")


        login_qs = VendorLogins.objects.filter(
            username=username, 
            password=password
        )

        if not login_qs:
            context = {"error": f"Please register first as a vendor"}
            return render(request, "biddingapp/error.html", context) 

        obj = login_qs.get() 
        request.session["vendor"] = obj.vendor_id
        return redirect(next_url)


    if request.session.get("vendor"):
        return redirect("/")

    if request.session.get("admin") == True:
        return redirect("/adminpanel/")

    return render(request, "biddingapp/login.html", {
        "next_url": request.GET.get("next_url", request.path_info),
        "testing_data": request.session.get("vendor")
    })

@csrf_exempt
def logout(request):
    request.session["vendor"]=None
    request.session.flush()
    return redirect("/")

@csrf_exempt
def list_items(request):
    return render(request, "biddingapp/items_list.html", {
        "items_list" : Item.objects.all()
    })

@csrf_exempt
def list_vendors(request):
    return render(request, "biddingapp/vendors_list.html", {
        "vendors_list" : Vendor.objects.all()
    })

@csrf_exempt
def bid_results(request):


    return render(request, "biddingapp/bid_results.html", {
        "items_list" : Item.objects.all(),
        "winners_list" : BidAllotment.objects.all(),
    })

