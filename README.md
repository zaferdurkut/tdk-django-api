# TDK Django Api
Bu projede Django Rest ile [TDK](https://sozluk.gov.tr/) API'si kullanılarak kelime için anlam ve atasözlerini döndüren bir web servisi çalışması yapılmıştır. Proje ile girilen kelime için anlam ve atasözlerine json formatında ulaşabilirsiniz.

 Projede;
- Django Rest Framework
- Django Swagger
- Django Health Check \
kullanılmıştır.

## Servisin Kurulumu

Kurulum için docker kurulu olmalıdır. Docker kullanılmadan kurulum için requirements.txt içerisinde lib'ler python 3 için kurulmalıdır. Docker ile kurulum için sırası ile;

```
git clone https://github.com/zaferdurkut/tdk_django_api.git
```


Projeye gidilir
```
cd tdk_django_api
```
Çalışıcak servis için .env dosyasının düzelenmesi gerekmektedir.
```
cp default.env .env
```
env dosyası düzenlendikten sonra servisi başlatmak için
```
docker-compose up --build -d
```
Servis ayağa kalktından sonra servise giriş için aşağıdaki komut çalıştırılır.
```
docker exec -it tdkapi_app_1 bash
```

## Servisin Çalıştırılması
Eğer python sürümü 3 değilse (alias python='/usr/bin/python3') komutunu çalıştırınız.
**Servisi çalıştırmak** için (eğer farklı bir porttan çıkılacak ise docker **üzerinden ilgili port dışarıya açılmalıdır.)
```
python manage.py runserver 0.0.0.0:8080
```
## Servisin Kullanımı
Servis endpointlerini görmek için [http://localhost:8080/api-docs](http://localhost:8080/api-docs) adresini kullanbilirsiniz. 
- **postman_collections** dizininde bulunan collections'lar ile servisin end pointlereini test edebilirsiniz.


### get_word - GET 
Bu method ile aşağıda bulunan body ile gönderildiğinde verdiğiniz parametrelere uygun olarak ilgili kelime için anlam ve atasözlerini opsiyonel olarak gösterir.

- request body 
```

{
	"word" : "toz",
	"anlam" : "True",
	"atasozu" :"True"
}
```

- response 
```

{
    "anlam": [
        "Çok küçük ve hafif parçacıklara bölünmüş toprak",
        "Çok küçük parçacıklara bölünmüş olan herhangi bir madde",
        "Bu durumda olan"
    ],
    "atasozu": [
        "toz almak",
        "tozdan dumandan ferman okunmamak",
        "toz etmek",
        "toz kondurmamak",
        "toz koparmak",
        "toz olmak",
        "tozu dumana katmak",
        "tozunu almak (veya atmak veya silkelemek veya silkmek)"
    ]
}
```
#### anlam is True
Response'da ilgili kelimenin anlamını döndürür
#### atasozu is True
Response'da üretilen kelime için atasözlerini döndürür.

### health_check - GET
http://localhost:8080/health_check/ adresinden servis durumunu görüntüleyebilirsiniz.
