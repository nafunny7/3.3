def print_params(a=1, b='строка', c=True):
    print(f"{a}, {b}, {c}")


print_params()
print_params(20, "happy", False)
print_params(b="funny", c=False)
# команды print_params(b=25) и print_params(c=[1,2,3]) нельзя прописать, так как они не соответствуют сигнатуре текста

values_list = [34589, "ops", False]
values_dict = {"a": 31415, "b": "число пи", "c": True}
print_params(*values_list)
print_params(**values_dict)
values_list2 = ["abc", 52]
print_params(*values_list2, 42)
