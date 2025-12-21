from lxml import etree

# Завантажуємо XML і XSLT
xml = etree.parse(r"C:\Projects\Data Migration\dataMigrationProject\xslt\legacy_customers.xml")
xslt = etree.parse(r"C:\Projects\Data Migration\dataMigrationProject\xslt\customer_transform.xslt")
transform = etree.XSLT(xslt)

# Виконуємо трансформацію
new_xml = transform(xml)

# Зберігаємо результат
new_xml.write("transformed_customers.xml", pretty_print=True, encoding="utf-8")


