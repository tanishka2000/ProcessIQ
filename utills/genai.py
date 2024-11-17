import google.generativeai as genai
import markdown

# Configure the Google Gemini API
GOOGLE_API_KEY = 'AIzaSyDm5uqGAm_Vv4w5_QJ3RQgu2WJzx0HcfTM'
genai.configure(api_key=GOOGLE_API_KEY)

# Generate response using the Gemini model
def genai_response(user_request, chat_history):
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(user_request)
        bot_response = response.text

        # Convert the bot response (Markdown) to HTML
        bot_response_html = markdown.markdown(bot_response)

        # Update chat history
        chat_history.append({"user": user_request, "bot": bot_response_html})

        return bot_response_html  # Return HTML formatted response instead of plain text

    except Exception as e:
        bot_response = f"Error: {str(e)}"
        return markdown.markdown(bot_response)  # Convert the error message to HTML
