from app import db
from sqlalchemy.dialects.postgresql import JSON


class Scholarship(db.Model):
    __tablename__ = "scholarship"
    __table_args__ = {'extend_existing': True}
    Scholarship_Id = db.Column(db.Integer, nullable=False, primary_key=True, unique=True)
    Scholarship_Name = db.Column(db.String(50), nullable=False)
    Max_Rank = db.Column(db.Integer, nullable=False)
    Amount_INR = db.Column(db.Integer, nullable=False)

    def __init__(self, Scholarship_Id, Scholarship_Name, Max_Rank, Amount_INR):
        self.Scholarship_Id = Scholarship_Id
        self.Scholarship_Name = Scholarship_Name
        self.Max_Rank = Max_Rank
        self.Amount_INR = Amount_INR

class User(db.Model):
    __tablename__ = 'User'
    __table_args__ = {'extend_existing': True}
    User_ID=    db.Column(db.Integer, primary_key=True)
    Email=      db.Column(db.String(80),nullable=False)
    Password=   db.Column(db.String(80),nullable=False)
    FirstName=  db.Column(db.String(80),nullable=False)
    MiddleName= db.Column(db.String(80),nullable=False)
    LastName=   db.Column(db.String(80),nullable=False)
    H_no=       db.Column(db.String(80),nullable=False)
    City=       db.Column(db.String(80),nullable=False)
    State=      db.Column(db.String(80),nullable=False)
    Pincode=    db.Column(db.Integer)
    Phone=      db.Column(db.String(80))
    Rank=       db.Column(db.Integer)
    Schp_Id=    db.Column(db.Integer, db.ForeignKey('scholarship.Scholarship_Id'))
    def __init__(self,User_ID,Email,Password,FirstName,MiddleName,LastName,H_no,City,State,Pincode,Phone,Rank,Schp_Id):
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
        self.Rank = Rank
        self.Schp_Id = Schp_Id

class Vechile(db.Model):
    __tablename__ = 'Vechile'
    __table_args__ = {'extend_existing': True}
    Vehicle_ID            =db.Column(db.Integer, primary_key=True)
    User_ID               =db.Column(db.Integer,nullable=False)
    Policy_ID             =db.Column(db.Integer,nullable=False)
    Vehicle_Reg_Number    =db.Column(db.String(80),nullable=False)
    Vehicle_Value         =db.Column(db.Integer,nullable=False)
    Vehicle_TYPE          =db.Column(db.String(80),nullable=False)
    Vehicle_Size          =db.Column(db.Integer,nullable=False)
    Number_of_passenger   =db.Column(db.Integer,nullable=False)
    Engine_number         =db.Column(db.String(80),nullable=False)
    Chasis_Number         =db.Column(db.String(80),nullable=False)
    Vechile_Model         =db.Column(db.String(80),nullable=False)
    Year                  =db.Column(db.Integer,nullable=False)
    Created_DT            =db.Column(db.DateTime,nullable=False)
    
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
    __tablename__ = 'Application'
    __table_args__ = {'extend_existing': True}
    Application_ID     = db.Column(db.Integer,primary_key=True)
    User_id            = db.Column(db.Integer)
    Vechile_ID         = db.Column(db.Integer)                 
    Application_Status = db.Column(db.String(80))                                          
    Coverage           = db.Column(db.String(80))                                
    Created_DT         = db.Column(db.DateTime)                
    Updated_DT         = db.Column(db.DateTime) 
        
    def __init__(self,Application_ID,User_id,Vechile_ID,Application_Status,Coverage,Created_DT,Updated_DT):
        self.Application_ID    =Application_ID    
        self.User_id           =User_id           
        self.Vechile_ID        =Vechile_ID        
        self.Application_Status=Application_Status
        self.Coverage          =Coverage          
        self.Created_DT        =Created_DT        
        self.Updated_DT        =Updated_DT 

