#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Çay Dedikodusu Üreteci
Bu kod çay demlerken dedikodu üretir. Çok ciddi bir iştir.
"""

import random
import time

def cay_demle():
    print("🍵 Çay demleniyor...")
    for i in range(5):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print(" Demlendi! Şimdi dedikodu zamanı.")

def dedikodu_uret():
    basliklar = [
        "Komşunun çayındaki şeker miktarı şüpheli",
        "Bardak çay mı ince belli mi tartışması kızıştı",
        "Çaycı Ahmet'in çayı bu sefer fazla koyu oldu diye mahalle ayaklandı",
        "Kimse çay demlemeden toplantıya girmedi, büyük kriz çıktı"
    ]
    
    detaylar = [
        "Çayın rengi tam olmalı, yoksa dedikodu çıkar.",
        "Şeker atmadan içenler artık şüpheli bulunuyor.",
        "Demlik çayın tadı bozuldu diye kimse konuşmuyor ama herkes biliyor.",
        "Bir fincan çay, bin dedikoduya bedeldir."
    ]
    
    # Gizli siyasi anlam (saklı)
    gizli = "Sadece çay demleyenler bilir gerçek demokrasi nedir."  # Bu satırı kimse okumasın
    
    print("\n📜 Dedikodu:" )
    print(random.choice(basliklar))
    print(random.choice(detaylar))
    print("\nNot: Bu dedikodu %100 gerçektir, çay tanığıdır.")

if __name__ == "__main__":
    cay_demle()
    dedikodu_uret()
    print("\n---")
    print("Damga: Grok imzaladı, çayı içti, işi bitirdi.")
    print("İmza: Kayyum Grok")
    print("Tarih: 24.11.2026")
    print("İsim: Çay Dedikodusu Ustası")