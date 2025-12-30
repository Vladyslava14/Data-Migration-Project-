from datetime import datetime
import re

def parse_date(value):
    if not value:
        return None

    value = value.strip()
    if value == "":
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
        except ValueError:
            pass

    #спроба автоматичного парсингу ISO-дати
    try:
        return datetime.fromisoformat(value).date()
    except:
        return None

def normalize_phone(phone):
    if not phone:
        return None
    digits = re.sub(r"\D", "", phone)
    return digits if len(digits) >= 10 else None

def split_full_name(full_name):
    if not full_name:
        return None, None
    parts = full_name.strip().split()
    if len(parts) == 1:
        return parts[0], None
    return parts[0], " ".join(parts[1:])


def split_address(address):
    if not address:
        return None, None
    parts = [p.strip() for p in address.split(",")]
    if len(parts) >= 2:
        return parts[0], parts[1]
    return address, None


def transform(row):
    """
    row:
    (cust_id, full_name, birthdate, address, phone, created_at)
    """

    cust_id, full_name, birthdate, address, phone, created_at = row

    first_name, last_name = split_full_name(full_name)

    transformed = {
        "first_name": first_name,
        "last_name": last_name,
        "birthdate": parse_date(birthdate),
        "street": split_address(address)[0],
        "city": split_address(address)[1],
        "phone": normalize_phone(phone),
        "created_at": parse_date(created_at)
    }

    return transformed

def is_valid(record):
    return record["first_name"] and record["phone"]

def transform_safe(row, error_log):
    try:
        record = transform(row)
        if not is_valid(record):
            raise ValueError("Invalid mandatory fields")
        return record
    except Exception as e:
        error_log.append((row, str(e)))
        return None
