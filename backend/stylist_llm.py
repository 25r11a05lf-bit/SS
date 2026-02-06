def generate_styling_advice(image_data, occasion, style, trends):
    advice = f"""
    Based on your {image_data['colors']} outfit:

    ✔ Occasion: {occasion}
    ✔ Style preference: {style}

    Suggestions:
    - Stick to {trends[0]}
    - Add matching shoes
    - Avoid loud accessories

    This outfit works well for the selected occasion.
    """
    return advice.strip()
