import streamlit as st

st.set_page_config(page_title="Cook With What You Have 🍽️", layout="wide")
st.title("Cook With What You Have 🍽️")

# Recipe Data (Backend Hatakar Direct Data)
recipes = {
    "chicken": [
        {"name": "Grilled Chicken", "image": "https://www.themealdb.com/images/media/meals/1548772327.jpg", "description": "Juicy grilled chicken with herbs."},
        {"name": "Chicken Biryani", "image": "https://www.themealdb.com/images/media/meals/xrttsx1487339558.jpg", "description": "Aromatic rice and chicken dish."},
    ],
    "egg": [
        {"name": "Omelette", "image": "https://joyfoodsunshine.com/wp-content/uploads/2022/07/best-omelette-recipe-1.jpg", "description": "Fluffy and cheesy omelette."},
        {"name": "Egg Curry", "image": "https://bing.com/th?id=OSK.301b185305939f6c5ebcf83d2f234313", "description": "Eggs in a rich tomato-based curry."},
    ],
    "rice": [
        {"name": "Fried Rice", "image": "https://www.themealdb.com/images/media/meals/1529445434.jpg", "description": "Delicious stir-fried rice with veggies."},
        {"name": "Rice Pudding", "image": "https://th.bing.com/th/id/R.18a4e0877d1ebcc88344c0878fe4a9d5?rik=3WSO2Y35et4lIw&pid=ImgRaw&r=0", "description": "Sweet and creamy rice pudding."},
    ],
    "sugar": [
        {"name": "Rice Pudding", "image": "https://www.themealdb.com/images/media/meals/1520081754.jpg", "description": "Sweet and creamy rice pudding."},
        {"name": "Sugar Cookies", "image": "https://www.themealdb.com/images/media/meals/1548772327.jpg", "description": "Classic homemade sugar cookies."},
    ],
    "mutton": [
        {"name": "Mutton Curry", "image": "https://www.themealdb.com/images/media/meals/uyqrrv1511553350.jpg", "description": "Spicy and flavorful mutton curry."},
        {"name": "Mutton Biryani", "image": "https://www.themealdb.com/images/media/meals/wyxwsp1486979827.jpg", "description": "Fragrant rice and mutton biryani."},
    ],
    "flour": [
        {"name": "Roti", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Indian_roti.jpg/640px-Indian_roti.jpg", "description": "Soft homemade roti."},
        {"name": "Pancakes", "image": "https://www.themealdb.com/images/media/meals/rwuyqx1511383174.jpg", "description": "Fluffy and delicious pancakes."},
    ],
}

# Function to Get Best Recipe
def get_best_recipe(ingredients):
    recipe_priority = {}

    for ingredient in ingredients:
        if ingredient in recipes:
            for recipe in recipes[ingredient]:
                if recipe["name"] in recipe_priority:
                    recipe_priority[recipe["name"]]["score"] += 1
                else:
                    recipe_priority[recipe["name"]] = {"recipe": recipe, "score": 1}

    if recipe_priority:
        best_match = max(recipe_priority.values(), key=lambda x: x["score"])
        return best_match["recipe"]

    return None

# Input for Ingredients
ingredients = st.text_input("Enter ingredients (comma-separated):")

if st.button("Get Recipe"):
    if ingredients:
        ingredient_list = [i.strip().lower() for i in ingredients.split(",")]
        best_recipe = get_best_recipe(ingredient_list)

        if best_recipe:
            st.subheader(f"🔹 Recipe: {best_recipe['name']}")
            
            # Show Image
            st.image(best_recipe["image"], caption=best_recipe["name"], width=300)

            st.write(f"📖 {best_recipe['description']}")
        else:
            st.error("No matching recipe found. Try different ingredients.")
    else:
        st.warning("⚠ Please enter at least one ingredient.")
