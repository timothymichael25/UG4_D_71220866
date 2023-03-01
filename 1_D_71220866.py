def aritmatika(a, b, n):
    total = (n/2)*(2*a + (n-1)*b)
    return total
a = float(input("Masukkan bilangan awal bang    : "))
b = float(input("Masukkan selisih bilangan bang : "))
n = int(input("Masukkan banyak sukunya bang   : "))
total = aritmatika(a, b, n)
print("Total dari deret aritmatika adalah", total, 'segini ya bang')