from app import db

# Faculty Model
class Faculty(db.Model):

    __tablename__ = 'faculty'

    id = db.Column(db.Integer, primary_key=True) 
    faculty_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(50), nullable=False)
    phoneNo = db.Column(db.Integer)
    qualification = db.Column(db.String(50))
    address = db.Column(db.String(50))
    gender = db.Column(db.String(20), default="NIL")

    # many to one relationship with class user
    user = db.relationship("User", back_populates="faculty", cascade="all, delete")
    
    def __repr__(self):
        return '<Faculty %r>' % self.faculty_id

