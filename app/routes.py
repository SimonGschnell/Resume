from app import app,db
from flask import render_template, request, flash, redirect, url_for
from app.forms import Contact
from app.models import People
from app.email import send_mail


# from app.forms import

@app.route('/index')
@app.route('/')
def index():

    return render_template('index.html', title='Simon Gschnell', name='Simon')


@app.route('/about')
def about():
    return render_template('about.html', title='Simon Gschnell')


@app.route('/contact', methods=['GET','POST'])
def contact():
    form = Contact()
    if form.validate_on_submit():
        contact = People(name=form.name.data,email=form.email.data,msg=form.message.data)
        db.session.add(contact)
        db.session.commit()
        send_mail('Someone contacted you!',app.config['ADMINS'][0],app.config['MY_MAIL'][0],render_template('email/contact_message_sent.txt',user=contact),render_template('email/contact_message_sent.html',user=contact))
        flash('Thank you for reaching out!','success')
        return redirect(url_for('index'))

    return render_template('contact.html', title='Simon Gschnell', form=form)


@app.route('/cv')
def cv():
    return render_template('cv.html', title='Simon Gschnell')


@app.route('/projects/<project>')
def projects(project):
    return render_template('projects.html', title='Simon Gschnell')
