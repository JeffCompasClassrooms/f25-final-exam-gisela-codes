import os
import pytest
import shutil
import sys
from christmas_list import ChristmasList

@pytest.fixture
def saved_presents():
    cl = ChristmasList("christmas_list.pkl")
    # cl.saveItems(["switch", "bike"])
    cl.add("bike")
    return cl

def describe_christmas_list():
    @pytest.fixture(autouse=True) 
    def setup_and_cleanup_database():
        # setup the pkl
        if os.path.isfile('christmas_list.pkl'):
            os.remove('christmas_list.pkl')
        
        # copy the empty to the test
        if os.path.isfile('empty_christmas_list.pkl'):
            shutil.copy('empty_christmas_list.pkl', 'christmas_list.pkl')
       
        yield

    
    def describe_init():
        def it_assigns_fname_attribute(mocker):
            mocker.patch("os.path.isfile", return_value=True)
            cl = ChristmasList("christmas_list.pkl")
            assert cl.fname == "christmas_list.pkl"
        def it_creates_empty_cl_if_it_does_not_exist(mocker):
            # set up stubs & mocks first
            mock_isfile = mocker.patch("os.path.isfile", return_value=False)
            mock_open = mocker.patch("builtins.open", mocker.mock_open())
            mock_dump = mocker.patch("pickle.dump")

            # execute on the test subject
            cl = ChristmasList("christmas_list.pkl")

            # assert what happened
            mock_isfile.assert_called_once_with("christmas_list.pkl")
            mock_open.assert_called_once_with("christmas_list.pkl", "wb")
            mock_dump.assert_called_once_with([], mock_open.return_value)

        def it_does_not_create_database_if_it_already_exists(mocker):
            mock_isfile = mocker.patch("os.path.isfile", return_value=True)
            mock_open = mocker.patch("builtins.open", mocker.mock_open())
            mock_dump = mocker.patch("pickle.dump")

            cl = ChristmasList("christmas_list.pkl")

            mock_isfile.assert_called_once_with("christmas_list.pkl")
            mock_open.assert_not_called()
            mock_dump.assert_not_called()

    def describe_print_list():
        #save items and add don't achieve the same thing?
        def check_off(saved_presents, capsys):
            cl = saved_presents
            cl.check_off('bike')
            h = cl.print_list()
            captured = capsys.readouterr()
            assert captured.out == "[x] bike\n"
        def dont_check_off(saved_presents, capsys):
            cl = saved_presents
            h = cl.print_list()
            captured = capsys.readouterr()
            assert captured.out == "[_] bike\n"


    def describe_loadItems():
        pass

    def describe_saveItems():
        pass
    def describe_add():
        pass
    def describe_check_off():
        pass
    def describe_remove():
        pass


