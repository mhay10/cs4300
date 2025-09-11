from src import task4
import pytest

# Check valid discounts between 1 and 100 with different datatypes
@pytest.mark.parametrize(
    "price, discount, result",
    [
        (100, 10, 90.0),
        (50.0, 20.0, 40.0),
        (200, 15.5, 169.0),
        (100, 0, 100.0),
        (100, 100, 0.0),
    ],
)
def test_valid_discounts(price, discount, result):
    assert task4.calculate_discount(price, discount) == result

# Test invalid discounts less than 0 or over 100
def test_invalid_discounts():
    with pytest.raises(ValueError):
        task4.calculate_discount(100, -5)
    with pytest.raises(ValueError):
        task4.calculate_discount(100, 150)

# Run tests
if __name__ == "__main__":
    pytest.main([__file__, "-v"])