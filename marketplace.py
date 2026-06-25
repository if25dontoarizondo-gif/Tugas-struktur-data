import csv, os

FILE = "data_marketplace.csv"
HEADER = ["id", "nama_produk", "kategori", "harga", "stok"]

# ================= LINKED LIST =================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def tambah(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            return

        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node

    def tampil(self):
        data = []
        cur = self.head
        while cur:
            data.append(cur.data)
            cur = cur.next
        return data

    def cari(self, id_produk):
        cur = self.head
        while cur:
            if cur.data["id"] == id_produk:
                return cur.data
            cur = cur.next
        return None

    def hapus(self, id_produk):
        cur = self.head
        prev = None

        while cur:
            if cur.data["id"] == id_produk:
                if prev:
                    prev.next = cur.next
                else:
                    self.head = cur.next
                return True

            prev = cur
            cur = cur.next

        return False


# ================= QUEUE =================
class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, produk):
        self.data.append(produk)

    def dequeue(self):
        if self.data:
            return self.data.pop(0)
        return None

    def tampil(self):
        return self.data


# ================= CSV =================
def load_csv(ll):
    if not os.path.exists(FILE):
        with open(FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(HEADER)
        return

    with open(FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            ll.tambah(row)

def save_csv(ll):
    with open(FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=HEADER)
        writer.writeheader()
        writer.writerows(ll.tampil())


# ================= FITUR =================
def generate_id(ll):
    return "P" + str(len(ll.tampil()) + 1).zfill(3)

def tambah_produk(ll):
    data = {
        "id": generate_id(ll),
        "nama_produk": input("Nama Produk : "),
        "kategori": input("Kategori    : "),
        "harga": input("Harga       : "),
        "stok": input("Stok        : ")
    }

    ll.tambah(data)
    save_csv(ll)
    print("Produk berhasil ditambahkan!")

def lihat_produk(ll):
    data = ll.tampil()

    if not data:
        print("Data produk kosong.")
    else:
        print("\n=== DATA PRODUK MARKETPLACE ===")
        for p in data:
            print(
                p["id"], "-",
                p["nama_produk"], "-",
                p["kategori"], "- Rp",
                p["harga"], "- Stok:",
                p["stok"]
            )

def cari_produk(ll):
    id_produk = input("Masukkan ID produk: ")
    produk = ll.cari(id_produk)

    if produk:
        print("Ditemukan:", produk)
    else:
        print("Produk tidak ditemukan.")

def update_produk(ll):
    id_produk = input("Masukkan ID produk: ")
    produk = ll.cari(id_produk)

    if produk:
        produk["nama_produk"] = input("Nama produk baru : ")
        produk["kategori"] = input("Kategori baru    : ")
        produk["harga"] = input("Harga baru       : ")
        produk["stok"] = input("Stok baru        : ")

        save_csv(ll)
        print("Data produk berhasil diupdate!")
    else:
        print("Produk tidak ditemukan.")

def hapus_produk(ll):
    id_produk = input("Masukkan ID produk: ")

    if ll.hapus(id_produk):
        save_csv(ll)
        print("Data produk berhasil dihapus!")
    else:
        print("Produk tidak ditemukan.")

def sorting_produk(ll):
    data = ll.tampil()
    data.sort(key=lambda x: x["nama_produk"])

    print("\nHasil sorting berdasarkan nama produk:")
    for p in data:
        print(
            p["id"], "-",
            p["nama_produk"], "- Rp",
            p["harga"], "- Stok:",
            p["stok"]
        )

def antrean_pesanan(ll, q):
    id_produk = input("Masukkan ID produk yang ingin dipesan: ")
    produk = ll.cari(id_produk)

    if produk:
        q.enqueue(produk)
        print("Produk masuk ke antrean pesanan.")
    else:
        print("Produk tidak ditemukan.")

def proses_pesanan(q):
    produk = q.dequeue()

    if produk:
        print("Pesanan sedang diproses:", produk["nama_produk"])
    else:
        print("Antrean pesanan kosong.")


# ================= MAIN PROGRAM =================
def main():
    ll = LinkedList()
    q = Queue()

    load_csv(ll)

    while True:
        print("\n=== SISTEM MARKETPLACE SEDERHANA ===")
        print("1. Tambah Produk")
        print("2. Lihat Produk")
        print("3. Cari Produk")
        print("4. Update Produk")
        print("5. Hapus Produk")
        print("6. Sorting Produk")
        print("7. Tambah Antrean Pesanan")
        print("8. Proses Pesanan")
        print("9. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            tambah_produk(ll)
        elif pilih == "2":
            lihat_produk(ll)
        elif pilih == "3":
            cari_produk(ll)
        elif pilih == "4":
            update_produk(ll)
        elif pilih == "5":
            hapus_produk(ll)
        elif pilih == "6":
            sorting_produk(ll)
        elif pilih == "7":
            antrean_pesanan(ll, q)
        elif pilih == "8":
            proses_pesanan(q)
        elif pilih == "9":
            save_csv(ll)
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")


main()