from members.TrinhBaoNgoc.w1 import translate


def test_transpose_normal_rectangular():
    """Test a normal rectangular matrix (2 rows, 3 columns)."""
    assert translate.transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]

def test_transpose_square_matrix():
    """Test a square matrix (2 rows, 2 columns)."""
    assert translate.transpose([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]

def test_transpose_empty_matrix():
    """Test an empty matrix."""
    assert translate.transpose([]) == []

def test_transpose_single_row():
    """Edge case: Test a matrix with only a single row."""
    assert translate.transpose([[1, 2, 3]]) == [[1], [2], [3]]

def test_transpose_single_column():
    """Edge case: Test a matrix with only a single column."""
    assert translate.transpose([[1], [2], [3]]) == [[1, 2, 3]]