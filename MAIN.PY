import datetime

class Receipt:
    def __init__(self, client_name, dedication, width, length, height, material_price):
        self.creation_time = datetime.datetime.now()
        self.client_name = client_name
        self.dedication = dedication
        self.width = width
        self.length = length
        self.height = height
        self.material_price = material_price
        self.total_amount = self.calculate_total()

    def calculate_total(self):
        labor_cost = 15
        VAT = 0.21
        product_price = (len(self.dedication) * 1.2) + (
            (self.width / 100) * (self.length / 100) * (self.height / 100) / 3 * self.material_price)
        VAT_amount = (product_price + labor_cost) * VAT
        total = (product_price + labor_cost) + VAT_amount
        return total

    def print_receipt(self):
        print("Rēķins")
        print("Izveidošanas laiks:", self.creation_time)
        print("Klienta vārds:", self.client_name)
        print("Veltījums:", self.dedication)
        print("Lādītes izmērs:", self.width, "mm x", self.length, "mm x", self.height, "mm")
        print("Kopējā summa: {:.2f} EUR".format(self.total_amount))

    def save_to_file(self):
        filename = f"receipt_{self.client_name}.txt"
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write("Rēķins\n")
                file.write("Izveidošanas laiks: {}\n".format(self.creation_time))
                file.write("Klienta vārds: {}\n".format(self.client_name))
                file.write("Veltījums: {}\n".format(self.dedication))
                file.write("Lādītes izmērs: {} mm x {} mm x {} mm\n".format(self.width, self.length, self.height))
                file.write("Kopējā summa: {:.2f} EUR\n".format(self.total_amount))
            print(f"Rēķins saglabāts failā: {filename}")
        except Exception as e:
            print(f"Kļūda saglabājot failā: {e}")

def main():
    print("Šī programma ļauj izveidot rēķinus koka lādīšu pasūtījumiem.")
    
    client_name = input("Ievadiet klienta vārdu: ")
    dedication = input("Ievadiet veltījuma tekstu: ")
    
    while True:
        try:
            width = int(input("Ievadiet lādītes platumu (mm): "))
            length = int(input("Ievadiet lādītes garumu (mm): "))
            height = int(input("Ievadiet lādītes augstumu (mm): "))
            material_price = float(input("Ievadiet kokmateriāla cenu (EUR/m2): "))
            break  # Ja viss ir kārtībā, beidz ciklu
        except ValueError:
            print("Lūdzu, ievadiet derīgas skaitliskas vērtības.")

    receipt = Receipt(client_name, dedication, width, length, height, material_price)
    
    receipt.print_receipt()
    receipt.save_to_file()

if __name__ == "__main__":
    main()
