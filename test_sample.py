import sample

def test_returnes_fizzbuzz_when_divisible_by_five_and_three():
    assert sample.Fizzbuzz(15) == "FizzBuzz"

def test_returnes_fizz_when_divisible_by_five():
    assert sample.Fizzbuzz(5) == "Buzz"

def test_returnes_fizz_when_divisible_by_three():
    assert sample.Fizzbuzz(3) == "Fizz"
