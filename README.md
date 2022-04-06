# Commission Counter Function

- High season: June - September => GuestReady commission is 15%
- Other months: commission is 10%

This function takes a date string in the format 'YYYY-MM-DD' or 'DD {month name}, YYYY' and platform (that defines a string format, like 'airbnb', 'bcom'...) and returns the commission:
get_commission(date_str, platform) -> float

### Tests - pytest

There is a separate test_commission_counter.py file with test script, that can be run with pytest

### Requirements:

Python==3.8.1
pytest==6.2.4
