# views.py
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from pymongo import MongoClient

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Connect to MongoDB
        client = MongoClient('mongodb+srv://jabintasnimjssho:iIlb3lNC7x4X46nq@cluster0.y4ixjrl.mongodb.net/?retryWrites=true&w=majority', 27017)
        db = client['userinfo']
        collection = db['idpass']

        # Retrieve the user from MongoDB
        user_data = collection.find_one({'email': email})

        if user_data:
            # Check the password
            if check_password(password, user_data['password']):
                # Successful login
                return JsonResponse({'message': 'Success'})
            else:
                # Invalid password
                return JsonResponse({'message': 'Invalid password'})
        else:
            # User not found
            return JsonResponse({'message': 'User not found'})
    else:
        return JsonResponse({'message': 'Invalid request'})
