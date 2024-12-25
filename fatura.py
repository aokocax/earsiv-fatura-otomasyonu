import json
import time
from helium import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC  # Burada EC'yi import ediyoruz

# JSON dosyasını oku
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

start_chrome('https://earsivportal.efatura.gov.tr/intragiris.html')  # veya kullandığınız başka bir browser driver

wait_until(S("#userid").exists, timeout_secs=10)
write("kullanici_adi", into=S("#userid"))
write("şifre", into=S("#password"))
click(S(".btn.waves-effect.waves-light"))

# Her öğeyi array üzerinde iterasyona sokuyoruz
for entry in data:
    ad =  entry['ad']
    soyad = entry['soyad']
    tarih = entry['tarih']
    tutar = entry['tutar']
    driver = get_driver()
    # Sayfada gerekli işlemleri başlatıyoruz
    wait_until(S("#gen__1006").exists, timeout_secs=10)
    driver.execute_script("$('select option:eq(1)').prop('selected', true).trigger('change');")

    element = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Belge İşlemleri')]"))
    )
    print("Öğe bulundu ve tıklanabilir durumda!")
    element.click()
    time.sleep(0.5)  # 500 milisaniye bekle
    element = driver.find_element(By.XPATH, "//a[contains(text(), 'Oluştur')]")
    element.click()

    wait_until(S("#gen__1033").exists, timeout_secs=10)
    write("11111111111", into=S("#gen__1033"))
    time.sleep(1.5)  # 500 milisaniye bekle

    #write(ad, into=S("#gen__1035"))
    select_box = Select(driver.find_element(By.ID, "gen__1042"))
    select_box.select_by_visible_text("Türkiye")
    time.sleep(0.5)  # 500 milisaniye bekle

    click(S("#gen__1089"))
    time.sleep(0.5)  # 500 milisaniye bekle

    write("Yapay zeka fotoğraf üretimi", into=S("#gen__1146"))
    write("1", into=S("#gen__1147"))
    Select(driver.find_element(By.ID, "gen__1148")).select_by_visible_text("Adet")

    write(str(tutar).replace('.', ','), into=S("#gen__1149"))
    Select(driver.find_element(By.ID, "gen__1156")).select_by_visible_text("20")
    write(ad, into=S("#gen__1035"))
    driver.execute_script(f"document.getElementById('date-gen__1026').value = '{tarih}';")
    driver.execute_script(f"document.getElementById('gen__1035').value = '{ad}';")
    driver.execute_script(f"document.getElementById('gen__1036').value = '{soyad}';")
    click(S("#gen__1108"))
    time.sleep(1.5)  # 500 milisaniye bekle
    driver.refresh()
