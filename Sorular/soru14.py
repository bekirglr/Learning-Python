#bir metin içerisnde ki sesli ve sessiz harfleri bulma

sesli_harfler = "aeıioöuü"
sessiz_harfler = "bcçdfgğhjklmnprsştvyz"
sesliler=""
sessizler=""
a=input("bir metin giriniz")

for i in a:
     if i in sesli_harfler:
           sesliler=sesliler+i
     if i in sessiz_harfler:
           sessizler=sessizler+i

print("sesli harfler",sesliler)
print("sessiz harfler",sessizler)