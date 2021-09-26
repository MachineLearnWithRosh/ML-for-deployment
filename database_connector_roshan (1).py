import pypyodbc 


class Conn:
    def __init__(self, db_server, db_name, db_username, db_password):
        self.db_username= db_username
        self.db_password = db_password
        self.db_server = db_server
        self.db_name = db_name
        self.conn = pypyodbc.connect("Driver={SQL Server Native Client 11.0};"
                        "Server="+self.db_server+";Database="+self.db_name+";uid="+self.db_username+";pwd="+self.db_password,autocommit=True)
        #self.conn = mysql.connector.connect(host= cfg.db_ip, user=cfg.db_user_name, password=self.db_password)
#         self.conn = pypyodbc.connect("Driver={SQL Server Native Client 11.0};"\
#                         "Server={0};".format(self.db_server)\
#                         "Database={0}".format(self.db_name)
#                         "uid={0};pwd={1}".format(self.db_username,self.db_password),autocommit=True)
        self.cursor = self.conn.cursor()


    def make_db(self):

        try:
            #self.conn.cursor.execute("CREATE DATABASE {}".format(cfg.db_name))
            #self.conn.cursor.execute("USE {}".format(cfg.db_name))
            #self.cursor.execute("CREATE DATABASE {}".format(cfg.db_name))
            self.cursor.execute("USE {}".format(cfg.db_name))
            print('database created!')
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))


    def drop_table(self):
        try:
            #self.conn.cursor.execute("DROP DATABASE {}".format(cfg.db_name))
            self.cursor.execute("DROP DATABASE {}".format(cfg.db_name))
            print('database dropped!')
        except mysql.connector.Error as err:
            print("Somethin went wrong: {}".format(err))


    # def make_table(self):
    #     try:
    #         #self.conn.cursor.execute(" use {}".format(cfg.db_name))  #Request ID INT NOT NULL PRIMARY KEY UNIQUE   DECIMAL(24,5)
    #         #self.conn.cursor.execute(
    #         self.cursor.execute(" use {}".format(cfg.db_name))
    #         self.cursor.execute(
    #             "CREATE TABLE {} (Request_ID CHAR(50) NOT NULL PRIMARY KEY, Candidate ID INT(20), Predicted_Performance CHAR(25), Confidence_Level Float(64,5), Method_Used CHAR(25), Decision_Driver1 CHAR(25), Decision_Driver2 CHAR(25), Decision_Driver3 CHAR(25), Decision_Driver4 CHAR(25), Decision_Driver5 CHAR(25), business_position CHAR(25),gender CHAR(25), year_of_birth INT(25), marital_status CHAR(25),Education_level CHAR(25), residential_area CHAR(25), business_Areas CHAR(25),Q4 CHAR(25), Q5 CHAR(25), Q6 CHAR(25), Q7 CHAR(25), Q8 CHAR(25), Q11 CHAR(25), Q15 CHAR(25), Q17 CHAR(25), Q18 CHAR(25), Q19 CHAR(25), Q20 CHAR(25), Q24 CHAR(25), Q28 CHAR(25), Q29 CHAR(25),Q30 CHAR(25), Q33 CHAR(25), Q34 CHAR(25), Q35 CHAR(25),Q38 CHAR(25), Q39 CHAR(25), Q40 CHAR(25), Q45 CHAR(25), Q47 CHAR(25), Q48 CHAR(25)""); ".format(
    #                 cfg.table_name))
    #         print('table created!')
    #     except mysql.connector.Error as err:
    #         print("Something went wrong: {}".format(err))

    def make_table(self):
        try:
            #self.conn.cursor.execute(" use {}".format(cfg.db_name))  #Request ID INT NOT NULL PRIMARY KEY UNIQUE   DECIMAL(24,5)
            #self.conn.cursor.execute(
            #self.cursor.execute(" use {}".format(cfg.db_name))
            self.cursor.execute('''CREATE TABLE tstndlrn_staging.Prediction_Table1 (Request_ID VARCHAR(50), 
                    Candidate_ID INT, Predicted_Performance VARCHAR(25), Confidence_Level Float,
                    Method_Used VARCHAR(25), Decision_Driver1 VARCHAR(25), Decision_Driver2 VARCHAR(25), 
                    Decision_Driver3 VARCHAR(25), Decision_Driver4 VARCHAR(25), Decision_Driver5 VARCHAR(25),
                    business_position VARCHAR(25), gender VARCHAR(25), year_of_birth INT, marital_status VARCHAR(25),
                    Education_level VARCHAR(25), residential_area VARCHAR(25), business_Areas VARCHAR(25),Q4 VARCHAR(25), 
                    Q5 VARCHAR(25), Q6 VARCHAR(25), Q7 VARCHAR(25), Q8 VARCHAR(25), Q11 VARCHAR(25), Q15 VARCHAR(25),
                    Q17 VARCHAR(25), Q18 VARCHAR(25), Q19 VARCHAR(25), Q20 VARCHAR(25), Q24 VARCHAR(25), Q28 VARCHAR(25),
                    Q29 VARCHAR(25),Q30 VARCHAR(25), Q33 VARCHAR(25), Q34 VARCHAR(25), Q35 VARCHAR(25),Q38 VARCHAR(25), 
                    Q39 VARCHAR(25), Q40 VARCHAR(25), Q45 VARCHAR(25), Q47 VARCHAR(25), Q48 VARCHAR(25));''')
            print('table created!')
        except Exception as err:
            print("Something went wrong: {}".format(err))


    def insert_data(self, d, db_table_name):
        try:
            #self.conn.cursor.execute("USE {}".format(cfg.db_name))
            #self.cursor.execute("USE {}".format(cfg.db_name))
            insert = ("INSERT INTO {} (Request_ID, Candidate_ID, Predicted_Performance, Confidence_Level, Method_Used, Decision_Driver1, Decision_Driver2, Decision_Driver3, Decision_Driver4, Decision_Driver5, business_position, gender, year_of_birth, marital_status, Education_level, residential_area, business_Areas,Q4, Q5, Q6, Q7, Q8, Q11, Q15, Q17, Q18, Q19, Q20, Q24, Q28, Q29,Q30, Q33, Q34, Q35,Q38, Q39, Q40, Q45, Q47, Q48) VALUES (%s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);".format(
                db_table_name))  # insert in table
            #self.conn.cursor.execute(insert
