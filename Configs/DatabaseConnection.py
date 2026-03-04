from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql://neondb_owner:npg_KBP3qJQf2Ele@ep-calm-mountain-a86jiyss-pooler.eastus2.azure.neon.tech/ba_database?sslmode=require&channel_binding=require"

engine = create_engine(DATABASE_URL)

"""
if __name__ == '__main__':
    try:
        with engine.connect() as conn:
            result = conn.execute(text('SELECT * FROM places'))
            for i in result:
                print(f"The name retrieved is {i[1]}")
    except Exception as e:
        print(f"Connection failed : more details in the following :"
              f"{e}")
"""