from Configs.DatabaseConnection import *

def retrieveNames():
    names=[]
    try:
        with engine.connect() as conn:
            result = conn.execute(text('SELECT *'
                                  'FROM places'))
            for i in result:
                names.append(i[1])
    except Exception as e:
        print(f"There was an issue with executing the following command:"
              f"{e}")

    return names