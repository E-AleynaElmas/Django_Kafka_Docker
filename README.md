# Django_Kafka_Docker
 
## PROJENİN ÇALIŞTIRILMASI 
Terminal üzerinden;
### 1. ADIM: Docker’ın Ayağa Kaldırılması.
   - Docker’ı ayağa kaldırmak için:
 
 `>> docker-compose build `
   
 `>> docker-compose up `
    
   ya da direk `>>docker-compose up` diyerek docker ve içindeki kafka, veritabanı gibi bağımlılıkları çalıştırabilirsiniz.
   
### 2. ADIM: Admin Oluşturmak.
   Terminal üzerinden;
   
   `>> python manage.py makemigrations`
   
   `>> python manage.py migrate`
   
 Sonrasında

`>> python manage.py createsuperuser`
 
diyerek bir admin kullanıcısı oluşturabilirsiniz.

  - [http://localhost:8000/admin/](http://localhost:8000/admin/) sayfasına giderek **"Django administration”** sayfasına ulaşabilirsiniz. Buradan event ekleyebilirsiniz.
 
![](https://github.com/E-AleynaElmas/Django_Kafka_Docker/blob/main/for_readme/django%20administration%20giri%C5%9F.PNG)

![](https://github.com/E-AleynaElmas/Django_Kafka_Docker/blob/main/for_readme/admin%20panel.PNG)

### 3. ADIM: Django ile API Çalıştırmak.

`>> python manage.py runserver`
     
  Komutunu terminalde çalıştırarak projenin tamamını çalışır hale getirilmesi sağlanmış olur.


# ENDPOİNT’LERE İSTEK ATMAK
## 1. GET Methodu İle Çalışmak
### a. Tüm dataları görmek
   - [http://localhost:8000/api/event](http://localhost:8000/api/event) isteği ile kaydedilmiş tüm eventleri görebilirsiniz.
   ![](https://github.com/E-AleynaElmas/Django_Kafka_Docker/blob/main/for_readme/get.png)
 ### b. Tek bir datayı görmek
   - [http://localhost:8000/api/event/detail/2/](http://localhost:8000/api/event/detail/2/) isteği ile 2 id’sine sahip tek bir datayı görüntüleyebilirsiniz.
   ![](https://github.com/E-AleynaElmas/Django_Kafka_Docker/blob/main/for_readme/get1.png)


## 2.	POST Methodu İle Çalışmak
  - [http://localhost:8000/api/event/create](http://localhost:8000/api/event/create)
  ![](https://github.com/E-AleynaElmas/Django_Kafka_Docker/blob/main/for_readme/create.png)
  Yukarıda görülen örnekteki gibi yeni bir datayı oluşturup kaydedebilirsiniz.
  

## 3.	PUT Methodu İle Çalışmak
  - [http://localhost:8000/api/event/update/2/](http://localhost:8000/api/event/update/2/) isteği ile var olan bir datayı güncelleyebilirsiniz. Olmayan bir id ile istek attığınızda ise yeni bir data oluşturacaktır.
![](https://github.com/E-AleynaElmas/Django_Kafka_Docker/blob/main/for_readme/update.png)
Yukarıdaki örnekte id=2’ ye sahip olan şarkının ismini değiştirebilir ve PUT butonuna basarak güncelleme işlemini gerçekleştirebilmiş olursunuz.


## 4.	DELETE Methodu İle Çalışmak
  - [http://localhost:8000/api/event/delete/1/](http://localhost:8000/api/event/delete/1/) isteği ile hangi id’ye sahip veriyi silmek istersek silebiliriz.
  ![](https://github.com/E-AleynaElmas/Django_Kafka_Docker/blob/main/for_readme/delete.png)
  Yukarıdaki örnekte 1 id’sine sahip veriyi kırmızı DELETE butonuna basarak,
  
   ![](https://github.com/E-AleynaElmas/Django_Kafka_Docker/blob/main/for_readme/sure.png)
  
Yukarıdaki gelen ekranı da onaylayarak silebilirsiniz.
