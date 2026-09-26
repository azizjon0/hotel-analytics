## DAX Measures

The Power BI model uses custom DAX measures to analyse bookings, cancellations, revenue, pricing, guest behaviour, and stay patterns.

### Total Bookings

Counts the total number of booking records.

```DAX
Total Bookings =
COUNTROWS(
    'public vw_hotel_analysis'
)
```

### Cancelled Bookings

Counts bookings where the reservation was cancelled.

```DAX
Cancelled Bookings =
CALCULATE(
    [Total Bookings],
    'public vw_hotel_analysis'[is_canceled] = 1
)
```

### Cancellation Rate

Measures the proportion of total bookings that were cancelled.

```DAX
Cancellation Rate =
DIVIDE(
    [Cancelled Bookings],
    [Total Bookings],
    0
)
```

### Average ADR

Calculates the average daily room rate across all bookings.

```DAX
Average ADR =
AVERAGE(
    'public vw_hotel_analysis'[adr]
)
```

### Estimated Revenue

Calculates the total estimated realised room revenue.

```DAX
Estimated Revenue =
SUM(
    'public vw_hotel_analysis'[estimated_realized_room_revenue]
)
```

### Lost Revenue

Estimates the total room value associated with cancelled bookings.

```DAX
Lost Revenue =
CALCULATE(
    SUM(
        'public vw_hotel_analysis'[estimated_room_value]
    ),
    'public vw_hotel_analysis'[is_canceled] = 1
)
```

### Repeat Guest Rate

Measures the proportion of bookings made by repeat guests.

```DAX
Repeat Guest Rate =
DIVIDE(
    CALCULATE(
        [Total Bookings],
        'public vw_hotel_analysis'[is_repeated_guest] = 1
    ),
    [Total Bookings],
    0
)
```

### Average Stay

Calculates the average total number of nights per booking.

```DAX
Average Stay =
AVERAGE(
    'public vw_hotel_analysis'[total_nights]
)
```

### Average Lead Time

Calculates the average number of days between booking and arrival.

```DAX
Average Lead Time =
AVERAGE(
    'public vw_hotel_analysis'[lead_time]
)
```

### Average Lead Time — Cancelled Bookings

Calculates the average lead time for cancelled reservations only.

```DAX
Average Lead Time - Cancelled =
CALCULATE(
    AVERAGE(
        'public vw_hotel_analysis'[lead_time]
    ),
    'public vw_hotel_analysis'[is_canceled] = 1
)
```

### Total Cancellations

Alternative cancellation count using a direct row count.

```DAX
Total Cancellations =
CALCULATE(
    COUNTROWS(
        'public vw_hotel_analysis'
    ),
    'public vw_hotel_analysis'[is_canceled] = 1
)
```