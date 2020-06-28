import os
from flask import flash, render_template, request, redirect, url_for, jsonify, make_response, session
from app import app, db, jwt, UPLOAD_FOLDER_IMG
from app.forms import LoginForm, RegistrationForm, ImageUploadForm, DistrictSelectForm, BranchSelectForm, VoteForm
from app.models import User, District, Image, Branch, Party, Candidate, Vote
from flask_login import current_user, login_user, logout_user, login_required
from flask_jwt_extended import (create_access_token, jwt_required, get_jwt_identity,
    verify_jwt_in_request, get_jwt_claims)
from datetime import datetime, timedelta
from flask_mail import Message
from sqlalchemy import desc, or_
from werkzeug.utils import secure_filename
import logging

logger = logging.getLogger(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('upload_image'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('upload_image'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))



@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html', title='Home')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/upload_image', methods=['GET', 'POST'])
def upload_image():
    if current_user.is_authenticated:   
        all_districts = District.query.all()
        districts = [(d.code, d.name) for d in all_districts] 
        form = ImageUploadForm()
        form.district.choices = districts
        if form.validate_on_submit():
            image_file = request.files['file']
            if image_file:
                district = District.query.filter_by(code=form.district.data).first()
                branch = Branch.query.filter_by(district=district, code=form.branch.data).first()
                saved_path = os.path.join(UPLOAD_FOLDER_IMG, secure_filename(image_file.filename))
                image_file.save(saved_path)
                image = Image(name=secure_filename(image_file.filename),
                              path=saved_path)
                if branch:
                    branch.images.append(image)
                db.session.add(image)
                db.session.commit()
                flash('Succesfully saved!')
            return redirect(url_for('index'))
        return render_template('insert_data.html', title='Register', form=form)
    return redirect(url_for('login'))


@app.route('/select_district', methods=['GET', "POST"])
def select_district():
    if current_user.is_authenticated:
        all_districts = District.query.all()
        districts = [(d.code, d.name) for d in all_districts] 
        form = DistrictSelectForm()
        branch_form = BranchSelectForm()
        vote_form = VoteForm()
        form.district.choices = districts
        if form.validate_on_submit():
            district = District.query.filter_by(code=form.district.data).first()
            all_branches = Branch.query.filter_by(district=district)
            branches = [(b.name, b.name) for b in all_branches]
            branch_form.branch.choices = branches
            return render_template('select_branch.html', form=branch_form)
        if branch_form.branch.data != "None":
            branch = Branch.query.filter_by(name=branch_form.branch.data).first()
            image = Image.query.filter_by(branch=branch).first()
            parties = Party.query.all()
            party = [(p.code, p.short_name) for p in parties]
            vote_form.party.choices = party
            return render_template('vote.html', form=vote_form, image=image)
        if vote_form.candidate.data != "None" and vote_form.party.data != "None":
            party = Party.query.filter_by(code=vote_form.party.data).first()
            candidate = Candidate.query.filter_by(name=vote_form.candidate.data.upper(), party=party).first()
            if not candidate:
                candidate = Candidate(name=vote_form.candidate.data.upper())
                party.candidates.append(candidate)
                
            vote = Vote(vote_number=int(vote_form.vote.data))
            party.votes.append(vote)
            candidate.votes.append(vote)
            db.session.add(candidate)
            db.session.add(vote)
            db.session.commit()
        return render_template('select_district.html', form=form)
    return redirect(url_for('login'))
