import streamlit as st
import pandas as pd
st.title('Hotel Booking Cancellation Predictor 🏨')
import pickle 

# Step 1: load the pickled model
model = open('xgb.pickle','rb')
xgbmodel=pickle.load(model)
model.close()

# Step 2: create a UI for front end user
from PIL import Image
hotel = st.radio("What's your Prefered Hotel type",('City Hotel','Resort Hotel'))
lead_time=st.slider('Enter Lead Time',1,200)
arrival_date_month=st.radio('Enter Month of Arrival',('April', 'August', 'December', 'February', 'January', 'July',
        'June', 'March', 'May', 'November', 'October', 'September'))
arrival_date_week_number=st.slider('Enter Week of Arrival',1,54)
arrival_date_day_of_month=st.slider('Enter Day of arrival',1,31)
stays_in_weekend_nights= st.slider('Enter number of Weekend stays',1,108)
stays_in_week_nights = st.slider('Enter number of Weekday stays',1,300)
adults = st.slider('Enter Number of adults',1,25)
children =  st.slider('Enter Number of children',1,20)
babies =  st.slider('Enter Number of babies',0,20)
meal =  st.radio('Select Meal Type',('BB', 'FB', 'HB', 'SC'))
country=  st.radio('Select Country of Origin ',('PRT', 'International'))
market_segment=  st.radio('Select Market Segment',('Direct', 'Corporate', 'Online TA', 'Offline TA/TO',
       'Complementary', 'Groups', 'Undefined', 'Aviation'))
distribution_channel=  st.radio('Select Distribution Channel',('Direct', 'Corporate', 'TA/TO','GDS'))
is_repeated_guest_radio= st.radio('Repeated Guest ?',('Yes','No'))
if is_repeated_guest_radio=='Yes':
    is_repeated_guest=1
else:
     is_repeated_guest=0
    
    
previous_cancellations=  st.slider('Enter Number of previous cancellations',1,30)
previous_bookings_not_canceled=  st.slider('Enter Number of previous bookings',1,50)
reserved_room_type=  st.radio('Reserved Room type',('C', 'A', 'D', 'E', 'G', 'F', 'H', 'L', 'P', 'B'))
assigned_room_type=  st.radio('Assigned Room type',('C', 'A', 'D', 'E', 'G', 'F', 'I', 'B', 'H', 'P', 'L', 'K'))
booking_changes=  st.slider('Enter changes made',1,100)
deposit_type=  st.radio("Choose Deposit type",('No Deposit', 'Refundable', 'Non Refund'))
agent=  st.radio("Booked via Agent ?",('Yes','No'))
company=  st.radio("Booked via company ?",('Yes','No'))
days_in_waiting_list=  st.slider('Enter Days in waiting list',1,800)
customer_type=  st.radio("Select Customer type ",('Transient', 'Contract', 'Transient-Party', 'Group'))
adr=  st.slider('Enter Cost per night',1,100)
required_car_parking_spaces=  st.slider('Number of car parking required',1,20)
total_of_special_requests=  st.slider('Number of special requests',1,50)
reserved_assigned=  st.radio("Is reserved room same as assigned room ?",('Yes','No'))
reservation_date=  st.slider('Date of last Reservation Status change ',1,31)
reservation_month=  st.slider('Month of last Reservation Status change',1,12)

# Step 3: Change user input as models input data
data={
'hotel' : hotel,
'lead_time': lead_time,
'arrival_date_month': arrival_date_month,
'arrival_date_week_number': arrival_date_week_number,
'arrival_date_day_of_month': arrival_date_day_of_month,
'stays_in_weekend_nights': stays_in_weekend_nights,
'stays_in_week_nights' : stays_in_week_nights,
'adults' : adults,
'children' : children,
'babies': babies,
'meal': meal,
'distribution_channel':distribution_channel,
'country': country,
'market_segment': market_segment ,
'is_repeated_guest' : is_repeated_guest ,                   
'previous_cancellations': previous_cancellations,
'previous_bookings_not_canceled':  previous_bookings_not_canceled,
'reserved_room_type': reserved_room_type,
'assigned_room_type': assigned_room_type,
'booking_changes':  booking_changes,
'deposit_type':  deposit_type,
'agent': agent,
'company': company ,
'days_in_waiting_list':  days_in_waiting_list,
'customer_type': customer_type,
'adr': adr,
'required_car_parking_spaces': required_car_parking_spaces,
'total_of_special_requests': total_of_special_requests,
'reserved_assigned':  reserved_assigned,
'reservation date': reservation_date,
'reservation month': reservation_month  
}

input_data = pd.DataFrame([data])
predictions = xgbmodel.predict(input_data)
if st.button('Predict'):
    if predictions==0:
        st.success('This Person is not likely to cancel')
    if predictions==1:
        st.error('High Chances of customer cancellation')