#             self.cursor.execute(insert, (respose_dictionary[cfg.logged_cols[0]], respose_dictionary[cfg.logged_cols[1]],
#                                         respose_dictionary[cfg.logged_cols[2]], float(respose_dictionary[cfg.logged_cols[3]]), respose_dictionary[cfg.logged_cols[4]],
#                                          respose_dictionary[cfg.logged_cols[5]], respose_dictionary[cfg.logged_cols[6]], respose_dictionary[cfg.logged_cols[7]], respose_dictionary[cfg.logged_cols[8]],
#                                          respose_dictionary[cfg.logged_cols[9]], respose_dictionary[cfg.input_data_cols[0]], respose_dictionary[cfg.input_data_cols[1]],respose_dictionary[cfg.input_data_cols[2]],
#                                          respose_dictionary[cfg.input_data_cols[3]],
#                                          respose_dictionary[cfg.input_data_cols[4]],
#                                          respose_dictionary[cfg.input_data_cols[5]],
#                                          respose_dictionary[cfg.input_data_cols[6]], respose_dictionary[cfg.input_data_cols[7]], respose_dictionary[cfg.input_data_cols[8]],respose_dictionary[cfg.input_data_cols[9]],
#                                          respose_dictionary[cfg.input_data_cols[10]],
#                                          respose_dictionary[cfg.input_data_cols[11]],
#                                          respose_dictionary[cfg.input_data_cols[12]],
#                                          respose_dictionary[cfg.input_data_cols[13]],
#                                          respose_dictionary[cfg.input_data_cols[14]],
#                                          respose_dictionary[cfg.input_data_cols[15]],
#                                          respose_dictionary[cfg.input_data_cols[16]],
#                                          respose_dictionary[cfg.input_data_cols[17]],
#                                          respose_dictionary[cfg.input_data_cols[18]],
#                                          respose_dictionary[cfg.input_data_cols[19]],
#                                          respose_dictionary[cfg.input_data_cols[20]],
#                                          respose_dictionary[cfg.input_data_cols[21]],
#                                          respose_dictionary[cfg.input_data_cols[22]],
#                                          respose_dictionary[cfg.input_data_cols[23]],
#                                          respose_dictionary[cfg.input_data_cols[24]],
#                                          respose_dictionary[cfg.input_data_cols[25]],
#                                          respose_dictionary[cfg.input_data_cols[26]],
#                                          respose_dictionary[cfg.input_data_cols[27]],
#                                          respose_dictionary[cfg.input_data_cols[28]],
#                                          respose_dictionary[cfg.input_data_cols[29]],
#                                          respose_dictionary[cfg.input_data_cols[30]]
                                        # ))
            #self.conn.cursor.execute("COMMIT")
            SQLCommand = "INSERT INTO tstndlrn_staging.Prediction_Table1 (Request_ID,Candidate_ID,Predicted_Performance,Confidence_Level,Method_Used,\
Decision_Driver1,Decision_Driver2,Decision_Driver3,Decision_Driver4,Decision_Driver5,business_position,gender,year_of_birth,\
marital_status,Education_level,residential_area,business_Areas,Q4,Q5,Q6,Q7,Q8,Q11,Q15,Q17,Q18,Q19,Q20,Q24,Q28,Q29,\
Q30,Q33,Q34,Q35,Q38,Q39,Q40,Q45,Q47,Q48) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);"
            values = ['IQVEAM',611746,'Low',0.56,'Unsupervised','Education','Education','Education','Education','Education','FWO','F',1997,'S','DAIHOC','South','South','B','C','D','C','C','D','B','C','B','D','D','D','A','D','B','C','B','D','B','D','D','B','C','A']
            self.cursor.execute(SQLCommand, values)
            self.cursor.execute("COMMIT")

            print("done!")


            # return show_data(database,table)
        except pypyodbc.Error as ex:
            print("Something went wrong: {}".format(ex.args[1]))


    def show_data(self):
        # try:
        use = ("USE {}".format(cfg.db_name))
        #self.conn.cursor.execute(use)
        self.cursor.execute(use)
        select = ("SELECT *FROM {}".format(cfg.db_table_name))
        #self.conn.cursor.execute(select)
        self.cursor.execute(select)

        #result = self.conn.cursor.fetchall()
        result = self.cursor.fetchall()

        print(result)