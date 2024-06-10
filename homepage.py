import streamlit as st
from Index import navbar


st.set_page_config(page_title="PREDICTIVE PRICE PREDICTION",page_icon='🔮')

page_bg_img='''
<style>
[data-testid="stAppViewContainer"]{
background-color:Light grey
}
</style>

'''
st.markdown(page_bg_img, unsafe_allow_html=True)

col1,col2=st.columns([1,10])
with col1:
 st.image('navigation.png',width=60 )


with col2:
 st.markdown(navbar, unsafe_allow_html=True)


st.sidebar.success("Select above option")
st.title('WELCOME TO HOME PAGE 🏡')
st.header('Predicting Prices with Accuracy 🚨')
st.write(' Are you looking to **BUY or SELL ASSESTS**. Welcome to **PREDICTIVE-PRICE-ESTIMATION** , where you can find accurate predictions for the prices of laptops, houses, smartphones and cars. Our platform utilizes advanced machine learning algorithms to provide reliable estimates tailored to each category.')
st.write("For all the projects i have trained all models on multiple algorithms like Ridge, Lasso, Linear Regression, Support Vector Regressor(SVR), DecisionTreeRegressor, ExtraTreeRegressor, KNeighborsRegressor, XGBRegressor , GradientBoostingRegressor , ExtraTreesRegressor, RandomForestRegressor etc. and select the algorithm that perform best on the models and return Highest Accuracy.")
st.markdown("---")

st.header('Laptop Price Prediction 💻')
st.write('Are you looking to buy or sell a new laptop? Our model is trained to predict laptop prices with precision. By considering various features such as brand, type, RAM, GPU, and more, we can help you estimate the cost of your next computing companion. With an accuracy of **97.77%**, our predictions ensure that you make informed decisions within your budget.')

st.markdown("### About Dataset 📚 ")
st.write("The  dataset is composed of 1,303 rows and 12 columns:  **Company ,TypeName , Inches , ScreenResolution , Cpu , Ram , Memory , Gpu , OpSys , Weight , and Price.** This format indicates the dataset is designed to detail various aspects of laptops, such as manufacturer, type, screen size and resolution, CPU, RAM, storage, GPU, operating system, weight, and price, serving as a basis for comparisons or analyses within the laptop market.")

st.markdown("### Algorithm Used 🔗")
st.write("In the project focused on predicting laptop prices, I utilized the **XGBoost (XGB) regressor** due to its high accuracy. XGBoost stands out for several reasons: its gradient boosting framework enhances computational efficiency, regularization helps in preventing overfitting, and it's capable of handling missing values directly. Additionally, XGBoost's scalability allows it to perform well on both single machines and distributed systems. Its unique tree pruning and built-in cross-validation features further contribute to its robustness, making it an excellent choice for complex predictive tasks such as laptop price prediction where understanding nuanced relationships between features is crucial")

st.markdown("---")

st.header('Car Price Prediction 🚘')
st.write("Planning to purchase or sell a new car ? Our website empowers you with insightful predictions for car prices. Whether you're considering brand, model, mileage, or additional features, our model takes into account various factors to deliver precise estimates. With an accuracy of  **99%**, you can navigate the automotive market confidently and find the perfect ride to suit your needs.")

st.markdown("### About Dataset 📚")
st.write("The dataset comprises 816 rows and 7 columns, specifically **name, company, year, Price, kms_driven, and fuel_type**. This structure suggests each entry details a car, including its model name, manufacturer, year of manufacture, sale price, kilometers driven, and the type of fuel it uses, providing a comprehensive overview for analyzing the used car market.")

st.markdown("### Algorithm Used 🔗")
st.write("The **Extra Trees Regressor** is a robust ensemble learning technique that excels in regression tasks like car price prediction. Unlike traditional decision trees, it splits nodes randomly, enhancing accuracy and generalization. By aggregating predictions from multiple de-correlated trees, it reduces overfitting and improves performance on unseen data, effectively capturing complex, non-linear relationships. Training on the entire dataset and reducing variance through averaging, the model is reliable and efficient, handling large datasets and noisy data well. Additionally, its parallel processing capability speeds up computation, making it suitable for real-time applications and large-scale data analysis.")

st.markdown("---")

st.header('House Price Prediction 🏠')
st.write('Finding the perfect home is an exciting journey. Our website offers predictive insights into house prices, enabling you to gauge the market value of properties. From location to size, amenities, and more, our model factors in key attributes to provide accurate estimates. With an accuracy of **98%**, you can confidently explore real estate opportunities with our predictions.')

st.markdown("### About Dataset 📚")
st.write("The house price prediction.csv dataset contains 68,720 rows and 11 columns, specifically: **POSTED_BY, UNDER_CONSTRUCTION, RERA, BHK_NO., BHK_OR_RK, SQUARE_FT, READY_TO_MOVE, RESALE, ADDRESS, LONGITUDE, and LATITUDE**. This setup suggests the dataset provides detailed information on various properties, including the listing type, construction status, regulatory approval, number and type of bedrooms, size, and geographic details, aimed at facilitating house price prediction analyses.")
st.markdown("### Algorithm Used 🔗")
st.write("In the house price prediction project, I opted for the **Decision Tree algorithm** due to its effectiveness and straightforward approach. Decision Trees are favored for their ability to create clear, understandable models that mimic human decision-making processes by breaking down data into smaller subsets. This method is particularly advantageous because it requires minimal data preprocessing, can handle both numerical and categorical data, and is interpretable, allowing for easy visualization of the decision-making path. Moreover, Decision Trees can model non-linear relationships, making them suitable for the complex dynamics of house pricing, where factors such as location, size, and amenities play intertwined roles in determining prices.")
st.markdown("---")


st.header('Smartphone Price Prediction 📞')
st.write('In a world filled with a myriad of smartphone options, choosing the right one can be overwhelming. Our platform simplifies the decision-making process by forecasting smartphone prices accurately. From brand to specifications and features, our model analyzes diverse parameters to offer reliable price estimates. With an accuracy of  **97%**, you can stay within your budget while enjoying the latest technology.')

st.markdown("### About Dataset 📚")
st.write("The dataset smartphone_specifications_and_prices.csv consists of 1,256 rows and 10 columns: **brand_name, model, display, front_camera, rare_camera, processor, battery_capacity, ram, internal_storage, and price**. This configuration suggests the dataset offers detailed specifications and pricing information for a variety of smartphone models, including their brand, model, screen details, camera specifications, processor type, battery capacity, memory sizes, and price, ideal for market analysis or consumer research.")

st.markdown("### Algorithm Used 🔗")
st.write("Random Forest Regressor is a versatile machine learning algorithm commonly used for regression tasks due to its robustness and effectiveness. It constructs multiple decision trees during training and outputs the average prediction of all trees, providing accurate results with reduced risk of overfitting. Its ensemble nature allows it to handle large datasets, high-dimensional feature spaces, and nonlinear relationships effectively. Additionally, it inherently performs feature selection, making it suitable for tasks with a large number of features. Overall, Random Forest Regressor is valued for its simplicity, scalability, and ability to deliver reliable predictions across various domains.")
st.markdown("---")

def add_footer():
    footer = """
        <style>
        .footer {
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #f0f0f0;
            text-align: center;
            padding: 10px 0;
            font-size: 14px;
        }
        </style>
        <div class="footer">
            <b>Note :</b> To Get The Access Of Dataset And Codes You Can Go To Contact Section And Visit My Github Account .
        </div>
    """
    st.markdown(footer, unsafe_allow_html=True)

add_footer()