# wap in python to fill  in  a   letter  template  given  below with the  name and date

letter = '''Dear <|Name|>,
You are selected as a  intern  in Microsoft
<|Date|>
'''
print(letter.replace('<|Name|>',"Himanshi Chouhan").replace('<|Date|>',"25 July 2026"))
