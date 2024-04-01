from django.db import models


class Content(models.Model):
  name='Content'
  hero_image= models.ImageField(upload_to='hero_img/')
  about_img=models.ImageField(upload_to='about_img/')
  intro_img=models.ImageField(upload_to='about_img/')
  no_weddings= models.IntegerField(blank=False)
  no_happyclient= models.IntegerField(blank=False)
  no_photos= models.IntegerField(blank=False)
  no_videos= models.IntegerField(blank=False)

  def __str__(self):
    return self.name
  
class Gallery(models.Model):
  name = models.CharField(max_length=255)
  description = models.TextField()
  image1 = models.ImageField(blank=False, default="images/about_bg.jpg", upload_to='gallery/')
  image2 = models.ImageField(blank=False, default="images/about_bg.jpg", upload_to='gallery/')
  created_at= models.DateField(auto_now_add =True)

  def __str__(self):
      return self.name
  
class Home_galley(models.Model):
  name = models.CharField(max_length=255)
  description = models.TextField()
  image = models.ImageField(blank=False, default="images/about_bg.jpg", upload_to='gallery/')
  image1 = models.ImageField(blank=False, default="images/about_bg.jpg", upload_to='gallery/')
  image2 = models.ImageField(blank=False, default="images/about_bg.jpg", upload_to='gallery/')
  image3 = models.ImageField(blank=False, default="images/about_bg.jpg", upload_to='gallery/')
  image4 = models.ImageField(blank=False, default="images/about_bg.jpg", upload_to='gallery/')
  image5 = models.ImageField(blank=False, default="images/about_bg.jpg", upload_to='gallery/')
  image6 = models.ImageField(blank=False, default="images/about_bg.jpg", upload_to='gallery/')
  created_at= models.DateField(auto_now_add =True)

  def __str__(self):
      return self.name

class Contact(models.Model):
    name = models.CharField(max_length=255, default="Your Name")
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email 