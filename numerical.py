numerical_cols = df.select_dtypes(include=['number']).columns
categorical_cols = df.select_dtypes(include=['object', 'category']).columns

numerical_df = df[numerical_cols]
categorical_df = df[categorical_cols]
