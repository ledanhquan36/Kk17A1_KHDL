#các số tờ tiền : 500000 , 200000 , 100000 , 50000
tien_muon_doi = 2250000
so_to_1 = tien_muon_doi //500000
tien_con_lai = tien_muon_doi%5000000
so_to_2 = tien_con_lai //200000
tien_con_lai = tien_con_lai%2000000
so_to_3 = tien_muon_doi //100000
tien_con_lai = tien_con_lai %100000
so_to_4 = tien_muon_doi // 50000
tien_con_lai = tien_con_lai %50000
print(so_to_1)
print(so_to_2)
print(so_to_3)
print(so_to_4)