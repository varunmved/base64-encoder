import base64

a = raw_input("Input the string you want to base64 encode\n")
encoded = base64.b64encode(a)

print("\nInput Value: %s\nEncoded Value %s" % (a, encoded))
