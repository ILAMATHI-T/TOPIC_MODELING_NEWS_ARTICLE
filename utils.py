def predict_topic(text_or_df):
    # Replace this with your actual model pipeline
    if isinstance(text_or_df, str):
        return "Politics"
    elif hasattr(text_or_df, 'iterrows'):
        return ["Business" for _ in range(len(text_or_df))]
