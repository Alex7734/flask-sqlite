from flask import Flask, render_template, request, Blueprint, redirect, url_for, session
from .repository import *
from .utils import *

problems = Blueprint('problems', __name__)

@problems.route('/')
def index():
    problems = get_problems_with_categories_and_difficulty()

    if len(problems) == 0:
        add_initial_data()
        problems = get_all_problems_with_categories()

    if 'loggedin' in session:
        return render_template('index.html', problems=problems, username=session['username'])
    return render_template('index.html', problems=problems)

@problems.route('/problem/<int:problem_id>')
def problem_details(problem_id):
    user_id = session.get('id')
    if user_id:
        track_user_problem(user_id, problem_id)
    problem, solutions = get_problem_details(problem_id)
    return render_template('problems/problem_details.html', problem=problem, solutions=solutions)

@problems.route('/submit_solution', methods=['POST'])
def submit_solution_route():
    user_id = session['id']
    problem_id = request.form['problem_id']
    submission_code = request.form['submission_code']
    submit_solution(user_id, problem_id, submission_code)
    return redirect(url_for('problems.problem_details', problem_id=problem_id))

@problems.route('/my_submissions')
def my_submissions():
    user_id = int(session['id'])
    submissions = get_user_submissions(user_id)
    return render_template('problems/my_submissions.html', submissions=submissions)
