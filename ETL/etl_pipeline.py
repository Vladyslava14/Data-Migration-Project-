import sys
from ETL.extract import extract
from ETL.transform import transform_safe
from ETL.load import load_to_postgres

def main():
    print(" Starting ETL pipeline")

    error_log = []
    success_count = 0

    try:
        # EXTRACT
        print("Extracting data from Legacy DB...")
        rows = extract()
        print(f"➡ Extracted rows: {len(rows)}")

        # TRANSFORM + LOAD
        print(" Transforming & Loading...")
        for row in rows:
            record = transform_safe(row, error_log)
            if record:
                try:
                    load_to_postgres(record)
                    success_count += 1
                except Exception as load_error:
                    error_log.append((row, f"Load error: {load_error}"))

        print("\n====================================")
        print("ETL completed")
        print(f"✔ Inserted: {success_count}")
        print(f"Errors: {len(error_log)}")
        print("====================================")

        # якщо були помилки — Java має знати
        if error_log:
            print("Some records failed")
            sys.exit(1)

        sys.exit(0)

    except Exception as pipeline_error:
        print(" Fatal ETL error:", pipeline_error)
        sys.exit(2)


if __name__ == "__main__":
    main()
