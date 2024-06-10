import streamlit as st


st.set_page_config(page_title="PREDICTIVE PRICE PREDICTION",page_icon='🔮')

st.markdown(
    f'''
        <style>
            .sidebar .sidebar-content {{
                width: 375px;
            }}
        </style>
    ''',
    unsafe_allow_html=True
)
st.sidebar.success("Select above option")
st.title('WELCOME TO HOME PAGE 🏡')
st.header('Predicting Prices with Accuracy')
st.write(' Welcome to **PREDICTIVE-PRICE-ESTIMATION** , where you can find accurate predictions for the prices of laptops, houses, smartphones and cars. Our platform utilizes advanced machine learning algorithms to provide reliable estimates tailored to each category.')
st.write("For all the projects i have trained all models on multiple algorithms like Ridge, Lasso, Linear Regression, Support Vector Regressor(SVR), DecisionTreeRegressor, ExtraTreeRegressor, KNeighborsRegressor, XGBRegressor , GradientBoostingRegressor , ExtraTreesRegressor, RandomForestRegressor etc. and select the algorithm that perform best on the models and return Highest Accuracy.")
st.markdown("---")