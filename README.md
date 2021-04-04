# Django_Kafka_Docker
 
## PROJENİN ÇALIŞTIRILMASI 
Terminal üzerinden;
### 1. ADIM: Docker’ın Ayağa Kaldırılması.
   - Docker’ı ayağa kaldırmak için:
 
 `>> docker-compose build `
   
 `>> docker-compose up`
    
   ya da direk `>>docker-compose up”` diyerek docker ve içindeki kafka, veritabanı gibi bağımlılıkları çalıştırabilirsiniz.

### 2. ADIM: Django ile API Çalıştırmak.
     >>	python manage.py
  Komutunu terminalde çalıştırarak projenin tamamını çalışır hale getirilmesi sağlanmış olur.

 ### OPSİYONEL: Admin Oluşturmak.
   Terminal üzerinden;
   
   `>> python manage.py makemigrations`
   
   `>> python manage.py migrate`

sonrasında

`>> python manage.py createsuperuser`
 
diyerek bir admin kullanıcısı oluşturabilirsiniz.

  - [http://localhost:8000/admin/](http://localhost:8000/admin/) sayfasına giderek **"Django administration”** sayfasına ulaşabilirsiniz. Buradan event ekleyebilirsiniz.
 
![giriş](file:///C:/Users/TULPAR/Desktop/FOR%20README/django%20administration%20giri%C5%9F.PNG)
