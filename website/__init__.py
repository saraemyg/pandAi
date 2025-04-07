from flask import Flask, render_template, url_for

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'saranadianisa'

    @app.route('/')
    def home():
        return render_template('home.html',
            username="Alex",
            learning_style="Visual Learner",
            module_length_pref="Short Modules Preferred",
            best_focus_time="Morning",
            math_score=85,
            science_score=92,
            history_score=78,
            ai_feedback="Based on your quiz results, focus on 'Data Analysis Basics'."
        )
    
    @app.route('/progress')
    def progress():
        return "<h2>Progress page coming soon...</h2>"

    @app.route('/settings')
    def settings():
        return "<h2>Settings page coming soon...</h2>"

    @app.route('/materials')
    def materials():
        return "<h2>Course materials page coming soon...</h2>"

    @app.route('/quiz/<int:quiz_id>')
    def quiz(quiz_id):
        return f"<h2>Quiz {quiz_id} page coming soon...</h2>"

    @app.route('/review')
    def review():
        return "<h2>Review topics page coming soon...</h2>"

        
    return app