CREATE VIEW vw_hotel_analysis AS
SELECT
    booking_row_id,
    arrival_date,
    hotel,
    country,
    market_segment,
    distribution_channel,
    customer_type,
    is_canceled,
    booking_status,
    is_repeated_guest,
    lead_time,
    total_nights,
    total_guests,
    adr,
    estimated_room_value,
    estimated_realized_room_revenue,
    deposit_type,
    reservation_status,
    previous_cancellations,
    previous_bookings_not_canceled,
    total_of_special_requests
FROM hotel_bookings;