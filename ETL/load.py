from lxml import etree
from datetime import datetime
import re

def parse_date(value):
    if not value:
        return None

    formats = [
        "%d-%m-%Y",
        "%d/%m/%Y",
        "%Y/%m/%d",
        "%Y-%m-%d",
        "%m-%d-%Y",
        "%m/%d/%Y",
    ]

    for fmt in formats:
        try:
            return datetime.strptime(value, fmt).date()
        except:
            pass

    try:
        return datetime.fromisoformat(value).date()
    except:
        return None

def normalize_phone(phone):
    if not phone:
        return None
    return re.sub(r"\D", "", phone)

def load_customers():
    xml = etree.parse("transformed_customers.xml")
    records = []

    for c in xml.xpath("//customer"):
        record = {
            "first_name": c.findtext("first_name"),
            "last_name": c.findtext("last_name"),
            "birthdate": parse_date(c.findtext("birthdate")),
            "street": c.findtext("street"),
            "city": c.findtext("city"),
            "phone": normalize_phone(c.findtext("phone")),
            "created_at": parse_date(c.findtext("created_at")),
        }
        records.append(record)

    return records