class Claim(db.Model):
    __tablename__ = 'Claim'
    __table_args__ = {'extend_existing': True}
    Claim_ID       = db.Column(db.Integer,primary_key=True) 
    User_ID        =db.Column(db.Integer,nullable=False) 
    Application_ID =db.Column(db.Integer,nullable=False) 
    Claim_Amount   =db.Column(db.Integer,nullable=False) 
    Damage_type    =db.Column(db.String(80),nullable=False) 
    Date_of_claim  =db.Column(db.DateTime,nullable=False)
    Status         =db.Column(db.String(80),nullable=False)
    Created_DT     =db.Column(db.DateTime,nullable=False)
    Updated_DT     =db.Column(db.DateTime,nullable=False)
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
    __tablename__ = 'Insurance_Company'
    __table_args__ = {'extend_existing': True}
    Company_Name              = db.Column(db.String(80),primary_key=True)
    Company_Contact_Number    =db.Column(db.String(80),nullable=False)  
    Company_Email             =db.Column(db.String(80),nullable=False)  
    Company_Website           =db.Column(db.String(80),nullable=False)  
    Company_Location          =db.Column(db.String(80),nullable=False)  
    Company_Department        =db.Column(db.String(80),nullable=False)  
    Company_Office_Name       =db.Column(db.String(80),nullable=False)  
    Created_DT                =db.Column(db.DateTime,nullable=False)
    Updated_DT                =db.Column(db.DateTime,nullable=False)
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
    __tablename__ = 'Insurance_Policy'
    __table_args__ = {'extend_existing': True}
    Policy_ID        = db.Column(db.Integer,primary_key=True)
    Application_ID   = db.Column(db.Integer,nullable=False)
    User_id          = db.Column(db.Integer,nullable=False)
    Department_name  = db.Column(db.String(80),nullable=False)
    Policy_Number    = db.Column(db.String(80),nullable=False)
    End_date         = db.Column(db.Integer,nullable=False)
    Term_Condition   = db.Column(db.String(80),nullable=False)
    Created_DT       = db.Column(db.DateTime,nullable=False) 
    Updated_DT       = db.Column(db.DateTime,nullable=False)
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
    __tablename__ = 'Quote'
    __table_args__ = {'extend_existing': True}
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
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    land_doc = db.Column(db.String)
    land_area = db.Column(db.Integer)
    land_pincode = db.Column(db.Integer)
    land_district = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('User.User_ID'))
    users = db.relationship("User", foreign_keys="Land.user_id")


    def __init__(self, land_doc, land_area, land_pincode, land_district, user_id):
        self.land_doc = land_doc
        self.land_area = land_area
        self.land_pincode = land_pincode
        self.land_district = land_district
        self.user_id = user_id

class College(db.Model):
    __tablename__ = "college"
    __table_args__ = {'extend_existing': True}
    College_Id = db.Column(db.Integer, nullable=False, primary_key=True, unique=True)
    College_Name = db.Column(db.String(50), nullable=False)
    Address = db.Column(db.String(50), nullable=False)
    Ph_No = db.Column(db.BigInteger, nullable=False)
    Email = db.Column(db.String(50), nullable=False)
    Max_Rank = db.Column(db.Integer, nullable=False)

    def __init__(self, College_Id, College_Name, Address, Ph_No, Email, Max_Rank):
        self.College_Id = College_Id
        self.College_Name = College_Name
        self.Address = Address
        self.Ph_No = Ph_No
        self.Email = Email
        self.Max_Rank = Max_Rank

class Program(db.Model):
    __tablename__ = "program"
    __table_args__ = {'extend_existing': True}
    Program_Name = db.Column(db.String(50), nullable=False, primary_key=True, unique=True)
    Branch = db.Column(db.String(50), nullable=False, primary_key=True, unique=True)
    College_Id = db.Column(db.Integer, db.ForeignKey('college.College_Id'), nullable=False, primary_key=True, unique=True)
    No_Of_Seats = db.Column(db.Integer, nullable=False)

    def __init__(self, Program_Name, Branch, College_Id, No_Of_Seats):
        self.Program_Name = Program_Name
        self.Branch = Branch
        self.College_Id = College_Id
        self.No_Of_Seats = No_Of_Seats
        
class Admission(db.Model):
    __tablename__ = 'admission'
    __table_args__ = {'extend_existing': True}
    User_Id = db.Column(db.Integer, db.ForeignKey('User.User_ID'), nullable=False, primary_key=True, unique=True)
    College_Id = db.Column(db.Integer, db.ForeignKey('program.College_Id'), nullable=False, primary_key=True, unique=True)
    Program_Name = db.Column(db.String(50), db.ForeignKey('program.Program_Name'), nullable=False, primary_key=True, unique=True)
    Branch = db.Column(db.String(80), db.ForeignKey('program.Branch'), nullable=False, primary_key=True, unique=True)

    def __init__(self, User_Id, College_Id, Program_Name, Branch):
        self.User_Id = User_Id
        self.College_Id = College_Id
        self.Program_Name = Program_Name
        self.Branch = Branch