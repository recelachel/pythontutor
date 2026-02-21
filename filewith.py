print("MENAMPILKAN DATA NILAI")

with open("nilai_siswa.txt", "r") as file:

    for line in file:
        data = line.strip().split(",")
        print(data[0], ":", data[1])

print("SELESAI")