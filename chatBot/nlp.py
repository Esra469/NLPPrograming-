import json
from difflib import get_close_matches as yakin_sonuclar
#json.dump() #herhangi bir json verisini dosyaya yazmamızı sağlıyor


def veritabanini_yukle():
    with open('C:\\NLPProgram\\chatBot\\chatbot.json','r') as dosya: #dosya okuma işlemi yapıyoruz
         return json.load(dosya)
    
def veritabanina_yaz(veriler):
     with open('C:\\NLPProgram\\chatBot\\chatbot.json','w') as dosya:
          json.dump(veriler,dosya,indent=2)


def yakin_sonuc_bul(soru,sorular):
     eslesenVeri=yakin_sonuclar(soru,sorular,n=1,cutoff=0.6)
     return eslesenVeri[0] if eslesenVeri else None

def cevabini_bul(soru,veritabani):
     for soru_cevaplar in veritabani["sorular"]:#json sorlrı buradan çekiyoruz
          if soru_cevaplar["soru"]==soru:
               return soru_cevaplar["cevap"]
     return None
     
def chat_bot():
     veritabani=veritabanini_yukle()
     while True:
          soru=input("Siz: ")

          if soru=='çık':
               break
          #veritabanındaki sorular verisi soru_cevap olarak tutulacak bunlar da liste olarak alınacak
          gelen_sonuc=yakin_sonuc_bul(soru,[soru_cevaplar["soru"] for soru_cevaplar in veritabani["sorular"]])
          
          if gelen_sonuc:
               verilecek_cevap=cevabini_bul(soru,veritabani)
               print(f"Bot :{verilecek_cevap}")
          else:
            print("Bot : bunu nasıl cevaplayacağımı bilmiyorum")
            yeni_cevap=input("öğretmek için yazabilir veya 'geç' diyebilirsinzi")
            
            if yeni_cevap !='geç':
                 veritabani["sorular"].append({
                      "soru":soru,
                      "cevap":yeni_cevap
                 })
                 veritabanina_yaz(veritabani)
                 print("Bot: teşekkürler sayenizde yeni bir şey öğrendim")

    
if __name__=='__main__': #ilk bunu çalıştıracak anlamına gelir 
     chat_bot()