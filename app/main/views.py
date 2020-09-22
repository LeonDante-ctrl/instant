from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User,Pitch,Comment
from .forms import UpdateProfile,PitchForm,CommentForm
from .. import db,photos
from flask_login import login_required,current_user
from datetime import datetime

@main.route('/')
def index():
    pitches = Pitch.query.order_by(Pitch.time.desc()).all()

    return render_template('index.html', pitches = pitches)