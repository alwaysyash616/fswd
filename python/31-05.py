"""
Assignment: 31
Problem: 05
Topic: dict
Description: Write a python script to create a dict object from a list of city names in such a way the alphabets are keys of the dictionary and list of city names starting from that alphabet will be its data value.
Date: 07-07-2026
"""

cities=['Morbi','Mehsana','Surendranagar','Mahisagar','Valsad','Dang','Botad','Amreli','Tapi','Panchmahal','Bhavnagar','Banaskantha','Narmada','Porbandar','Kutch','Aravalli','Junagarh','Cuddalore','Chengalpattu','Vellore','Tiruvallur','Ranipet','Erode','Mysore','Chennai','Surat','Bagalkot','Bidar','Yadgir','Kolar','Haveri','Belagavi','Chamrajnagar','Chitradurga','Asansol']
d1=dict()
for letter in 'abcedfghijklmnopqrstuvwxyz':
    temp=[city for city in cities if city.startswith(letter.upper())]
    if len(temp)>0:
        d1[letter]=temp
for k,o in d1.items():
    print(k,o)