# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import pymysql
    import pandas as pd
    connect=pymysql.Connect(host='localhost',user='root',passwd='1996812wjAbk&ys',database='leetcode',charset='utf8')
    cursor=connect.cursor()
    sql_drop = "DROP TABLE IF EXISTS {}".format("Person","Address")
    cursor.execute(sql_drop)
    sqls=["Create table If Not Exists Person (PersonId int, FirstName varchar(255), LastName varchar(255))",
         "Create table If Not Exists Address (AddressId int, PersonId int, City varchar(255), State varchar(255))",
         "Truncate table Person",
         "insert into Person (PersonId, LastName, FirstName) values ('1', 'Wang', 'Allen')",
         "insert into Person (PersonId, LastName, FirstName) values ('2', 'Alice', 'Bob')",
         "Truncate table Address",
         "insert into Address (AddressId, PersonId, City, State) values ('1', '2', 'New York City', 'New York')",
         "insert into Address (AddressId, PersonId, City, State) values ('2', '3', 'Leetcode', 'California')"]
    for sql in sqls:
        cursor.execute(sql)
    query="SELECT Person.FirstName, Person.LastName, Address.City, Address.State FROM Person LEFT JOIN Address on Person.PersonId = Address.PersonId"
    df = pd.read_sql(query, connect)
    cursor.execute("SHOW DATABASES")
    print('finished')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
