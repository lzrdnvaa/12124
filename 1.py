def binary_and_sum(binary_a, binary_b):
    a = int(binary_a, 2)
    b = int(binary_b, 2)
    and_result = a & b
    sum_result = a + b
    binary_and_result = bin(and_result)[2:]
    binary_sum_result = bin(sum_result)[2:]
    return binary_and_result, binary_sum_result

binary_a = "101101"
binary_b = "110011"
and_result, sum_result = binary_and_sum(binary_a, binary_b)

print("Побитовое AND:", and_result) 
print("Сумма:", sum_result)         