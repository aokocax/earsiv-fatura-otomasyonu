# E-arşiv Fatura otomasyon scripti.
E-arsiv üzerinden otomatik olarak fatura oluşturmanızı sağlayan bir script.

https://github.com/user-attachments/assets/9edffdab-8e5a-488a-80ca-0b447fb344be

Öncelikle script dosyamızı çalıştırabilmek için Helium kütüphanesine ihtiyacımız oluyor.
```bash
git clone https://github.com/mherrmann/helium
```

diyerek helium'u indiriyoruz. Daha sonra bu repository üzerindeki [fatura.py](https://github.com/aokocax/earsiv-fatura-otomasyonu/blob/main/fatura.py) dosyasını açarak kullanıcı adı ve şifre bilgilerini kendinize göre düzenliyorsunuz. Aynı dizine indirdiğiniz [data.json](https://github.com/aokocax/earsiv-fatura-otomasyonu/blob/main/data.json) dosyasına fatura bilgilerini giriyorsunuz.

Son olarak fatura.py dosyasını çalıştırıyorsunuz ve data.json içindeki kişiler için verilen fatura tutarında faturalar teker teker ekleniyor.
```bash
python fatura.py
```



