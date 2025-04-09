from flask import Flask, render_template, url_for, request, jsonify
from google import genai
import os
from dotenv import load_dotenv

def create_app():
    load_dotenv() 
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'saranadianisa'

    # # Configure Gemini AI
    # GOOGLE_API_KEY = os.getenv('AIzaSyAgmrGP_X5q0jGiXsndQ0bO-D4lSXxSwQw')
    # if not GOOGLE_API_KEY:
    #     raise ValueError("No GOOGLE_API_KEY found in environment variables")
    
    # Initialize Gemini client
    client = genai.Client(api_key='AIzaSyAgmrGP_X5q0jGiXsndQ0bO-D4lSXxSwQw')

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
        return render_template('review.html')

    @app.route('/get_ai_response', methods=['POST'])
    def get_ai_response():
        data = request.json
        user_message = data.get('message')

        try:
            # Add context to the AI prompt
            prompt = f"""You are an educational AI assistant helping a student learn.
            Context: The student is asking about: {user_message}
            Instructions: Provide a clear, educational response that is helpful and concise.
            Keep the tone friendly and encouraging."""

            # Generate response using Gemini AI
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt
            )
            
            if response.text:
                return jsonify({'response': response.text})
            else:
                return jsonify({'response': 'I apologize, but I could not generate a response. Please try rephrasing your question.'}), 400

        except Exception as e:
            print(f"Error: {str(e)}")  # For debugging
            return jsonify({'response': 'An error occurred while processing your request. Please try again.'}), 500

    return app