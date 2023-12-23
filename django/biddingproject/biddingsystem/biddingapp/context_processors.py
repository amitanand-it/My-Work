from biddingapp.models import Vendor

def custom_processor(request):

    data = {"login": False, "admin": False}

    try:

        admin = request.session.get("admin")
        if admin:
            data["login"] = True
            data["admin"] = True
            data["vendor_details"] =  dict(
                username = "Admin",
                company_name = "Staff" ,
                email = "admin@biddingsystem.com",
            ) 
            return data


        vendor_id = request.session.get("vendor")

        if vendor_id:

            vendor = Vendor.objects.get(pk=vendor_id)

            vendor_details = dict(
                username = vendor.contact_person,
                company_name = vendor.company_name,
                email = vendor.email
            )
            data["vendor_details"] = vendor_details 
            data["login"] = True

    except Exception as e:
        pass

    return data
    


