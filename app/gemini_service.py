import google.generativeai as genai

from config import GEMINI_API_KEY


def get_ai_diet_plan(
    nutrients,
    user_data,
    cuisine
):

    genai.configure(
        api_key=GEMINI_API_KEY
    )

    model_id = "gemini-2.5-flash"

    try:

        gemini = genai.GenerativeModel(
            model_id
        )

        prompt = f"""
        Context: You are 'ArogyaIQ', an expert Clinical
        Nutritionist and Personalized Wellness Advisor.

        User Profile: {user_data}

        Selected Cuisine Preference: {cuisine}

        Calculated Health Metrics:

        - Calories: {nutrients[0]:.0f} kcal

        - Protein: {nutrients[1]:.1f}g

        - Fats: {nutrients[2]:.1f}g

        - Carbohydrates: {nutrients[3]:.1f}g


        Task:

        Create a personalized 7-day meal plan
        from Monday to Sunday.


        Important:

        Use ONLY {cuisine} cuisine meals.


        If the selected cuisine is Indian,
        provide only Indian meals.


        If the selected cuisine is Asian,
        provide only Asian meals.


        If the selected cuisine is Mediterranean,
        provide only Mediterranean meals.


        If the selected cuisine is Western,
        provide only Western meals.


        For each day include:

        - Breakfast

        - Mid-morning snack

        - Lunch

        - Evening snack

        - Dinner


        Also include:

        - Portion sizes

        - Water intake

        - Physical activity recommendations

        - Sleep recommendations


        Requirements:

        - Follow the selected cuisine strictly

        - Meet nutritional targets every day

        - Avoid repetitive meals

        - Keep meals practical and realistic


        Format the output day-wise
        from Monday to Sunday.
        """

        response = gemini.generate_content(
            prompt
        )

        return response.text

    except Exception as e:

        return f"Gemini Error: {e}. Ensure the model '{model_id}' is available in your region."