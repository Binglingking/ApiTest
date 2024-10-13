import pytest

# @pytest.mark.usefixtures('use_usefixture1')
@pytest.mark.usefixtures('use_usefixture','use_usefixture1')
def test_usefixtures(use_usefixture):
    print("你好test_usefixtures")
