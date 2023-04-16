import ctypes
dll_path = r'Z:\___advanced python\testDll.dll'
dl = ctypes.cdll.LoadLibrary(dll_path)

# If there is no error, the dll was loaded!

# Declare the return type of the C function
dl.doubleFunc.restype = ctypes.c_double

# Configure the input with it's type
double_in = ctypes.c_double(1.23)

print(dl.doubleFunc(double_in))


a = ctypes.c_int(2)
b = ctypes.c_int(3)

dl.swap(ctypes.byref(a), ctypes.byref(b))

print(a)
print(b)