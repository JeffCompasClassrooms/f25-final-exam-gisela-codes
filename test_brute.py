import pytest
from brute import Brute
from unittest.mock import Mock

@pytest.fixture
def brute_simple():
    return Brute("h1")

@pytest.fixture
def brute_hard():
    return Brute("43prefd9fds")


def describe_brute():
        
    def describe_bruteOnce():
        def it_returns_false_with_wrong_password(brute_simple):
            #setup
            b = brute_simple
            #doing the thing
            t = b.bruteOnce("hi")
            #testing
            assert t == False
        def it_returns_true_with_correct_password(brute_simple):
            #setup
            b = brute_simple
            #doing the thing
            t = b.bruteOnce("h1")
            #testing
            assert t == True

    def describe_bruteMany():
        def it_returns_time(brute_hard, mocker):
            #setup
            b = brute_hard
            mock_randomGuess = mocker.patch.object(b, "randomGuess", return_value="43prefd9fds")
            #doing THEE thing
            t = b.bruteMany(limit=100)
            #testing
            assert t != -1
            assert type(t) == float
            mock_randomGuess.assert_called_once_with()

        def it_does_not_return_time(brute_hard, mocker):
            b = brute_hard
            mock_randomGuess = mocker.patch.object(b, "randomGuess", return_value="43prefd9fd")
            t = b.bruteMany(limit=1)
            assert t == -1
            assert type(t) == int

