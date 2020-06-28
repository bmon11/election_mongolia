from datetime import datetime
from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Model(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now())
    created_by = db.Column(db.String(50))
    updated_at = db.Column(db.DateTime)
    updated_by = db.Column(db.String(50))
    deleted_at = db.Column(db.DateTime)
    deleted_by = db.Column(db.String(50))


class User(Model, UserMixin):
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.Integer)  # 0 - admin, 1 - moderator

    def is_active(self):
        return True

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Image(Model):

    name = db.Column(db.String(80))
    path = db.Column(db.String(100))
    is_approved = db.Column(db.Boolean, default=False)
    branch_id = db.Column(db.Integer, db.ForeignKey('branch.id'))
    branch = db.relationship('Branch')
    device_id = db.Column(db.Integer, db.ForeignKey('device.id'))
    device = db.relationship('Device')

    def __repr__(self):
        return '<Image: {}>'.format(self.name)


class Vote(Model):
    vote_number = db.Column(db.Integer, default=0)
    is_approved = db.Column(db.Boolean, default=False)

    candidate_id = db.Column(db.Integer, db.ForeignKey('candidate.id'))
    candidate = db.relationship('Candidate')
    district_id = db.Column(db.Integer, db.ForeignKey('district.id'))
    district = db.relationship('District')
    branch_id = db.Column(db.Integer, db.ForeignKey('branch.id'))
    branch = db.relationship('Branch')
    party_id = db.Column(db.Integer, db.ForeignKey('party.id'))
    party = db.relationship('Party')
    device_id = db.Column(db.Integer, db.ForeignKey('device.id'))
    device = db.relationship('Device')


class Candidate(Model):
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    gender = db.Column(db.Integer)

    district_id = db.Column(db.Integer, db.ForeignKey('district.id'))
    district = db.relationship('District')
    party_id = db.Column(db.Integer, db.ForeignKey('party.id'))
    party = db.relationship('Party')
    votes = db.relationship('Vote', backref='candidate_votes', lazy='dynamic')

    def __repr__(self):
        return '<Candidate {}>'.format(self.first_name)


class Party(Model):
    name = db.Column(db.String(100))
    short_name = db.Column(db.String(20))
    code = db.Column(db.Integer)

    candidates = db.relationship('Candidate', backref='party_candidates', lazy='dynamic')
    votes = db.relationship('Vote', backref='party_votes', lazy='dynamic')
    
    def __repr__(self):
        return '<Party {}>'.format(self.name)


class District(Model):
    code = db.Column(db.String(10))
    name = db.Column(db.String(40))
    quote = db.Column(db.Integer)
    votes = db.relationship('Vote', backref='district_votes', lazy='dynamic')
    candidates = db.relationship('Candidate', backref='district_candidates', lazy='dynamic')
    branches = db.relationship('Branch', backref='district_branches', lazy='dynamic')

    def __repr__(self):
        return '<District {}>'.format(self.name)


class Branch(Model):
    name = db.Column(db.String(140))
    address = db.Column(db.String(250))
    code = db.Column(db.String(10))
    district_id = db.Column(db.Integer, db.ForeignKey('district.id'))
    district = db.relationship('District')
    devices = db.relationship('Device', backref='branch_devices', lazy='dynamic')
    images = db.relationship('Image', backref='branch_images', lazy='dynamic')
    votes = db.relationship('Vote', backref='branch_votes', lazy='dynamic')

    def __repr__(self):
        return '<Branch {}>'.format(self.name)


class Device(Model):
    device_type = db.Column(db.String(40))
    device_number = db.Column(db.String(40))
    software_version = db.Column(db.String(40))
    branch_id = db.Column(db.Integer, db.ForeignKey('branch.id'))
    branch = db.relationship('Branch')
    district_id = db.Column(db.Integer, db.ForeignKey('district.id'))
    district = db.relationship('District')

    images = db.relationship('Image', backref='device_images', lazy='dynamic')
    votes = db.relationship('Vote', backref='device_votes', lazy='dynamic')

    def __repr__(self):
        return '<Device {}>'.format(self.device_number)




