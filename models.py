from app import db
from sqlalchemy.dialects.postgresql import JSON

class User(db.Model):
    __table__ = 'User'
    User_ID=    db.column(db.Integer, primary_key=True)
    Email=      db.column(db.String(80),nullable=False)
    Password=   db.column(db.String(80),nullable=False)
    FirstName=  db.column(db.String(80),nullable=False)
    MiddleName= db.column(db.String(80),nullable=False)
    LastName=   db.column(db.String(80),nullable=False)
    H_no=       db.column(db.String(80),nullable=False)
    City=       db.column(db.String(80),nullable=False)
    State=      db.column(db.String(80),nullable=False)
    Pincode=    db.column(db.Integer)
    Phone=      db.column(db.String80)
    def __init__(self,User_ID,Email,Password,FirstName,MiddleName,LastName,H_no,City,State,Pincode,Phone):
        self.User_ID=User_ID
        self.Email=Email
        self.Password=Password
        self.FirstName=FirstName
        self.MiddleName=MiddleName
        self.LastName=LastName
        self.H_no=H_no
        self.City=City
        self.State=State
        self.Pincode=Pincode
        self.Phone=Phone
    

class Vechile(db.Model):
    __tablename__ = 'Vechile'
    Vehicle_ID            =db.Column(db.Integer, primary_key=True)
    User_ID               =db.column(db.Integer,nullable=False)
    Policy_ID             =db.column(db.Integer,nullable=False)
    Vehicle_Reg_Number    =db.column(db.String(80),nullable=False)
    Vehicle_Value         =db.column(db.Integer,nullable=False)
    Vehicle_TYPE          =db.column(db.String(80),nullable=False)
    Vehicle_Size          =db.column(db.Integer,nullable=False)
    Number_of_passenger   =db.column(db.Integer,nullable=False)
    Engine_number         =db.column(db.String(80),nullable=False)
    Chasis_Number         =db.column(db.String(80),nullable=False)
    Vechile_Model         =db.column(db.String(80),nullable=False)
    Year                  =db.column(db.Integer,nullable=False)
    Created_DT            =db.column(db.DateTime,nullable=False)
    
    def __init__(self,Vehicle_ID,User_ID,Policy_ID,Vehicle_Reg_Number,Vehicle_Value,Vehicle_TYPE,Vehicle_Size,Number_of_passenger,Engine_number,Chasis_Number,Vechile_Model,Year):
        self.Vehicle_ID=Vehicle_ID
        self.User_ID=User_ID
        self.Policy_ID=Policy_ID
        self.Vehicle_Reg_Number=Vehicle_Reg_Number
        self.Vehicle_Value=Vehicle_Value
        self.Vehicle_TYPE=Vehicle_TYPE
        self.Vehicle_Size=Vehicle_Size
        self.Number_of_passenger=Number_of_passenger
        self.Engine_number=Engine_number
        self.Chasis_Number=Chasis_Number
        self.Vechile_Model=Vechile_Model
        self.Year=Year

class Application(db.Model):
    __table__ = 'Application'
    Application_ID     = db.Column(db.Integer,primary_key=True)
    User_id            = db.column(db.Integer)
    Vechile_ID         = db.column(db.Integer)                 
    Application_Status = db.column(db.String80)                                          
    Coverage           = db.column(db.String80)                                
    Created_DT         = db.column(db.DateTime)                
    Updated_DT         = db.column(db.DateTime) 
        
    def __init__(self,Application_ID,User_id,Vechile_ID,Application_Status,Coverage,Created_DT,Updated_DT):
        self.Application_ID    =Application_ID    
        self.User_id           =User_id           
        self.Vechile_ID        =Vechile_ID        
        self.Application_Status=Application_Status
        self.Coverage          =Coverage          
        self.Created_DT        =Created_DT        
        self.Updated_DT        =Updated_DT 

class Claim(db.Model):
    __table__ = 'Claim'
    Claim_ID       = db.Column(db.Integer,primary_key=True) 
    User_ID        =db.column(db.Integer,nullable=False) 
    Application_ID =db.column(db.Integer,nullable=False) 
    Claim_Amount   =db.column(db.Integer,nullable=False) 
    Damage_type    =db.column(db.String(80),nullable=False) 
    Date_of_claim  =db.column(db.DateTime,nullable=False)
    Status         =db.column(db.String(80),nullable=False)
    Created_DT     =db.column(db.DateTime,nullable=False)
    Updated_DT     =db.column(db.DateTime,nullable=False)
    def __init__(self,Claim_ID,User_ID,Application_ID,Claim_Amount,Damage_type,Date_of_claim,Status,Created_DT,Updated_DT):
        self.Claim_ID       =Claim_ID       
        self.User_ID        =User_ID        
        self.Application_ID =Application_ID 
        self.Claim_Amount   =Claim_Amount   
        self.Damage_type    =Damage_type    
        self.Date_of_claim  =Date_of_claim  
        self.Status         =Status         
        self.Created_DT     =Created_DT     
        self.Updated_DT     =Updated_DT 

