def get_confidence_info(confidence):
    """
    Returns confidence level and message based on prediction confidence.
    """

    if confidence >= 95:
        return {
            "level": "Very High",
            "message": "The prediction is highly reliable."
        }

    elif confidence >= 80:
        return {
            "level": "High",
            "message": "The prediction is reliable. You can proceed with the suggested treatment."
        }

    elif confidence >= 60:
        return {
            "level": "Medium",
            "message": "The prediction is moderately reliable. Consider uploading a clearer image."
        }

    else:
        return {
            "level": "Low",
            "message": "The prediction confidence is low. Please upload a clear image of a single leaf under good lighting."
        }