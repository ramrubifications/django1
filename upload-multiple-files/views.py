@login_required(login_url='login')
def postad(request):
    
    if request.method == 'POST':
        activeuser = request.user
        
        adform = AdForm(request.POST, request.FILES)
        files = request.FILES.getlist('pictures')
        
        catform = CatForm(request.POST)
        subcatform = SubCatForm(request.POST)
        stateform = StateForm(request.POST)
        cityform = CityForm(request.POST)
        if adform.is_valid() and catform.is_valid() and subcatform.is_valid() and stateform.is_valid() and cityform.is_valid():
            ad = adform.save(commit=False)
            ad.user = request.user
        

            cat_title = catform.cleaned_data['category_title']
            cat_title_1 = Category.objects.get(category_title=cat_title)
            ad.category_id = cat_title_1.pk

            subcat_title = subcatform.cleaned_data['subcategory_title']
            subcat_title_1 = SubCategory.objects.get(subcategory_title=subcat_title)
            ad.subcategory_id = subcat_title_1.pk

            state_title = stateform.cleaned_data['state_title']
            state_title_1 = State.objects.get(state_title=state_title)
            ad.state_id = state_title_1.pk

            city_title = cityform.cleaned_data['city_title']
            city_title_1 = City.objects.get(city_title=city_title)
            ad.city_id = city_title_1.pk

            

            for idx, f in enumerate(files):
                if idx == 0:
                    file_instance = AD(picture1=f)
                    print(f)
                    ad.picture1 = f
                   
                if idx == 1:
                    file_instance = AD(picture2=f)
                    
                    ad.picture2 = f
                if idx == 2:
                    file_instance = AD(picture3=f)
                    
                    ad.picture3 = f
                if idx == 3:
                    file_instance = AD(picture4=f)
                    
                    ad.picture4 = f
                if idx == 4:
                    file_instance = AD(picture5=f)
                    
                    ad.picture5 = f
                if idx == 5:
                    file_instance = AD(picture6=f)
                   
                    ad.picture6 = f
                if idx == 6:
                    file_instance = AD(picture7=f)
                    
                    ad.picture7 = f
                if idx == 7:
                    file_instance = AD(picture8=f)
                    
                    ad.picture8 = f
                    break


            ad_title = adform.cleaned_data['ad_title']
            
            ad.adslug = slugify(ad_title)
            ad.adslug += slugify(activeuser.username)
            temp = random.randint(1000,99999999)
            ad.adslug += slugify(temp)
                 

            ad.save()
           
            messages.success(request, 'sucess, ad has been posted')
            return redirect('index')
        else:
            print("form valid failed")
            adform = AdForm()
            catform = CatForm()
            subcatform = SubCatForm()
            stateform = StateForm()
            cityform = CityForm()

            

            
            context = {
            'adform': adform,
            'catform': catform,
            'subcatform': subcatform,
            'stateform': stateform,
            'cityform': cityform,
          
            }
            return render(request, 'ads/postad.html', context)
    else:
        adform = AdForm()
        catform = CatForm()
        subcatform = SubCatForm()
        stateform = StateForm()
        cityform = CityForm()

       

        
        context = {
        'adform': adform,
        'catform': catform,
        'subcatform': subcatform,
        'stateform': stateform,
        'cityform': cityform,
     
        }
        return render(request, 'ads/postad.html', context)
