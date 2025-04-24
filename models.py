from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Athlete(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    height = db.Column(db.Float, nullable=False)  # in cm
    weight = db.Column(db.Float, nullable=False)  # in kg
    sport = db.Column(db.String(50), nullable=False)
    medical_reports = db.relationship('MedicalReport', backref='athlete', lazy=True)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "height": self.height,
            "weight": self.weight,
            "sport": self.sport
        }

class MedicalReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    athlete_id = db.Column(db.Integer, db.ForeignKey('athlete.id'), nullable=False)
    heart_rate = db.Column(db.Integer, nullable=False)
    blood_pressure_sys = db.Column(db.Integer, nullable=False)  # systolic
    blood_pressure_dia = db.Column(db.Integer, nullable=False)  # diastolic
    oxygen_level = db.Column(db.Integer, nullable=False)  # SpO2 %
    training_hours = db.Column(db.Float, nullable=False)  # hours/week
    injury_risk = db.Column(db.Boolean, nullable=False)
    risk_probability = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def serialize(self):
        return {
            "id": self.id,
            "heart_rate": self.heart_rate,
            "blood_pressure": f"{self.blood_pressure_sys}/{self.blood_pressure_dia}",
            "oxygen_level": self.oxygen_level,
            "training_hours": self.training_hours,
            "injury_risk": self.injury_risk,
            "risk_probability": self.risk_probability,
            "created_at": self.created_at.isoformat()
        }