class Insurance_Company(db.Model):
    __table__ = 'Insurance_Company'
    Company_Name              = db.Column(db.String(80),primary_key=True)
    Company_Contact_Number    =db.column(db.String(80),nullable=False)  
    Company_Email             =db.column(db.String(80),nullable=False)  
    Company_Website           =db.column(db.String(80),nullable=False)  
    Company_Location          =db.column(db.String(80),nullable=False)  
    Company_Department        =db.column(db.String(80),nullable=False)  
    Company_Office_Name       =db.column(db.String(80),nullable=False)  
    Created_DT                =db.column(db.DateTime,nullable=False)
    Updated_DT                =db.column(db.DateTime,nullable=False)
    def __init__(self,Company_Name,Company_Contact_Number,Company_Email,Company_Website,Company_Location,Company_Department,Company_Office_Name,Created_DT,Updated_DT):
        self.Company_Name          =Company_Name          
        self.Company_Contact_Number=Company_Contact_Number
        self.Company_Email         =Company_Email         
        self.Company_Website       =Company_Website       
        self.Company_Location      =Company_Location      
        self.Company_Department    =Company_Department    
        self.Company_Office_Name   =Company_Office_Name   
        self.Created_DT            =Created_DT            
        self.Updated_DT            =Updated_DT   

class Insurance_Policy(db.Model):
    __table__ = 'Insurance_Policy'
    Policy_ID        = db.Column(db.Integer,primary_key=True)
    Application_ID   = db.column(db.Integer,nullable=False)
    User_id          = db.column(db.Integer,nullable=False)
    Department_name  = db.column(db.String(80),nullable=False)
    Policy_Number    = db.column(db.String(80),nullable=False)
    End_date         = db.column(db.Integer,nullable=False)
    Term_Condition   = db.column(db.String(80),nullable=False)
    Created_DT       = db.column(db.DateTime,nullable=False) 
    Updated_DT       = db.column(db.DateTime,nullable=False)
    def __init__(self,Policy_ID,Application_ID,User_id,Department_name,Policy_Number,End_date,Term_Condition,Created_DT,Updated_DT):
        self.Policy_ID        =Policy_ID      
        self.Application_ID   =Application_ID 
        self.User_id          =User_id        
        self.Department_name  =Department_name
        self.Policy_Number    =Policy_Number  
        self.End_date         =End_date       
        self.Term_Condition   =Term_Condition 
        self.Created_DT       =Created_DT     
        self.Updated_DT       =Updated_DT    

class Quote(db.Model):
    __table__ = 'Quote'
    Quote_ID       =db.Column(db.Integer,primary_key=True)
    Application_ID =db.Column(db.Integer,nullable=False)
    User_id        =db.Column(db.Integer,nullable=False)
    issue_date     =db.Column(db.DateTime,nullable=False)
    Start_date     =db.Column(db.DateTime,nullable=False)
    End_date       =db.Column(db.DateTime,nullable=False)
    Description    =db.Column(db.Integer,nullable=False)
    Created_DT     =db.Column(db.DateTime,nullable=False)
    Updated_DT     =db.Column(db.DateTime,nullable=False)
    
    def __init__(self,Quote_ID,Application_ID ,User_id,issue_date,Start_date,End_date,Description,Created_DT,Updated_DT):
        self.Quote_ID       =Quote_ID         
        self.Application_ID =Application_ID 
        self.User_id        =User_id        
        self.issue_date  =issue_date  
        self.Start_date     =Start_date     
        self.End_date       =End_date       
        self.Description    =Description    
        self.Created_DT     =Created_DT     
        self.Updated_DT     =Updated_DT     
        
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)


    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    exam_rank = db.Column(db.Integer)

class Land(db.Model):
    __tablename__ = 'land'
    id = db.Column(db.Integer, primary_key=True)
    land_doc = db.Column(db.String)
    land_area = db.Column(db.Integer)
    land_pincode = db.Column(db.Integer)
    land_district = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    users = db.relationship("User", foreign_keys="Land.user_id")


    def __init__(self, land_doc, land_area, land_pincode, land_district, user_id):
        self.land_doc = land_doc
        self.land_area = land_area
        self.land_pincode = land_pincode
        self.land_district = land_district
        self.user_id = user_id
