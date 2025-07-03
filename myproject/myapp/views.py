from django.shortcuts import render

# Create your views here.
# views.py
from django.http import JsonResponse
from .models import User, Apartment
# views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer, ApartmentSerializer
from django.utils import timezone

def user_list(request):
    users = User.objects.all().values('name', 'userId')
    return JsonResponse(list(users), safe=False)

def apartment_list(request):
    apartments = Apartment.objects.all().values('name', 'apartmentId','rent','rooms','date','location','category','user')
    return JsonResponse(list(apartments), safe=False)

@api_view(['GET'])
def api_user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def api_apartment_list(request):
    apartments = Apartment.objects.all()
    serializer = ApartmentSerializer(apartments, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def api_add_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def api_add_apartement(request):
    serializer = ApartmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def api_update_user(request, user_id):
    try:
        user = User.objects.get(userId=user_id)
    except User.DoesNotExist:
        return Response(status=404)

    serializer = UserSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def api_update_user_apartment(request, apartment_id):
    try:
        apartment = Apartment.objects.get(id=apartment_id)
    except Apartment.DoesNotExist:
        return Response(status=404)

    serializer = ApartmentSerializer(apartment, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def api_delete_user(request, user_id):
    try:
        user = User.objects.get(userId=user_id)
    except User.DoesNotExist:
        return Response(status=404)

    user.delete()
    return Response(status=204)
@api_view(['DELETE'])
def api_delete_apartment(request, apartment_id):
    try:
        apartment = Apartment.objects.get(id=apartment_id)
    except Apartment.DoesNotExist:
        return Response(status=404)

    apartment.delete()
    return Response(status=204)

@api_view(['GET'])
def view_apartments_by_location(request, location):
    apartments = Apartment.objects.filter(location=location)
    serializer = ApartmentSerializer(apartments, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def view_apartments_by_category(request, category):
    apartments = Apartment.objects.filter(category=category)
    serializer = ApartmentSerializer(apartments, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def view_by_rent_range(request, min_rent, max_rent):
    apartments = Apartment.objects.filter(rent__gte=min_rent, rent__lte=max_rent)
    serializer = ApartmentSerializer(apartments, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def sort_apartments_by_rent(request):
    apartments = Apartment.objects.all().order_by('rent')
    serializer = ApartmentSerializer(apartments, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def view_apartments_with_pagination(request, page_number, page_size):
    from django.core.paginator import Paginator
    apartments = Apartment.objects.all()
    paginator = Paginator(apartments, page_size)
    page = paginator.get_page(page_number)
    serializer = ApartmentSerializer(page, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def sort_by_date(request):
    apartments = Apartment.objects.all().order_by('date')
    serializer = ApartmentSerializer(apartments, many=True)
    return Response(serializer.data)

def refresh_page_in_every_2_seconds(request):
    current_time = timezone.now()
    return JsonResponse({'message': 'Page refreshed', 'time': current_time.strftime('%Y-%m-%d %H:%M:%S')})

