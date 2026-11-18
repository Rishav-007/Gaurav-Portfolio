with open(r"D:\Projects\gaurav-portfolio\index.html", encoding="utf-8") as f:
    s=f.read()
print("Length:", len(s))
print("Has contact-link:", "contact-link" in s)
print("Has contact-cta:", "contact-cta" in s)
print("Has gradient text:", "background-clip:text" in s)
