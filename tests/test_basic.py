"""Basic tests for the IndoTool package."""


def test_version_exists():
    """Test that the version attribute exists."""
    from indotool import __version__

    assert __version__ is not None


def test_version_format():
    """Test that the version follows semantic versioning."""
    from indotool import __version__

    parts = __version__.split(".")
    assert len(parts) == 3
    for part in parts:
        assert part.isdigit()
