class AD(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ad_title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(max_length=250, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    picture1 = models.ImageField(upload_to='adimages', null=False, blank=False)
    picture2 = models.ImageField(upload_to='adimages', blank=True, null=True)
    picture3 = models.ImageField(upload_to='adimages', blank=True, null=True)
    picture4 = models.ImageField(upload_to='adimages', blank=True, null=True)
    picture5 = models.ImageField(upload_to='adimages', blank=True, null=True)
    picture6 = models.ImageField(upload_to='adimages', blank=True, null=True)
    picture7 = models.ImageField(upload_to='adimages', blank=True, null=True)
    picture8 = models.ImageField(upload_to='adimages', blank=True, null=True)
    adslug = models.SlugField(max_length = 250, null = True, blank = True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ad_title
