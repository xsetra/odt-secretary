# -*- coding: utf-8 -*-


class Budget:
	def __init__(self, yil, tur, gerekce, miktar, birim_fiyat):
		self.yil = yil
		self.tur = tur
		self.gerekce = gerekce
		self.miktar = miktar
		self.birim_fiyat = birim_fiyat
		self.toplam_tutar = self.toplam_tutar_hesapla()

	def toplam_tutar_hesapla(self):
		return (self.miktar * self.birim_fiyat)

	@property
	def get_toplam_tutar(self):
		self.toplam_tutar_hesapla()
		return self.__toplam_tutar
