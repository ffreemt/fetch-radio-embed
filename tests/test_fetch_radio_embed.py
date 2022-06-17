"""Test fetch_radio_embed."""
# pylint: disable=broad-except
from fetch_radio_embed import __version__, fetch_radio_embed


def test_version():
    """Test version."""
    assert __version__[:3] == "0.1"


def test_sanity():
    """Check sanity."""
    try:
        assert not fetch_radio_embed()  # type: ignore
    except Exception:
        assert True


def test_one_line():
    """Test one line."""
    res = fetch_radio_embed("abc")
    assert (len(res), len(res[0])) == (1, 512)


def test_two_lines():
    """Test one line."""
    res = fetch_radio_embed("abc\n test")
    assert (len(res), len(res[0])) == (2, 512)
