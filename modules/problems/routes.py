from flask import Flask, render_template, request, Blueprint, redirect, url_for, session, flash
from .repository import *
from .utils import *
from .openai_api import *

problems = Blueprint('problems', __name__)

@problems.route('/')
def index():
    name_filter = request.args.get('name', '')
    category_filter = request.args.get('category', '')
    difficulty_filter = request.args.get('difficulty', '')

    problems = filter_problems(name_filter, category_filter, difficulty_filter)

    profile_info = None
    if 'loggedin' in session:
        profile_info = get_profile_info(session['id'])

    categories = get_all_categories()

    return render_template('index.html', problems=problems, profile_info=profile_info, categories=categories)

@problems.route('/problem/<int:problem_id>')
def problem_details(problem_id, result=None):
    user_id = session.get('id')
    if user_id:
        track_user_problem(user_id, problem_id)
    problem, solutions = get_problem_details(problem_id)

    # Attempt to retrieve flashed messages if they exist
    result = {}
    if 'info_score' in session:
        result['score'] = session['info_score']
        result['comments'] = session['info_comments']
        session.pop('info_score', None)
        session.pop('info_comments', None)

    print(result)
    return render_template('problems/problem_details.html', problem=problem, solutions=solutions, result=result)

@problems.route('/submit_solution', methods=['POST'])
def submit_solution_route():
    user_id = session['id']
    problem_id = request.form['problem_id']
    submission_code = request.form['submission_code']

    problem_title = get_problem_title(problem_id)
    problem_description = get_problem_description(problem_id)

    # Get the score from OpenAI
    score, comments = evaluate_code(submission_code, problem_title, problem_description)
    submit_solution(user_id, problem_id, submission_code, score)

    session['info_score'] = score
    session['info_comments'] = comments
    return redirect(url_for('problems.problem_details', problem_id=problem_id))

@problems.route('/my_submissions')
def my_submissions():
    user_id = int(session['id'])
    submissions = get_user_submissions(user_id)
    return render_template('problems/my_submissions.html', submissions=submissions)

@problems.route('/add_problem', methods=['GET', 'POST'])
def add_problem_route():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        category_name = request.form['category_name']
        example_code = request.form['example_code']

        add_problem(title, description, category_name)
        problem_id = get_last_problem_id()
        add_solution(problem_id, example_code)

        return redirect(url_for('problems.index'))

    categories = get_all_categories()
    return render_template('problems/add_problem.html', categories=categories)
