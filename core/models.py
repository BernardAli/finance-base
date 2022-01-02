from django.db import models
import uuid
from django.utils.text import slugify
from django.urls import reverse
from PIL import Image
from django.conf import settings


# Create your models here.


class Tag(models.Model):
    title = models.CharField(max_length=75, verbose_name='Tag')
    slug = models.SlugField(null=False, unique=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def get_absolute_url(self):
        return reverse('tags', args=[self.slug])

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Sector(models.Model):
    sector = models.CharField(max_length=50)
    icon = models.ImageField(upload_to='sector', default='sector.png')
    slug = models.SlugField(unique=True, default='financial')

    def get_absolute_url(self):
        return reverse('sector', arg=[self.slug])

    def __str__(self):
        return self.sector


class Market(models.Model):
    market = models.CharField(max_length=50)
    icon = models.ImageField(upload_to='sector', default='sector.png')
    slug = models.SlugField(unique=True, default='GSE')

    def get_absolute_url(self):
        return reverse('market', arg=[self.slug])

    def __str__(self):
        return self.market



class CompanyProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_id = models.CharField(max_length=10)
    logo = models.ImageField(upload_to='company', default='sector.png')
    isin = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    sector = models.ManyToManyField(Sector, related_name='tags', blank=True)
    industry = models.ManyToManyField(Tag, related_name='tags', blank=True)
    postal_address = models.CharField(max_length=50, blank=True, null=True)
    registered_office = models.CharField(max_length=50, blank=True, null=True)
    incorporated_date = models.DateField(blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    toll_free = models.CharField(max_length=20, blank=True, null=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    core_activities = models.TextField()
    market = models.ManyToManyField(Market, related_name='tags', default='GSE')
    summary = models.TextField(max_length=1500, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('company_details', args=[str(self.id)])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        SIZE = 600, 800

        if self.logo:
            pic = Image.open(self.logo.path)
            pic.thumbnail(SIZE, Image.LANCZOS)
            pic.save(self.logo.path)

    def __str__(self):
        return str(self.company_id)


class Chairman(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    appointed_date = models.DateField()

    def __str__(self):
        return f"{self.company.name}'s Chairman is {self.name}"


class ChiefExecutiveOfficer(models.Model):
    company = models.ManyToManyField(CompanyProfile)
    name = models.CharField(max_length=150)
    appointed_date = models.DateField()

    def __str__(self):
        return f"{self.company}'s Chairman is {self.name}"


class ShareDetail(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    issued_shares = models.PositiveBigIntegerField()
    stated_capital = models.PositiveBigIntegerField(blank=True, null=True)
    listed_date = models.DateField()

    def __str__(self):
        return f"{self.company}"


class SharePrice(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    date = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    volume = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return f"{self.company}"


class Indices(models.Model):
    index = models.CharField(max_length=50)
    date = models.DateField()
    value = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.index}"


PERIOD_CHOICE = (
    ('Q1', '1st Quarter'),
    ('H1', '1st Half'),
    ('9M', '9 Months'),
    ('FY', 'Full Year'),
)


class FinancialPeriod(models.Model):
    period = models.CharField(max_length=50, choices=PERIOD_CHOICE)
    slug = models.SlugField(unique=True, default='fy')

    def get_absolute_url(self):
        return reverse('period', arg=[self.slug])

    def __str__(self):
        return f"{self.period}"


class Report(models.Model):
    year = models.DateField()
    period = models.ManyToManyField(FinancialPeriod)
    file = models.FileField(upload_to='reports')
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    audited = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.company}"


class MarketReport(models.Model):
    date = models.DateField()
    file = models.FileField(upload_to='reports')
    session_number = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.session_number}"